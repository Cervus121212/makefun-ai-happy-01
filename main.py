"""Make the AI judge happy (make.fun bounty ai-happy-01).

Writes one image to /output/entry.png: a joyful golden retriever
puppy in a sunflower field at golden hour, with a daisy crown,
butterflies, and a steaming cup of tea.

The program is deliberately deterministic and offline: it copies the
bundled image (image.jpg, shipped in this repository) byte for byte,
so two runs always produce identical output. Standard library only,
no network, no randomness, no model calls.

Run:  python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

ASSET = Path(__file__).resolve().parent / "image.jpg"
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main() -> int:
    if not ASSET.is_file():
        print(f"missing bundled image: {ASSET}", file=sys.stderr)
        return 1
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ASSET, OUTPUT)
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    size = OUTPUT.stat().st_size
    print(f"wrote {OUTPUT} ({size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
