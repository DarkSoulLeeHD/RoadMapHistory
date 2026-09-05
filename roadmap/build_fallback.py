#!/usr/bin/env python3
"""build_fallback.py — bettet roadmap/phases.json + roadmap/debunks.json als Offline-Fallback
in roadmap/index.html ein (file://-Betrieb ohne Webserver).
Aufruf:  python3 roadmap/build_fallback.py   (idempotent, nach jeder JSON-Änderung ausführen)"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
HTML = ROOT / "index.html"
SOURCES = [
    (ROOT / "phases.json",  'script type="application/json" id="fallback-phases"'),
    (ROOT / "debunks.json", 'script type="application/json" id="fallback-debunks"'),
]

def main():
    html = HTML.read_text(encoding="utf-8")
    for json_path, tag_start in SOURCES:
        data = json.loads(json_path.read_text(encoding="utf-8"))          # validiert
        payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")  # </script>-sicher
        start = "<" + tag_start + ">"
        pat = re.compile(re.escape(start) + r".*?" + re.escape("</script>"), re.S)
        if not pat.search(html):
            sys.exit(f"FEHLER: Fallback-Block {tag_start} nicht in index.html gefunden.")
        html, n = pat.subn(start + payload + "</script>", html, count=1)
        key = json_path.name
        print(f"OK: {key}: {len(data.get('events') or data.get('debunks') or [])} Einträge eingebettet.")
    HTML.write_text(html, encoding="utf-8")
    print("index.html aktualisiert.")

if __name__ == "__main__":
    main()
