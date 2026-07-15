# Vi Excess Damage Aggro (Synergy)

## Snapshot

| Field | Value |
|---|---|
| Category | Synergy |
| Legend | Vi - Piltover Enforcer |
| Domains | Fury, Order |
| Chosen champion | Vi - Peacekeeper |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | None |
| Difficulty | Medium |
| Core plan | Strip the blocker with stuns and removal, swing with Assault attackers so the conquer is nearly all excess damage, then cash that excess damage in three separate times: the Legend's free unit-ready, `Yeti Brawler`'s Gold gear tokens, and `Tryndamere - Barbarian`'s point. |

## Why This Is A Synergy Deck

`Vi - Piltover Enforcer`'s "When you conquer, if you assigned 3 or more
excess damage, you may exhaust me to ready a unit" only pays off when a
conquer leaves an opponent's blocker dealt with cheaply — a fair 1-for-1
trade produces little or no excess damage. Every stun in this list
(`Vi - Peacekeeper`'s and `Leona - Determined`'s on-attack stun, `Solari
Chief`'s stun-or-kill, `Heroic Charge`'s stun-plus-buff) exists to remove
the blocker's ability to fight back so the attacker's full Might becomes
excess damage instead of getting traded off. `Yeti Brawler` (3+ excess
damage) and `Tryndamere - Barbarian` (5+ excess damage) read the exact
same battlefield state as the Legend and turn it into Gold gear tokens
or a scored point, so a single well-set-up conquer can trigger two or
three payoffs from one attack.

## Legality Notes

- Domain identity: Vi - Piltover Enforcer is Fury/Order. Every main deck
  card is single-domain Fury or single-domain Order.
- Copy-limit check: `Vi - Peacekeeper` has 1 chosen-champion copy plus 2
  main deck copies (3 total, at the limit). No other card exceeds 3
  copies.
- Signature check: no Signature cards are included. Signature cards must
  match the Champion Legend's tag, and Vi's own signature (`Hextech
  Gauntlets`, UNL-188 — the card printed directly after the Legend) has
  an incomplete stat line in the local card database, so it is left out
  rather than included with unverified text. An earlier revision of this
  file wrongly ran `Void Rush` (Rek'Sai's signature) and `Noxian
  Guillotine` (Darius's signature); those never matched Vi's tag and
  were removed.
- Banned/errata check: no card used here is marked Banned in the local
  card database.
- Champion tag: `Vi - Peacekeeper` is inferred to carry the `Vi`
  champion tag from card name and the Legend's own name, following this
  project's existing convention (see `draven-assault-aggro-synergy.md`).
  The source export has no explicit tag column — confirm the printed tag
  before tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Vi - Piltover Enforcer | UNL-187 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Vi - Peacekeeper | UNL-176 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Vi - Peacekeeper | UNL-176 | Champion Unit | 5 |
| 3 | Vayne - Hunter | OGN-035 | Champion Unit | 4 |
| 3 | Lucian - Gunslinger | SFD-028 | Champion Unit | 3 |
| 2 | Rek'Sai - Breacher | SFD-029 | Champion Unit | 3 |
| 3 | Sharkling | UNL-006 | Unit | 3 |
| 3 | Chemtech Enforcer | OGN-003 | Unit | 2 |
| 2 | Inferna | UNL-002 | Unit | 2 |
| 2 | Captain Farron | OGN-015 | Unit | 4 |
| 2 | Lord Broadmane | UNL-012 | Unit | 5 |
| 2 | Leona - Determined | OGN-238 | Unit | 4 |
| 3 | Solari Chief | OGN-225 | Unit | 5 |
| 2 | Tryndamere - Barbarian | OGN-034 | Unit | 7 |
| 2 | Yeti Brawler | UNL-018 | Unit | 6 |
| 3 | Blood Rush | SFD-003 | Spell | 1 |
| 3 | Cleave | OGN-004 | Spell | 1 |
| 3 | Heroic Charge | UNL-155 | Spell | 3 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 8 | Fury Rune | OGN-007 |
| 4 | Order Rune | OGN-214 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Trapping Grounds | UNL-217 | Names the exact same "3+ excess damage" condition as the Legend, so a single qualifying conquer here doubles up on payoffs. |
| Trifarian War Camp | OGN-294 | A flat Might buff for units here, including attackers, makes it easier to clear the 3-5 excess damage thresholds this deck is built around. |
| The Candlelit Sanctum | OGN-291 | On-conquer card selection smooths draws for a deck that wants specific stun/removal pieces online before it commits to a big attack. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Vi - Piltover Enforcer | Legend | | | When you conquer, if you assigned 3+ excess damage, you may exhaust me to ready a unit. | Converts a clean, one-sided conquer into a free extra attacker or blocker. |
| Vi - Peacekeeper | Champion Unit | 5 | 5 | [Ambush]. When I attack, stun an enemy unit here. | Chosen champion; strips a blocker before combat so the attack becomes excess damage instead of a trade. |
| Vayne - Hunter | Champion Unit | 4 | 2 | [Assault 3]. Enters ready if the opponent controls a battlefield. May bounce itself on conquer for 1 Energy. | Cheap body that swings for 5 while attacking and can reset to hand to dodge removal after conquering. |
| Lucian - Gunslinger | Champion Unit | 3 | 2 | [Assault]. On attack, deal damage equal to my Assault to an enemy unit here. | Pings a blocker down before combat damage, making it easier to push the fight to a clean win. |
| Rek'Sai - Breacher | Champion Unit | 3 | 3 | [Accelerate]. [Assault]. Friendly units played from elsewhere than hand have Accelerate. | A ready attacker on curve; its granted-Accelerate clause mostly matters if the deck adds recursion later. |
| Sharkling | Unit | 3 | 1 | [Accelerate]. [Assault 4]. | Enters ready and swings for 5 while attacking off a 3-cost body — a large Might swing to push excess damage. |
| Chemtech Enforcer | Unit | 2 | 2 | [Assault 2]. On play, discard 1. | Cheap early attacker; the discard is a minor cost, not a payoff in this build. |
| Inferna | Unit | 2 | 1 | [Ambush]. [Assault 2]. | Cheap surprise attacker that can reinforce a fight the same turn it's played. |
| Captain Farron | Unit | 4 | 5 | Other friendly units here have Assault. | A local anthem that turns every ally at its battlefield into an attacker threat. |
| Lord Broadmane | Unit | 5 | 5 | [Ambush]. On play, other units here get Assault this turn. | A one-turn version of Captain Farron's effect, timed right before a big attack. |
| Leona - Determined | Unit | 4 | 4 | [Shield]. When I attack, stun an enemy unit here. | A second on-attack stun, so the deck can strip a blocker even without the Chosen Champion in play. |
| Solari Chief | Unit | 5 | 4 | On play, choose an enemy unit: kill it if stunned, otherwise stun it. | Turns any of this deck's own stuns into a kill, or stuns a fresh target itself. |
| Tryndamere - Barbarian | Unit | 7 | 8 | When I conquer after an attack, if you assigned 5+ excess damage, score 1 point. | Top-end payoff reading a higher version of the Legend's own excess damage condition. |
| Yeti Brawler | Unit | 6 | 6 | On conquer, if you assigned 3+ excess damage, play two Gold gear tokens exhausted. | A second card keyed to the exact same "3+ excess damage" trigger as the Legend. |
| Blood Rush | Spell | 1 | | [Action], [Repeat] 1 Energy. Assault 2 this turn. | Cheap, repeatable combat trick to push a fight over a stunned blocker's remaining Might. |
| Cleave | Spell | 1 | | [Action]. Assault 3 this turn. | Efficient one-shot Might swing. |
| Heroic Charge | Spell | 3 | | [Action]. Give a friendly unit +1 Might this turn and stun an enemy unit at its location. | A buff and a stun in one card — sets up a clean, high-excess-damage attack by itself. |

## How To Play

1. Play cheap Assault attackers early (`Chemtech Enforcer`, `Inferna`,
   `Sharkling`) to start pressuring a battlefield.
2. Before attacking with your main threat, strip the blocker with a stun
   (`Vi - Peacekeeper`'s or `Leona - Determined`'s on-attack stun,
   `Solari Chief`, or `Heroic Charge`) so the attack lands as excess
   damage instead of trading into a fight.
3. Sequence `Lucian - Gunslinger`'s on-attack ping before committing
   bigger attackers, since it can shave a blocker's Might down to a size
   your other units clear outright.
4. Once a conquer is set up to land 3+ excess damage, exhaust
   `Vi - Piltover Enforcer` to ready an attacker for a second swing the
   same turn, and expect `Yeti Brawler` to add two Gold gear tokens if
   it was the one conquering.
5. Play `Tryndamere - Barbarian` once the deck is reliably clearing
   blockers; its 5+ excess damage point only needs one big, clean hit,
   not repeated small ones.
6. Hold `Blood Rush` or `Cleave` as insurance to push a fight that would
   otherwise land under the 3-excess-damage threshold.

## Mulligan

Keep:

- one cheap attacker: `Chemtech Enforcer`, `Inferna`, or `Sharkling`;
- one stun or removal piece: `Vi - Peacekeeper`, `Leona - Determined`,
  `Solari Chief`, or `Heroic Charge`;
- one cheap combat trick (`Blood Rush` or `Cleave`) as backup excess
  damage insurance.

Avoid keeping `Tryndamere - Barbarian` or `Yeti Brawler` without any
early attackers or stun pieces to support them — both need the board
already pressuring a battlefield to find a clean, high-excess-damage
conquer.

## Watch Outs

- "Excess damage" only exists past the amount needed to kill the
  defender, so a stunned defender at 0 effective Might this combat still
  needs enough attacking Might to clear its full printed Might before any
  of it counts as excess — stunning removes its damage output, not its
  Might total.
- `Vi - Piltover Enforcer`'s ready effect is once per qualifying conquer
  and costs exhausting the Legend itself, so it can't also react on a
  turn the Legend is already exhausted for something else.
- `Vayne - Hunter`'s enters-ready clause depends on the opponent
  controlling a battlefield at all — it won't be ready if they don't
  control anything yet.
- `Solari Chief`'s ability only kills a target that is already stunned
  when it enters — playing it before a stun lands just stuns the target
  instead of killing it.

## Upgrade Paths

- Add more direct-damage spells (`Hextech Ray`, `Incinerate`) if the
  deck needs a way to shave down blockers that dodge the stun effects.
- For a lower-complexity version, cut `Rek'Sai - Breacher` and
  `Tryndamere - Barbarian` (both have conditional value that needs board
  state awareness) and add extra copies of the cheap Assault units and
  stun spells instead.
- Add a simulation once this deck has an opponent list to test the
  stun-into-excess-damage sequencing against a real defensive board,
  following `references/simulation-playtest-protocol.md`.
