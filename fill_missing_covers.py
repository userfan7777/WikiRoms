import json
import shutil
from pathlib import Path

with open("games.json", "r", encoding="utf-8") as f:
    games = json.load(f)

covers = Path("covers")
default = covers / "default.png"

for g in games:
    target = covers / f"{g['title_id']}.png"
    if not target.exists():
        shutil.copy(default, target)

print("✔ Default asignado a todas las carátulas faltantes")
