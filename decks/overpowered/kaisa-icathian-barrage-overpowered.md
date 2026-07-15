# Kai'Sa Icathian Barrage (Overpowered)

## Snapshot

| Field | Value |
|---|---|
| Category | Overpowered |
| Legend | Kai'Sa - Daughter of the Void |
| Domains | Fury, Mind |
| Chosen champion | Kai'Sa - Survivor |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | `Icathian Rain` (3) |
| Difficulty | Medium-High |
| Core plan | Bonus Damage multiplies with *instances*, not spells. `Icathian Rain` is six separate "deal 2" instances — with `Annie - Fiery` in play that's 18 damage, at `Void Gate` it's 24, and `Ravenborn Tome` stacks another +6. The Legend adds a free spell-only rune every turn to keep the barrage firing, and `Kai'Sa - Evolutionary` recasts the best spell in the trash for free after every conquer. |

## Why This Is An Overpowered Deck

Like the lab's other overpowered lists (Master Yi, Kha'Zix), this deck
tests a scaling ceiling — here, the instance-multiplication rule
(confirmed in `simulations/SIM-0007-annie-vs-khazix-rules-smoke.md`,
rule 417.6.c territory: Void Gate boosts spell/ability damage per
instance, not per cast):

- `Annie - Fiery`: your spells and abilities deal 1 Bonus Damage — *per
  instance*;
- `Icathian Rain` (Kai'Sa's signature): "Deal 2 to a unit" printed six
  times — six instances, so every +1 source adds +6 total;
- `Bellows Breath`: up to three instances for 1 Energy, with [Repeat];
- `Falling Star` and `Crescent Strike`: multi-instance removal that the
  same multipliers turn into board wipes;
- `Kai'Sa - Daughter of the Void`: exhaust at reaction speed for a
  spell-only Any Rune — a free cast every turn;
- `Kai'Sa - Evolutionary`: on conquer, play a spell from your trash
  with Energy cost below your points, free — late game that means
  `Icathian Rain` again, every conquer;
- `Eager Apprentice` shaves every spell by 1 (no 4+-spend constraint
  here, unlike the Jhin deck — this deck *wants* discounts).

## Legality Notes

- Domain identity: Kai'Sa - Daughter of the Void is Fury/Mind. Every
  main deck card is single-domain Fury, single-domain Mind, or the
  Fury/Mind Signature card `Icathian Rain`.
- Copy-limit check: `Kai'Sa - Survivor` has 1 chosen-champion copy plus
  2 main deck copies (3 total, at the limit). No other card exceeds 3
  copies.
- Signature check: `Icathian Rain` (OGN-248) is Kai'Sa's own signature
  (printed directly after the Legend, OGN-247); 3 copies sit exactly at
  the 3-signature limit and match the Legend's tag.
- Banned/errata check: no card used here is marked Banned in the local
  card database. `Get Excited!` is intentionally excluded (whiffs as
  last card in hand — bug found in SIM-0001 lineage; see the Jinx deck's
  notes).
- Champion tag: `Kai'Sa - Survivor` and `Kai'Sa - Evolutionary` are
  inferred to carry the `Kai'Sa` champion tag from card name and the
  Legend's own name, per this project's convention. The source export
  has no explicit tag column — confirm the printed tag before
  tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Kai'Sa - Daughter of the Void | OGN-247 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Kai'Sa - Survivor | OGN-039 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Kai'Sa - Survivor | OGN-039 | Champion Unit | 4 |
| 2 | Kai'Sa - Evolutionary | OGN-112 | Champion Unit | 6 |
| 2 | Annie - Fiery | OGS-001 | Champion Unit | 5 |
| 3 | Ravenbloom Student | OGN-103 | Unit | 2 |
| 2 | Eager Apprentice | OGN-084 | Unit | 3 |
| 3 | Lecturing Yordle | OGN-087 | Unit | 3 |
| 2 | Riptide Rex | OGN-092 | Unit | 6 |
| 3 | Icathian Rain | OGN-248 | Signature Spell | 7 |
| 3 | Hextech Ray | OGN-009 | Spell | 1 |
| 2 | Incinerate | OGS-003 | Spell | 2 |
| 2 | Falling Star | OGN-029 | Spell | 2 |
| 2 | Monster Harpoon | UNL-014 | Spell | 1 |
| 2 | Void Seeker | OGN-024 | Spell | 3 |
| 2 | Bellows Breath | SFD-080 | Spell | 1 |
| 2 | Crescent Strike | UNL-072 | Spell | 3 |
| 2 | Downstage Dramatics | UNL-061 | Spell | 2 |
| 2 | Premonition | SFD-087 | Spell | 2 |
| 2 | Ravenborn Tome | OGN-032 | Gear | 3 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 5 | Fury Rune | OGN-007 |
| 7 | Mind Rune | OGN-089 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Void Gate | OGN-296 | +1 Bonus Damage per instance to units here — the deck's entire thesis as a battlefield. |
| Marai Spire | SFD-211 | Repeat costs 1 less: `Bellows Breath` repeats become nearly free instance batches. |
| The Candlelit Sanctum | OGN-291 | On-conquer topdeck filtering keeps the barrage fed between refuels. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Kai'Sa - Daughter of the Void | Legend | | | Exhaust: [Reaction] — Add Any Rune, only to play spells. | A free spell rune every turn, at reaction speed. |
| Kai'Sa - Survivor | Champion Unit | 4 | 4 | [Accelerate]. When I conquer, draw 1. | Chosen champion; the aggressive body that refuels the hand. |
| Kai'Sa - Evolutionary | Champion Unit | 6 | 6 | [Ganking]. On conquer, play a spell from trash with Energy cost < your points, free; then recycle it. | The late-game loop: every conquer replays the best spell you've cast. |
| Annie - Fiery | Champion Unit | 5 | 4 | Your spells and abilities deal 1 Bonus Damage (per instance). | The multiplier that turns Rain from 12 into 18. |
| Ravenbloom Student | Unit | 2 | 2 | When you play a spell, +1 Might this turn. | Early body that grows on the deck's every action. |
| Eager Apprentice | Unit | 3 | 3 | While at a battlefield, your spells cost 1 less (min 1). | The discount this shell wants (and the Jhin shell had to refuse). |
| Lecturing Yordle | Unit | 3 | 2 | [Tank]. On play, draw 1. | A cantripping wall to hold ground while the spells work. |
| Riptide Rex | Unit | 6 | 6 | On play, deal 6 to an enemy unit at a battlefield. | An ability instance too — Annie makes it deal 7. |
| Icathian Rain | Signature Spell | 7 | | Deal 2 to a unit ×6 (six separate instances). | The barrage: 12 base, 18 with Annie, 24 at Void Gate. |
| Hextech Ray | Spell | 1 | | [Action]. Deal 3 to a unit at a battlefield. | Efficient single instance; 4 with Annie. |
| Incinerate | Spell | 2 | | [Action]. Deal 2 to a unit at a battlefield. | Filler removal that multipliers upgrade. |
| Falling Star | Spell | 2 | | Deal 3 to a unit. Deal 3 to a unit. | Two instances — a 2-cost 8-damage split with Annie. |
| Monster Harpoon | Spell | 1 | | [Action]. Deal 2 (4 if you control a facedown card). | Cheap instance with upside. |
| Void Seeker | Spell | 3 | | [Action]. Deal 4, draw 1. | Removal that replaces itself. |
| Bellows Breath | Spell | 1 | | [Action]. [Repeat] 1 Energy + Mind Rune. Deal 1 to up to three units at one location. | Three instances per cast — the multipliers' favorite card. |
| Crescent Strike | Spell | 3 | | [Action]. Deal 4 to one enemy at a battlefield and 1 to each other enemy there. | Multi-instance sweep that Annie turns into 5 + 2s. |
| Downstage Dramatics | Spell | 2 | | [Reaction]. [Repeat] 2 Energy. Draw 1. | Draw that can wait for the Legend's spare rune. |
| Premonition | Spell | 2 | | [Reaction]. Draw 3. | Refuel. |
| Ravenborn Tome | Gear | 3 | | Exhaust: The next spell you play this turn deals 1 Bonus Damage. | A second +1-per-instance, on a repeatable gear. |

## How To Play

1. Early turns: cheap bodies plus efficient removal. Spend the Legend's
   spell rune every turn — it's a free `Hextech Ray` forever.
2. Position the fight at `Void Gate` when you can — every instance the
   deck fires gains +1 there.
3. The barrage turn: `Annie - Fiery` down, exhaust `Ravenborn Tome`,
   then `Icathian Rain` — six instances at 2+1+1 = 24 damage, split any
   way across up to six targets.
4. `Bellows Breath` with multipliers is the sleeper sweep: 1 Energy for
   three instances of 1+1(+1) — a 6-9 damage spray on token boards.
5. `Kai'Sa - Evolutionary` late: conquer, then replay `Icathian Rain`
   (or `Crescent Strike`) from the trash for free. With points at 8+,
   every attack is also your best spell again.
6. `Kai'Sa - Survivor` Accelerated keeps the conquer count and the
   cards flowing while the opponent answers spells instead of bodies.

## Mulligan

Keep:

- one or two cheap bodies (`Ravenbloom Student`, `Lecturing Yordle`);
- one cheap removal instance (`Hextech Ray`, `Monster Harpoon`,
  `Incinerate`);
- `Eager Apprentice` or `Premonition` to bridge to the barrage.

Avoid keeping multiple `Icathian Rain` in the opener — one is a plan,
two is a dead hand until turn 6.

## Watch Outs

- Bonus Damage applies **per damage instance** — but only to *your
  spells and abilities*. Combat damage gains nothing from Annie, the
  Tome, or Void Gate.
- `Icathian Rain`'s six instances can each pick any unit — including
  the same one — but each instance is dealt separately: a 3-Might unit
  eats two instances (with Annie), not one 18-point bolt. Overkill on
  one target wastes the rest.
- `Kai'Sa - Evolutionary` checks Energy cost **less than your points**
  — at 6 points she can't replay the 7-cost Rain yet. Count before
  promising yourself the loop.
- The Legend's rune is spell-only; it can't help deploy units.
- `Eager Apprentice` must be **at a battlefield** for its discount —
  in base it does nothing.
- Void Gate boosts damage **to units at Void Gate** — the multiplier
  follows the target's location, not the caster's.

## Upgrade Paths

- `Raging Firebrand` (next spell costs 5 less) makes turn-5 Rain
  possible — fine here, poison in the Jhin deck; the two shells must
  not be mixed casually.
- `Thousand-Tailed Watcher` is off-domain (Calm/Mind is Ahri's pair;
  the Watcher itself is Mind and legal) — its -3 shrink before a
  `Bellows Breath` spray converts damage into a full sweep.
- `Progress Day` and `Fate Weaver` deepen the refuel if games go long.
- Against go-tall decks, swap `Crescent Strike` for `Falling Comet`
  (one big instance beats many small ones into 8-Might bodies).
