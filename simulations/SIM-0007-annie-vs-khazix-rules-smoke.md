# SIM-0007: Annie Spell Burn vs Kha'Zix XP Burst

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0007 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 4 rounds by design |
| Purpose | Sample-size batch; both decks share the Chaos domain but no cards, and neither had been paired against a spell-heavy deck's bonus-damage math before. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Annie. Second player: Kha'Zix
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation, same documented deterministic
  shortcut as prior sims): `Void Gate` for Annie, `Sunken Temple` for
  Kha'Zix.
- Both opening hands kept. Annie: `Blast Corps Cadet`, `Hextech Ray`,
  `Mystic Poro`, `Incinerate` (plus draws). Kha'Zix: `Gemhand Hunter`,
  `Mister Root`, `Grim Resolve`, `Voracious Gromp` (plus draws).

## Turn Log

### Turn 1

- **Annie**: Channels 2. Plays `Blast Corps Cadet` for 2 Energy (not paying
  its optional additional cost). Score 0.
- **Kha'Zix**: Channels 3 (extra rune). Plays `Gemhand Hunter` for 2
  Energy. Score 0, XP 0.

### Turn 2

- **Annie**: Plays `Mystic Poro` for 2 Energy. Moves `Blast Corps Cadet` to
  `Void Gate` (uncontrolled → conquers, scores 1).
- **Kha'Zix**: Plays `Voracious Gromp` for 5 Energy. Moves `Gemhand Hunter`
  to `Sunken Temple` (uncontrolled → conquers, scores 1; `[Hunt]` gains 1
  XP).

Score: Annie 1, Kha'Zix 1.

### Turn 3

- **Annie**: Holds `Void Gate` → scores 1 (1 → 2). Plays chosen champion
  `Annie - Fiery` from the Champion Zone for 5 Energy.
- **Kha'Zix**: Holds `Sunken Temple` → scores 1 (1 → 2). Plays
  `Crowd Favorite` for 3 Energy. Moves `Voracious Gromp` (Might 5) to
  `Void Gate`, contesting `Blast Corps Cadet` (Might 2, ready) — Combat
  stages.
  - Both pass. **`Void Gate`'s "Spells and abilities deal 1 Bonus Damage to
    units here" does not apply to this fight** — Combat damage's source is
    the participating Units themselves, not a spell or ability
    (rule 417.6.c: "Damage Dealt as a result of being assigned during
    Combat has the Units as its source"), so the battlefield's bonus never
    triggers on plain combat damage. `Voracious Gromp` deals 5 to
    `Blast Corps Cadet` (dies); `Blast Corps Cadet` deals 2 to
    `Voracious Gromp` (survives).
  - Combat Cleanup: only Kha'Zix's unit remains — conquers `Void Gate` from
    Annie, scores 1 (2 → 3). `[Hunt 3]` — wait, `Voracious Gromp`'s
    Hunt is on conquer or hold, and it conquered here, so it fires: gain 3
    XP (1 → 4). Heals its 2 marked damage.

Score: Annie 2, Kha'Zix 3, XP 4.

### Turn 4

- **Annie**: Lost `Void Gate`, no hold. Plays `Incinerate` targeting
  `Gemhand Hunter` at `Sunken Temple` — this **is** a spell, so
  `Annie - Fiery`'s "your spells and abilities deal 1 Bonus Damage" applies
  normally (2 → 3 total), same distinction as above but confirming the
  positive case: spell damage gets the bonus, combat damage doesn't.
  `Gemhand Hunter` (Might 2) dies. At the following Cleanup, `Sunken Temple`
  becomes uncontrolled (Kha'Zix has no units left there — same
  "loses Control the moment the last unit is gone" precedent from
  SIM-0001/0005, now confirmed for spell-based removal specifically, not
  only combat). Moves `Annie - Fiery` there afterward, in the same turn:
  now-uncontrolled → Non-Combat Showdown → both pass → Annie conquers,
  scores 1 (2 → 3).
- **Kha'Zix**: Holds `Void Gate` → scores 1 (3 → 4). Plays `Mister Root` for
  2 Energy. Plays `Insightful Investigator` for 3 Energy — its text is
  "choose an opponent, **they reveal their hand**. You may pay 2 XP to
  choose a card from it..." The reveal is unconditional; the optional
  discard is XP-gated. Kha'Zix only has 1 XP banked (needs 2), so Annie
  still reveals her hand (real information for Kha'Zix), but no card is
  discarded since the optional clause can't be paid for.

Score: Annie 3, Kha'Zix 4.

## Findings

- **Bonus-damage-to-"spells and abilities" effects never apply to Combat
  damage.** Both `Void Gate`'s battlefield bonus and `Annie - Fiery`'s
  Legend-style bonus are worded around spells and abilities specifically,
  and rule 417.6.c makes the Units themselves the source of Combat damage —
  so these effects boost `Incinerate` but never boost a unit's raw attack
  or defense damage. Worth remembering any time a deck (like this Annie
  list) leans on "my bonus damage" language — it's a spell-and-ability
  buff, not a combat buff.
- **Losing your last unit at a battlefield to a spell works the same way
  as losing it in combat** — Control is lost at the next Cleanup either
  way, confirmed here for `Incinerate` specifically rather than only mass
  removal like `Firestorm` in SIM-0001.
- **An unconditional clause before an optional XP/cost-gated clause still
  happens even when the optional part can't be paid for.** `Insightful
  Investigator`'s hand-reveal isn't part of the "you may pay" sentence, so
  it fires regardless of whether the XP cost that follows it is affordable.

## Recommended Next Step

Stop here; three clean rules findings in four rounds, none of them repeats
of prior sims. No rerun needed.