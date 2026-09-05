### 🗳️ BALLOT ALPHA: INHALTLICHE LÜCKEN

**Vorbemerkung / Methodik:** phases.json enthält 32 Events (e01–e32). Gegenprüfung gegen docs/01–06 und docs/04 (Tier-1/-2-Katalog): Zahlreiche in den Docs BEREITS belegte Ereignisse fehlen als eigenständige Roadmap-Events. Regionale Bilanz: **Ägypten** — Sinai-Abzug 1982 in e11 bereits abgedeckt („Sinai-Rückzug bis 25.4.1982"), KEIN eigenständiges Event nötig. **Jordanien** — durch e13/e14/e19 solide abgedeckt. **Libanon** — SCHWERE LÜCKE (1978, 1982/Sabra-Schatila, 2000, 2006 fehlen als Events). **Syrien** — Golan 1981/UNSC 497 fehlt. **Theologische Kritik** — Pittsburgh 1885, Bund, Brit Shalom/Buber fehlen. **Phase VI** — IGH/ICC in e22 präzise; es fehlt UNGA ES-10/23.

**GAP 1 — e33 · Pittsburgh-Plattform (16.–19.11.1885) · Cluster A · Phase I · Relevanz 4**
Fehlendes Ereignis: Erste organisierte innerjüdische Ablehnung des politischen Zionismus durch das amerikanische Reformjudentum („We consider ourselves no longer a nation, but a religious community…"). In docs/01 (Z.62) und docs/04 belegt, kein Event.
Quellen: T1 Pittsburgh Platform (1885). T2 Laqueur, *A History of Zionism* (2003).
Formulierungsvorschlag:
```json
{"id":"e33","date":"16.–19.11.1885","phase":"I","cluster":"A","core":false,"title":"Pittsburgh-Plattform: Reformjudentum gegen den Nationalismus","actors":"Konferenz des amerikanischen Reformjudentums (Kaufmann Kohler u. a.)","summary":"Acht-Punkte-Programm: „Wir betrachten uns nicht länger als Nation, sondern als religiöse Gemeinschaft und erwarten daher weder eine Rückkehr nach Palästina… noch die Wiederherstellung eines jüdischen Staates.“","consequence":"Erste organisierte innerjüdische Gegenposition zum politischen Zionismus; Wende erst mit der Columbus-Plattform (1937) und der Schoa.","tier":["T1","T2"],"sources":[{"name":"Pittsburgh Platform (1885)","doc_id":"Text (myjewishlearning.com / posenlibrary.com)"},{"name":"Laqueur, A History of Zionism","doc_id":"2003"}],"doc_ref":"docs/01_ideologie_1882-1948.md (innerjüdische Kritik)"}
```

**GAP 2 — e34 · Jüdischer Arbeiterbund (Bund), Oktober 1897 Wilna · Cluster A · Phase I · Relevanz 4**
Fehlendes Ereignis: Säkulare, sozialistische Gegenposition „Doikayt" statt Staatsbildung in Palästina; wichtigste nicht-zionistische jüdische Massenbewegung Osteuropas. In docs/01 (Z.63) belegt.
Quellen: T1 Bund-Programm/Archiv (YIVO). T2 Pickhan, *Gegen den Strom* (2001); Frankel, *Prophecy and Politics* (1981).
Formulierungsvorschlag:
```json
{"id":"e34","date":"Oktober 1897","phase":"I","cluster":"A","core":false,"title":"Gründung des Jüdischen Arbeiterbunds (Bund) in Wilna — „Doikayt“","actors":"Jüdische Arbeiterführer in Wilna (u. a. Arkadi Kremer, Wladimir Medem)","summary":"Säkulare, sozialistische Massenbewegung; programmatische „Doikayt“ (hier-ness): jüdische Autonomie in Osteuropa statt territorialer Staatsbildung in Palästina.","consequence":"Stärkste nicht-zionistische jüdische Bewegung bis zur Schoa; dauerhafte Gegenposition zum politischen Zionismus.","tier":["T1","T2"],"sources":[{"name":"Bund-Programm/Archiv","doc_id":"YIVO"},{"name":"Pickhan, Gegen den Strom (Bund)","doc_id":"2001"}],"doc_ref":"docs/01_ideologie_1882-1948.md (innerjüdische Kritik)"}
```

**GAP 3 — e35 · Brit Shalom (1925, Jerusalem): Buber/Magnes/Scholem · Cluster A · Phase II · Relevanz 5**
Fehlendes Ereignis: Binationale Zwei-Nationen-Lösung als innerzionistische Kritik an der Mehrheitslogik. DOPPELLÜCKE: fehlt nicht nur in phases.json, sondern auch vollständig in docs/01–06 (kein Treffer für Brit Shalom/Buber/Magnes/Ahad Ha'am).
Quellen: T1 Buber, *A Land of Two Peoples* (1983); Magnes, *Like All the Nations?* (1930). T2 Shlaim (2000); Laqueur (2003).
Formulierungsvorschlag:
```json
{"id":"e35","date":"1925","phase":"II","cluster":"A","core":false,"title":"Brit Shalom: binationale Zwei-Nationen-Lösung (Buber, Magnes)","actors":"Martin Buber, Judah L. Magnes, Gershom Scholem, Henrietta Szold","summary":"Innerzionistische Gruppierung für einen binationalen Staat mit gleichen Rechten für Juden und Araber; Kritik an der nationalstaatlichen Mehrheitslogik und der „Eisernen Mauer“.","consequence":"Wichtigste intellektuelle Gegenstimme zum Mehrheitsnationalismus; marginalisiert, aber bleibende Referenz der israelischen Friedensbewegung.","tier":["T1","T2"],"sources":[{"name":"Buber, A Land of Two Peoples","doc_id":"hg. P. Mendes-Flohr, 1983"},{"name":"Magnes, Like All the Nations?","doc_id":"1930"},{"name":"Shlaim, The Iron Wall","doc_id":"2000"}],"doc_ref":"docs/01_ideologie_1882-1948.md (innerjüdische Kritik) — NEU anzulegen"}
```

**GAP 4 — e36 · Operation Litani (14.3.–13.6.1978) · Cluster B · Phase IV · Relevanz 4**
Fehlendes Ereignis: Erste großflächige Libanon-Invasion nach dem Küstenstraßen-Massaker (11.3.1978); UNSC 425/426, UNIFIL. In docs/02 (Z.29) belegt.
Quellen: T1 UNSC 425/426. T2 Shlaim (2000); Morris (2001).
Formulierungsvorschlag:
```json
{"id":"e36","date":"14.3.–13.6.1978","phase":"IV","cluster":"B","core":false,"title":"Operation Litani: erste Libanon-Invasion und UNIFIL","actors":"Israel (IDF); PLO; UN-Sicherheitsrat","summary":"Vergeltungsinvasion Südlibanons nach dem Küstenstraßen-Massaker (11.3.1978); UNSC 425 fordert Rückzug, UNSC 426 errichtet UNIFIL.","consequence":"Israelischer Teilrückzug; de-facto-Sicherheitszone unter SLA/Haddad ab 1979; Beginn der 22-jährigen Libanon-Verstrickung.","tier":["T1","T2"],"sources":[{"name":"UNSC 425 / 426","doc_id":"S/RES/425 (1978), S/RES/426 (UNIFIL)"},{"name":"Shlaim, The Iron Wall","doc_id":"2000"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 2, Libanon)"}
```

**GAP 5 — e37 · Libanonkrieg 1982 + Sabra/Schatila (16.–18.9.1982) · Cluster B · Phase IV · Relevanz 5**
Fehlendes Ereignis: Das gravierendste fehlende Einzelereignis der Roadmap. UNSC 508/509/520; UNGA 37/123 D („act of genocide"); Kahan-Bericht (indirekte Verantwortung, Sharon-Rücktritt). In docs/02 (Z.30–31) und docs/03 (M15) belegt.
Quellen: T1 UNSC 508/509/520; UNGA 37/123 D; Kahan-Bericht. T2 Shlaim (2000); Morris (2001); Khalidi, *Under Siege* (1986).
Formulierungsvorschlag:
```json
{"id":"e37","date":"6.6.1982–1983 (Sabra/Schatila 16.–18.9.1982)","phase":"IV","cluster":"B","core":true,"title":"Libanonkrieg 1982 und das Massaker von Sabra/Schatila","actors":"Israel (Begin/Sharon); PLO; libanesische Phalange; UN","summary":"Großinvasion („Frieden für Galiläa“) mit dem Ziel der PLO-Vernichtung; Belagerung Beiruts; PLO-Abzug nach Tunis; Massaker von Sabra/Schatila (460–3.500 Tote) unter den Augen der IDF.","consequence":"UNGA 37/123 D stuft Sabra/Schatila als „act of genocide“ ein; Kahan-Bericht stellt indirekte Verantwortung Israels fest; Sharon-Rücktritt (1983); Hisbollah-Gründung als direkte Folge der Besatzung.","tier":["T1","T2"],"sources":[{"name":"UNSC 508/509/520","doc_id":"S/RES/508/509/520 (1982)"},{"name":"UNGA 37/123 D","doc_id":"A/RES/37/123D (16.12.1982)"},{"name":"Kahan Commission Report","doc_id":"8.2.1983 (JVL)"},{"name":"Khalidi, Under Siege","doc_id":"1986"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 2) · docs/03_klagekatalog_massaker.md (M15)"}
```

**GAP 6 — e38 · Golan-Gesetz 14.12.1981 + UNSC 497 (17.12.1981) · Cluster C · Phase IV · Relevanz 5**
Fehlendes Ereignis: Effektive Annexion der Golanhöhen; UNSC 497: „null and void and without international legal effect". Völkerrechtliches Pendant zu e30 (Jerusalem/UNSC 478). In docs/02 (Z.48) belegt.
Quellen: T1 Golan Heights Law; UNSC 497. T2 Shlaim (2000).
Formulierungsvorschlag:
```json
{"id":"e38","date":"14.12.1981 / 17.12.1981","phase":"IV","cluster":"C","core":false,"title":"Golan-Gesetz und UNSC 497: Annexion „null und nichtig“","actors":"Knesset (Golan-Gesetz 14.12.1981); UN-Sicherheitsrat (UNSC 497, 17.12.1981)","summary":"Israel wendet Recht und Verwaltung auf die besetzten Golanhöhen an; UNSC 497 erklärt die Maßnahme für „null and void and without international legal effect“.","consequence":"Internationale Nicht-Anerkennung der Annexion (Ausnahme: US 25.3.2019); jährliche UNGA-Bestätigung; bis heute völkerrechtlich offen.","tier":["T1","T2"],"sources":[{"name":"Golan Heights Law","doc_id":"14.12.1981"},{"name":"UNSC 497","doc_id":"S/RES/497 (17.12.1981)"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 4, Syrien/Golan)"}
```

**GAP 7 — e39 · Libanon-Rückzug (24.5.2000) + Blue Line (16.6.2000) · Cluster B · Phase V · Relevanz 4**
Fehlendes Ereignis: Ende der 22-jährigen Präsenz; UN bestätigt Rückzug gemäß UNSC 425 (S/2000/590). In docs/02 (Z.32) belegt.
Quellen: T1 UNSC 425; S/2000/590. T2 Shlaim (2000).
Formulierungsvorschlag:
```json
{"id":"e39","date":"24.5.2000 / 16.6.2000","phase":"V","cluster":"B","core":false,"title":"Israelischer Rückzug aus dem Libanon und Blue Line","actors":"Israel (Barak); Hisbollah; UN (S/2000/590)","summary":"Einseitiger Abzug Israels aus der Sicherheitszone; UN bestätigt Rückzug gemäß UNSC 425 und zieht die Blue Line (16.6.2000).","consequence":"Kollaps der SLA; Stärkung der Hisbollah; Shebaa-Farmen-Streit bleibt Konfliktherd (Vorfeld 2006).","tier":["T1","T2"],"sources":[{"name":"UNSC 425","doc_id":"S/RES/425 (1978, fortlaufend)"},{"name":"UN-Bericht Blue Line","doc_id":"S/2000/590 (16.6.2000)"}],"doc_ref":"docs/02_operationen_besatzung.md (Sicherheitszone 1985–2000)"}
```

**GAP 8 — e40 · Zweiter Libanonkrieg (12.7.–14.8.2006) · Cluster B · Phase V · Relevanz 5**
Fehlendes Ereignis: UNSC 1701; Winograd-Bericht („ohne klaren militärischen Sieg"); ~1.100–1.200 libanesische, 165 israelische Tote. Nur indirekt via e25 (Dahiya-Doktrin) gestreift. In docs/02 (Z.33) belegt.
Quellen: T1 UNSC 1701; Winograd-Bericht. T2 Shlaim (2000); Morris (2001).
Formulierungsvorschlag:
```json
{"id":"e40","date":"12.7.–14.8.2006","phase":"V","cluster":"B","core":true,"title":"Zweiter Libanonkrieg und UNSC 1701","actors":"Israel (Olmert); Hisbollah (Nasrallah); UN-Sicherheitsrat","summary":"Eskalation nach Hisbollah-Überfall (12.7.2006); 34-tägiger Krieg; UNSC 1701 fordert Waffenruhe und Hisbollah-Entwaffnung südlich des Litani.","consequence":"~1.100–1.200 libanesische und 165 israelische Tote; Winograd-Bericht (2008): „ohne klaren militärischen Sieg“; Geburtsstunde der Dahiya-Doktrin; unvollständige Hisbollah-Entwaffnung.","tier":["T1","T2"],"sources":[{"name":"UNSC 1701","doc_id":"S/RES/1701 (11.8.2006)"},{"name":"Winograd Commission Report","doc_id":"30.1.2008 (JVL)"}],"doc_ref":"docs/02_operationen_besatzung.md (2. Libanonkrieg) · docs/01 (Dahiya-Doktrin)"}
```

**GAP 9 — e41 · UNGA ES-10/23 (18.9.2024) · Cluster C · Phase VI · Relevanz 4**
Fehlendes Ereignis: Folgeresolution zum IGH-Gutachten 19.7.2024, die Israel auffordert, die unrechtmäßige Präsenz binnen 12 Monaten zu beenden. e22 erfasst IGH/ICC, aber nicht die datierte UNGA-Umsetzung.
Quellen: T1 A/RES/ES-10/23 (18.9.2024). T2 IGH-Gutachten 19.7.2024.
Formulierungsvorschlag:
```json
{"id":"e41","date":"18.9.2024","phase":"VI","cluster":"C","core":false,"title":"UNGA ES-10/23: Umsetzung des IGH-Gutachtens binnen 12 Monaten","actors":"UN-Generalversammlung (Notstandssession); Israel; Drittstaaten","summary":"Auf Basis des IGH-Gutachtens vom 19.7.2024 fordert die Resolution Israel auf, die unrechtmäßige Präsenz im besetzten Gebiet binnen 12 Monaten zu beenden; Drittstaaten zu Nicht-Anerkennung und Sanktionen verpflichtet.","consequence":"Völkerrechtliches Handlungsmandat mit Frist; verschärft die Pflichtenlage für Drittstaaten; Referenzpunkt der laufenden Verfahren.","tier":["T1","T2"],"sources":[{"name":"UNGA ES-10/23","doc_id":"A/RES/ES-10/23 (18.9.2024, UN Digital Library)"},{"name":"IGH Advisory Opinion","doc_id":"19.7.2024"}],"doc_ref":"docs/02_operationen_besatzung.md (Abschn. 1b) · docs/04_forschungsprotokoll.md §5"}
```

**Rangfolge (Priorisierung):** 1. e37 Libanon 1982/Sabra-Schatila (5) · 2. e40 2. Libanonkrieg 2006 (5) · 3. e38 Golan 1981/UNSC 497 (5) · 4. e35 Brit Shalom/Buber (5, Doppellücke) · 5. e36 Litani 1978 (4) · 6. e33 Pittsburgh 1885 + e34 Bund 1897 (4) · 7. e39 Libanon-Rückzug 2000 (4) · 8. e41 ES-10/23 (4).