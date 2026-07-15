#!/usr/bin/env python3
"""Validate Riftbound deck profile files against the local card database.

Checks per deck file:
- main deck table sums to exactly 40;
- rune deck table sums to exactly 12;
- every (name, card ID) pair in Legend / Chosen Champion / Main Deck /
  Rune Deck tables exists in riftbound_cards_organized.md;
- no card is marked Banned in the database;
- copy limit: no name exceeds 3 total copies counting the chosen champion;
- signature limit: at most 3 Signature-supertype cards, with a heuristic
  champion-tag check (a signature's card ID should sit within 3 IDs after
  a Legend of the same champion name in the same set).

Usage: python3 scripts/validate_decks.py [deck-file ...]
Defaults to all decks/**/*.md except README files.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "riftbound_cards_organized.md"


def load_db():
    cards = {}     # (name, id) -> row dict
    by_id = {}     # id -> row dict
    for line in DB.read_text().splitlines():
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 14:
            continue
        name, cid, setname, typ, supertype = parts[1:6]
        banned = parts[12]
        if typ not in ("Unit", "Spell", "Gear", "Legend", "Battlefield", "Rune"):
            continue
        row = {
            "name": name, "id": cid, "set": setname, "type": typ,
            "super": supertype, "banned": banned == "Yes",
        }
        cards.setdefault((name, cid), row)
        by_id.setdefault(cid, row)
    return cards, by_id


ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([A-Z]{3}[A-Z0-9-]*)\s*\|")


def parse_deck(path):
    """Return dict of section -> list of (count, name, id)."""
    sections = {}
    current = None
    for line in path.read_text().splitlines():
        h = line.strip()
        if h.startswith("### "):
            current = h[4:].strip()
            sections.setdefault(current, [])
            continue
        if h.startswith("## "):
            current = None
            continue
        if current:
            m = ROW_RE.match(line)
            if m:
                sections[current].append(
                    (int(m.group(1)), m.group(2).strip(), m.group(3).strip())
                )
    return sections


def sig_owner_ok(sig_row, legend_rows, by_id):
    """Heuristic: signature ID must sit within +1..+3 of a same-set Legend ID
    belonging to this deck's Legend champion."""
    m = re.match(r"([A-Z]+)-(\d+)", sig_row["id"])
    if not m:
        return False
    prefix, num = m.group(1), int(m.group(2))
    for lr in legend_rows:
        lm = re.match(r"([A-Z]+)-(\d+)", lr[2])
        if lm and lm.group(1) == prefix and 1 <= num - int(lm.group(2)) <= 3:
            return True
    return False


def validate(path, cards, by_id):
    errs, warns = [], []
    secs = parse_deck(path)
    main = secs.get("Main Deck", [])
    runes = secs.get("Rune Deck", [])
    legend = secs.get("Legend", [])
    chosen = secs.get("Chosen Champion", [])

    if sum(c for c, _, _ in main) != 40:
        errs.append(f"main deck totals {sum(c for c, _, _ in main)}, expected 40")
    if sum(c for c, _, _ in runes) != 12:
        errs.append(f"rune deck totals {sum(c for c, _, _ in runes)}, expected 12")
    if len(legend) != 1:
        errs.append(f"expected exactly 1 Legend row, found {len(legend)}")
    if len(chosen) != 1:
        errs.append(f"expected exactly 1 Chosen Champion row, found {len(chosen)}")

    all_rows = legend + chosen + main + runes
    for cnt, name, cid in all_rows:
        row = cards.get((name, cid))
        if row is None:
            if cid in by_id:
                errs.append(f"name/ID mismatch: '{name}' vs {cid} "
                            f"(DB has '{by_id[cid]['name']}')")
            else:
                errs.append(f"unknown card: '{name}' {cid}")
            continue
        if row["banned"]:
            errs.append(f"banned card: '{name}' {cid}")

    # copy limit: chosen champion + main deck, by name
    counts = {}
    for cnt, name, cid in chosen + main:
        counts[name] = counts.get(name, 0) + cnt
    for name, total in counts.items():
        if total > 3:
            errs.append(f"copy limit exceeded: '{name}' x{total}")

    # signature limit + tag heuristic
    sig_total = 0
    for cnt, name, cid in main:
        row = cards.get((name, cid))
        if row and row["super"] == "Signature":
            sig_total += cnt
            if not sig_owner_ok(row, legend, by_id):
                warns.append(f"signature '{name}' {cid} does not sit directly "
                             f"after this deck's Legend ID; verify champion tag")
    if sig_total > 3:
        errs.append(f"signature limit exceeded: {sig_total} > 3")

    return errs, warns


def main():
    cards, by_id = load_db()
    if len(sys.argv) > 1:
        files = [Path(a).resolve() for a in sys.argv[1:]]
    else:
        files = sorted(p for p in (ROOT / "decks").rglob("*.md")
                       if p.name != "README.md")
    failures = 0
    for f in files:
        errs, warns = validate(f, cards, by_id)
        status = "FAIL" if errs else "OK  "
        print(f"{status} {f.relative_to(ROOT)}")
        for e in errs:
            print(f"     ERROR {e}")
        for w in warns:
            print(f"     WARN  {w}")
        failures += bool(errs)
    print(f"SUMMARY files={len(files)} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
