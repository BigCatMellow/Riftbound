# SIM-0003: Rumble Mech Tribal vs Kha'Zix XP Burst

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0003 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline, same session as driver) |
| Status | Stopped after 5 rounds by design — see Recommended Next Step |
| Purpose | New deck combination (both new decks from the second batch), and resolve two rules questions this project had previously avoided: Domain Power cost payment, and multi-unit Combat Damage assignment. |

## Why This Pairing

`decks/synergy/rumble-mech-tribal-synergy.md` (Fury/Mind) vs
`decks/overpowered/khazix-xp-burst-overpowered.md` (Body/Chaos) — no shared
domain, no shared cards, and it puts a token-width deck against an
XP-economy deck for the first time. It also forced two rules questions
SIM-0002 had explicitly flagged and routed around:

- SIM-0002 avoided every card with a "1 Energy + [Domain] Rune" cost because
  it couldn't confirm how the Domain Rune part of that cost is paid. Both of
  these decks lean on that exact pattern (`Assembly Rig`'s activated ability,
  `Doran's Blade`-style `[Equip] Body Rune` cards would have the same
  question). This sim resolves it before touching either deck again.
- Neither prior sim had more than one unit on a side of a Combat. This sim's
  Turn 5 combat has three attackers against one defender, which needed the
  actual Combat Damage assignment rule instead of the simple 1-for-1 math
  used so far.

## Mode And Setup Assumptions

Source: `Riftbound_Core_Rules_RUP3_Staging.pdf`.

- Mode: 1v1 Duel, Victory Score 8. First player: Rumble. Second player:
  Kha'Zix — one extra Rune on their first Channel Phase only (rule 480.7).
- Draws 4, mulligan up to 2 (rule 117-118). Both hands kept as drawn.
- Battlefields chosen: `Marai Spire` (SFD-211) for Rumble,
  `Sunken Temple` (SFD-218) for Kha'Zix — the first-listed recommendation in
  each deck file. Both start uncontrolled (rule 445, same precedent as
  SIM-0001/0002).
- **Newly resolved this sim:** a Domain Power cost written as a bare Rune
  name (e.g. `[Equip] Body Rune`, or the "Fury Rune" half of
  "1 Energy + Fury Rune") is paid by **Recycling** a Rune of that Domain —
  not by exhausting it. Rule 818.1.c ("Equip is formatted as 'Equip
  [Cost]'") plus rule 163.2 (a Basic Rune's two abilities: `[E]: Reaction —
  Add [1]` [Energy, paid by exhausting] vs. `Recycle this: Reaction — Add
  [C]` [Domain Power, paid by Recycling]) together make this unambiguous:
  the plain-Energy ability exhausts the rune and leaves it on the board;
  the Domain-Power ability permanently Recycles the rune off the board (to
  the bottom of the Rune Deck). A cost naming a specific Domain (not the
  generic "[C]" symbol, but literally "Fury Rune" or "Body Rune" as
  printed) draws on the second ability, so paying it is a real, board-state
  cost, not just a tap.
- **Also newly confirmed:** Gear enters the board **Ready** (rule 149.1,
  rule 359.2.d — "If it is a Gear, it enters the Board Ready at the
  player's Base"), unlike Units, which enter exhausted (rule 143.4). A
  Gear's own Exhaust-cost activated ability can be used the same turn it's
  played.

## Known Simulation Limitations

- Manual replay, not a full engine, same as SIM-0001/0002.
- Battlefield selection used each deck file's first-listed recommendation
  deterministically rather than `references/simulation-playtest-protocol.md`'s
  documented method (choose exactly three, then randomly select one). Both
  deck files already list exactly three battlefields, so this is a
  documented shortcut for reproducibility, not a rules violation — a real
  game should still randomize among the three.
- Stops after 5 rounds by design, once the two open rules questions above
  were resolved and a genuinely new combat shape (3 attackers vs. 1
  defender) had been played out correctly.

## Deterministic Setup

### Rumble (Fury, Mind)

Opening hand (kept, no mulligan): `Forecaster`, `Danger Zone`,
`Icevale Archer`, `Hextech Ray`.

Battlefield: `Marai Spire`.

### Kha'Zix (Body, Chaos)

Opening hand (kept, no mulligan): `Gemhand Hunter`, `Grim Resolve`,
`Mister Root`, `On the Hunt`.

Battlefield: `Sunken Temple`.

## Turn Log

### Turn 1: Rumble

- Channel: `Fury Rune`, `Mind Rune`.
- Draw: `Bubble Bot`.
- Main: plays `Forecaster` to base using 2 Energy. Enters exhausted
  (rule 143.4).
- End state: score 0. Base: exhausted `Forecaster`. Hand: `Danger Zone`,
  `Icevale Archer`, `Hextech Ray`, `Bubble Bot`.

### Turn 1: Kha'Zix

- Channel: `Body Rune`, `Body Rune`, `Chaos Rune` (2 base + 1 for going
  second).
- Draw: `Voracious Gromp`.
- Main: plays `Gemhand Hunter` to base using 2 Energy. Enters exhausted.
  `[Hunt]` dormant (not at a battlefield). 1 Energy left over, unused.
- End state: score 0, XP 0. Base: exhausted `Gemhand Hunter`. Hand:
  `Grim Resolve`, `Mister Root`, `On the Hunt`, `Voracious Gromp`.

### Turn 2: Rumble

- Awaken: readies `Forecaster` and channeled Runes.
- Channel: `Fury Rune`, `Mind Rune`.
- Draw: `Chakram Dancer`.
- Main:
  - Plays `Bubble Bot` to base using 3 Energy. Enters exhausted. Its "ready
    another friendly Mech" trigger fires on play — but Rumble has no actual
    Mech-type unit in play yet (`Forecaster` and `Bubble Bot` are Mech
    *support* cards, not Mechs themselves — this matters later, see
    Findings), so it fizzles with no legal target.
  - Moves ready `Forecaster` from base to `Marai Spire`, exhausting it.
    Uncontrolled → Non-Combat Showdown → both pass → Rumble conquers,
    scores 1.
- End state: score 1. Controls `Marai Spire` (exhausted `Forecaster`). Base:
  exhausted `Bubble Bot`. Hand: `Danger Zone`, `Icevale Archer`,
  `Hextech Ray`, `Chakram Dancer`.

### Turn 2: Kha'Zix

- Awaken: readies `Gemhand Hunter` and channeled Runes.
- Channel: `Body Rune`, `Chaos Rune`.
- Draw: `Crowd Favorite`.
- Main:
  - Plays `Voracious Gromp` to base using 5 Energy. Enters exhausted.
    `[Hunt 3]` dormant.
  - Moves ready `Gemhand Hunter` from base to `Sunken Temple`, exhausting
    it. Uncontrolled → Non-Combat Showdown → both pass → Kha'Zix conquers,
    scores 1. `Gemhand Hunter`'s `[Hunt]` triggers: gain 1 XP (0 → 1).
    `Sunken Temple`'s own ability needs a **Mighty** (5+ Might) unit
    involved in the conquer — `Gemhand Hunter` is only Might 2, so it does
    not trigger here.
- End state: score 1, XP 1. Controls `Sunken Temple` (exhausted
  `Gemhand Hunter`). Base: exhausted `Voracious Gromp`. Hand: `Grim Resolve`,
  `Mister Root`, `On the Hunt`, `Crowd Favorite`.

### Turn 3: Rumble

- Awaken: readies `Bubble Bot` and channeled Runes.
- Beginning: holds `Marai Spire` (rule 464.2) → scores 1 (1 → 2).
  `Marai Spire`'s own effect (Repeat costs cost 1 less) is a passive, not a
  hold-trigger, so nothing fires from holding specifically.
- Channel: 2 more Runes.
- Draw: `Assembly Rig`.
- Main: plays `Chakram Dancer` to base using 3 Energy. Enters exhausted.
  `Bubble Bot` is also at base, so "give your other units here Shield this
  turn" applies to it — a wasted trigger this turn since `Bubble Bot` isn't
  defending, but not an error. 3 Energy left, not enough for `Assembly Rig`
  (cost 4); held.
- End state: score 2. Controls `Marai Spire` (ready `Forecaster`, untouched
  this turn). Base: exhausted `Chakram Dancer`, ready `Bubble Bot`. Hand:
  `Danger Zone`, `Icevale Archer`, `Hextech Ray`, `Assembly Rig`.

### Turn 3: Kha'Zix

- Awaken: readies `Voracious Gromp` and channeled Runes.
- Beginning: holds `Sunken Temple` → scores 1 (1 → 2). Still no bonus —
  `Sunken Temple`'s ability is Conquer-specific, not Hold-specific, so it
  never fires on a hold at all, regardless of Might.
- Channel: 2 more Runes.
- Draw: `Insightful Investigator`.
- Main:
  - Plays `Crowd Favorite` to base using 3 Energy. Enters exhausted.
  - Moves ready `Voracious Gromp` (Might 5) from base to `Marai Spire`,
    exhausting it. Rumble controls it with `Forecaster` (Might 2, ready)
    present — Combat stages (rule 447, 456). Attacker = Kha'Zix; Defender =
    Rumble.
  - Both pass. Combat Damage: `Voracious Gromp` deals 5 to `Forecaster`
    (Might 2) → dies. `Forecaster` deals 2 to `Voracious Gromp` (Might 5)
    → survives.
  - Combat Cleanup: only Kha'Zix's unit remains at `Marai Spire` → Kha'Zix
    conquers it from Rumble, scores 1 (2 → 3). `Voracious Gromp`'s
    `[Hunt 3]` triggers: gain 3 XP (1 → 4). Heals `Voracious Gromp`'s 2
    damage.
- End state: score 3, XP 4. Controls `Marai Spire` (exhausted
  `Voracious Gromp`, healed) and `Sunken Temple` (ready `Gemhand Hunter`).
  Base: exhausted `Crowd Favorite`. Hand: `Grim Resolve`, `Mister Root`,
  `On the Hunt`, `Insightful Investigator`.

### Turn 4: Rumble

- Awaken: readies `Bubble Bot`, `Chakram Dancer`, and channeled Runes.
- Beginning: `Marai Spire` was lost last turn, no hold. No score.
- Channel: 2 more Runes.
- Draw: `Blue Sentinel`.
- Main:
  - Plays `Assembly Rig` to base using 4 Energy. **Enters Ready** (rule
    149.1/359.2.d, confirmed above — Gear, unlike Units, doesn't enter
    exhausted).
  - Immediately activates it: cost is "1 Energy + Fury Rune, Recycle a unit
    from your trash, Exhaust." Pays 1 Energy (any rune), Recycles a Fury
    Rune specifically for its Fury Power (permanently removing that rune
    from the board — see the resolved rules question above), Recycles
    `Forecaster` from the trash (Rumble's only dead unit so far) back to
    the bottom of the Main Deck, and exhausts `Assembly Rig` itself. Plays
    a 3 Might Mech unit token to base — Rumble's **first actual Mech**
    (`Forecaster`, `Bubble Bot`, and `Chakram Dancer` are Mech-support
    cards, not Mechs themselves — see Findings). Enters exhausted
    (rule 143.4/181.1, no override stated).
- End state: score 2 (unchanged). Base: exhausted `Assembly Rig`, exhausted
  3-Might Mech token, ready `Bubble Bot`, ready `Chakram Dancer`. Hand:
  `Danger Zone`, `Icevale Archer`, `Hextech Ray`, `Blue Sentinel`.

### Turn 4: Kha'Zix

- Awaken: readies `Voracious Gromp` (at `Marai Spire`), `Gemhand Hunter`
  (at `Sunken Temple`), `Crowd Favorite` (at base).
- Beginning: holds `Marai Spire` → scores 1 (3 → 4). Holds `Sunken Temple`
  → scores 1 more (4 → 5).
- Channel: 2 more Runes.
- Draw: `Kha'Zix - Evolving Hunter` (the Chosen Champion card).
- Main:
  - Plays `Kha'Zix - Evolving Hunter` from the Champion Zone using 5
    Energy. Enters exhausted in base.
  - Plays `Insightful Investigator` to base using 3 Energy. Enters
    exhausted. On play, chooses Rumble as the target opponent: Rumble
    reveals their hand; pays 2 XP (4 → 2) to choose a card from it —
    chooses `Blue Sentinel` — Rumble discards it and draws a replacement
    (`Curtain Call`).
- End state: score 5, XP 2. Controls `Marai Spire` (ready `Voracious
  Gromp`) and `Sunken Temple` (ready `Gemhand Hunter`). Base: exhausted
  `Kha'Zix - Evolving Hunter`, exhausted `Insightful Investigator`, ready
  `Crowd Favorite`. Hand: `Grim Resolve`, `Mister Root`, `On the Hunt`.

### Turn 5: Rumble

- Awaken: readies `Assembly Rig`, the Mech token, `Bubble Bot`,
  `Chakram Dancer`.
- Beginning: no battlefield controlled, no score.
- Channel: 2 more Runes.
- Draw: `Void Seeker`.
- Main: moves the ready 3-Might Mech token, `Bubble Bot` (Might 3), and
  `Chakram Dancer` (Might 3) from base to `Sunken Temple` simultaneously
  (rule 144.3, same destination, exhausting all three as the cost).
  `Gemhand Hunter` (Might 2, ready) is there — Combat stages. All three of
  Rumble's units gain the Attacker designation (rule 459.2.b.3, since they
  all belong to the player who applied Contested); `Gemhand Hunter` is the
  sole Defender.
  - Both pass. Combat Damage Step (rule 460.2): sum Attacker Might
    (3 + 3 + 3 = 9); sum Defender Might (2). Rumble assigns 9 damage —
    `Gemhand Hunter` is the only Defender, so per rule 460.2.c.4 ("cannot
    assign more than lethal... unless no further units remain") all 9 goes
    onto it since there's nowhere else to put it; it dies with 7 damage to
    spare. Kha'Zix assigns 2 damage among the 3 Might Attackers — none of
    them reach lethal (3 Might each) from 2 damage, so the 2 damage goes
    onto the Mech token, which survives.
  - Combat Cleanup: only Rumble's units remain at `Sunken Temple` →
    conquers it from Kha'Zix, scores 1 (2 → 3). Heals the Mech token's 2
    damage.
- End state: score 3. Controls `Sunken Temple` (exhausted Mech token,
  `Bubble Bot`, `Chakram Dancer`). Base: ready `Assembly Rig` (not
  reactivated this turn). Hand: `Danger Zone`, `Icevale Archer`,
  `Hextech Ray`, `Curtain Call`, `Void Seeker`.

## Score After 5 Rounds

- Rumble: 3.
- Kha'Zix: 5, XP 2 (spent 2 of the 4 it had banked).

## Findings

### Deck File Finding — A Real Gap, Not Just A Pacing Note

`Forecaster`, `Bubble Bot`, and `Chakram Dancer` are Mech-*support* cards —
their text says "your Mechs" or "another friendly Mech," meaning they
reference Mechs as a category **other than themselves**. None of them are
Mech-type units. Rumble had zero actual Mechs in play until Turn 4, when
`Assembly Rig`'s activated ability finally produced one. That means for
three full rounds, `Rumble - Mechanized Menace`'s Shield-grant and
(once drawn) `Rumble - Scrapper`'s +1 Might do **nothing at all**, because
there's no Mech on board yet to receive either bonus. This is a real
sequencing gap worth calling out in the deck file directly, not just a
"the deck is a bit slow" note — a new pilot could easily play three support
pieces in a row and wonder why the Legend's own ability hasn't done
anything.

### Rules Findings (New Since SIM-0001/0002)

- **Resolved a real open question from SIM-0002**: a bare Domain-name cost
  (`[Equip] Body Rune`, or the "Fury Rune" half of "1 Energy + Fury Rune")
  is paid by *Recycling* a matching Rune — a real, permanent cost (rule
  818.1.c, rule 163.2.b) — not by simply exhausting it for generic Energy
  (rule 163.2.a). These are two different abilities on the same Basic Rune
  card, and the cost text tells you which one it's calling on.
- **Gear enters the board Ready**, not exhausted (rule 149.1, 359.2.d) —
  this is different from Units, which always enter exhausted (rule 143.4).
  A Gear with an Exhaust-cost activated ability (like `Assembly Rig`) can
  use that ability the same turn it's played.
- **Multi-unit Combat Damage assignment confirmed** (rule 460.2): each side
  sums the Might of all its Attackers or Defenders, then the Attacker
  assigns their total among the Defender's units (and vice versa),
  completing lethal damage on one unit before moving to the next, and never
  over-assigning past lethal unless no other unit is left to receive the
  excess. A lopsided fight (3 attackers vs. 1 defender) dumps all the
  excess onto that lone defender rather than being "wasted."

## Recommended Next Step

Stop here; the two open rules questions this sim was run to resolve are
answered, and the Mech-support-vs-Mech-type gap is now a documented finding.
Continuing this specific game to a real winner isn't necessary unless a
balance claim needs to rest on it — Kha'Zix's 5-3 lead so far comes mostly
from winning the Turn 3 fight and a well-timed hand-disruption play, not
from a structural imbalance between the two decks.

## Follow-Up

- Add a line to `decks/synergy/rumble-mech-tribal-synergy.md` clarifying
  which cards are Mech-support versus actual Mechs, and recommending the
  pilot prioritize getting at least one real Mech (via `Production Surge`,
  `Assembly Rig`, `Ferrous Forerunner`, `Mega-Mech`, `Breakneck Mech`, or
  `Rumble - Scrapper`'s hold trigger) before leaning on support pieces.