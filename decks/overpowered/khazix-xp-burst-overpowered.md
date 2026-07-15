# Kha'Zix XP Burst Reach (Overpowered)

## Snapshot

| Field | Value |
|---|---|
| Category | Overpowered |
| Legend | Kha'Zix - Voidreaver |
| Domains | Body, Chaos |
| Chosen champion | Kha'Zix - Evolving Hunter |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | `Void Assault` (2) |
| Difficulty | Medium |
| Core plan | Bank XP from combat wins, Hunt triggers, and movement, then cash it in all at once for direct, repeatable burst damage that doesn't care what's blocking — `Kha'Zix - Evolving Hunter`'s attack trigger deals damage equal to its own Might to anything at the battlefield, no combat math required. |

## Why This Is Overpowered

Most of this card pool's removal deals a fixed, telegraphed amount of
damage from a spell you can see coming. This deck's finisher is different: once
`Kha'Zix - Evolving Hunter` is attacking, spending 3 banked XP deals damage
equal to its *own Might* directly to a chosen enemy unit — no combat, no
blocking required, and the amount scales with however big the deck has made
that unit that game. `Kha'Zix - Voidreaver`'s legend ability turns every won
combat into more XP to spend, and `Conscription` can outright steal an
opponent's unit for 5 banked XP. Stacking XP-into-direct-effect payoffs this
densely means a long game increasingly turns every fight this deck wins into
another removal spell or a stolen unit, on top of combat itself — flag it
before a casual game the same way the Legend/Domain gap suggests.

## Legality Notes

- Domain identity: Kha'Zix - Voidreaver is Body/Chaos. Every main deck card
  is single-domain Body, single-domain Chaos, or the dual Body/Chaos
  Signature card `Void Assault`.
- Copy-limit check: `Kha'Zix - Evolving Hunter` has 1 chosen-champion copy
  plus 2 main deck copies (3 total). No other card exceeds 3 copies.
- Signature check: `Void Assault` (UNL-202) is Kha'Zix's own signature
  (printed directly after the Legend, UNL-201), so 2 copies are legal and
  match the Legend's tag. An earlier revision ran `On the Hunt` (SFD-204),
  which is Sivir's signature and never matched Kha'Zix's tag; it was
  swapped for `Void Assault` when `scripts/validate_decks.py` caught the
  mismatch.
- Banned/errata check: no card used here is marked banned in the local card
  database.
- Champion tag: `Kha'Zix - Evolving Hunter` is inferred to carry the
  `Kha'Zix` champion tag from card name and the Legend's own name;
  `Kha'Zix - Mutating Horror` is included as a generic Chaos unit, not the
  Chosen Champion, so its own tag match doesn't need separate confirmation.
  The source export has no explicit tag column — confirm the printed tag on
  `Kha'Zix - Evolving Hunter` before tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Kha'Zix - Voidreaver | UNL-201 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Kha'Zix - Evolving Hunter | UNL-119 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Kha'Zix - Evolving Hunter | UNL-119 | Champion Unit | 5 |
| 3 | Kha'Zix - Mutating Horror | UNL-143 | Champion Unit | 4 |
| 3 | Voracious Gromp | UNL-100 | Unit | 5 |
| 3 | Gemhand Hunter | UNL-094 | Unit | 2 |
| 2 | Crowd Favorite | UNL-102 | Unit | 3 |
| 2 | Vicious Snapjaws | UNL-129 | Unit | 5 |
| 2 | Mister Root | UNL-127 | Unit | 2 |
| 2 | Arachnoid Horror | UNL-117 | Unit | 6 |
| 2 | Targonian Visionary | UNL-098 | Unit | 6 |
| 2 | Wily Newtfish | UNL-108 | Unit | 4 |
| 3 | Grim Resolve | UNL-095 | Spell | 2 |
| 2 | Stare Down | UNL-107 | Spell | 2 |
| 3 | Concentrate | UNL-091 | Spell | 5 |
| 2 | Void Assault | UNL-202 | Signature Spell | 2 |
| 1 | Conscription | UNL-140 | Spell | 5 |
| 2 | Blood Rose | UNL-109 | Gear | 1 |
| 2 | Insightful Investigator | UNL-135 | Unit | 3 |
| 2 | Megatusk | UNL-126 | Unit | 6 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 6 | Body Rune | OGN-126 |
| 6 | Chaos Rune | OGN-166 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Sunken Temple | SFD-218 | Conquering with a Mighty (5+) unit draws a card, rewarding the deck's own buff-and-XP-fed Might growth. |
| Windswept Hillock | OGN-297 | Units here get Ganking, letting an XP-fed attacker reposition to find its next target. |
| Trapping Grounds | UNL-217 | Conquering with 3+ excess damage makes a Deflect token — a natural byproduct of an oversized attacker winning easily. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Kha'Zix - Voidreaver | Legend | | | Win a combat, gain 1 XP. Spend 1 XP, exhaust: buff a unit. Spend 2 XP, exhaust: recall an exhausted friendly unit. | Converts combat wins directly into ongoing buff and repositioning fuel. |
| Kha'Zix - Evolving Hunter | Champion Unit | 5 | 5 | [Hunt]. On attack, may spend 3 XP for damage equal to my Might to an enemy unit here. | Chosen champion; the deck's core finisher — unblockable, scaling burst damage. |
| Kha'Zix - Mutating Horror | Champion Unit | 4 | 4 | [Ambush]. On attack/defend vs. a lone enemy, +2 Might and gain 2 XP. | Cheap XP engine that punishes an opponent who commits only one unit to a fight. |
| Voracious Gromp | Unit | 5 | 5 | [Hunt 3]. | The single biggest XP burst from one conquer or hold. |
| Gemhand Hunter | Unit | 2 | 2 | [Hunt]. Level 6: +1 Might. | Cheap early XP source with its own scaling upside. |
| Crowd Favorite | Unit | 3 | 3 | [Hunt]. Spend 2 XP: buff itself. | An XP sink that also generates XP. |
| Vicious Snapjaws | Unit | 5 | 5 | When another friendly unit dies, gain 1 XP. | Turns unfavorable trades into more fuel for the finisher. |
| Mister Root | Unit | 2 | 1 | [Accelerate]. On move to a battlefield, gain 2 XP. | Cheap, repeatable XP if it can keep moving. |
| Arachnoid Horror | Unit | 6 | 6 | [Hunt 2]. Can be played into an occupied battlefield if an enemy is alone there. | Bypasses the normal "can't play into an occupied enemy battlefield" restriction to force a fight. |
| Targonian Visionary | Unit | 6 | 6 | Level 11: +4 Might. | Big late-game stat payoff once XP is high. |
| Wily Newtfish | Unit | 4 | 4 | If you gained XP this turn, +1 Might and Ganking. | Cheap payoff for a turn where any XP source already fired. |
| Grim Resolve | Spell | 2 | | +3 Might this turn; gain 2 XP on a win. | Combat trick that directly feeds the XP counter. |
| Stare Down | Spell | 2 | | Bounce weaker enemies at a battlefield; gain 1 XP. | Tempo and board control that also feeds XP. |
| Concentrate | Spell | 5 | | Draw 2; cheaper at Level 6/11. | Card advantage that gets more efficient as XP climbs. |
| Void Assault | Signature Spell | 2 | | Move a friendly unit, then move an enemy unit. If both move to a battlefield you don't control, you're the attacker. | Manufactures a combat on demand — dragging a small enemy into your Hunt unit's battlefield sets up the win-a-combat XP triggers. |
| Conscription | Spell | 5 | | May spend 5 XP to steal any enemy unit at a battlefield instead of only a small one. | The deck's biggest XP sink; converts banked XP directly into the opponent's best unit. |
| Blood Rose | Gear | 1 | | Pay 1 Energy on a unit play for 1 XP. Spend 3 XP, exhaust: ready a unit. | A cheap, steady XP trickle plus a ready-effect XP sink. |
| Insightful Investigator | Unit | 3 | 3 | On play, may pay 2 XP to make an opponent discard a chosen card. | Hand disruption paid for entirely with banked XP. |
| Megatusk | Unit | 6 | 6 | Spend 3 XP: give units here Ganking this turn. | Late-game XP sink that turns a held battlefield into a launchpad. |

## How To Play

1. Play cheap `[Hunt]` units early (`Gemhand Hunter`, `Mister Root`) to start
   banking XP before `Kha'Zix - Evolving Hunter` is affordable.
2. Win combats with any unit to trigger the Legend's XP gain — this doesn't
   require `Kha'Zix - Evolving Hunter` to be on board yet.
3. Once `Kha'Zix - Evolving Hunter` is out, hold at least 3 XP before it
   attacks so the direct-damage trigger is available every combat.
4. Use `Grim Resolve` before an attack you expect to win — it both helps win
   the fight and immediately banks 2 more XP from that win.
5. Save `Conscription` for a real threat: spending 5 XP to steal any unit at
   a battlefield (instead of only a 3-Might-or-less one) is usually the
   correct line once the XP is available.
6. Use `Void Assault` to manufacture a winnable combat on your terms: move
   a Hunt unit and drag a small enemy unit to the same battlefield, then
   collect the win-a-combat XP triggers.

## Mulligan

Keep:

- two cheap XP sources: `Gemhand Hunter`, `Mister Root`, or `Crowd Favorite`;
- one combat trick: `Grim Resolve` or `Stare Down`;
- `Kha'Zix - Mutating Horror` if you also have an early XP source to pair
  with it.

Avoid keeping `Conscription`, `Megatusk`, or `Targonian Visionary` in an
opening hand with no early XP source — all three want XP already banked to
be worth their slot.

## Watch Outs

- This deck's finisher is genuinely hard to interact with: a 3-XP attack
  trigger deals damage with no combat step to answer with a trick or a
  bigger blocker. Agree on power level with the table before bringing this
  to a casual game, the same way you would for a board-wide stat buff.
- `Kha'Zix - Evolving Hunter`'s burst damage equals its *own* Might, so
  removing or shrinking it before it attacks directly weakens the burst, not
  just the combat.
- `Conscription`'s 5-XP mode is powerful but a real investment — don't spend
  it on a unit you could have removed more cheaply with `Grim Resolve` plus
  combat.
- The deck has almost no hard removal outside of XP-gated effects
  (`Conscription`, `Kha'Zix - Evolving Hunter`'s attack trigger). Against a
  fast aggressive opponent, XP may not accumulate before you're under real
  pressure.

## Upgrade Paths

- Add `Poppy - Paragon` (Body) as a second XP-gated late-game body if games
  regularly run long.
- Add more early `[Hunt]` units if games end before enough XP accumulates
  for the direct-damage trigger to matter.
- For a lower-power, more casual-friendly version, cut `Conscription` and
  treat `Kha'Zix - Evolving Hunter`'s attack trigger as the deck's ceiling
  instead of also chasing unit theft.
