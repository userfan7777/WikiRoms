import re
from pathlib import Path

covers_dir = Path("covers")

pattern = re.compile(r"\[(PC[A-Z]{2}\d{5})\]", re.IGNORECASE)

renamed = 0
skipped = 0

for img in covers_dir.glob("*.png"):
    match = pattern.search(img.name)
    if not match:
        skipped += 1
        continue

    titleid = match.group(1).upper()
    new_name = f"{titleid}.png"
    new_path = covers_dir / new_name

    if new_path.exists():
        skipped += 1
        continue

    img.rename(new_path)
    renamed += 1

print(f"Renombradas: {renamed}")
print(f"Omitidas: {skipped}")
