# HANDOFF — Projekt „RoadMapHistory" (Stand 05.09.2026, nach Ausbauzyklus 0–4)

> Vollständiger Übergabestand zur Re-Initialisierung künftiger Sessions oder fremder Agenten (z. B. Gemini Flash 3.8).
> Projektordner: `/home/mattheusfinkelstein/Documents/RoadMapHistory`

## 1. Projekt
Quellengestützte interaktive chronologische Roadmap (1880–heute): Geschichte, Ideologie, Kriege, Besatzung, Sicherheitsapparat und Konfliktdynamiken des Zionismus/Nahostkonflikts. Bildungszweck. Politisch sensibel → strikte Fakten/Mythos-Trennung („Cluster D").

## 2. Verbindliche Methodik (Projekt-SOUL)
- Zero-Hallucination: keine erfundenen Daten/Zitate/Resolutionen. Marker: `[unverified]`, `[Zahlen variieren]`, `[Hypothese]`.
- Quellen-Tiers: **T1** Primärquellen (UN/IGH/ICC/Akten/Verträge) · **T2** Standardwerke (Morris, Shlaim, Khalidi, Oren, Segev, Pappé, Ravitzky, Pollack) · **T3** Institutionen/Berichte (B'Tselem, Amnesty, HRW, OCHA, INSS, Kommissionen).
- Keine Pauschalisierung gegen Juden; Analyse von Staatshandlungen/Doktrinen; theologische Positionen sachlich.
- Zahlen mit Spanne + Quelle. „Massaker/Genozid" nur mit Einordnung; rechtlich präzise („IGH-verfahrenanhängig" ≠ festgestellt).
- Zeitstrahl: `[Jahr] | Ereignis | Akteure | Beweislage | Konsequenz`.
- Dateiänderungen im Projekt nur nach Nutzer-Freigabe.

## 3. Projektstruktur (bestehend)
```
RoadMapHistory/
├── IDEA.md · README.md · HANDOFF_GEMINI.md (diese Datei)
├── docs/
│   ├── 01_ideologie_1882-1948.md              (Herzl/Jabotinsky, Parteien/Doktrinen, orthodoxe Opposition, Mizrahim)
│   ├── 02_operationen_besatzung.md            (Palästina/Libanon/Ägypten/Syrien + Regionaldossier Jordanien & Golf)
│   ├── 03_klagekatalog_massaker.md            (54er-Liste: 9 belegt · 26 korrigiert · 2 Doppelungen · 17 verworfen)
│   ├── 04_forschungsprotokoll.md              (Arbeitsbericht, Quellen-URLs inkl. UN-Digital-Library-Records)
│   ├── 05_cluster_c_sicherheitsapparat.md     (Mossad/Shin Bet: Susannah, Eichmann, Wrath of God, Landau; NSO; Hasbara; Epstein-Abgrenzung)
│   └── 06_cluster_d_faktencheck.md            (Cluster-D-Modul: Screening-Methodik, 17 verworfenen Behauptungen, Kernfälle, Fehlerquellen der 26 Korrekturen)
├── agents/                                 (5 Rollen-Profile 01–05, 4 Blind-Ballots, consensus_patch_plan.md)
└── roadmap/
    ├── phases.json                            (Datenmodell: 41 Events/20 Kern, Cluster A–D, Tier, Quellen, doc_ref, 7 primary_quotes)
    ├── debunks.json                           (17 Faktencheck-Einträge: claim, verdict, real_history, sources)
    ├── build_fallback.py                      (bettet beide JSONs als Offline-Fallback ein; idempotent)
    └── index.html                             (Welcome-Page First-Visit + ℹ-Button, Tabs Roadmap|Faktencheck, Suche, Filter-Chips mit Zählern, ⭐Kern-Toggle, Timeline-Spine, Evidence-Modal + Toast, Export, Fallback)
```

## 4. Sechs-Phasen-Modell (Kern der Roadmap)
I 1880–1917 Ursprünge · II 1917–1948 Mandatszeit · III 1948–1967 Staatsgründung/Nakba/Kriege · IV 1967–1993 Besatzung/Friedensverträge · V 1993–2023 Oslo-Ära · VI 2023–heute 7. Oktober & Systemkrise.
Kern-Wendepunkte (20) und Schlüsselereignisse (41 gesamt) vollständig in `roadmap/phases.json` mit `doc_ref`-Querverweisen.

## 5. Kernbefunde (verifiziert)
- Ableitungen: Jabotinsky→Likud (1973); Herzl/Ben-Gurion→Mapai→Avoda (1968); Siedlerparteien programmatisch verwandt, nicht institutionelle Erben. Doktrinen: Ben-Gurion-Offensivdoktrin, Präemption 1967, Begin-Doktrin (Osirak, UNSC 487), Dahiya (INSS/Siboni 2008).
- Orthodoxe Opposition: Kethubot 111a (drei Schwüre); Sonnenfeld/Edah HaCharedit 1921; Aguda 1912; Wasserman; Satmar/VaYoel Moshe 1961; Neturei Karta 1938; Reform: Pittsburgh 1885; Gegenposition Mizrachi 1902/Kook; Status-quo-Brief 19.6.1947.
- Mizrahim: Shohat 1988/Shenhav 2006; Jemen 1881/82; Farhud 6/1941; Irak-Exodus 1950/51; Ma'abrot; Jemeniten-Kinder-Affäre; Wadi Salib 1959; Black Panthers 1971; Mahapach 1977.
- Klagekatalog-Korrekturen: Balad al-Shaykh real 31.12.1947/1.1.1948 (60–70); Bahr al-Baqar real 8.4.1970 (30–46 Kinder); „Safa"→Safsaf 29.10.1948 (52–70); Haifa-Raffinerie 30.12.1947 = 39–41 jüdische Opfer; Jenin 2002 kein Massaker (UN/HRW); Gaza 2014: OCHA 2.251; GMR 2018/19: 223 (46 Kinder); Gaza-Krieg ≥76.600 Tote bis 28.8.2026.
- Cluster B neu (docs/02 §5): Karameh 21.3.1968 (Israel 28 Tote/17 Fahrzeuge; PLO-Mythos); Schwarzer September 17.9.1970–7/1971 (syrische Invasion ab 18.9.; Israel/USA-Abschreckung); Friedensvertrag Jordanien 26.10.1994; Golfkrieg 1991 (Scuds, Patriot, Arafat/Saddam); Kuwait-Exodus ~200.000–400.000; Arabische Friedensinitiative 2002; Abraham Accords 2020.
- Cluster C: Susannah/Lavon 1954; Eichmann 11.5.1960 (UNSC 138); Wrath of God/Lillehammer 21.7.1973; Bus 300 (1984)→Landau (1987)→HCJ 5100/94 (1999); NSO/Pegasus (2021); Hasbara; Epstein nur Gerichtsakten (Giuffre v. Maxwell, 1/2024), spekulative Verflechtungen verworfen.

## 6. Tier-1-Quellen-Kernbestand (Records/URLs in docs/04 §2)
UNSC 101·242·338·350·425/426·446 (record/1696)·452 (3657)·465 (11767)·478 (25618)·487 (22225)·497·508/509/520·672·904·1397·1701 (581053)·2334 (853446)·2712·2728
UNGA 181(II)·194(III)·302(IV)·2625(XXV) (record/202170)·997–1001(ES-I)·37/123D·ES-10/15·ES-10/21
IGH: Mauer 9.7.2004 (case/131) · AO 19.7.2024 · Orders 26.1./24.5.2024 · ICC 5.2.2021 + 21.11.2024
Primärtexte: Balfour, Mandat 1922, Cmd 6019, Plan Dalet, Camp David 1978, Friedensverträge 1979/1994, Oslo-DoP 1993, API 2002, Abraham 2020, Kethubot 111a, Iron Wall 1923, VaYoel Moshe 1961, Pittsburgh 1885.

## 7. Aktuelle Lage-Eckdaten (Sept. 2026)
Gaza: Waffenruhe ab 10.10.2025; bis 11.8.2026 weitere 1.259 Tote; Hamas-Entwaffnungsrahmen 2026 („Board of Peace"); IGH ohne Endurteil. Libanon-Waffenruhe 27.11.2024. Assad-Sturz 8.12.2024 (Israel in Pufferzone). Iran: 12-Tage-Krieg 13.–24.6.2025; Irankrieg ab 28.2.2026 (Khamenei getötet; Waffenruhe 8.4.2026 kollabierte 8.7.2026; Kämpfe ab 9/2026).

## 8. Status nach Ausbauzyklus 0–4
- [x] Aufgabe 0: HANDOFF_GEMINI.md erstellt
- [x] Aufgabe 1: Primärquellen UNSC 446/452/465/478/487/1701 + UNGA 2625 in docs/04 (mit Digital-Library-Records)
- [x] Aufgabe 2: Cluster-B-Regionaldossier Jordanien/Golf in docs/02 §5
- [x] Aufgabe 3: roadmap/phases.json (27 Events, Cluster, Tier, Quellen) + index.html-Upgrade (Suche, Filter, Badges, Modal, Export, Fallback)
- [x] Aufgabe 4: doc_ref-Querverweise in phases.json
- [x] Cluster-D-Zyklus: docs/06_cluster_d_faktencheck.md + roadmap/debunks.json (17 Einträge) + UI-Tabs [Roadmap|Faktencheck] + ⭐Kern-Toggle; Build & Konsistenz validiert
- [x] Sprint 3 (Evidence-Vault): 7 wörtliche Primärzitate in phases.json (Basler Programm e01, UNGA 181 e06, UNSC 242 e09, IGH-2024-Dispositiv e22, Iron Wall e28, Ketubot 111a/Steinsaltz e29, UNSC 478 e30); neue Events e28–e32 (Iron Wall, Drei Schwüre, UNSC 478, NSO/Pegasus, Epstein-Abgrenzung); docs/05-Anker (lavon-affaire, eichmann-1960, wrath-of-god, bus-300, nso-pegasus, epstein-abgrenzung); UI: Evidence-Blockquote + 📋Zitat-kopieren + @media print; Build validiert (32 Events)
- [x] Sprint 4 (Multi-Agenten-Peer-Review, DeepSeek V4 Pro): 4 Blind-Audits (Alpha/Beta/Gamma/Delta) + Epsilon-Konsens in `agents/`; umgesetzt: 2 Beta-Vetos (e16 Kuwait-Spanne, M05-Haifa-Doppelzuordnung), 9 Alpha-Events e33–e41 (Pittsburgh 1885, Bund 1897, Brit Shalom 1925, Litani 1978, Sabra/Schatila 1982 [Kern], Golan-Gesetz/UNSC 497 1981, Libanon-Rückzug 2000, 2. Libanonkrieg 2006 [Kern], UNGA ES-10/23), 7 Beta-Folgekorrekturen (u. a. e30-‚basic law‘, e24-Art-2(4)-Formulierung, UNSC-1397-Record 459885, Deir-Yassin-Spanne, 1.195-Zählung), Delta-UI (Timeline-Spine, Chip-Trefferzähler, Toast, 44px-Touch-Targets, Modal-Scroll-Lock, --gold-Fix), docs/01 Abschnitt E + Anker #innerjuedische-kritik; Build & alle Systemtests grün (41 Events/20 Kern)
- [x] Sprint 5 (Welcome-Page): Intro-Overlay (Mission · Bildungszweck · 4 Methodik-Leitplanken mit T1–T3-Badges · How-To) · First-Visit-Logik localStorage `seenWelcome` · Header-Button „ℹ Über dieses Archiv" · Escape-/Fokus-/Scroll-Lock-Handling · responsiv (Mobile 1-Spalte, 16px) · Print ausgeblendet · Build + alle Tests grün
- [x] Sprint 6 (Master-Überarbeitung: Dossier-Ausbau): Datenmodell v1.1 — `goal` (41/41), `deep_analysis` (41/41, 3 Absätze/Kern, ~6.900 Wörter), `extended_quotes` (12 Events, alle wörtlich aus Primärtexten verifiziert: Herzl-Vorposten, Balfour, UNGA 181 A.3/194 Abs.11, UNSC 242 op.1/338 op.1/478 op.5/497/1701 op.1, IGH-Dispositiv 2024, Iron Wall, Steinsaltz-Rashi), `direct_url`+`tier` pro Quelle (38 Links, alle HTTP 200/206 geprüft, 5 tote URLs ersetzt: UNEF→Wikisource GA 997, Balfour-CAB→Wikisource, NYT→UN News, Britannica→archive.org, INSS→archive.org) · UI: Dossier-Lesemodus (Goal-Banner, Historische Analyse, Zitat-Karten mit Kopierbutton, klickbare Quellen-Karten ↗ mit target=_blank rel=noopener noreferrer, Modal 860px) · Build + alle Systemtests grün

## 9. Offene Punkte / mögliche nächste Aufgaben
1. Review-Runde der UI (Vorschau, Barrierefreiheit, Export-Tests)
2. phases.json ↔ index.html-Fallback synchron halten (Hinweis im Code)
3. Cluster-D-Abschnitt „nicht verifizierte Social-Media-Behauptungen" (17 verworfenen Einträge) als Transparenzliste
4. Aktualisierung der Roadmap bei neuen Entwicklungen (Phase VI ist „laufend")
5. Optional: zweisprachige Fassung (EN) oder Zitat-/Beleg-Modal mit wörtlichen Quellenpassagen (Evidence-Mode)
