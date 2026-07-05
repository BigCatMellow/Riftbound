# Teemo Hidden Ambush (Advanced)

## Snapshot

| Field | Value |
|---|---|
| Category | Advanced |
| Legend | Teemo - Swift Scout |
| Domains | Mind, Chaos |
| Chosen champion | Teemo - Scout |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | None |
| Difficulty | High |
| Core plan | Play cards face down with `[Hidden]` for a discounted future reveal, then flip them at the moment they're most disruptive, while `Teemo - Strategist` and `Ember Monk` turn every Hidden card into extra payoff. |

## Why This Is Advanced

`[Hidden]` cards are played face down cheaply now ("Hide now for Any Rune")
and revealed later for 0 Energy, which means this deck is constantly playing
a card now to bank a play for later — the pilot has to track what's under
each facedown card, what battlefield it's at, and when flipping it does the
most damage or disruption, all information the opponent can't see either.
`Teemo - Strategist`'s defend trigger deals damage based on how many Hidden
cards are revealed off the top of the deck (not in play), which rewards
knowing your own deck's Hidden density, and `Ember Monk` only grows when a
card is played *from* Hidden, not just any card. None of this is
straightforward removal-and-attack; it's a deck built entirely around
information and timing.

## Legality Notes

- Domain identity: Teemo - Swift Scout is Mind/Chaos. Every main deck card is
  single-domain Mind, single-domain Chaos, or the dual Mind/Chaos
  `Guerilla Warfare`.
- Copy-limit check: `Teemo - Scout` has 1 chosen-champion copy plus 2 main
  deck copies (3 total). No other card exceeds 3 copies.
- Signature check: no signature cards are included.
- Banned/errata check: `Fight or Flight` (OGN-168) is marked **Banned** in
  the local card database and is intentionally excluded. `Pyke - Returned`
  (also a Hidden Chaos card) fills that slot instead. No other card used
  here is banned.
- Champion tag: `Teemo - Scout` is inferred to carry the `Teemo` champion
  tag from card name and the Legend's own name. The source export has no
  explicit tag column — confirm the printed tag before tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Teemo - Swift Scout | OGN-263 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Teemo - Scout | OGN-197 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Teemo - Scout | OGN-197 | Champion Unit | 2 |
| 3 | Teemo - Strategist | OGN-121 | Champion Unit | 2 |
| 3 | Ember Monk | OGN-167 | Unit | 4 |
| 3 | Evelynn - Entrancing | UNL-141 | Champion Unit | 2 |
| 2 | Windsinger | SFD-138 | Unit | 2 |
| 2 | Tideturner | OGN-199 | Unit | 2 |
| 2 | Pyke - Returned | UNL-145 | Champion Unit | 3 |
| 2 | Blastcone Fae | OGN-097 | Unit | 2 |
| 2 | Keeper of Masks | UNL-081 | Unit | 2 |
| 3 | Bone Skewer | UNL-139 | Spell | 2 |
| 2 | Switcheroo | SFD-145 | Spell | 2 |
| 2 | Smoke and Mirrors | UNL-083 | Spell | 2 |
| 2 | Sprite Call | OGN-094 | Spell | 3 |
| 3 | Wages of Pain | SFD-070 | Spell | 3 |
| 3 | Consult the Past | OGN-083 | Spell | 4 |
| 2 | Edge of Night | SFD-139 | Gear | 3 |
| 2 | Guerilla Warfare | OGN-264 | Spell | 2 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 6 | Mind Rune | OGN-089 |
| 6 | Chaos Rune | OGN-166 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Bandle Tree | OGN-278 | Lets you hide an additional card here, directly increasing the deck's Hidden density at this location. |
| Ravenbloom Conservatory | SFD-215 | Defend trigger can find a free spell, refueling the deck's Hidden spell count. |
| Zaun Warrens | OGN-298 | Conquer trigger discards then draws, feeding `Guerilla Warfare`'s trash-recursion. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Teemo - Swift Scout | Legend | | | You may pay 1 Energy to hide a card instead of Any Rune. Exhaust: return a Teemo unit to hand. | Cheapens every Hidden play in the deck and can rebuy a Teemo body. |
| Teemo - Scout | Champion Unit | 2 | 1 | [Hidden]. On play, +3 Might this turn. | Chosen champion; cheap and can ambush for a surprising 4 Might swing. |
| Teemo - Strategist | Champion Unit | 2 | 2 | [Hidden]. On defend, reveal the top 5 of your deck; deal 1 to a chosen enemy unit per Hidden card revealed. | Direct payoff for deck density — the more Hidden cards left in the deck, the bigger this hits. |
| Ember Monk | Unit | 4 | 4 | When you play a card from Hidden, +2 Might this turn. | Grows every time a facedown card is flipped, not just played normally. |
| Evelynn - Entrancing | Champion Unit | 2 | 2 | [Hidden], [Backline]. Flipped on your turn, may pull an enemy unit to your battlefield. | Ambush piece that repositions an enemy blocker before combat. |
| Windsinger | Unit | 2 | 1 | [Hidden]. On play, may bounce a 3-Might-or-less unit. | Cheap tempo bounce, more surprising when flipped from face down. |
| Tideturner | Unit | 2 | 2 | [Hidden]. On play, may swap locations with a friendly unit elsewhere. | Repositions a unit across the board without a normal Move. |
| Pyke - Returned | Champion Unit | 3 | 3 | [Hidden], [Backline]. Once per turn, an enemy death here makes a Gold token. | Sits safely as a backline attacker while converting combat trades into resources. |
| Blastcone Fae | Unit | 2 | 2 | [Hidden]. On play, -2 Might to a unit this turn. | Shrinks a blocker or attacker right before combat math matters. |
| Keeper of Masks | Unit | 2 | 1 | [Hidden], [Temporary]. On play, two Reflection copies of itself. | Turns one flip into three bodies for the turn. |
| Bone Skewer | Spell | 2 | | [Hidden]. Force an opponent to play a revealed unit onto a battlefield, then stun it. | Disruption that can strip a card from their hand at a bad time for them. |
| Switcheroo | Spell | 2 | | [Hidden], [Action]. Swap the Might of two units at a battlefield this turn. | Can turn a losing fight into a winning one when flipped mid-combat setup. |
| Smoke and Mirrors | Spell | 2 | | [Hidden], [Action]. Reposition two friendly units; draw 1. | Flexible repositioning plus a cantrip. |
| Sprite Call | Spell | 3 | | [Hidden], [Action]. Play a ready 3 Might Sprite token. | A surprise extra body right when it's needed. |
| Wages of Pain | Spell | 3 | | [Hidden], [Action]. Deal 3 to a unit; make a Gold token. | Removal that also generates a resource. |
| Consult the Past | Spell | 4 | | [Hidden], [Reaction]. Draw 2. | Card advantage that can be banked face down and cashed in on the opponent's turn. |
| Edge of Night | Gear | 3 | 2 | [Hidden]. Flipped on your turn, attaches to a unit here. [Equip] Chaos Rune. | A surprise Might boost that snaps onto a unit right when combat starts. |
| Guerilla Warfare | Spell | 2 | | Return up to two Hidden cards from your trash; hide cards for free this turn. | Refuels the Hidden plan and can chain several flips in one turn. |

## How To Play

1. Hide cheap, cost-efficient cards early (`Windsinger`, `Blastcone Fae`,
   `Teemo - Scout`) to bank cheap future plays and start feeding
   `Ember Monk`.
2. Flip Hidden cards at the moment they matter most — right before combat
   for a Might swing (`Switcheroo`, `Edge of Night`), or on the opponent's
   turn for a Reaction like `Consult the Past`.
3. Keep `Teemo - Strategist` alive as a defender; the more Hidden cards
   still in your deck, the bigger its reveal-and-damage trigger becomes.
4. Use `Guerilla Warfare` to bring back Hidden cards that were discarded or
   traded away, and to re-hide new cards for free the same turn.
5. Land `Ember Monk` once a few Hidden cards are already down — every flip
   from that point on grows it further.
6. Use `Bone Skewer` to force an awkward play out of the opponent's hand
   when you have information (from earlier reveals) about what they're
   holding.

## Mulligan

Keep:

- one cheap Hidden play: `Teemo - Scout`, `Windsinger`, or `Blastcone Fae`;
- `Teemo - Strategist` if you expect an early defensive turn;
- one piece of removal or disruption: `Wages of Pain` or `Bone Skewer`.

Avoid keeping too many 4-cost cards (`Ember Monk`, `Consult the Past`)
without early Hidden plays to set them up.

## Watch Outs

- Hiding a card now costs a Rune (or 1 Energy via the Legend); revealing it
  later costs 0 Energy but still needs "Any Rune to react with" at the time
  you flip it — track that resource, not just the card.
- `Teemo - Strategist`'s damage depends on your deck's remaining Hidden
  density, which drops as you draw and play more of the deck. It's strongest
  early and mid-game, weaker once most Hidden cards are gone from the deck.
- `Ember Monk` only grows from playing a card *from* Hidden — playing a
  Hidden-capable card normally, face up, does not trigger it.
- This deck is genuinely information-heavy. If tracking every facedown
  card's identity and location becomes unmanageable, it's a sign to trim the
  Hidden count rather than push further.
- You can only hide a card at a battlefield you currently control, and a
  hidden permanent's play effect can only target something at that specific
  battlefield unless no legal target exists there at all. Only hide
  location-locked cards like `Blastcone Fae` or `Edge of Night` where you
  expect an enemy unit to actually be when you flip them — otherwise you're
  stuck debuffing or equipping your own stuff, or holding the card longer
  than planned. Confirmed in `simulations/SIM-0004-teemo-vs-lucian-rules-smoke.md`.
- Losing Control of a battlefield removes anything hidden there during the
  next Cleanup (rule 107.3.d) — a hidden card is not safe just because it's
  face down. Don't hide your best payoffs at a battlefield you can't hold.

## Upgrade Paths

- Add `Ava Achiever` (Mind) to tutor a Hidden card straight from hand for
  free when attacking.
- Add more Reaction-speed Hidden cards if the meta rewards holding up
  interaction during the opponent's turn.
- For a lower-complexity version, cut the reposition-focused cards
  (`Tideturner`, `Smoke and Mirrors`) and keep only the highest-impact
  Hidden payoffs, trading some ceiling for easier sequencing.
