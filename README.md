# RoadMapHistory — Interaktive Roadmap: Geschichte, Ideologie und Konfliktdynamiken des Zionismus

> **Projektstatus: Dokumentations- & Verifikationsphase (Stand: 05.09.2026)**
> Bildungs- und Aufklärungsprojekt auf Basis überprüfbarer Primär- und Sekundärquellen (siehe `IDEA.md`).

## Projektziel
Entwicklung einer detaillierten, interaktiven chronologischen Roadmap (1880–heute) zur Geschichte des Zionismus und des Nahostkonflikts: Ursprünge, Ideologien, Kriege, Besatzung, Geheimdienst-/Militärstrukturen, innerjüdische Kritik — ausschließlich quellengestützt.

## Themencluster (aus IDEA.md)
- **Cluster A:** Ursprung & Ideologiegeschichte (Herzl, Jabotinsky, Achad Ha'am, orthodoxe Opposition, Bund)
- **Cluster B:** Staatsgründung & regionale Dimension (1948, 1956, 1967, 1973, Libanon, Syrien, Jordanien)
- **Cluster C:** Strukturelle Analyse (IDF-Doktrinen, Geheimdienste, Hasbara, Völkerrecht: UNSC/IGH/ICC)
- **Cluster D:** Fact-Checking & Abgrenzung (belegte Fakten vs. Mythen, Aktenlage)

## Quellen-Hierarchie (verbindlich)
| Tier | Typ | Beispiele |
|---|---|---|
| 1 | Primärquellen | UN-Resolutionen, IGH/ICC-Dokumente, deklassifizierte Akten, historische Verträge, Originalessays |
| 2 | Akademische Standardwerke | Morris, Shlaim, Khalidi, Oren, Segev, Pappé, Ravitzky, Shafir/Peled u. a. |
| 3 | Offizielle Berichte/Institutionen | B'Tselem, Amnesty, HRW, OCHA, INSS, Kommissionen (Kahan, Winograd) |

Unbelegte/umstrittene Angaben werden explizit markiert: `[Hypothese]`, `[Unbestätigt]`, `[Zahlen variieren]`.

## Projektstruktur
```
RoadMapHistory/
├── IDEA.md                     # Projektidee (Original)
├── README.md                   # diese Datei
├── docs/
│   ├── 01_ideologie_1882-1948.md    # Deep-Research A: ideologische Strömungen
│   ├── 02_operationen_besatzung.md  # Deep-Research B: Militäroperationen & Besatzung
│   ├── 03_klagekatalog_massaker.md  # 54-Vorfälle-Katalog — FINALER Stand (Batches 1–4)
│   ├── 04_forschungsprotokoll.md    # Arbeitsbericht, Quellenregister, offene Punkte
│   ├── 05_cluster_c_sicherheitsapparat.md  # Geheimdienste, dokumentierte Operationen, Hasbara, Epstein-Abgrenzung
│   └── 06_cluster_d_faktencheck.md  # Cluster-D-Modul: Methodik, 17 verworfenen Behauptungen, Kernfälle, Fehlerquellen
├── agents/                       # Multi-Agenten-Audit-System: 5 Rollen-Profile + 4 Blind-Ballots + Konsens-Plan
└── roadmap/
    ├── phases.json                # Datenmodell: 41 Events (20 Kern) + 7 Primärzitate (Evidence-Vault), Cluster A–D, doc_ref
    ├── debunks.json               # Faktencheck-Daten: 17 verworfenen Behauptungen (Verdict, Realbefund, Quellen)
    ├── build_fallback.py          # bettet phases.json + debunks.json als Offline-Fallback in index.html ein (idempotent)
    └── index.html                 # UI: Welcome-Page (First-Visit, localStorage), Tabs [Roadmap|Faktencheck], Suche, Filter-Chips mit Trefferzählern, ⭐Kern-Toggle, Timeline-Spine, Evidence-Modal (Zitat kopieren + Toast), Print-Styles, Export
```

## Ist-Zustand (05.09.2026)
- ✅ Sechs Forschungs-/Dokumentationsberichte (`docs/01–06`; docs/02 mit Regionaldossier Jordanien & Golf)
- ✅ Interaktive Roadmap (`roadmap/`): phases.json (**41 Events, 20 Kern, 7 wörtliche Primärzitate**) + debunks.json (17 Faktencheck-Einträge) + index.html (Tabs, Suche, Filter-Chips mit Live-Trefferzählern, ⭐Kern-Modus, Timeline-Spine mit Phasen-Nodes, Evidence-Modal mit 📋Zitat-Kopieren + Toast, Print-Styles, Export, Offline-Fallback)
- ✅ Multi-Agenten-Peer-Review (09/2026): 4 Blind-Audits (Alpha Lücken / Beta Fakten / Gamma Tech / Delta UI) + Epsilon-Konsens-Arbiter — Profile, Ballots und `consensus_patch_plan.md` in `agents/`; Beschlüsse vollständig umgesetzt
- ✅ Welcome-Page (Intro-Overlay): Mission, Bildungszweck, 4 Methodik-Leitplanken (Tier-Badges T1–T3) + Bedienungsanleitung; First-Visit-Logik via localStorage (`seenWelcome`), Header-Button „ℹ Über dieses Archiv", Escape-/Fokus-Handling, responsiv
- ✅ Verifikations-Pipeline **54/54 abgeschlossen**: 9 belegt · 26 belegt-mit-Korrektur · 2 Doppelungen zusammengeführt · 17 verworfen
- ✅ Cluster-D-Transparenzmodul: docs/06 + Faktencheck-Tab in der UI (17 Warn-Cards: Behauptung vs. Realbefund)
- ✅ Primärquellen vervollständigt: UNSC 446/452/465/478/487/1701 + UNGA 2625 mit UN-Digital-Library-Records in docs/04
- ✅ HANDOFF_GEMINI.md für Session-Re-Initialisierung
- ⏳ Ausstehend: manuelle Browser-QA (Gamma G-07/G-08: Tab-Reihenfolge, Escape/Fokus, @media print, Clipboard unter file://), optionale EN-Fassung
