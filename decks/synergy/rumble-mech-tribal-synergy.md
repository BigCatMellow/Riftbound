# Rumble Mech Tribal (Synergy)

## Snapshot

| Field | Value |
|---|---|
| Category | Synergy |
| Legend | Rumble - Mechanized Menace |
| Domains | Fury, Mind |
| Chosen champion | Rumble - Scrapper |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | `Danger Zone` (3) |
| Difficulty | Medium |
| Core plan | Flood the board with Mech tokens, buff them as a type with the Legend's Shield and the chosen champion's +1 Might, and grind out combat with defenders that get stronger every fight. |

## Why This Is A Synergy Deck

Every Mech card in this pool cares about the "Mech" type collectively:
`Rumble - Mechanized Menace` gives all Mechs Shield, `Rumble - Scrapper` gives
them all +1 Might and makes more of them on hold, `Forecaster` gives them
Vision, and `Breakneck Mech` gives them Deflect and Ganking. The named Mech
package in this card pool is genuinely small (a handful of unique cards), so
this deck is honest about supplementing it with generic Fury/Mind removal
and card draw rather than pretending there are 20 unique Mech cards to
choose from — the synergy is real and stacks hard once online, it's just a
tight core surrounded by generic support.

## Legality Notes

- Domain identity: Rumble - Mechanized Menace is Fury/Mind. Every main deck
  card is single-domain Fury, single-domain Mind, or the dual Fury/Mind
  Signature card `Danger Zone`.
- Copy-limit check: `Rumble - Scrapper` has 1 chosen-champion copy plus 2
  main deck copies (3 total). No other card exceeds 3 copies.
- Signature check: `Danger Zone` (SFD-182) is a Signature card — it is
  Rumble's own signature (printed directly after the Legend, SFD-181), so
  3 copies sit exactly at the 3-signature limit and match the Legend's
  tag. An earlier revision also ran 2 copies of `Curtain Call` (UNL-182),
  which is Jhin's signature and never matched Rumble's tag; it was
  replaced with `Upstage Comedy` when `scripts/validate_decks.py` caught
  the 5-signature overrun.
- Banned/errata check: no card used here is marked banned in the local card
  database.
- Champion tag: `Rumble - Scrapper` is inferred to carry the `Rumble`
  champion tag from card name and the Legend's own name. The source export
  has no explicit tag column — confirm the printed tag before tournament
  play.
- Token note: the 3-Might Mech tokens created by `Ferrous Forerunner`,
  `Bubble Bot`'s targets, `Production Surge`, `Assembly Rig`, and
  `Rumble - Scrapper`'s hold trigger are not Main Deck cards and are not
  counted in the 40 — they're created during play per rule 176 (Tokens).

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Rumble - Mechanized Menace | SFD-181 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Rumble - Scrapper | SFD-089 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Rumble - Scrapper | SFD-089 | Champion Unit | 5 |
| 3 | Ferrous Forerunner | SFD-021 | Unit | 6 |
| 3 | Forecaster | SFD-065 | Unit | 2 |
| 3 | Bubble Bot | SFD-062 | Unit | 3 |
| 2 | Mega-Mech | OGN-088 | Unit | 7 |
| 1 | Breakneck Mech | SFD-071 | Unit | 8 |
| 3 | Production Surge | SFD-076 | Spell | 4 |
| 2 | Assembly Rig | SFD-019 | Gear | 4 |
| 3 | Danger Zone | SFD-182 | Spell | 1 |
| 2 | Blue Sentinel | UNL-087 | Unit | 4 |
| 2 | Chakram Dancer | UNL-071 | Unit | 3 |
| 2 | Icevale Archer | UNL-065 | Unit | 2 |
| 2 | Hextech Ray | OGN-009 | Spell | 1 |
| 2 | Void Seeker | OGN-024 | Spell | 3 |
| 2 | Incinerate | OGS-003 | Spell | 2 |
| 2 | Upstage Comedy | UNL-009 | Spell | 2 |
| 2 | Bellows Breath | SFD-080 | Spell | 1 |
| 2 | Premonition | SFD-087 | Spell | 2 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 6 | Fury Rune | OGN-007 |
| 6 | Mind Rune | OGN-089 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Marai Spire | SFD-211 | Friendly Repeat costs cost 1 Energy less, cheapening `Danger Zone`, `Upstage Comedy`, and `Bellows Breath`'s repeat clauses. |
| Ornn's Forge | SFD-213 | The first friendly non-token gear each turn costs 1 Energy less, discounting `Assembly Rig`. |
| Forgotten Library | UNL-211 | Predicts off any spell where you spend 4+ Energy, smoothing draws from `Production Surge` or a repeated `Upstage Comedy`. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Rumble - Mechanized Menace | Legend | | | Your Mechs have [Shield]. | Every Mech becomes a better defender for free. |
| Rumble - Scrapper | Champion Unit | 5 | 4 | Your Mechs have +1 Might (including me). On hold, play a 3 Might Mech token. | Chosen champion; a permanent stat buff plus ongoing token generation once you're holding a battlefield. |
| Ferrous Forerunner | Unit | 6 | 6 | [Deathknell] — play two 3 Might Mech tokens. | Trades into two bodies, refilling the board even in a losing fight. |
| Forecaster | Unit | 2 | 2 | Your Mechs have [Vision]. | Cheap curve filler that smooths every future Mech's draw. |
| Bubble Bot | Unit | 3 | 3 | On play, ready another friendly Mech. | Lets a Mech attack and then defend again, or defend twice in one round. |
| Mega-Mech | Unit | 7 | 8 | (No text.) | Big vanilla stats that still benefit from every Mech-wide buff. |
| Breakneck Mech | Unit | 8 | 7 | Your Mechs have [Deflect] and [Ganking]. Enters ready if you control another Mech. | Top-end payoff; often enters ready and immediately makes the whole board hard to target or pin down. |
| Production Surge | Spell | 4 | | Costs 2 less with a Mech in play. Play a 3 Might Mech token; draw 1. | Cheap token generation plus card advantage once the deck is online. |
| Assembly Rig | Gear | 4 | | 1 Energy + Fury Rune, recycle a unit, exhaust: play a 3 Might Mech token. | Repeatable token generation late game. |
| Danger Zone | Spell | 1 | | [Reaction], [Repeat] 1 Energy + Any Rune. Give your Mechs +1 Might this turn. | Cheap, repeatable combat trick that scales with board width. |
| Blue Sentinel | Unit | 4 | 4 | [Shield 2]. Hold effects here trigger twice; adds Any Rune on hold. | Doubles `Rumble - Scrapper`'s own hold trigger at this battlefield. |
| Chakram Dancer | Unit | 3 | 3 | [Ambush]. On play, give other units here Shield this turn. | Ambushes into a fight and turns the whole board into temporary blockers. |
| Icevale Archer | Unit | 2 | 2 | On attack, may pay 1 Energy for -1 Might to a unit here. | Cheap attacker that can also shrink a blocker. |
| Hextech Ray | Spell | 1 | | [Action]. Deal 3 to a unit at a battlefield. | Efficient removal. |
| Void Seeker | Spell | 3 | | [Action]. Deal 4 to a unit at a battlefield. Draw 1. | Removal that replaces itself. |
| Incinerate | Spell | 2 | | [Action]. Deal 2 to a unit at a battlefield. | Cheap early removal. |
| Upstage Comedy | Spell | 2 | | [Repeat] 2 Energy. Ready a unit. | Readies a Mech to defend again (stacking with tribal Shield) or to attack twice; Repeat scales late and gets cheaper at Marai Spire. |
| Bellows Breath | Spell | 1 | | [Action], [Repeat] 1 Energy + Mind Rune. Deal 1 to up to three units at a location. | Cheap, repeatable board control against small tokens. |
| Premonition | Spell | 2 | | [Reaction]. Draw 3. | Big card advantage to refill after an aggressive curve. |

## How To Play

1. Play cheap Mech-support units (`Forecaster`, `Icevale Archer`) early, then
   land `Ferrous Forerunner` or `Production Surge` to establish actual Mech
   bodies. `Forecaster`, `Bubble Bot`, and `Chakram Dancer` are support cards
   that reference Mechs as a category, not Mechs themselves — the Legend's
   Shield and `Rumble - Scrapper`'s +1 Might do nothing until an actual Mech
   (from `Production Surge`, `Assembly Rig`, `Ferrous Forerunner`,
   `Mega-Mech`, `Breakneck Mech`, or a hold trigger) is on board.
2. Get `Rumble - Scrapper` down as soon as it's affordable — it buffs every
   Mech immediately and starts making more of them every time you hold a
   battlefield.
3. Use `Bubble Bot` to double up a Mech's usefulness in a single turn:
   attack, then ready it to defend, or vice versa.
4. Hold `Danger Zone` and `Upstage Comedy` as combat tricks; both get cheaper
   with `Marai Spire` in play, letting you re-buy their effects repeatedly.
5. Land `Breakneck Mech` once you already control another Mech — it enters
   ready and immediately makes your whole Mech board hard to target or pin
   in place.
6. Use the deck's removal (`Hextech Ray`, `Void Seeker`, `Incinerate`) to
   keep the board clear while the Mech package assembles; it's slower to
   come online than a pure aggro deck.

## Mulligan

Keep:

- one cheap Mech piece: `Forecaster` or `Icevale Archer`;
- one piece of removal: `Hextech Ray`, `Incinerate`, or `Void Seeker`;
- one Mech generator: `Ferrous Forerunner`, `Production Surge`, or
  `Rumble - Scrapper` if you also have an early play to bridge to it.

Avoid keeping `Breakneck Mech` or `Mega-Mech` without any early Mech
generation to support them.

## Watch Outs

- The Mech package is genuinely thin — don't expect to always have a Mech in
  play by the time `Production Surge`'s discount or `Breakneck Mech`'s
  enters-ready clause would matter. The generic removal is there to buy time
  while the deck assembles.
- `Rumble - Mechanized Menace`'s Shield only helps while defending. Don't
  expect it to protect an attacking Mech.
- `Ferrous Forerunner`'s two tokens only trigger on death (Deathknell), so it
  does nothing extra if it's returned to hand or otherwise removed from the
  board without dying.
- `Breakneck Mech`'s enters-ready clause needs another Mech already in play
  first — it enters exhausted like normal if it's your first Mech.

## Upgrade Paths

- Add `Rumble - Hotheaded` (Fury) as a second Rumble body if the deck wants
  more direct Mech-recursion from the trash.
- Add more card draw (`Progress Day`, `Consult the Past`) if games run long
  enough for the Mech package to matter more than early tempo.
- For a more advanced version, lean into `Blue Sentinel`'s doubled hold
  triggers and stack multiple hold-payoff battlefields, which asks for
  tighter battlefield-selection sequencing than this list needs.
