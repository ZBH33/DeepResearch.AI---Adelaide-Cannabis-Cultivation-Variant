#!/usr/bin/env python3
"""
Refresh README folder map.
"""
import pathlib, datetime, textwrap
root = pathlib.Path(__file__).resolve().parents[1]
folders = [f.name + '/' for f in root.iterdir() if f.is_dir() and not f.name.startswith('.')]
map_block = "## Folder Map (" + datetime.date.today().isoformat() + ")\n\n" + \
            "\n".join(f"* `{name}`" for name in sorted(folders)) + "\n"
readme = root / "README.md"
text = readme.read_text(encoding="utf-8")
# Replace existing map (if any)
start = text.find("## Folder Map")
end   = text.find("\n##", start + 1)
if start != -1:
    new_text = text[:start] + map_block + text[end if end != -1 else len(text):]
else:  # no map yet, append
    new_text = text + "\n" + map_block
readme.write_text(new_text, encoding="utf-8")
