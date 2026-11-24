#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (at most 200 characters) to
<output>/entry.txt, where <output> is $MAKEFUN_OUTPUT_DIR or /output.
Standard library only; deterministic; no network.
"""

import os

# The roast: a phone with cavernous storage that still makes its owner
# delete family photos to install an update nobody asked for.
LINE = (
    "My phone has 256 gigabytes of storage and still makes me delete "
    "photos of my own family to install an update I never asked for."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1..200 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
