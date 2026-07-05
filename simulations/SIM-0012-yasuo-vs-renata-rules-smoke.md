# SIM-0012: Yasuo Ganking Tempo vs Renata Gold Engine

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0012 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 3 rounds by design — shorter than prior sims since it produced its key finding early |
| Purpose | Second test for Yasuo; confirms `Windswept Hillock`'s granted Ganking actually enables a cross-battlefield attack in real play. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Yasuo. Second player: Renata
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation, same documented deterministic
  shortcut as prior sims): `Windswept Hillock` for Yasuo, `Treasure Hoard`
  for Renata.
- Both opening hands kept. Yasuo: `Mister Root`, `Treasure Hunter`,
  `Ribbon Dancer`, `Isolate` (plus draws). Renata: `Plundering Poro`,
  `Honest Broker`, `Blood Money`, `Trifarian Gloryseeker` (plus draws).

## Turn Log

### Turn 1

- **Yasuo**: Channels 2. Plays `Mister Root` for 2 Energy. Score 0.
- **Renata**: Channels 3 (extra rune). Plays `Plundering Poro` for 2
  Energy. Score 0.

### Turn 2

- **Yasuo**: Plays `Treasure Hunter` for 2 Energy. Moves `Mister Root` to
  `Windswept Hillock` (uncontrolled → conquers, scores 1).
- **Renata**: Plays `Honest Broker` for 2 Energy. Moves `Plundering Poro`
  to `Treasure Hoard` (uncontrolled → conquers, scores 1; makes a Gold
  token).

Score: Yasuo 1, Renata 1.

### Turn 3

- **Yasuo**: Holds `Windswept Hillock` → scores 1 (1 → 2). Plays
  `Ribbon Dancer` for 3 Energy. Moves `Treasure Hunter` to join
  `Mister Root` at `Windswept Hillock` (on-move: makes a Gold token).
  **Tests the battlefield's own passive directly**: `Mister Root` has no
  printed `[Ganking]`, but `Windswept Hillock`'s text ("Units here have
  Ganking") grants it while present. Moves `Mister Root` **directly from
  `Windswept Hillock` to `Treasure Hoard`** — a genuine Battlefield-to-
  Battlefield Move, legal only with Ganking (rule 144.4.c). The granted
  keyword is checked live at the moment of the move (consistent with the
  "static conditions re-check continuously" finding from SIM-0006), and
  it works: `Honest Broker` (Might 2, exhausted but still a legal Combat
  participant) is there, so this stages Combat. Both pass. Combat Damage:
  `Mister Root` (Might 1) deals 1 to `Honest Broker` (survives); `Honest
  Broker` deals 2 to `Mister Root` (dies). A losing trade tactically — 1
  Might attacking into 2 Might is a bad attack — but it cleanly confirms
  the mechanic itself works exactly as the deck file's Battlefield
  Recommendation claims.
- **Renata**: Holds `Treasure Hoard` → scores 1 (1 → 2); pays 1 Energy for
  another Gold token. Plays `Trifarian Gloryseeker` (first card, Legion
  inactive) and `Watchful Sentry`.

Score: Yasuo 2, Renata 2.

## Findings

### Confirmed — A Granted Keyword Enables The Same Actions As A Printed One, Checked Live

`Windswept Hillock`'s "Units here have Ganking" isn't just flavor text for
units that already have it printed — it directly enabled a genuine
Battlefield-to-Battlefield Move for a unit with no Ganking of its own,
confirming the deck file's own claim about this battlefield in actual
play. The move was legal because Ganking was present *at the moment the
Move was declared* (the unit was still at `Windswept Hillock` when it
qualified), consistent with granted/static abilities being continuously
re-checked rather than snapshotted.

### Strategic Note, Not A Rules Finding

The attack itself was a poor trade (1 Might into a 2 Might defender) —
worth remembering that Ganking enables *reaching* a fight, it doesn't make
that fight worth having. The mechanic working correctly and the tactical
decision being sound are two different things; this sim confirmed the
former, not the latter.

## Recommended Next Step

Stop here — three rounds was enough to produce and confirm the specific
mechanic this sim was run to test. No deck-file fix needed; the Windswept
Hillock recommendation in `decks/synergy/yasuo-ganking-tempo-synergy.md`
already correctly describes this behavior.