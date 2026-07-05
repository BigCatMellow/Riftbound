# SIM-0009: Yasuo Ganking Tempo vs Lillia Sprite Swarm

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0009 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 4 rounds by design |
| Purpose | First test for both of these new decks. Deliberately exercises the Yasuo deck's flagged-but-unconfirmed Legend-move assumption, and surfaces a significant, previously-undocumented timing gap in the Lillia deck's own token plan. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Yasuo. Second player: Lillia
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation, same documented deterministic
  shortcut as prior sims): `Windswept Hillock` for Yasuo, `The Grand Plaza`
  for Lillia.
- Both opening hands kept. Yasuo: `Mister Root`, `Charm`, `Ribbon Dancer`,
  `Treasure Hunter` (plus draws). Lillia: `Sprite Mother`, `Desert's Call`,
  `Trevor Snoozebottom`, `Sprite Fountain` (plus draws).

## Turn Log

### Turn 1

- **Yasuo**: Channels 2. Plays `Mister Root` for 2 Energy. Score 0.
- **Lillia**: Channels 3 (extra rune). Plays `Sprite Fountain` for 2
  Energy — enters Ready (Gear), its on-play effect makes a **ready** 3
  Might Sprite token to base immediately (`[Temporary]`). Score 0.

### Turn 2

- **Yasuo**: Plays `Ribbon Dancer` for 3 Energy. Moves `Mister Root` to
  `Windswept Hillock` (uncontrolled → conquers, scores 1). Its "units here
  have Ganking" passive doesn't matter yet since `Mister Root` already used
  its one move this turn.
- **Lillia**: Plays `Trevor Snoozebottom` for 3 Energy. Moves the ready
  Sprite token to `The Grand Plaza` (uncontrolled → conquers, scores 1).
  Plays `Desert's Call` for 2 Energy, making an exhausted 2 Might Sand
  Soldier token in base (no "ready" override on this card, unlike the
  Sprite-specific ones).

Score: Yasuo 1, Lillia 1.

### Turn 3

- **Yasuo**: Holds `Windswept Hillock` → scores 1 (1 → 2). Plays
  `Fae Porter` for 4 Energy. Moves `Ribbon Dancer` to join `Mister Root` at
  `Windswept Hillock`; its on-move effect gives `Mister Root` +1 Might this
  turn. **Exercises the deck's flagged assumption**: activates the Legend's
  "2 Energy, Exhaust: Move a friendly unit to or from its base" on the
  now-buffed `Mister Root`, moving it from `Windswept Hillock` to base.
  Consistent with the deck file's reasoning, this does **not** exhaust
  `Mister Root` (the Legend's own Exhaust and 2 Energy are the stated cost,
  not the moved unit's own exhausting) — `Mister Root` arrives at base
  still Ready. Its own Standard Move is then used to send it right back to
  `Windswept Hillock` (exhausting itself this time, the normal Standard
  Move cost). Net result: `Mister Root` moved twice this turn, once "for
  free" via the Legend and once via its own action — this is the clearest
  practical demonstration of the assumption so far, though it remains an
  assumption, not a confirmed rule. Its temporary +1 Might buff persists
  through the round trip since Base and Battlefields are both part of "The
  Board" (rule 106-107) — only moving to/from a Non-Board Zone clears
  temporary modifications (rule 110), and this shuffle never left the
  Board.
- **Lillia**: Holds `The Grand Plaza`... or does she? **See Findings below
  — this hold does not actually score.** Plays `Sprite Mother` directly to
  the now-uncontrolled `The Grand Plaza`, which applies Contested the same
  way a Move would; Non-Combat Showdown, both pass, Lillia conquers it
  (first time scoring this specific battlefield *this* turn), scores 1
  (1 → 2). Its on-play effect makes another ready 3 Might Sprite token at
  the same location, giving `The Grand Plaza` a non-Temporary unit
  (`Sprite Mother`) alongside a Temporary one this time.

Score: Yasuo 2, Lillia 2.

### Turn 4

- **Yasuo**: Holds `Windswept Hillock` → scores 1 (2 → 3). Plays
  `Kayn - Unleashed` for 6 Energy.
- **Lillia**: Beginning Phase: the Turn 3 Sprite token dies (Temporary,
  "before scoring"), but `Sprite Mother` — not Temporary — is still there,
  so `The Grand Plaza` **stays controlled** this time, and the hold scores
  1 (2 → 3) normally. Plays `Zilean - Time Mage` for 5 Energy directly to
  `The Grand Plaza`, positioning to double a future token play there.

Score: Yasuo 3, Lillia 3.

## Findings

### Significant Deck Finding — Solo Temporary Tokens Cannot Hold Into Their Own Next Scoring Tick

Turn 3's Lillia sequence exposed something the Lillia deck file didn't
anticipate: a `[Temporary]` token's own death clause is worded "Kill it at
the start of the controller's Beginning Phase, **before scoring**." Turn
Phase order is Awaken → Beginning (Beginning Step, then Scoring Step)
(rule 315.1-315.2.b). The Temporary kill lands in the Beginning Step,
strictly before the Scoring Step that checks for holds. That means:

- A lone Temporary token that conquered a battlefield on one turn will
  **always die at the very start of its controller's next Beginning
  Phase**, before that same Beginning Phase's Scoring Step can credit a
  hold — so it can never score a hold on its controller's following turn
  by itself, no matter how uncontested the battlefield is.
- The battlefield becomes uncontrolled the moment the token dies (same
  Cleanup-driven Control loss confirmed in SIM-0001/0005/0007), so unless
  another non-Temporary unit is also there, the hold attempt fails
  entirely — not "scores less," but doesn't happen at all.
- This is exactly why replaying `Sprite Mother` at `The Grand Plaza` (a
  non-Temporary unit) fixed the problem on the very next turn: once a
  permanent unit shares the location, the Temporary token's death no
  longer costs Control.

This directly changes the deck's actual game plan: **Temporary tokens are
conquer tools and combat bodies for the turn they're made, not a hold
plan** — a real pilot needs a non-Temporary unit at any battlefield they
intend to hold across turns. Recommend adding this to the deck's Watch
Outs explicitly, since the original deck file's description of the Legend
and its token generators didn't flag this timing trap.

### Rules Finding — Playing A Card Directly To An Uncontrolled Battlefield Applies Contested The Same Way Moving There Does

Playing `Sprite Mother` straight to `The Grand Plaza` (rather than playing
it to base and moving it later) still triggered Contested → Non-Combat
Showdown → Conquer, the same sequence a Move would cause. Arriving at a
location you don't control applies Contested regardless of whether the
unit got there by being Played or by Moving.

### Follow-Up Resolution — Legend Move Doesn't Exhaust The Moved Unit

Turn 3 demonstrated the Yasuo deck's flagged reading in a concrete
double-move line (Legend move, then a Standard Move back), and a temporary
buff correctly survived the Base↔Battlefield round trip since neither zone
is a Non-Board Zone (rule 110 only clears temporary modifications on a
Non-Board Zone transition). After this sim, a closer re-read of rules
440-448 and 453.1 (prompted by codex-lab-zola's reminder to keep this
caveated absent a direct citation) found stronger support than "assumption"
implies: Standard Move's cost is specifically "exhausting the unit"
(rule 144.2, unique to that action); effect-caused Moves (rule 444) are a
separate mechanism with no general exhaust clause anywhere in rules
440-448; and the closely related Recall rule states outright that
"Exhausted Status... will remain unaffected" by a relocation unless the
source says otherwise (rule 453.1). Together these support treating
effect-caused Moves as not exhausting their target by default — upgraded
in `decks/synergy/yasuo-ganking-tempo-synergy.md` from "flagged assumption"
to "well-supported reading." No single rule states this in as many words
for Moves specifically (only for the parallel Recall case), so it's a
reading backed by three converging citations, not a direct quote.

## Recommended Next Step

Stop here; the Temporary-token hold-timing finding is significant enough on
its own to justify a deck-file fix. Apply that fix, then continue testing
these two decks further only if a future balance question specifically
needs it.

## Follow-Up

- Add a Watch Out to `decks/synergy/lillia-sprite-swarm-synergy.md`: a
  Temporary token cannot hold a battlefield into its controller's next
  scoring tick by itself — it dies at the start of that Beginning Phase,
  before the Scoring Step. Pair token conquers with a non-Temporary unit at
  the same location before relying on holding it.