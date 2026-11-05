#!/usr/bin/env python3
"""Report em dash and en dash characters in UTF-8 files."""
import argparse
from pathlib import Path

FORBIDDEN = {"\u2014": "em dash", "\u2013": "en dash"}

def violations(text):
    return [(line_no, col_no, FORBIDDEN[ch])
            for line_no, line in enumerate(text.splitlines(), 1)
            for col_no, ch in enumerate(line, 1)
            if ch in FORBIDDEN]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    found = False
    for path in args.files:
        for line, col, kind in violations(path.read_text(encoding="utf-8")):
            print(f"{path}:{line}:{col}: {kind}")
            found = True
    return int(found)

if __name__ == "__main__":
    raise SystemExit(main())
