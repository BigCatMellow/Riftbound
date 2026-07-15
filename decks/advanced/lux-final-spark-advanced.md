# Lux Final Spark Control (Advanced)

## Snapshot

| Field | Value |
|---|---|
| Category | Advanced |
| Legend | Lux - Lady of Luminosity - Starter |
| Domains | Mind, Order |
| Chosen champion | Lux - Crownguard |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | `Final Spark` (3) |
| Difficulty | High |
| Core plan | Every big spell replaces itself: the Legend draws a card whenever you play a spell costing 5+ Energy, and fifteen main-deck spells qualify. `Lux - Crownguard` adds 2 spell-only Energy at reaction speed, `Eager Apprentice` shaves every cast, and `The Academy` gives the next spell [Repeat] — a held Academy plus `Final Spark` is "deal 8, deal 8, draw a card." |

## Why This Is An Advanced Deck

Big-spell control lives or dies on tempo bridges and card parity. This
shell wires both into the Legend:

- `Lux - Lady of Luminosity`: 5+ cost spell → draw 1 — the removal
  suite cantrips, so trading one-for-one never runs you out;
- `Lux - Crownguard` (chosen): exhaust at reaction speed → Add 2
  Energy, spells only — turn 4 casts turn-6 spells;
- `Eager Apprentice`: all your spells cost 1 less while he holds a
  battlefield — unlike the Jhin shell (which must *spend* 4+), this
  Legend reads **printed cost**, so discounts are pure upside;
- `Lux - Illuminated`: +3 Might per 5+ spell — the finisher grows off
  the control plan itself;
- `Imperial Decree` re-defines the deck's small spells: with Decree
  resolved, `Stupefy`'s -1 or any chip damage becomes a kill sentence
  ("when any unit takes damage this turn, kill it");
- `The Academy`, `Forgotten Monument`, and `Obelisk of Power` slow the
  game and enlarge it — exactly the axis this deck wins on.

## Legality Notes

- Domain identity: Lux - Lady of Luminosity is Mind/Order. Every main
  deck card is single-domain Mind, single-domain Order, or the
  Mind/Order Signature card `Final Spark`.
- Copy-limit check: `Lux - Crownguard` has 1 chosen-champion copy plus
  2 main deck copies (3 total, at the limit). `Lux - Illuminated` is a
  different card name. No other card exceeds 3 copies.
- Signature check: `Final Spark` (OGS-022) is Lux's own signature
  (printed directly after the Legend, OGS-021); 3 copies sit exactly at
  the 3-signature limit and match the Legend's tag.
- Banned/errata check: no card used here is marked Banned in the local
  card database.
- Champion tag: `Lux - Crownguard` and `Lux - Illuminated` are inferred
  to carry the `Lux` champion tag from card name and the Legend's own
  name, per this project's convention. The source export has no
  explicit tag column — confirm the printed tag before tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Lux - Lady of Luminosity - Starter | OGS-021 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Lux - Crownguard | OGS-014 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Lux - Crownguard | OGS-014 | Champion Unit | 4 |
| 2 | Lux - Illuminated | OGS-006 | Champion Unit | 6 |
| 2 | Eager Apprentice | OGN-084 | Unit | 3 |
| 3 | Lecturing Yordle | OGN-087 | Unit | 3 |
| 2 | Fate Weaver | UNL-064 | Unit | 5 |
| 2 | Jeweled Colossus | OGN-086 | Unit | 5 |
| 3 | Final Spark | OGS-022 | Signature Spell | 8 |
| 3 | Falling Comet | OGN-085 | Spell | 5 |
| 2 | Singularity | OGN-105 | Spell | 6 |
| 2 | Progress Day | OGN-114 | Spell | 6 |
| 2 | Blast of Power | OGS-012 | Spell | 6 |
| 2 | Imperial Decree | OGN-221 | Spell | 5 |
| 1 | The Ruination | UNL-180 | Spell | 9 |
| 1 | Grand Strategem | OGN-233 | Spell | 6 |
| 3 | Premonition | SFD-087 | Spell | 2 |
| 2 | Stupefy | OGN-095 | Spell | 1 |
| 2 | Hidden Blade | OGN-213 | Spell | 2 |
| 2 | Soul Harvest | UNL-159 | Spell | 2 |
| 2 | Energy Conduit | OGN-098 | Gear | 3 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 6 | Mind Rune | OGN-089 |
| 6 | Order Rune | OGN-214 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| The Academy | UNL-216 | Holding gives your next spell [Repeat] equal to its base cost — a doubled Final Spark ends most games. |
| Forgotten Monument | SFD-209 | No scoring before turn 3 blunts aggression while the spell mana grows. |
| Obelisk of Power | OGN-284 | Both players channel early — symmetric ramp always favors the deck with the bigger spells. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Lux - Lady of Luminosity | Legend | | | When you play a spell that costs 5+ Energy, draw 1. | The parity engine: every haymaker replaces itself. |
| Lux - Crownguard | Champion Unit | 4 | 2 | Exhaust: [Reaction] — Add 2 Energy, spells only. | Chosen champion; two turns of tempo hidden in one body. |
| Lux - Illuminated | Champion Unit | 6 | 5 | When you play a 5+ cost spell, +3 Might this turn. | The finisher that the game plan feeds by itself. |
| Eager Apprentice | Unit | 3 | 3 | While at a battlefield, your spells cost 1 less (min 1). | Pure upside here — the Legend reads printed cost, not spend. |
| Lecturing Yordle | Unit | 3 | 2 | [Tank]. On play, draw 1. | Cantripping wall that buys the mid-turns. |
| Fate Weaver | Unit | 5 | 4 | On play, look at top 4; may draw a spell costing 4+. | Digs for the right haymaker while holding ground. |
| Jeweled Colossus | Unit | 5 | 5 | [Vision]. [Shield]. | An honest wall with topdeck smoothing. |
| Final Spark | Signature Spell | 8 | | [Action]. Deal 8 to a unit. | Kills anything in the game; at The Academy, kills two. |
| Falling Comet | Spell | 5 | | [Action]. Deal 6 to a unit at a battlefield. | The workhorse: removal plus a card, every time. |
| Singularity | Spell | 6 | | Deal 6 to each of up to two units. | A two-for-one that draws — three-for-one in practice. |
| Progress Day | Spell | 6 | | Draw 4. | Five cards deep with the Legend's trigger. |
| Blast of Power | Spell | 6 | | [Action]. Kill a unit at a battlefield. | Unconditional answer, cantripped. |
| Imperial Decree | Spell | 5 | | [Action]. Any unit that takes damage this turn dies. | The redefiner: every ping becomes an execution. |
| The Ruination | Spell | 9 | | Kill all units. | The reset button, drawn into via everything else. |
| Grand Strategem | Spell | 6 | | [Action]. Friendly units +5 Might this turn. | The surprise kill turn off two walls and a Lux. |
| Premonition | Spell | 2 | | [Reaction]. Draw 3. | The cheap half of the draw engine. |
| Stupefy | Spell | 1 | | [Reaction]. -1 Might (min 1). Draw 1. | Early interaction; a death sentence under Decree. |
| Hidden Blade | Spell | 2 | | [Hidden]. [Action]. Kill a unit at a battlefield; controller draws 2. | Cheap removal early; the drawback matters less when you out-draw them anyway. |
| Soul Harvest | Spell | 2 | | Kill a unit at a battlefield with ≤3 Might. | Answers aggro's curve on curve. |
| Energy Conduit | Gear | 3 | | Exhaust: [Reaction] — Add 1 Energy. | The ramp that bridges 5-cost turns to 8-cost turns. |

## How To Play

1. Survive the early turns cheaply: `Soul Harvest`, `Stupefy`, `Hidden
   Blade`, and the cantripping walls. Don't fire 5+ spells at 2-Might
   targets.
2. Deploy `Energy Conduit` and `Lux - Crownguard` before the haymaker
   turns — Crownguard's +2 is spell-only, so plan unit deployment on
   its own mana.
3. From turn 4-5, aim for one Legend trigger per turn minimum. With
   `Eager Apprentice` down, `Imperial Decree` at 4 is still a 5+ spell
   (printed cost) — the discount never costs you the draw.
4. `Imperial Decree` plus any damage is a board wipe: Decree, then
   `Stupefy`... no — Stupefy deals no damage; pair Decree with
   `Singularity`, `Falling Comet`, or combat itself.
5. Hold `The Academy` before your biggest turn: the next spell's
   [Repeat] on `Final Spark` or `Singularity` usually ends the game on
   the spot.
6. `Lux - Illuminated` closes: two 5+ spells in a turn make her an
   11-Might attacker that also drew you two cards.

## Mulligan

Keep:

- one cheap answer (`Soul Harvest`, `Stupefy`, `Hidden Blade`);
- one wall (`Lecturing Yordle`, `Jeweled Colossus`);
- `Energy Conduit` or `Premonition` to bridge.

Avoid keeping two or more 6+ cost spells in the opener — the deck
needs to live to its mana, not admire it.

## Watch Outs

- The Legend reads **printed Energy cost** ("costs 5 or more"), so
  discounts are safe — but 4-cost spells never trigger it no matter
  how much you actually paid. This is the mirror image of the Jhin
  deck's rule; don't port cards between the shells without rechecking.
- `Imperial Decree` kills **any** unit that takes damage — including
  yours. Sequence your own combats before it, or accept the symmetry.
- `The Ruination` kills your walls and your Lux too — it's the button
  for lost boards, not winning ones.
- `Hidden Blade` gives its controller's victim's owner 2 cards — fine
  early, dangerous against decks that convert cards faster than you.
- `Lux - Crownguard`'s Energy is spell-only and she must exhaust — she
  can't block the turn she banks tempo.
- `Grand Strategem` pumps only until end of turn: it's an attack
  enabler, not a permanent anthem.

## Upgrade Paths

- `Time Warp` (10: extra turn) is the ceiling if games regularly reach
  double-digit Energy — an extra turn with The Academy held is
  usually lethal.
- `Promising Future` adds a chaotic symmetric cascade for grindy
  mirrors.
- `Divine Judgment` (7, Order) is a softer sweeper that spares two of
  your permanents; consider it over The Ruination against midrange.
- `Mirror Image` is LeBlanc's signature and illegal here; copy effects
  for this pair live only in that shell.
