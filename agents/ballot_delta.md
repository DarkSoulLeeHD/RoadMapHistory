### 🗳️ BALLOT DELTA: UI/UX-UPGRADES

**Datenbasis geprüft (phases.json / debunks.json, Ist-Zustand):** 32 Ereignisse, davon 18 Kern-Wendepunkte. Tier-Verteilung: T1 = 25, T2 = 10, T3 = 6. Cluster: A=6, B=18, C=6, D=2. Phasen: I=4, II=4, III=3, IV=10, V=6, VI=5. 17 Debunks.
⚠️ Hinweis: Das Aufgabenbeispiel „Tier 1 (18)" ist irreführend — „18" ist die Kern-Anzahl (core=true), NICHT T1. T1 hat tatsächlich 25 Treffer. Die Zähler unten nutzen die echten Werte.
⚠️ Bug-Fund: Zeile 49 `.b-core{ border-color:var(--gold); color:var(--gold) }` referenziert `--gold`, das in `:root` NICHT definiert ist → KERN-Badge bekommt keine Farbe (fällt auf `currentColor`/ungültig zurück). Fix: `--gold:#d4a72c` in `:root` ergänzen.

---

**Vorschlag 1 — Timeline-Spine/Rail (vertikale Achse mit Phasen-Nodes)**

- Komponente / Element: `.phase`-Sektionen und `.ev`-Karten (renderMap), Timeline-Visualisierung.
- UX-Problem / Optimierungspotenzial: Ereignisse sind aktuell nur gestapelte Karten ohne visuelle Zeitachse. Eine vertikale Spine mit leuchtenden, phasen-gefärbten Nodes macht den chronologischen Fluss sofort ablesbar (Scannability) und nutzt die vorhandenen `PHASE_COLORS`.
- Konkreter CSS/JS-Codebaustein:

```css
/* CSS: in den <style>-Block einfügen (nach .ev-Regeln) */
.phase{position:relative}
.phase::before{                      /* vertikale Spine im linken Gutter */
  content:""; position:absolute; left:18px; top:16px; bottom:16px; width:2px;
  background:linear-gradient(180deg, var(--phase-c,var(--accent)), #0000);
  opacity:.35; border-radius:1px;
}
.phase .ev{position:relative; margin-left:20px}
.phase .ev::before{                  /* Node, erbt --phase-c von der Sektion */
  content:""; position:absolute; left:-13px; top:16px; width:10px; height:10px;
  border-radius:50%; background:var(--phase-c,var(--accent));
  border:2px solid var(--bg);
  box-shadow:0 0 0 2px var(--phase-c,var(--accent)), 0 0 10px var(--phase-c,var(--accent));
  transition:box-shadow .2s;
}
.phase .ev.open::before{ box-shadow:0 0 0 2px var(--phase-c,var(--accent)), 0 0 16px var(--phase-c,var(--accent)) }
```

```js
// JS: renderMap, Zeile 216 — der <section class="phase" …> Aufruf
// ALT: '<section class="phase" style="border-left-color:'+PHASE_COLORS[key]+'">'
// NEU (eine CSS-Variable --phase-c setzen, erbt in alle Nodes dieser Phase):
'<section class="phase" style="--phase-c:'+PHASE_COLORS[key]+';border-left-color:'+PHASE_COLORS[key]+'">'
```

Optionaler Zeit-Ruler (leichtgewichtig, nur falls gewünscht): Ein schmaler Jahresstreifen in `.phase-head` — die Jahreszahlen stehen bereits im Phasentitel (z. B. „I (1880–1917)"), daher ist ein separater Ruler redundant; ich empfehle, ihn NICHT zu bauen (YAGNI).
- Performance-Impact: Minimal — reines CSS (`::before`-Pseudo-Elemente) + eine zusätzliche CSS-Variable pro Sektion. Keine zusätzlichen DOM-Knoten, kein Reflow-Framing-Problem (Positionierung absolut).

---

**Vorschlag 2 — Filter-Chips mit Trefferzählern**

- Komponente / Element: `.chip`-Buttons in `#fPhase`, `#fCluster`, `#fTier` (makeChips / renderMap).
- UX-Problem / Optimierungspotenzial: Nutzer sehen nicht, wie viele Treffer ein Filter liefert, bevor sie klicken. Ein Zähler (z. B. „T1 · 25") zeigt die verfügbare Menge pro Dimension und reagiert dynamisch auf Suche + andere aktive Filter („nur noch 3 im Cluster B bei aktivem Tier T1").
- Konkreter CSS/JS-Codebaustein:

```css
.chipcount{
  background:#ffffff14; border-radius:8px; padding:0 6px; font-size:10.5px;
  font-variant-numeric:tabular-nums; color:var(--fg); margin-left:2px;
}
.chip.active .chipcount{ background:var(--accent); color:#0d1117 }
```

```js
// Zählt Treffer pro Chip-Wert, unter Anwendung aller Filter AUSSER der eigenen Dimension.
function chipCounts(){
  if(!PHASES) return null;
  const q = state.q.trim().toLowerCase();
  const pass = ev => {
    if(state.coreOnly && !ev.core) return false;
    if(q){ const h=(ev.title+" "+ev.actors+" "+ev.summary+" "+ev.date).toLowerCase(); if(h.indexOf(q)<0) return false; }
    return true;
  };
  const c = {phase:{}, cluster:{}, tier:{}};
  PHASE_KEYS.forEach(k=>{ c.phase[k] = PHASES.events.filter(ev=>ev.phase===k && pass(ev)
      && (!state.clusters.size||state.clusters.has(ev.cluster)) && (!state.tiers.size||ev.tier.some(t=>state.tiers.has(t)))).length; });
  ["A","B","C","D"].forEach(x=>{ c.cluster[x] = PHASES.events.filter(ev=>ev.cluster===x && pass(ev)
      && (!state.phases.size||state.phases.has(ev.phase)) && (!state.tiers.size||ev.tier.some(t=>state.tiers.has(t)))).length; });
  ["T1","T2","T3"].forEach(x=>{ c.tier[x] = PHASES.events.filter(ev=>ev.tier.includes(x) && pass(ev)
      && (!state.phases.size||state.phases.has(ev.phase)) && (!state.clusters.size||state.clusters.has(ev.cluster))).length; });
  return c;
}
function updateChipCounts(){
  const c = chipCounts(); if(!c) return;
  document.querySelectorAll(".chip").forEach(b=>{
    const v = b.dataset.v;
    const dim = b.closest("#fPhase") ? "phase" : b.closest("#fCluster") ? "cluster" : "tier";
    const el = b.querySelector(".chipcount");
    if(el) el.textContent = (c[dim]&&c[dim][v]!=null) ? c[dim][v] : "0";
  });
}
```

```js
// makeChips (Zeile 325–340): im Button-Markup den Zähler ergänzen:
// ALT: '…<span class="dot '+dotClass+'"></span>'+esc(v)+'</button>'
// NEU: '…<span class="dot '+dotClass+'"></span>'+esc(v)+'<span class="chipcount"></span></button>'
// Zusätzlich am Ende von renderMap() (nach $("status").textContent = …) aufrufen:
updateChipCounts();
```

- Performance-Impact: Neutral — `updateChipCounts()` läuft einmal pro renderMap-Aufruf über max. 32 Events (trivial). Kein Re-Fetch, reine In-Memory-Filterung. Zähler stehen als `tabular-nums`, kein Layout-Springen.

---

**Vorschlag 3 — Micro-Interactions: Toast + Hover/Focus auf Cards**

- Komponente / Element: (a) `#copyQuote`-Button + Kopier-Feedback, (b) `.ev`-Karten.
- UX-Problem / Optimierungspotenzial: (a) Kopieren gibt nur stilles Button-Text-„✓ Kopiert!" zurück — leicht zu übersehen, kein globales Feedback, und der Text-Strip-Mechanismus (`innerText.replace(...)`) ist fragil. (b) Cards haben kein Hover-/Focus-Feedback; Tastaturnutzer (role="button", tabindex=0) sehen keinen Fokus-Ring.
- Konkreter CSS/JS-Codebaustein:

```css
/* Toast */
#toast{position:fixed; bottom:22px; left:50%; transform:translate(-50%,16px);
  background:var(--panel2); color:var(--fg); border:1px solid var(--accent);
  border-radius:8px; padding:10px 16px; font-size:13px; opacity:0; pointer-events:none;
  transition:opacity .2s, transform .2s; z-index:200; box-shadow:0 6px 20px #0009}
#toast.show{opacity:1; transform:translate(-50%,0)}

/* Card Hover/Focus */
.ev{transition:border-color .15s, box-shadow .15s}
.ev:hover{border-color:var(--accent); box-shadow:0 4px 14px rgba(88,166,255,.12)}
.ev-head:focus-visible{outline:2px solid var(--accent); outline-offset:2px}
.ev-head:hover .t{color:var(--accent)}
@media (prefers-reduced-motion:reduce){
  .ev, #toast, .ev-head .arrow{transition:none}
}
```

```html
<!-- HTML: vor <footer> (Zeile 151) einfügen -->
<div id="toast" role="status" aria-live="polite"></div>
```

```js
// JS: nach closeModal/Keydown-Handlern einfügen
let toastTimer=null;
function showToast(msg){
  const t=$("toast"); if(!t) return;
  t.textContent=msg; t.classList.add("show");
  clearTimeout(toastTimer); toastTimer=setTimeout(()=>t.classList.remove("show"),2200);
}
```

```js
// JS: Kopier-Handler (Zeile 364–376) — 'done'-Callback ersetzen:
// ALT:  const done = ()=>{ cb.textContent="✓ Kopiert!"; setTimeout(()=>{ cb.textContent="📋 Zitat kopieren"; },2000); };
// NEU (robuster: nur blockquote + Quelle kopieren, Toast statt stillem Button):
const done = ()=>{ showToast("Zitat in Zwischenablage kopiert ✓"); };
// und die Zeile davor: statt innerText.replace() gezielter Textaufbau:
// const text = (q.querySelector("blockquote")?.textContent||"") + "\n— " + (q.querySelector(".qsrc")?.textContent||"");
```

- Performance-Impact: Minimal — Toast ist ein einzelner, wiederverwendeter DOM-Knoten (kein Neu-Erstellen pro Klick). Hover/Transitionen sind GPU-freundlich (border-color/box-shadow/opacity). `prefers-reduced-motion` respektiert.

---

**Vorschlag 4 — Mobile: Touch-Targets, Modal-Scrolling, Lesbarkeit**

- Komponente / Element: `.chip`, `.btn`, `.tabbtn`, `.modal`, `.modal-backdrop`, Basis-Typografie, `#q`.
- UX-Problem / Optimierungspotenzial: (a) Chips/Buttons sind unter 44px (WCAG 2.5.5 Target Size) — schwer zu treffen. (b) Modal scrollt zwar, aber ohne `overscroll-behavior` und ohne Body-Scroll-Lock wackelt der Hintergrund mit. (c) `#q` mit 14px löst auf iOS den Auto-Zoom aus; Basis 15px ist auf kleinen Screens knapp.
- Konkreter CSS/JS-Codebaustein:

```css
/* Touch-Targets (44px) — global, gilt auch Desktop */
.chip{min-height:44px; padding:6px 14px; align-items:center}
.btn{min-height:44px; padding:8px 16px}
.tabbtn{min-height:44px}
.modal .close{min-width:44px; min-height:44px}

/* Modal-Scrolling */
.modal{overscroll-behavior:contain; -webkit-overflow-scrolling:touch}
body.modal-open{overflow:hidden}

@media (max-width:680px){
  body{font-size:16px}               /* Lesbarkeit */
  #q{font-size:16px}                 /* verhindert iOS-Auto-Zoom (<16px zoomen) */
  .modal{max-height:92vh; max-width:100%; border-radius:10px; padding:16px}
  .modal-backdrop{padding:3vh 10px; align-items:flex-start}
  .chip{font-size:13px}              /* größer trotz 44px-Target */
}
```

```js
// JS: Body-Scroll-Lock beim Öffnen/Schließen des Modals
// In openModal() nach classList.add("open") ergänzen:
document.body.classList.add("modal-open");
// In closeModal() nach classList.remove("open") ergänzen:
document.body.classList.remove("modal-open");
```

- Performance-Impact: Minimal — reine Layout-/Größen-Anpassungen und eine Scroll-Lock-Klasse. Kein JS-Scrolling, kein Resize-Handler. `overscroll-behavior:contain` verhindert Scroll-Chaining ohne JS.

---

**Zusammenfassung der Prioritäten (Delta-Empfehlung):** V2 (Chip-Zähler) und V4 (Touch/Modal) haben den höchsten konkreten UX-Nutzen bei Null-Risiko; V1 (Spine) ist der größte visuelle Gewinn; V3 (Toast) ist ein kleiner, robuster Qualitätsgewinn. Alle vier sind standalone-fähig (file://), nutzen keine externen Frameworks/CDNs, und bewahren das Dark-Theme (`--bg`, `--panel`, `--accent`, `--t1/t2/t3`) sowie die Phasen-Farben unverändert.