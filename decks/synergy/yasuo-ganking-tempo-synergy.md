# Yasuo Ganking Tempo (Synergy)

## Snapshot

| Field | Value |
|---|---|
| Category | Synergy |
| Legend | Yasuo - Unforgiven |
| Domains | Calm, Chaos |
| Chosen champion | Yasuo - Windrider |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | None |
| Difficulty | Medium |
| Core plan | Reposition units constantly with "on move" payoffs and the Legend's own free repositioning ability, generate card/resource value every time something moves, and let `Yasuo - Windrider` cash in a third move each turn for a bonus point. |

## Why This Is A Synergy Deck — And Why It Exists

Every prior deck built for this project either lacked `[Ganking]` entirely
(`decks/synergy/lucian-equipment-assault-synergy.md` has none, confirmed and
noted after `simulations/SIM-0004-teemo-vs-lucian-rules-smoke.md` found that
gap) or only used movement incidentally. This deck builds around movement on
purpose: `Yasuo - Windrider`, `Nocturne - Horrifying`, `Sivir - Mercenary`,
and `Kayn - Unleashed` all have `[Ganking]`, and a wide supporting cast of
units and spells trigger off "when I move" or "move a unit" as their core
text, not as an afterthought.

## Legality Notes

- Domain identity: Yasuo - Unforgiven is Calm/Chaos. Every main deck card is
  single-domain Calm, single-domain Chaos, or Colorless.
- Copy-limit check: `Yasuo - Windrider` has 1 chosen-champion copy plus 2
  main deck copies (3 total). No other card exceeds 3 copies.
- Signature check: no signature cards are included.
- Banned/errata check: no card used here is marked banned in the local card
  database.
- Champion tag: `Yasuo - Windrider` is inferred to carry the `Yasuo`
  champion tag from card name and the Legend's own name. The source export
  has no explicit tag column — confirm the printed tag before tournament
  play.
- **Well-supported reading, not a single explicit rule statement:** the
  Legend's own activated ability ("2 Energy, Exhaust: Move a friendly unit
  to or from its base") is an effect-caused Move (rule 444), not the
  target unit's own Standard Move (rule 144). Three separate rules point
  the same direction: Standard Move's cost is specifically "exhausting the
  *moved* unit" (rule 144.2, unique to that action); rule 444 describes
  effect-caused Moves as their own mechanism with their own stated costs,
  with no general "and it becomes exhausted" clause anywhere in rules
  440-448; and the closely related Recall rule states outright that
  "Exhausted Status... will remain unaffected" by a relocation unless the
  source of the effect says otherwise (rule 453.1). Taken together, this
  deck treats effect-caused Moves — including the Legend's own ability —
  as **not** exhausting the moved unit by default. Demonstrated in play in
  `simulations/SIM-0009-yasuo-vs-lillia-rules-smoke.md`, though no single
  rule states this in as many words for Moves specifically (only for the
  parallel Recall case), so it remains a reading rather than a citation.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Yasuo - Unforgiven | OGN-259 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Yasuo - Windrider | OGN-205 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Yasuo - Windrider | OGN-205 | Champion Unit | 5 |
| 2 | Nocturne - Horrifying | OGN-194 | Champion Unit | 4 |
| 2 | Sivir - Mercenary | SFD-143 | Champion Unit | 4 |
| 2 | Kayn - Unleashed | OGN-189 | Champion Unit | 6 |
| 3 | Ribbon Dancer | SFD-038 | Unit | 3 |
| 2 | Stellacorn Herder | SFD-048 | Unit | 4 |
| 3 | Mister Root | UNL-127 | Unit | 2 |
| 2 | Treasure Hunter | SFD-130 | Unit | 2 |
| 2 | Corrupt Enforcer | SFD-123 | Unit | 3 |
| 2 | Fae Porter | SFD-125 | Unit | 4 |
| 2 | Harpoon Squad | SFD-137 | Unit | 4 |
| 2 | Stealthy Pursuer | OGN-177 | Unit | 4 |
| 3 | Charm | OGN-043 | Spell | 1 |
| 2 | Ride the Wind | OGN-173 | Spell | 2 |
| 3 | Isolate | UNL-124 | Spell | 2 |
| 2 | Flash | OGS-011 | Spell | 2 |
| 2 | The Syren | OGN-184 | Gear | 2 |
| 2 | Forgotten Signpost | UNL-045 | Gear | 2 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 6 | Calm Rune | OGN-042 |
| 6 | Chaos Rune | OGN-166 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Windswept Hillock | OGN-297 | Grants Ganking to every unit here, letting even non-Ganking units in this list hop battlefields freely while they're at this one. |
| Star Spring | UNL-215 | The first non-token unit played here each turn can move another unit to base, adding a second move to the same turn for free. |
| Vilemaw's Lair | OGN-295 | Denies "move to base" specifically at this battlefield, which is irrelevant to units attacking out from it and can lock in a fight the deck wants to have. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Yasuo - Unforgiven | Legend | | | 2 Energy, Exhaust: Move a friendly unit to or from its base. | Free (Energy-only) repositioning outlet, separate from any unit's own Standard Move. |
| Yasuo - Windrider | Champion Unit | 5 | 4 | [Ganking]. The third time I move in a turn, you score 1 point. | Chosen champion; the deck's payoff for stacking several moves in one turn. |
| Nocturne - Horrifying | Champion Unit | 4 | 4 | [Ganking]. May banish itself off the top of the deck to play for Any Rune. | Mobile body with a cheap-cast option when drawn or revealed. |
| Sivir - Mercenary | Champion Unit | 4 | 4 | [Accelerate]. +2 Might and Ganking if you've spent Any Rune this turn. | Turns any Domain Power spend that turn into a mobile, bigger attacker. |
| Kayn - Unleashed | Champion Unit | 6 | 6 | [Ganking]. Takes no damage if it's moved twice this turn. | Big finisher that becomes hard to remove once it's already moved around. |
| Ribbon Dancer | Unit | 3 | 3 | On move to a battlefield, +1 Might to another friendly unit this turn. | Cheap mover with a built-in combat trick. |
| Stellacorn Herder | Unit | 4 | 3 | On move, draw 1. | Card advantage every time it repositions. |
| Mister Root | Unit | 2 | 1 | [Accelerate]. On move to a battlefield, gain 2 XP. | Cheap early mover; the XP isn't the deck's plan, just a side benefit. |
| Treasure Hunter | Unit | 2 | 1 | On move, play a Gold gear token exhausted. | Cheap mover that pays for itself in resources. |
| Corrupt Enforcer | Unit | 3 | 4 | On move to a battlefield, discard 1. On combat win, draw 1. | Efficient body with a move-triggered discard outlet and combat payoff. |
| Fae Porter | Unit | 4 | 4 | On move to a battlefield, may pay Chaos Rune to bring another unit along. | Moves two units for the price of one Move action. |
| Harpoon Squad | Unit | 4 | 4 | On move *from* a battlefield, +2 Might this turn. | Rewards retreating or repositioning away, not just arriving. |
| Stealthy Pursuer | Unit | 4 | 4 | When a friendly unit moves from its location, may move with it. | A second body that piggybacks on any other unit's move for free. |
| Charm | Spell | 1 | | Move an enemy unit. | Cheap disruption; can clear a blocker or separate a pair of enemy units. |
| Ride the Wind | Spell | 2 | | [Action]. Move a friendly unit and ready it. | Repositions and keeps the unit usable the same turn. |
| Isolate | Spell | 2 | | Move an enemy unit to base; draw 1 if it leaves a lone enemy unit behind. | Disruption that can also replace itself. |
| Flash | Spell | 2 | | [Reaction]. Move up to 2 friendly units to base. | Protects units from a bad fight or resets position defensively. |
| The Syren | Gear | 2 | | 1 Energy, Exhaust: move a friendly unit at a battlefield to base. | A second, repeatable move outlet independent of the Legend's own ability. |
| Forgotten Signpost | Gear | 2 | | Exhaust a unit, exhaust this: move a different unit to the exhausted one's location. | Repositions a unit without spending the Legend's ability or a card. |

## How To Play

1. Use cheap movers (`Mister Root`, `Treasure Hunter`, `Ribbon Dancer`) early
   to bank small value every time something relocates.
2. Get `Yasuo - Windrider` down and look for lines that string together
   three moves in one turn — the Legend's own ability, `The Syren`, and
   `Forgotten Signpost` all add moves without needing a unit's own Standard
   Move, so they can supplement `Yasuo - Windrider`'s own Ganking hops.
3. Use `Fae Porter` and `Stealthy Pursuer` to get two units moving off a
   single trigger, accelerating toward the third-move bonus.
4. Hold `Flash` and `Charm` as reactive tools — `Flash` protects your board
   from a bad fight, `Charm` can pull an enemy blocker out of position right
   before you commit an attacker.
5. Land `Kayn - Unleashed` once the deck is already generating multiple
   moves a turn — its damage immunity kicks in as a natural side effect of
   the deck's own gameplan.

## Mulligan

Keep:

- one cheap mover: `Mister Root`, `Treasure Hunter`, or `Ribbon Dancer`;
- one disruption spell: `Charm` or `Isolate`;
- one Ganking payoff: `Yasuo - Windrider` or `Sivir - Mercenary`, only with
  an early mover already in hand to support it.

Avoid keeping `Kayn - Unleashed` without any early movement pieces —
it needs the deck's plan already running to earn its damage immunity.

## Watch Outs

- The Legend-ability-doesn't-exhaust-the-moved-unit reading above is this
  deck's working assumption, not a confirmed ruling — verify it before
  relying on "move and still attack the same turn" as a guaranteed line.
- `Yasuo - Windrider`'s bonus point needs a literal third move *in the same
  turn* — moves from different turns don't add up toward it.
- `Sivir - Mercenary`'s bonus requires spending Domain Power ("Any Rune")
  that turn specifically, not just Energy — a turn that only spends Energy
  doesn't turn it on.
- `Harpoon Squad`'s bonus triggers on moving *away*, the opposite timing
  from most of this deck's other payoffs — don't expect it to reward
  arriving somewhere.

## Upgrade Paths

- Add `Megatusk` (Chaos) to grant an entire board Ganking for a turn instead
  of relying on individual Ganking units.
- Add more Domain Power sinks if `Sivir - Mercenary`'s bonus condition feels
  hard to hit consistently.
- For a lower-complexity version, cut `Fae Porter` and `Stealthy Pursuer`
  (both ask for multi-unit sequencing) and keep only the single-unit move
  payoffs.
