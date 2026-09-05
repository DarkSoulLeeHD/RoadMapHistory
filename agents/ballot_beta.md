### 🗳️ BALLOT BETA: FEHLER & HALLUZINATIONEN

**Gesamturteil:** Keine KRITISCHE Beanstandung (keine Halluzination, kein falsches Zitat, keine falsche Record-ID). Alle 7 `primary_quote`-Texte buchstabengetreu gegen die Originale verifiziert (Basler Programm/Wikisource, Iron-Wall-PDF jabotinsky.org, Steinsaltz ketubot111, UNGA 181 Wikisource, UNSC 242, UNSC 478 Wikisource, IGH-AO-PDF 19.7.2024). Alle 7 UN-Digital-Library-Records korrekt. Beanstandungen: 2 × MITTEL, 7 × KOSMETISCH.

---

**1. ZITATE-AUDIT (7/7 verifiziert)**
- e01 Basler Programm: `"Zionism strives to create for the Jewish people a home in Palestine secured by public law."` — VERIFIZIERT, buchstabengetreu (Wikisource „Zionism/The Basel Programme"; deckungsgleich mit zionistarchives.org.il). ✔
- e28 Iron Wall: `"Zionist colonisation must either stop, or else proceed regardless of the native population…"` — VERIFIZIERT gegen en.jabotinsky.org/media/9747/the-iron-wall.pdf (S. „The Iron Wall"). Einzige Abweichung: Original `That is our Arab policy;` (Semikolon) → Zitat `Arab policy…` (Ellipse als korrekte Auslassungskennung). ✔
- e29 Ketubot 111a: VERIFIZIERT buchstabengetreu gegen steinsaltz.org/daf/ketubot111/ (inkl. „be-homah – like a wall"). ✔
- e06 UNGA 181: `"The Mandate for Palestine shall terminate as soon as possible but in any case not later than 1 August 1948."` — VERIFIZIERT (Wikisource, Part I A.1). ✔
- e09 UNSC 242: `"Emphasizing the inadmissibility of the acquisition of territory by war…"` — VERIFIZIERT (Präambel, wortgleich UNISPAL/JVL). ✔
- e30 UNSC 478: VERIFIZIERT gegen Wikisource-Volltext (operativer Abs. 3). Abweichung: Original setzt `"basic law"` in Anführungszeichen — im Zitat getilgt (KOSMETISCH, s. unten).
- e22 IGH 19.7.2024: Dispositiv-Ziffer (7) VERIFIZIERT wortgleich gegen UNISPAL-PDF (186-20240719-adv-01-00-en.pdf); Abstimmung **12:3 korrekt** (dort „By twelve votes to three"; AGAINST: Sebutinde, Abraham, Aurescu). ✔

---

**2. BEANSTANDUNGEN**

- **Betroffene Event-ID:** e16 (Palästinenser-Exodus Kuwait 1991)
- **Gefundener Fehler:** Interne Zahlen-Widersprüchlichkeit innerhalb desselben Events. `actors`-Feld: „~350.000–400.000 Palästinenser"; `summary`-Feld: „Vertreibung/Flucht von ~200.000–400.000 Palästinensern [Zahlen variieren]". Untergrenze divergiert (200k vs. 350k) — dasselbe Ereignis trägt zwei verschiedene Spannen.
- **Schweregrad:** MITTEL (ungenaue/widersprüchliche Zahl)
- **Korrekter Befund:** Die Vertreibung der Palästinenser aus Kuwait 1991 wird in der Literatur (HRW 1991; Shlaim) überwiegend mit ~300.000–450.000 (Ausgangsbevölkerung) bzw. ~200.000–400.000 (dauerhaft Vertriebene) angegeben. Die 350k–400k-Untergrenze im `actors`-Feld ist nicht durch die zitierten Quellen gedeckt; konsistente Spanne = 200k–400k.
- **Veto:** JA (Feld angleichen; sonst doppelte, sich widersprechende Angabe im selben Datensatz)

- **Betroffene Event-ID / Datei:** debunks.json (D02) i. V. m. docs/03_klagekatalog_massaker.md
- **Gefundener Fehler:** Doppelzuordnung des Eintrags M05 „Haifa 1939". In docs/03 erscheint M05 (a) in der Tabelle „Belegt-mit-Korrektur" (Zeile „M01/M03/M05 | Haifa 1937/38/39 → Epochen-Eintrag") UND (b) in der Liste „✖ Verworfen (17)" („M05 Haifa 1939 (Einzelereignis)"). debunks.json D02 führt M05 als „Nicht belegt". Dadurch wird M05 in zwei disjunkten Buckets gezählt.
- **Schweregrad:** MITTEL (Datenintegrität)
- **Korrekter Befund:** Die Aufsummierung 9 belegt + 26 korrigiert + 2 Doppelung + 17 verworfen = 54 ist nur dann stimmig, wenn jede M-ID genau einmal zugeordnet ist. Die Doppelung M05 gefährdet die 54/54-Arithmetik. Auflösung nötig: M05 entweder ausschließlich als „verworfen (Einzelereignis)" führen und aus der Korrektur-Zeile streichen (dort bliebe M01/M03 für die Epochen-Kampagne), oder umgekehrt.
- **Veto:** JA (Zählung bereinigen)

- **Betroffene Event-ID:** e30 (UNSC 478, primary_quote)
- **Gefundener Fehler:** Im Zitat fehlen die Anführungszeichen um `"basic law"` (Original: „the recent 'basic law' on Jerusalem"). Wortlaut ansonsten korrekt.
- **Schweregrad:** KOSMETISCH
- **Korrekter Befund:** Wikisource-Volltext Abs. 3 enthält „in particular the recent 'basic law' on Jerusalem". Zitattechnisch sollte die Hervorhebung des Quelltextes erhalten bleiben.
- **Veto:** NEIN (Empfehlung)

- **Betroffene Event-ID:** e09 (UNSC 242)
- **Gefundener Fehler:** Quellen-Inkonsistenz: `sources[].url` = digitallibrary.un.org/record/90717, aber `primary_quote.author_or_source` = „UN-PDF (Peacemaker)". Zwei verschiedene Fundstellen für denselben Text.
- **Schweregrad:** KOSMETISCH
- **Korrekter Befund:** Record 90717 (UN-Digital-Library) und das Peacemaker-PDF (peacemaker.un.org) enthalten denselben Wortlaut; die Angabe sollte vereinheitlicht werden.
- **Veto:** NEIN

- **Betroffene Event-ID:** e30 (UNSC 478) / docs/04 §2
- **Gefundener Fehler:** docs/04 führt UNSC 478 als record/25618 (verifiziert korrekt); phases.json e30 nutzt stattdessen die Wikisource-URL. Keine falsche ID, aber uneinheitliche Fundstellen-Führung.
- **Schweregrad:** KOSMETISCH
- **Veto:** NEIN

- **Betroffene Event-ID:** e24 (Begin-Doktrin, UNSC 487)
- **Gefundener Fehler:** summary: „UNSC 487 verurteilt Angriff als Verstoß gegen Art. 2(4) UN-Charta". UNSC 487 verurteilt den Angriff als „clear violation of the Charter of the United Nations" — der Resolutionstext zitiert **keine** spezifische Artikelnummer (Art. 2(4)).
- **Schweregrad:** KOSMETISCH (substantiell zutreffende, aber im Wortlaut nicht gedeckte Überattribuierung)
- **Korrekter Befund:** „Verstoß gegen die UN-Charta (Verbot der Gewaltanwendung)" wäre quellengetreu; „Art. 2(4)" ist eine zulässige juristische Konkretisierung, aber kein Zitat der Resolution.
- **Veto:** NEIN (Empfehlung: Formulierung „Verstoß gegen die UN-Charta" oder Kennzeichnung als Auslegung)

- **Betroffene Event-ID:** e18 (UNSC 1397)
- **Gefundener Fehler:** `sources[].url` = unctad.org/.../sres1397_en.pdf — eine UNCTAD-URL als Beleg für eine Sicherheitsrats-Resolution (ungewöhnlicher Host; Resolution 1397, 12.3.2002, ist inhaltlich korrekt datiert und zitiert).
- **Schweregrad:** KOSMETISCH
- **Veto:** NEIN

- **Betroffene Event-ID:** e21 (Gazakrieg) / docs/04 §5
- **Gefundener Fehler:** Todeszahl 7.10.2023 divergiert: phases.json e21 = „~1.195", docs/04 §5 = „~1.200 Tote, 251 Geiseln [BBC]". Beide Werte beziehen sich auf denselben Anschlag (offizielle israelische Zählung später auf 1.195 präzisiert).
- **Schweregrad:** KOSMETISCH
- **Veto:** NEIN (Zahl vereinheitlichen)

- **Betroffene Datei:** docs/03 vs. docs/06 (Deir Yassin)
- **Gefundener Fehler:** Spanne wird uneinheitlich geführt: docs/03 „≥107; Morris ~112", docs/06-Tabelle „107–254". Die Obergrenze 254 (= de Reynière, Rotes Kreuz) fehlt in docs/03, wird aber in docs/04 §7 korrekt benannt („de Reyniès 254").
- **Schweregrad:** KOSMETISCH
- **Veto:** NEIN (Spanne vereinheitlichen)

---

**3. POSITIV-VERMERKE (keine Beanstandung)**
- Alle 7 UN-Digital-Library-Records verifiziert: 1696=UNSC 446, 3657=UNSC 452, 11767=UNSC 465, 25618=UNSC 478, 22225=UNSC 487, 581053=UNSC 1701, 202170=UNGA 2625. ✔
- Debunks juristisch/historisch wasserdicht: Verdict „Nicht belegt" korrekt abgegrenzt von „Widerlegt" (nur D15 Qalunya, D17 Jerusalem 1967 als aktiv widerlegt geführt — beides zutreffend; D17 führt korrekt den Mughrabi-Abriss als dokumentierten Ersatzbefund). Keine Täter-Opfer-Umkehr im Debunk-Katalog; Selektivitätsbefund (fehlende jüdische Opfer: Hebron 1929, Kfar Etzion, Hadassah-Konvoi, Kafr Qasim) korrekt und methodisch sauber.
- Nakba-Spanne 700.000–750.000 (e07) quellenkonform (UN/Morris). Gaza-Zahlen als Spannen mit MoH/Israel-Attribution geführt.
