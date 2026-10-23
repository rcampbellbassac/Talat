"""Rebuild the font: python scripts/build.py (needs the reference fonts; see family.BASES)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fontlab_mcp import family
root = Path(__file__).resolve().parents[1]
spec = json.loads((root / 'recipe.json').read_text())
print(family.build_family(spec, root / 'fonts'))
