# Ahri Shrink and Sweep (Advanced)

## Snapshot

| Field | Value |
|---|---|
| Category | Advanced |
| Legend | Ahri - Nine-Tailed Fox |
| Domains | Calm, Mind |
| Chosen champion | Ahri - Alluring |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | `Fox-Fire` (3) |
| Difficulty | High |
| Core plan | Never race — dissolve. The Legend shrinks every attacker into your battlefields; stacked -Might effects turn their board into 1-Might husks; and `Fox-Fire` reads "kill any number of units with **total** Might 4 or less," so four shrunken units die to one 3-cost spell. Meanwhile `Ahri - Alluring` converts each quiet hold into a point. |

## Why This Is An Advanced Deck

Most removal in this game is damage. This deck's removal is *subtraction*,
and subtraction stacks with everything:

- `Ahri - Nine-Tailed Fox` gives every attacker into your battlefields
  -1 Might, automatically, forever;
- Shield/Tank defenders (`Mutated Mouser` defends as a 3 for 2 Energy)
  beat shrunken attackers in ordinary combat math;
- `Vilemaw` stops units with less Might than him from dealing combat
  damage at all — after a `Smoke Screen` or `Thousand-Tailed Watcher`,
  that is usually the whole battlefield;
- `Fox-Fire` counts **total current Might**: four units shrunk to 1 each
  are a legal, lethal target — the sweep is sized by how hard you
  shrank, not how big they were;
- and the deck never needed to attack: `Ahri - Alluring` scores a point
  per hold, `Grove of the God-Willow` draws per hold, and `Iascylla`
  drags fresh victims into the kill zone.

## Legality Notes

- Domain identity: Ahri - Nine-Tailed Fox is Calm/Mind. Every main deck
  card is single-domain Calm, single-domain Mind, or the Calm/Mind
  Signature card `Fox-Fire`.
- Copy-limit check: `Ahri - Alluring` has 1 chosen-champion copy plus 2
  main deck copies (3 total, at the limit). No other card exceeds 3
  copies.
- Signature check: `Fox-Fire` (OGN-256) is Ahri's own signature (printed
  directly after the Legend, OGN-255); 3 copies sit exactly at the
  3-signature limit and match the Legend's tag.
- Banned/errata check: no card used here is marked Banned in the local
  card database.
- Champion tag: `Ahri - Alluring` and `Ahri - Inquisitive` are inferred
  to carry the `Ahri` champion tag from card name and the Legend's own
  name, per this project's convention. The source export has no explicit
  tag column — confirm the printed tag before tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Ahri - Nine-Tailed Fox | OGN-255 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Ahri - Alluring | OGN-066 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Ahri - Alluring | OGN-066 | Champion Unit | 5 |
| 3 | Ahri - Inquisitive | OGN-119 | Champion Unit | 3 |
| 3 | Mutated Mouser | UNL-036 | Unit | 2 |
| 2 | Blastcone Fae | OGN-097 | Unit | 2 |
| 2 | Sunlit Guardian | OGN-054 | Unit | 3 |
| 2 | Iascylla | UNL-050 | Unit | 7 |
| 2 | Vilemaw | UNL-060 | Unit | 8 |
| 2 | Thousand-Tailed Watcher | OGN-116 | Unit | 7 |
| 3 | Fox-Fire | OGN-256 | Signature Spell | 3 |
| 3 | Stupefy | OGN-095 | Spell | 1 |
| 3 | Smoke Screen | OGN-093 | Spell | 2 |
| 2 | Frigid Touch | SFD-066 | Spell | 2 |
| 2 | Eclipse | UNL-063 | Spell | 3 |
| 1 | Moonlight Affliction | UNL-066 | Spell | 7 |
| 2 | Premonition | SFD-087 | Spell | 2 |
| 2 | Block | OGN-057 | Spell | 2 |
| 2 | Meditation | OGN-048 | Spell | 2 |
| 2 | Orb of Regret | OGN-090 | Gear | 1 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 5 | Calm Rune | OGN-042 |
| 7 | Mind Rune | OGN-089 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Grove of the God-Willow | OGN-280 | Holding draws a card — the deck's whole game plan, paid by the turn. |
| Fortified Position | OGN-279 | Defending grants [Shield 2] — one more +2/-2 swing in combat math that already favors you. |
| Bandle Tree | OGN-278 | An extra hidden slot for `Fox-Fire` and `Block`, so the sweep costs zero Energy exactly when the shrink lands. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Ahri - Nine-Tailed Fox | Legend | | | Enemy unit attacks a battlefield you control → it gets -1 Might this turn (min 1). | The ambient tax. Every combat starts a point in your favor. |
| Ahri - Alluring | Champion Unit | 5 | 4 | When I hold, you score 1 point. | Chosen champion; the win condition that never has to attack. |
| Ahri - Inquisitive | Champion Unit | 3 | 3 | When I attack or defend, give an enemy unit here -2 Might this turn (min 1). | A body whose every combat shrinks someone — stacks with the Legend to -3. |
| Mutated Mouser | Unit | 2 | 1 | [Shield 2]. [Tank]. | Defends as a 3 for 2 Energy; against shrunken attackers, wins outright. |
| Blastcone Fae | Unit | 2 | 2 | [Hidden]. On play, give a unit -2 Might this turn (min 1). | Shrink at reaction speed from facedown — showdown maths ambush. |
| Sunlit Guardian | Unit | 3 | 3 | [Shield]. [Tank]. | The second wall. |
| Iascylla | Unit | 7 | 6 | When I hold, at the start of your next Main Phase you may move an enemy unit to this battlefield. | Drags victims into the kill zone — into the Legend's tax, Vilemaw's shadow, and Fox-Fire range. |
| Vilemaw | Unit | 8 | 8 | [Ambush]. Enemy units here with less Might than me don't deal combat damage. When I hold, draw 1. | After any shrink, "less Might than 8" is everyone — the battlefield goes silent. |
| Thousand-Tailed Watcher | Unit | 7 | 7 | [Accelerate]. On play, give enemy units -3 Might this turn (min 1). | The board-wide shrink that sets up the biggest Fox-Fire turns. |
| Fox-Fire | Signature Spell | 3 | | [Hidden]. [Action]. Kill any number of units at a battlefield with **total** Might 4 or less. | The sweep. Total, not each: four 1-Might husks die to one cast. |
| Stupefy | Spell | 1 | | [Reaction]. -1 Might this turn (min 1). Draw 1. | The cheapest possible nudge over a kill threshold, cantripped. |
| Smoke Screen | Spell | 2 | | [Reaction]. Give a unit -4 Might this turn (min 1). | Turns their finisher into a husk mid-combat. |
| Frigid Touch | Spell | 2 | | [Reaction]. [Repeat] 2 Energy. -2 Might this turn. | Scalable shrink; the Repeat buys exactly the amount you need. |
| Eclipse | Spell | 3 | | [Reaction]. -4 Might this turn. [Predict]. | Smoke Screen's twin with topdeck smoothing attached. |
| Moonlight Affliction | Spell | 7 | | [Reaction]. Give a unit -10 Might this turn. | Deletes any one attacker from combat math; sets up Fox-Fire on a giant. |
| Premonition | Spell | 2 | | [Reaction]. Draw 3. | Fuel. |
| Block | Spell | 2 | | [Hidden]. [Action]. Give a unit [Shield 3] and [Tank] this turn. | The other half of combat math — your side goes up while theirs goes down. |
| Meditation | Spell | 2 | | [Reaction]. Exhaust a friendly unit → draw 2; else draw 1. | Holding units are exhausted anyway — the cost is often free. |
| Orb of Regret | Gear | 1 | | Exhaust: Give a unit -1 Might this turn (min 1). | A shrink you never have to redraw — one per turn, forever. |

## How To Play

1. Deploy walls early (`Mutated Mouser`, `Sunlit Guardian`) and take
   battlefields the opponent isn't contesting. You want to be the
   defender everywhere.
2. Let the Legend and cheap shrinks make every attack into you a bad
   trade. Spend -Might effects *inside* combat, after attackers commit.
3. Hide `Fox-Fire` early (`Bandle Tree` helps). The kill window is the
   moment their units are shrunk — usually right after `Thousand-Tailed
   Watcher` lands or a `Smoke Screen` resolves.
4. Count Fox-Fire targets by *current total* Might: three attackers at
   -1 from the Legend plus one `Stupefy` is often exactly 4.
5. Land `Ahri - Alluring` once you hold two battlefields; from there the
   game ends on schedule without a single attack.
6. `Iascylla` and `Vilemaw` make one battlefield a death zone — drag
   their best unit in, silence it, shrink it, sweep it.

## Mulligan

Keep:

- two cheap defenders (`Mutated Mouser`, `Sunlit Guardian`,
  `Blastcone Fae`);
- one cheap shrink (`Stupefy`, `Smoke Screen`, `Orb of Regret`);
- `Premonition` or `Meditation` for fuel.

Avoid keeping multiple 7-8 drops; the walls have to hold the early game
first.

## Watch Outs

- **The minimum-1 floor cuts both ways**: nothing shrinks below 1, so
  `Fox-Fire` on four husks needs total 4 exactly — a fifth unit puts the
  pile at 5 and the whole cast is illegal. Choose "any number" carefully.
- All the shrinks are "this turn": Fox-Fire must land **the same turn**
  as the shrink effects, not the turn after.
- The Legend triggers only on attacks into battlefields **you control**
  — it does nothing while you're the attacker, which this deck almost
  never wants to be anyway.
- `Vilemaw` compares *current* Might: a buffed attacker can cross back
  over him mid-combat if you let a pump resolve unanswered.
- `Meditation`'s exhaust cost can't be paid by a unit you need ready to
  defend — pay with a holder that already did its job.
- `Ahri - Alluring` scores on *her* hold, so she must be at the held
  battlefield when it scores, not resting in base.

## Upgrade Paths

- `Mageseeker Warden` (opponents can only play units to their base;
  spells can't ready their units) locks the door completely in a slower
  meta.
- `Leona - Zealot` plus stun effects is a sister package (-8 Might to
  stunned enemies here) if the deck drifts toward Calm-heavy control.
- `The List` (name a tag, repeatable -2) answers champion-tribal decks.
- `Alpha Wildclaw` protects the walls from targeted removal if opponents
  start going around combat.
