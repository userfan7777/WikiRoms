import json
from pathlib import Path

covers = Path("covers")
files = [f.name for f in covers.glob("*.png")]

with open(covers / "index.json", "w", encoding="utf-8") as f:
    json.dump(files, f, indent=2, ensure_ascii=False)

print(f"✔ index.json creado con {len(files)} carátulas")
