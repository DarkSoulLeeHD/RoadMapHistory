# Forschungsprotokoll — RoadMapHistory (05.09.2026)

Kompletter Arbeitsbericht der Session: was wurde recherchiert, verifiziert, dokumentiert — und was bleibt offen.

## 1. Ablauf (5 Arbeitsturns)

| Turn | Aufgabe | Ergebnis |
|---|---|---|
| 1 | Projekt-Initialisierung (IDEA.md/Soul.md), Grundgerüst, 6 Phasen | Sechs-Phasen-Modell konzipiert (1880–1917 / 1917–1948 / 1948–1967 / 1967–1993 / 1993–2023 / 2023–heute); 18 Wendepunkte mit Tier-1-Dokumenten recherchiert; **Datei-Grundgerüst nicht erstellt** (Turn-Suchlimit) |
| 2 | Deep-Research A: Ideologie 1882–1948 | Vollständiger Bericht → gesichert als `docs/01_ideologie_1882-1948.md` |
| 3 | Deep-Research B: Militäroperationen/Besatzung | Vollständiger Bericht → `docs/02_operationen_besatzung.md` |
| 4 | Screenshot @GEO_BRIEF (54 Vorfälle) | Transkription, Klassifikation A/B/C, 54 Todos (M01–M54) |
| 5 | Batch 1 ([A]-Einträge) | 9/9 verifiziert; Todos completed |
| 6 | Empfehlungs-Todos F01–F05 | Dateien `README.md`, `docs/01–04` angelegt |
| 7 | Batches 2–4 der Verifikations-Pipeline | M01–M54 **54/54 abgeschlossen** (9 belegt · 26 belegt-mit-Korrektur · 2 Doppelungen · 17 verworfen); Katalog final in `docs/03` |
| 8 | Interaktives Grundgerüst | `roadmap/index.html` (self-contained: 6 Phasen, 18 Wendepunkte, Tier-Chips, Quellen-Links) |
| 9 | Cluster-C-Vertiefung | `docs/05_cluster_c_sicherheitsapparat.md` (Mossad/Shin Bet, Susannah, Eichmann, Wrath of God, Landau, Hasbara, Epstein-Abgrenzung) |
| 10 | Ausbauzyklus 0–4 | HANDOFF_GEMINI.md · UNSC-Records 446/452/465/478/487/1701 + UNGA 2625 in §2 · Regionaldossier Jordanien/Golf in docs/02 §5 · phases.json (27 Events) · index.html-UI (Suche/Filter/Modal/Export/Fallback) · build_fallback.py |
| 11 | Cluster-D-Transparenzzyklus | docs/06_cluster_d_faktencheck.md · roadmap/debunks.json (17 Einträge) · UI: Faktencheck-Tab + ⭐Kern-Toggle · README/HANDOFF/docs-04-Update |
| 12 | Sprint 3 „Evidence-Vault" | 7 wörtliche Primärzitate (Primärtext-Retrieval: Jabotinsky-PDF, UNGA-181-UNISPAL, UNSC-242/478-Volltext, IGH-AO-PDF, Steinsaltz-Ketubot, Basler Programm) in phases.json · 5 neue Events e28–e32 · docs/05-Anker · UI: Evidence-Blockquote + Zitat-Kopieren + Print-CSS |
| 13 | Sprint 4 „Multi-Agenten-Peer-Review" | agents/-System (5 Profile) · 4 Blind-Audits auf DeepSeek V4 Pro (Alpha/Beta/Gamma/Delta; Beta/Gamma mit Timeout → Ballot-Rekonstruktion aus Transkripten + Parent-Verifikation) · Epsilon-Konsens (consensus_patch_plan.md) · Umsetzung: 2 Beta-Vetos, 7 Beta-Folgekorrekturen, 9 Alpha-Events e33–e41 (41 Events/20 Kern), Delta-UI-Upgrades (Spine/Zähler/Toast/Touch), docs/01 §E #innerjuedische-kritik · Build + Systemtests grün |
| 14 | Sprint 5 „Welcome-Page" | Intro-Overlay (Mission/Bildungszweck/Leitplanken/How-To) · First-Visit localStorage `seenWelcome` · ℹ-Header-Button · Escape/Fokus/Scroll-Lock · responsive · Print aus · Build + alle Tests grün |

## 2. Verifizierte Primärquellen (Retrieval dieser Session, Auswahl)

**UN-Sicherheitsrat:** 101 (1953) · 242 (1967) · 338 (1973) · 350 (1974) · 425/426 (1978) · 446 (22.3.1979; Siedlungen rechtswidrig/GC IV; digitallibrary.un.org/record/1696) · 452 (20.7.1979; Siedlungsstopp; record/3657) · 465 (1.3.1980, einstimmig; Rückbau-Aufforderung; record/11767) · 478 (20.8.1980; Jerusalem-Gesetz null & void; record/25618) · 487 (19.6.1981; Osirak-Verurteilung/Art. 2(4); record/22225) · 497 (1981) · 508/509/520 (1982) · 672 (1990) · 904 (1994) · 1397 (2002) · 1701 (11.8.2006; Libanon-Waffenruhe/Blaue Linie/UNIFIL; record/581053) · 2334 (2016; record/853446) · 2712 (2023) · 2728 (2024)
**UN-Generalversammlung:** 181 (II) 1947 · 194 (III) 1948 · 302 (IV) 1949 · **2625 (XXV) 24.10.1970 — „Friendly Relations Declaration": Verbot gewaltsamen Gebietserwerbs (Art. 2(4)-Konkretisierung; digitallibrary.un.org/record/202170, PDF A_RES_2625(XXV)-EN)** · 997–1001 (ES-I) 1956 · 37/123 D (1982) · ES-10/15 (2004) · ES-10/21 (2023)
**IGH:** Gutachten Mauer (9.7.2004, case/131) · Gutachten Besatzung (19.7.2024) · SA v. Israel: Orders 26.1.2024 & 24.5.2024 (Rafah)
**ICC:** Ermittlungsautorisierung Palästina (5.2.2021) · Haftbefehle Netanyahu/Gallant/Deif (21.11.2024)
**Primärtexte:** Balfour-Deklaration (2.11.1917) · Völkerbundmandat 1922 · 1939er-Weißbuch (Cmd 6019) · Plan Dalet (10.3.1948) · Camp-David-Abkommen 1978 · Israel-Ägypten-Vertrag 1979 · Oslo-DoP 1993 (A/48/486-S/26560) · Arabische Friedensinitiative 2002 · Abraham Accords 2020 · Kethubot 111a · Jabotinsky „The Iron Wall" (1923) · VaYoel Moshe (1961) · Pittsburgh-Plattform (1885)

## 3. Standardwerke (Tier 2, durchgängig verwendet)
Morris (2001/2004/2008) · Khalidi (1992) · Shlaim (2000/2023) · Oren (2002) · Segev (1986/98/2007) · Pappé · Ravitzky (1996) · Shafir/Peled (2002) · Chetrit (2009) · Shohat (1988) · Shenhav (2006) · Laqueur (2003) · Vital (1975) · Shindler (1991) · Bacon (1996) · Friedman (1977) · Pickhan (2001) · Cohen (1998/2010) · Masalha

## 4. Wichtige institutionelle/URL-Belege (Tier 1–3)
- Jabotinsky-Institut: en.jabotinsky.org/media/9747/the-iron-wall.pdf
- Sefaria: sefaria.org/Ketubot.111a · Steinsaltz: steinsaltz.org/daf/ketubot111/
- UN-Digital-Library: digitallibrary.un.org (u. a. records 71622, 853446, 90717)
- UNISPAL: un.org/unispal (u. a. auto-insert-185393 [GA 181], 178680 [PLO 1988], 180015 [Oslo], 179511 [UNSC 350], 186-20240719 AO-PDF)
- peacemaker.un.org (UNSC 242/338-PDFs) · icj-cij.org/case/131 · icc-cpi.int (21.11.2024) · news.un.org (2728) · UN-Yearbook 1956 (cdn.un.org)
- INSS: inss.org.il (Siboni, „Disproportionate Force", 2008) · JVL: Kahan-Bericht, Winograd-Bericht
- 2001-2009.state.gov (Camp David) · web.archive.org (Friedensvertrag 1979, MFA) · state.gov (Abraham Accords PDF)
- UB Frankfurt/Compact Memory (Kongress-Protokolle) · PalQuest/Palestine-Studies (Plan Dalet, Saliha) · Forensic Architecture (al-Dawayima) · deiryassin.org (Morris-Interview) · B'Tselem/OCHA (aktuelle Daten)

## 5. Aktuelle Lage-Eckdaten (2023–2026, für Phase VI)
- 7.10.2023: Hamas-Angriff (~1.195 Tote [später offizielle israelische Zählung], 251 Geiseln [BBC]); Gazakrieg
- UNSC 2712 (15.11.2023), ES-10/21 (27.10.2023), UNSC 2728 (25.3.2024)
- IGH SA v. Israel: Antrag 29.12.2023; einstw. Maßnahmen 26.1.2024; Rafah-Order 24.5.2024; Verfahren in Schriftphase (Stand Sept. 2026, Mail&Guardian 3.6.2026)
- ICC-Haftbefehle 21.11.2024 (Netanjahu, Gallant, Deif)
- Libanon: Nasrallah getötet 27.9.2024; Bodeninvasion 1.10.2024; Waffenruhe 27.11.2024
- Assad-Sturz 8.12.2024 (HTS-Offensive; SWP-Analyse)
- Gaza-Waffenruhe 19.1.2025 (Phase 1: 33 Geiseln, ~1.900 Gefangene); Bruch 18.3.2025; neue Waffenruhe ab 10.10.2025; bis 11.8.2026 weitere 1.259 Tote [Gisha/MoH]; Hamas-Entwaffnungsrahmen Juli/Aug. 2026 („Board of Peace")
- 12-Tage-Krieg Israel–Iran: 13.–24.6.2025 (US-B-2-Schläge; Waffenruhe 24.6.2025)
- 2026er-Irankrieg („Dritter Golfkrieg"): Beginn 28.2.2026 (US-israelische Schläge; Khamenei getötet); Waffenruhe 8.4.2026 + Islamabad-Memorandum; Kollaps 8.7.2026; Kämpfe wieder ab Sept. 2026 [Wikipedia-Timeline als Live-Synthese; Primärbelege folgen]

## 6. Offene Punkte / nächste Schritte
1. ~~Todo-Batches 2–4~~ → **abgeschlossen** (54/54; Details `docs/03`)
2. ~~Interaktives Grundgerüst~~ → **abgeschlossen** (`roadmap/index.html`)
3. ~~Cluster-C-Vertiefung~~ → **abgeschlossen** (`docs/05`)
4. Cluster-B-Vertiefung: Jordanien (Schwarzer September 1970), Irak-Kriegskontext 1991, Golfstaaten-Dimension — **erledigt** (docs/02 §5)
5. Datenmodell `phases.json` — **erledigt** (27 Events; debunks.json separat)
6. UI-Review-Runde: interaktive Vorschau prüfen, ggf. Design-Feinschliff — offen
7. ~~Quellenregister-Volltext-URLs für UNSC 446/452/465/478/487/1701 & UNGA 2625 ergänzen~~ → **erledigt** (Records in §2: digitallibrary 1696/3657/11767/25618/22225/581053/202170)
8. Cluster-D-Transparenzliste — **erledigt** (docs/06 + debunks.json + UI-Tab)
9. phases.json/debunks.json-Pflege bei neuen Ereignissen; optionale EN-Fassung — offen
10. Sprint 3 Evidence-Vault — **erledigt** (7 Primärzitate, Events e28–e32, Evidence-UI, Print-CSS)
11. UI-Endreview im Browser (Modal-Interaktion, Kopierfunktion, Druckansicht testen; = Gamma G-07/G-08) — offen
12. Sprint 4 Multi-Agenten-Peer-Review — **erledigt** (4 Blind-Audits + Epsilon-Konsens; 9 Events e33–e41; 20 Kern; UI-Upgrades; alle Tests grün)
13. Sprint 5 Welcome-Page — **erledigt** (Intro-Overlay, First-Visit-Logik, ℹ-Button, alle Tests grün)

## 7. Methodische Standards (verbindlich, vgl. Soul.md)
- Keine Fakten ohne Quellenbeleg; `[unverified]`/`[Zahlen variieren]` bei Unsicherheit
- Keine Pauschalisierung gegen jüdische Menschen; Analyse von Staatshandlungen/Doktrinen
- Massaker-Begriff nur mit Einordnung; Social-Media-Listen sind Primärquelle nur für „Behauptung", nie für „Fakt"
- Zahlen immer mit Spanne + Quellenangabe (Beispiel: Deir Yassin ≥107, Morris ~112, de Reyniès 254)
