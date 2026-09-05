### 🏛️ KONSENS-BESCHLUSS & MASTER-PATCH-PLAN

**Arbiter (AGENT EPSILON) — Verfassungsprüfung abgeschlossen.**
Verifizierte Ist-Zustände: phases.json enthält 32 Events (e01–e32), keine e33–e41 vorhanden (Doppelungen ausgeschlossen). Kein Brit Shalom/Buber/Magnes/Pittsburgh/Litani/Sabra-Schatila/Blue Line/ES-10/23 als Event — GAP-Befund Alpha bestätigt. debunks.json D02 (claim M05, „Nicht belegt") bestätigt. docs/03 Zeile 20 führt „M01/M03/M05" in der Korrektur-Tabelle UND Zeile 46 „M05" in „Verworfen (17)" → Doppelzuordnung bestätigt. index.html Zeile 49 `.b-core{border-color:var(--gold); color:var(--gold)}` ohne `--gold`-Definition in `:root` (JS-Zeile 197 maskiert via Inline-Style) → Delta-Bug bestätigt. e16 (actors 350k–400k vs. summary 200k–400k), e30 („basic law" ohne Anführungszeichen), e09 (URL record/90717 vs. Peacemaker), e24 („Art. 2(4)"), e21 (1.195 vs. docs/04 „1.200"), Deir Yassin (docs/03 ≥107/Morris ~112 vs. docs/06 107–254) — sämtlich verifiziert.

---

## 1. Angenommene Faktenkorrekturen (Beta) — 2 × MITTEL, VETO JA (absolut, ohne Abstimmung)

**B-01 · e16 Kuwait-Zahlenwiderspruch (VETO JA, MITTEL)**
- Befund: `actors` „~350.000–400.000" widerspricht `summary` „~200.000–400.000" im selben Datensatz; Untergrenze 350k nicht durch HRW/Shlaim gedeckt.
- Patch (phases.json, e16):
  - ALT: `"actors": "Kuwait; PLO (Arafat/Saddam); ~350.000–400.000 Palästinenser",`
  - NEU: `"actors": "Kuwait; PLO (Arafat/Saddam); ~200.000–400.000 Palästinenser",`

**B-02 · M05-Haifa-Doppelzuordnung (VETO JA, MITTEL)**
- Befund: M05 in zwei disjunkten Buckets gezählt, gefährdet 54/54-Arithmetik (9 belegt + 26 korrigiert + 2 Doppelung + 17 verworfen).
- Auflösung (gewählt): M05 ausschließlich als „verworfen (Einzelereignis)" führen; aus der Korrektur-Zeile streichen; M01/M03 verbleiben für den Epochen-Eintrag (Irgun-Bombenkampagne 1936–39).
- Patch (docs/03_klagekatalog_massaker.md, Zeile 20):
  - ALT: `| M01/M03/M05 | Haifa 1937/38/39 | Keine drei Einzel-Massaker belegt; dokumentiert: **Irgun-Bombenkampagne auf arabische Zivilisten 1936–39** (u. a. Haifa-Markt 6.7.1938, ~18 Tote 1937 je Quelle) → Epochen-Eintrag |`
  - NEU: `| M01/M03 | Haifa 1937/38 | Keine zwei Einzel-Massaker belegt; dokumentiert: **Irgun-Bombenkampagne auf arabische Zivilisten 1936–39** (u. a. Haifa-Markt 6.7.1938, ~18 Tote 1937 je Quelle) → Epochen-Eintrag |`
  - „Verworfen (17)"-Liste (Zeile 46) und debunks.json D02 („Nicht belegt") bleiben unverändert — sie sind untereinander konsistent. Die 54/54-Arithmetik wird wieder stimmig.

**Folge-Korrekturen (Beta KOSMETISCH, Veto NEIN — als Qualitäts-Fixes übernommen):**
- **B-03 · e30 „basic law"-Anführungszeichen** (phases.json, primary_quote.text):
  - ALT: `and in particular the recent basic law on Jerusalem,`
  - NEU: `and in particular the recent 'basic law' on Jerusalem,`
- **B-04 · e09 Quellenvereinheitlichung** (phases.json, e09 primary_quote.author_or_source):
  - ALT: `"author_or_source": "UNSC Res. 242 (1967), Präambel (22.11.1967), UN-PDF (Peacemaker)",`
  - NEU: `"author_or_source": "UNSC Res. 242 (1967), Präambel (22.11.1967), UN Digital Library record 90717",`
- **B-05 · e30/docs04 Fundstellenvereinheitlichung**: docs/04 führt UNSC 478 als record/25618, e30 nutzt Wikisource. Beide korrekt. Ergänzend in e30 `sources[]` einen zweiten Eintrag `{"name":"UNSC Res. 478","doc_id":"S/RES/478 (1980) — UN Digital Library record 25618","url":"https://digitallibrary.un.org/record/25618"}` ergänzen (Wikisource-Volltext als primärer Beleg bleibt).
- **B-06 · e24 Art. 2(4)-Überattribuierung** (phases.json, e24 summary):
  - ALT: `UNSC 487 verurteilt Angriff als Verstoß gegen Art. 2(4) UN-Charta`
  - NEU: `UNSC 487 verurteilt Angriff als klare Verletzung der UN-Charta (Verbot der Gewaltanwendung, Art. 2(4))`
- **B-07 · e18 UNCTAD-URL**: `sources[].url` = unctad.org/.../sres1397_en.pdf ist ein ungewöhnlicher Host für eine Sicherheitsrats-Resolution. Durch UN-Digital-Library-Record für UNSC 1397 ersetzen (Record-ID vor Einpflege verifizieren).
- **B-08 · e21 Todeszahl vereinheitlichen** (docs/04 §5, Zeile 44):
  - ALT: `- 7.10.2023: Hamas-Angriff (~1.200 Tote, 251 Geiseln [BBC]); Gazakrieg`
  - NEU: `- 7.10.2023: Hamas-Angriff (~1.195 Tote [später offizielle israelische Zählung], 251 Geiseln [BBC]); Gazakrieg`
- **B-09 · Deir-Yassin-Spanne vereinheitlichen** (docs/03, Zeile 15):
  - ALT: `Deir Yassin 9.4.1948 (≥107; Morris ~112)`
  - NEU: `Deir Yassin 9.4.1948 (≥107; Morris ~112; de Reynière 254)`
  (angleicht an docs/06 „107–254" und docs/04 §7 „de Reyniès 254").

---

## 2. Angenommene Inhaltserweiterungen (Alpha) — 9 Events e33–e41 (alle Relevanz ≥ 4 UND Tier-1/2 → Verfassungsregel 2 erfüllt)

Alle neun Lückenanträge sind durch die in ballot_alpha.md benannten Tier-1/2-Quellen gedeckt und NICHT bereits in phases.json vorhanden. Sie werden als neue Events in `roadmap/phases.json` (in der `events`-Liste, geordnet nach Datum innerhalb der jeweiligen Phase) eingefügt:

**e33 — Pittsburgh-Plattform (16.–19.11.1885) · Phase I · Cluster A · Relevanz 4**
```json
{"id":"e33","date":"16.–19.11.1885","phase":"I","cluster":"A","core":false,"title":"Pittsburgh-Plattform: Reformjudentum gegen den Nationalismus","actors":"Konferenz des amerikanischen Reformjudentums (Kaufmann Kohler u. a.)","summary":"Acht-Punkte-Programm: „Wir betrachten uns nicht länger als Nation, sondern als religiöse Gemeinschaft und erwarten daher weder eine Rückkehr nach Palästina… noch die Wiederherstellung eines jüdischen Staates.","consequence":"Erste organisierte innerjüdische Gegenposition zum politischen Zionismus; Wende erst mit der Columbus-Plattform (1937) und der Schoa.","tier":["T1","T2"],"sources":[{"name":"Pittsburgh Platform (1885)","doc_id":"Text (myjewishlearning.com / posenlibrary.com)"},{"name":"Laqueur, A History of Zionism","doc_id":"2003"}],"doc_ref":"docs/01_ideologie_1882-1948.md (innerjüdische Kritik)"}
```

**e34 — Jüdischer Arbeiterbund (Bund), Oktober 1897 Wilna · Phase I · Cluster A · Relevanz 4**
```json
{"id":"e34","date":"Oktober 1897","phase":"I","cluster":"A","core":false,"title":"Gründung des Jüdischen Arbeiterbunds (Bund) in Wilna — „Doikayt“","actors":"Jüdische Arbeiterführer in Wilna (u. a. Arkadi Kremer, Wladimir Medem)","summary":"Säkulare, sozialistische Massenbewegung; programmatische „Doikayt“ (hier-ness): jüdische Autonomie in Osteuropa statt territorialer Staatsbildung in Palästina.","consequence":"Stärkste nicht-zionistische jüdische Bewegung bis zur Schoa; dauerhafte Gegenposition zum politischen Zionismus.","tier":["T1","T2"],"sources":[{"name":"Bund-Programm/Archiv","doc_id":"YIVO"},{"name":"Pickhan, Gegen den Strom (Bund)","doc_id":"2001"}],"doc_ref":"docs/01_ideologie_1882-1948.md (innerjüdische Kritik)"}
```

**e35 — Brit Shalom (1925, Jerusalem): Buber/Magnes/Scholem · Phase II · Cluster A · Relevanz 5 (Doppellücke)**
```json
{"id":"e35","date":"1925","phase":"II","cluster":"A","core":false,"title":"Brit Shalom: binationale Zwei-Nationen-Lösung (Buber, Magnes)","actors":"Martin Buber, Judah L. Magnes, Gershom Scholem, Henrietta Szold","summary":"Innerzionistische Gruppierung für einen binationalen Staat mit gleichen Rechten für Juden und Araber; Kritik an der nationalstaatlichen Mehrheitslogik und der „Eisernen Mauer“.","consequence":"Wichtigste intellektuelle Gegenstimme zum Mehrheitsnationalismus; marginalisiert, aber bleibende Referenz der israelischen Friedensbewegung.","tier":["T1","T2"],"sources":[{"name":"Buber, A Land of Two Peoples","doc_id":"hg. P. Mendes-Flohr, 1983"},{"name":"Magnes, Like All the Nations?","doc_id":"1930"},{"name":"Shlaim, The Iron Wall","doc_id":"2000"}],"doc_ref":"docs/01_ideologie_1882-1948.md (innerjüdische Kritik) — NEU anzulegen"}
```
**⚠ Pflicht-Voraussetzung (Doppellücke):** e35 fehlt nicht nur in phases.json, sondern auch in docs/01–06. Vor/parallel zum Event-Eintrag muss der doc_ref-Abschnitt in `docs/01_ideologie_1882-1948.md` mit den Quellen (Buber, Magnes, Shlaim) neu angelegt und mit einem Anker versehen werden, sonst bricht die doc_ref-Anker-Garantie (Gamma G-05).

**e36 — Operation Litani (14.3.–13.6.1978) · Phase IV · Cluster B · Relevanz 4**
```json
{"id":"e36","date":"14.3.–13.6.1978","phase":"IV","cluster":"B","core":false,"title":"Operation Litani: erste Libanon-Invasion und UNIFIL","actors":"Israel (IDF); PLO; UN-Sicherheitsrat","summary":"Vergeltungsinvasion Südlibanons nach dem Küstenstraßen-Massaker (11.3.1978); UNSC 425 fordert Rückzug, UNSC 426 errichtet UNIFIL.","consequence":"Israelischer Teilrückzug; de-facto-Sicherheitszone unter SLA/Haddad ab 1979; Beginn der 22-jährigen Libanon-Verstrickung.","tier":["T1","T2"],"sources":[{"name":"UNSC 425 / 426","doc_id":"S/RES/425 (1978), S/RES/426 (UNIFIL)"},{"name":"Shlaim, The Iron Wall","doc_id":"2000"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 2, Libanon)"}
```

**e37 — Libanonkrieg 1982 + Sabra/Schatila (16.–18.9.1982) · Phase IV · Cluster B · Relevanz 5 · core=true**
```json
{"id":"e37","date":"6.6.1982–1983 (Sabra/Schatila 16.–18.9.1982)","phase":"IV","cluster":"B","core":true,"title":"Libanonkrieg 1982 und das Massaker von Sabra/Schatila","actors":"Israel (Begin/Sharon); PLO; libanesische Phalange; UN","summary":"Großinvasion („Frieden für Galiläa“) mit dem Ziel der PLO-Vernichtung; Belagerung Beiruts; PLO-Abzug nach Tunis; Massaker von Sabra/Schatila (460–3.500 Tote) unter den Augen der IDF.","consequence":"UNGA 37/123 D stuft Sabra/Schatila als „act of genocide“ ein; Kahan-Bericht stellt indirekte Verantwortung Israels fest; Sharon-Rücktritt (1983); Hisbollah-Gründung als direkte Folge der Besatzung.","tier":["T1","T2"],"sources":[{"name":"UNSC 508/509/520","doc_id":"S/RES/508/509/520 (1982)"},{"name":"UNGA 37/123 D","doc_id":"A/RES/37/123D (16.12.1982)"},{"name":"Kahan Commission Report","doc_id":"8.2.1983 (JVL)"},{"name":"Khalidi, Under Siege","doc_id":"1986"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 2) · docs/03_klagekatalog_massaker.md (M15)"}
```

**e38 — Golan-Gesetz 14.12.1981 + UNSC 497 (17.12.1981) · Phase IV · Cluster C · Relevanz 5**
```json
{"id":"e38","date":"14.12.1981 / 17.12.1981","phase":"IV","cluster":"C","core":false,"title":"Golan-Gesetz und UNSC 497: Annexion „null und nichtig“","actors":"Knesset (Golan-Gesetz 14.12.1981); UN-Sicherheitsrat (UNSC 497, 17.12.1981)","summary":"Israel wendet Recht und Verwaltung auf die besetzten Golanhöhen an; UNSC 497 erklärt die Maßnahme für „null and void and without international legal effect“.","consequence":"Internationale Nicht-Anerkennung der Annexion (Ausnahme: US 25.3.2019); jährliche UNGA-Bestätigung; bis heute völkerrechtlich offen.","tier":["T1","T2"],"sources":[{"name":"Golan Heights Law","doc_id":"14.12.1981"},{"name":"UNSC 497","doc_id":"S/RES/497 (17.12.1981)"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 4, Syrien/Golan)"}
```

**e39 — Libanon-Rückzug (24.5.2000) + Blue Line (16.6.2000) · Phase V · Cluster B · Relevanz 4**
```json
{"id":"e39","date":"24.5.2000 / 16.6.2000","phase":"V","cluster":"B","core":false,"title":"Israelischer Rückzug aus dem Libanon und Blue Line","actors":"Israel (Barak); Hisbollah; UN (S/2000/590)","summary":"Einseitiger Abzug Israels aus der Sicherheitszone; UN bestätigt Rückzug gemäß UNSC 425 und zieht die Blue Line (16.6.2000).","consequence":"Kollaps der SLA; Stärkung der Hisbollah; Shebaa-Farmen-Streit bleibt Konfliktherd (Vorfeld 2006).","tier":["T1","T2"],"sources":[{"name":"UNSC 425","doc_id":"S/RES/425 (1978, fortlaufend)"},{"name":"UN-Bericht Blue Line","doc_id":"S/2000/590 (16.6.2000)"}],"doc_ref":"docs/02_operationen_besatzung.md (Sicherheitszone 1985–2000)"}
```

**e40 — Zweiter Libanonkrieg (12.7.–14.8.2006) · Phase V · Cluster B · Relevanz 5 · core=true**
```json
{"id":"e40","date":"12.7.–14.8.2006","phase":"V","cluster":"B","core":true,"title":"Zweiter Libanonkrieg und UNSC 1701","actors":"Israel (Olmert); Hisbollah (Nasrallah); UN-Sicherheitsrat","summary":"Eskalation nach Hisbollah-Überfall (12.7.2006); 34-tägiger Krieg; UNSC 1701 fordert Waffenruhe und Hisbollah-Entwaffnung südlich des Litani.","consequence":"~1.100–1.200 libanesische und 165 israelische Tote; Winograd-Bericht (2008): „ohne klaren militärischen Sieg“; Geburtsstunde der Dahiya-Doktrin; unvollständige Hisbollah-Entwaffnung.","tier":["T1","T2"],"sources":[{"name":"UNSC 1701","doc_id":"S/RES/1701 (11.8.2006)"},{"name":"Winograd Commission Report","doc_id":"30.1.2008 (JVL)"}],"doc_ref":"docs/02_operationen_besatzung.md (2. Libanonkrieg) · docs/01 (Dahiya-Doktrin)"}
```

**e41 — UNGA ES-10/23 (18.9.2024) · Phase VI · Cluster C · Relevanz 4**
```json
{"id":"e41","date":"18.9.2024","phase":"VI","cluster":"C","core":false,"title":"UNGA ES-10/23: Umsetzung des IGH-Gutachtens binnen 12 Monaten","actors":"UN-Generalversammlung (Notstandssession); Israel; Drittstaaten","summary":"Auf Basis des IGH-Gutachtens vom 19.7.2024 fordert die Resolution Israel auf, die unrechtmäßige Präsenz im besetzten Gebiet binnen 12 Monaten zu beenden; Drittstaaten zu Nicht-Anerkennung und Sanktionen verpflichtet.","consequence":"Völkerrechtliches Handlungsmandat mit Frist; verschärft die Pflichtenlage für Drittstaaten; Referenzpunkt der laufenden Verfahren.","tier":["T1","T2"],"sources":[{"name":"UNGA ES-10/23","doc_id":"A/RES/ES-10/23 (18.9.2024, UN Digital Library)"},{"name":"IGH Advisory Opinion","doc_id":"19.7.2024"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 1b) · docs/04_forschungsprotokoll.md §5"}
```

---

## 3. Angenommene Code-Fixes (Gamma)

**Keine Pflicht-Bugs.** Gamma G-01 bis G-06 ergeben 0 Fehler:
- G-01/G-06: `node --check` des Haupt-Scripts → EXIT 0 (JS-Syntax valide).
- G-02/G-06: Offline-Fallback (file://) intakt — `fallback-phases` (32/32) und `fallback-debunks` (17/17) PARSE_OK + MATCH_SOURCE.
- G-03/G-05: Vollständige doc_ref-Anker-Prüfung über alle 32 Events → 0 fehlende Dateien/Anker.
- G-04: onkeydown-Escaping valide (kein Bug; Negativtest war künstlich).

**Kein Code-Patch nötig.** Als verpflichtende QA-Aufgaben (keine Patches, manuell) übernommen:
- G-07: Manueller Browser-Test von Tab-Reihenfolge, Escape-Schließen, Fokus-Rückkehr, `@media print`.
- G-08: Clipboard-Fallback (`fallbackCopy`) einmal praktisch unter `file://` testen.
- **Neu (Folge aus Alpha e35):** Nach Einfügen von e35–e41 müssen die doc_ref-Anker für alle 9 neuen Events erneut per Gamma G-05-Skript geprüft werden; für e35 ist der Ziel-Abschnitt in docs/01 erst anzulegen (siehe Abschnitt 2).

---

## 4. Angenommene UI-Upgrades (Delta) — alle standalone, keine externen Frameworks/CDNs

**D-BUG (Pflicht-Fix) · `--gold` in `:root` ergänzen** (index.html, Zeile 49):
- ALT: `.b-core{border-color:var(--gold); color:var(--gold)}`
- NEU (zusätzlich im `:root`-Block ergänzen): `--gold:#d4a72c;` und Zeile 49 unverändert belassen. Damit ist `.b-core` auch ohne den Inline-Style-Fallback (JS Zeile 197) korrekt gefärbt.

**V1 — Timeline-Spine/Rail (angenommen)**
- CSS (in `<style>` nach den `.ev`-Regeln einfügen):
```css
.phase{position:relative}
.phase::before{content:""; position:absolute; left:18px; top:16px; bottom:16px; width:2px; background:linear-gradient(180deg, var(--phase-c,var(--accent)), #0000); opacity:.35; border-radius:1px;}
.phase .ev{position:relative; margin-left:20px}
.phase .ev::before{content:""; position:absolute; left:-13px; top:16px; width:10px; height:10px; border-radius:50%; background:var(--phase-c,var(--accent)); border:2px solid var(--bg); box-shadow:0 0 0 2px var(--phase-c,var(--accent)), 0 0 10px var(--phase-c,var(--accent)); transition:box-shadow .2s;}
.phase .ev.open::before{box-shadow:0 0 0 2px var(--phase-c,var(--accent)), 0 0 16px var(--phase-c,var(--accent))}
```
- JS (renderMap, section-Aufruf): ALT `'<section class="phase" style="border-left-color:'+PHASE_COLORS[key]+'">'` → NEU `'<section class="phase" style="--phase-c:'+PHASE_COLORS[key]+';border-left-color:'+PHASE_COLORS[key]+'">'`

**V2 — Filter-Chips mit Trefferzählern (angenommen)**
- CSS:
```css
.chipcount{background:#ffffff14; border-radius:8px; padding:0 6px; font-size:10.5px; font-variant-numeric:tabular-nums; color:var(--fg); margin-left:2px;}
.chip.active .chipcount{background:var(--accent); color:#0d1117}
```
- JS: `chipCounts()` + `updateChipCounts()` exakt wie im Ballot Delta V2 (Zählung pro Chip-Wert unter Anwendung aller Filter außer der eigenen Dimension); in `makeChips` das `<span class="chipcount"></span>` nach `esc(v)` ergänzen; `updateChipCounts()` am Ende von `renderMap()` aufrufen.

**V3 — Toast + Card Hover/Focus (angenommen)**
- HTML: vor `<footer>` (Zeile 151): `<div id="toast" role="status" aria-live="polite"></div>`
- CSS: `#toast`/`#toast.show` sowie `.ev:hover`/`.ev-head:focus-visible`/`.ev-head:hover .t` und `@media (prefers-reduced-motion:reduce)` exakt wie Delta V3.
- JS: `showToast(msg)`; Kopier-Handler `done` → `showToast("Zitat in Zwischenablage kopiert ✓")`; Textaufbau statt `innerText.replace()`: `(q.querySelector("blockquote")?.textContent||"") + "\n— " + (q.querySelector(".qsrc")?.textContent||"")`.

**V4 — Mobile/Touch + Modal-Scroll-Lock (angenommen)**
- CSS: `.chip/.btn/.tabbtn/.modal .close` auf min-height 44px; `.modal{overscroll-behavior:contain; -webkit-overflow-scrolling:touch}`; `body.modal-open{overflow:hidden}`; `@media (max-width:680px)`-Block (font-size 16px, `#q{font-size:16px}`, `.modal{max-height:92vh;...}`, `.chip{font-size:13px}`) exakt wie Delta V4.
- JS: in `openModal()` nach `classList.add("open")`: `document.body.classList.add("modal-open");`; in `closeModal()` nach `classList.remove("open")`: `document.body.classList.remove("modal-open");`.

---

## 5. Abgelehnte Anträge (mit demokratischer Begründung)

- **Delta V1 optionaler „Zeit-Ruler" (Jahresstreifen):** ABGELEHNT (YAGNI). Die Jahreszahlen stehen bereits im Phasentitel (z. B. „I (1880–1917)"); ein separater Ruler wäre redundant. Delta selbst empfiehlt, ihn nicht zu bauen — der Arbiter folgt dieser Selbst-Zurücknahme.
- **Gamma G-07/G-08 als „Pflicht-Patches":** ABGELEHNT als Code-Patches. Es sind keine reproduzierbaren Bugs (0 Pflicht-Bugs in G-01–G-06), sondern manuelle QA-Aufträge; sie werden als Arbeitsaufträge (Abschnitt 3) geführt, nicht als Master-Patch.
- **Keine Alpha-Ablehnungen:** Alle 9 Lückenanträge (e33–e41) erfüllen Relevanz ≥ 4 UND Tier-1/2-Nachweis; keine Doppelung zu e01–e32 festgestellt. Sämtlich angenommen.
- **Keine weiteren Beta-Ablehnungen:** Die 7 KOSMETISCH-Befunde sind als Folge-Korrekturen (B-03 bis B-09) aufgenommen, da sie Quellentreue und Konsistenz ohne Faktenänderung verbessern.

---

**Schlusszählung (verbindlich):** 2 Pflicht-Faktenkorrekturen (Veto JA) · 7 kosmetische Folge-Korrekturen · 9 neue Events (e33–e41) · 0 Pflicht-Code-Bugs · 1 Pflicht-CSS-Fix (`--gold`) · 4 UI-Upgrades (V1–V4) · 2 QA-Aufträge (Gamma G-07/G-08) · 1 abgelehnter Zusatz (Zeit-Ruler).