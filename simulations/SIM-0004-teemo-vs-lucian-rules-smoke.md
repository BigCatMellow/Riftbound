# SIM-0004: Teemo Hidden Ambush vs Lucian Equipment Assault

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0004 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline, same session as driver) |
| Status | Stopped after 4 rounds by design — see Recommended Next Step |
| Purpose | New deck combination; first real test of the `[Hidden]` mechanic's actual constraints (previously only lightly touched) and the `[Weaponmaster]`/Equip mechanic in live play. |

## Why This Pairing

`decks/advanced/teemo-hidden-ambush-advanced.md` (Mind/Chaos) vs
`decks/synergy/lucian-equipment-assault-synergy.md` (Fury/Body) — no shared
domain, no shared cards, and it's the first sim to actually read the full
Hidden rule (rather than just the reminder text) and the first to play
Equipment attach/detach and Weaponmaster in a real game.

## Mode And Setup Assumptions

Source: `Riftbound_Core_Rules_RUP3_Staging.pdf`.

- Mode: 1v1 Duel, Victory Score 8. First player: Lucian. Second player:
  Teemo — one extra Rune on their first Channel Phase only (rule 480.7).
- Draws 4, mulligan up to 2 (rule 117-118). Both hands kept as drawn.
- Battlefields chosen: `Forge of the Fluft` (SFD-208) for Lucian,
  `Bandle Tree` (OGN-278) for Teemo — the first-listed recommendation in
  each deck file. Both start uncontrolled (same precedent as prior sims).
- Standard Move only costs exhausting the unit (rule 144.2) — no Energy —
  and Standard Move only goes Base↔Battlefield, never
  Battlefield↔Battlefield, unless the unit has `[Ganking]` (rule 144.4).
  This matters directly in this sim (see Turn 4 Lucian).

### Newly Read This Sim: The Full `[Hidden]` Rule (rule 811)

Prior sims only used the card-text reminder ("Hide now for Any Rune to
react with later for 0 Energy"). The full rule (811.1.b) adds real
constraints:

- Hiding a card requires the hiding player to **control a battlefield**
  right now — the card goes face down into that specific battlefield's
  Facedown Zone. You cannot hide a card before you control anywhere.
- Each battlefield's Facedown Zone holds only **one** hidden card per
  player by default; `Bandle Tree`'s own text ("you may hide an additional
  card here") raises that specific location's cap to two, not unlimited.
- A hidden card cannot be revealed the turn it was hidden — rule 811.1.b:
  "Beginning on the next turn, this gains [Reaction]." The earliest reveal
  is the hiding player's *next* turn.
- If a hidden permanent's play effect targets something, the target must be
  chosen from among options **at the battlefield where it was hidden**
  (rule 811.1.d.2), unless that would leave literally zero legal targets, in
  which case it can target freely. `Blastcone Fae`'s own reminder text is
  the rulebook's own worked example of this exact restriction.
- Losing Control of the battlefield where a card is hidden gets that card
  removed during the next Cleanup (rule 107.3.d, found while re-reading the
  Facedown Zone rule for this sim) — a hidden card is not safe just because
  it's face down.

## Known Simulation Limitations

- Manual replay, not a full engine, same as prior sims.
- Battlefield selection used each deck file's first-listed recommendation
  deterministically rather than `references/simulation-playtest-protocol.md`'s
  documented method (choose exactly three, then randomly select one). Both
  deck files already list exactly three battlefields, so this is a
  documented shortcut for reproducibility, not a rules violation — a real
  game should still randomize among the three.
- Stops after 4 rounds by design, once the Hidden-targeting-restriction
  finding and the Weaponmaster/Ganking findings below were produced.

## Deterministic Setup

### Lucian (Fury, Body)

Opening hand (kept, no mulligan): `Veteran Poro`, `Doran's Blade`,
`Long Sword`, `Angle Shot`.

Battlefield: `Forge of the Fluft`.

### Teemo (Mind, Chaos)

Opening hand (kept, no mulligan): `Teemo - Scout` (one of the two extra
Main Deck copies — the Chosen Champion's own copy started in the Champion
Zone per rule 103.2.a.1 and is separate from this one), `Blastcone Fae`,
`Wages of Pain`, `Ember Monk`.

Battlefield: `Bandle Tree`.

## Turn Log

### Turn 1: Lucian

- Channel: `Fury Rune`, `Body Rune`.
- Draw: `Sentinel Adept`.
- Main: plays `Veteran Poro` to base using 2 Energy. Enters exhausted.
  `[Weaponmaster]`'s optional Equip trigger has no Equipment on board to
  choose from yet, so it does nothing this turn.
- End state: score 0. Base: exhausted `Veteran Poro`. Hand: `Doran's Blade`,
  `Long Sword`, `Angle Shot`, `Sentinel Adept`.

### Turn 1: Teemo

- Channel: `Chaos Rune`, `Chaos Rune`, `Mind Rune` (2 base + 1 for going
  second).
- Draw: `Tideturner`.
- Main: plays `Teemo - Scout` **face up, normally** (not hidden — Teemo
  doesn't control any battlefield yet, so Hiding isn't available per rule
  811.1.b) to base using 2 Energy. Enters exhausted. On-play +3 Might this
  turn — a wasted bonus this turn since it isn't fighting, but legal.
- End state: score 0. Base: exhausted `Teemo - Scout`. Hand: `Blastcone Fae`,
  `Wages of Pain`, `Ember Monk`, `Tideturner`.

### Turn 2: Lucian

- Awaken: readies `Veteran Poro` and channeled Runes.
- Channel: 2 more Runes.
- Draw: `Strike Down`.
- Main:
  - Plays `Long Sword` to base using 2 Energy. **Enters Ready** (Gear, rule
    149.1). `[Quick-Draw]` is a Reaction that fires immediately on play,
    attaching it to `Veteran Poro` (the only unit Lucian controls) at no
    additional cost. `Lucian - Purifier`'s Legend ability grants
    `[Assault]` to every Equipped unit, so `Veteran Poro` is now Might 2
    (base) + 2 (`Long Sword`'s own Might bonus) = 4, plus +1 while
    attacking from the Legend's granted Assault.
  - Moves ready `Veteran Poro` from base to `Forge of the Fluft`,
    exhausting it. Uncontrolled → Non-Combat Showdown → both pass → Lucian
    conquers, scores 1.
- End state: score 1. Controls `Forge of the Fluft` (exhausted
  `Veteran Poro`, equipped with `Long Sword`). Base: empty. Hand:
  `Doran's Blade`, `Angle Shot`, `Sentinel Adept`, `Strike Down`.

### Turn 2: Teemo

- Awaken: readies `Teemo - Scout`; its +3 Might expired at the end of Turn 1
  (rule 317.2.c, "all 'this turn' effects expire simultaneously").
- Channel: 2 more Runes.
- Draw: `Keeper of Masks`.
- Main:
  - Moves ready `Teemo - Scout` from base to `Bandle Tree`, exhausting it.
    Uncontrolled → Non-Combat Showdown → both pass → Teemo conquers, scores
    1. Now controlling a battlefield, Hiding is available.
  - Hides `Blastcone Fae` at `Bandle Tree`, paying 1 Energy via
    `Teemo - Swift Scout`'s Legend discount (instead of recycling Any
    Rune). `Bandle Tree`'s own text raises its Facedown Zone cap to 2, so
    also hides `Wages of Pain` there for another 1 Energy. 2 Energy spent
    total; both cards are now face down, tied specifically to `Bandle
    Tree`'s Facedown Zone.
- End state: score 1. Controls `Bandle Tree` (ready `Teemo - Scout`, 2
  hidden cards: `Blastcone Fae`, `Wages of Pain`). Hand: `Ember Monk`,
  `Tideturner`, `Keeper of Masks`.

### Turn 3: Lucian

- Awaken: readies `Veteran Poro` (with `Long Sword` attached) and channeled
  Runes.
- Beginning: holds `Forge of the Fluft` → scores 1 (1 → 2).
- Channel: 2 more Runes.
- Draw: `Boneshiver`.
- Main:
  - Plays `Sentinel Adept` to base using 3 Energy. Enters exhausted.
    `[Weaponmaster]`'s Equip clause allows attaching Equipment "even if
    it's already attached" — moves `Long Sword` off `Veteran Poro` and onto
    `Sentinel Adept` instead, discounted to free by Weaponmaster's "for Any
    Rune less." `Veteran Poro` reverts to its base Might 2 (no Equipment,
    no Legend Assault bonus); `Sentinel Adept` becomes Might 3 (base) + 2
    (`Long Sword`) = 5, plus Assault while attacking.
  - Plays `Doran's Blade` to base using 2 Energy. Enters Ready but
    unattached (it has no Quick-Draw). Activates its own `[Equip] Body
    Rune` ability: Recycles a Body Rune (removed from the board — see the
    resolved Domain Power rule from SIM-0003) to attach it to
    `Veteran Poro`, bringing it back to Might 2 + 2 = 4, plus Assault while
    attacking.
- End state: score 2. Controls `Forge of the Fluft` (ready `Veteran Poro`
  with `Doran's Blade`, ready `Sentinel Adept` with `Long Sword`). Hand:
  `Angle Shot`, `Strike Down`, `Boneshiver`.

### Turn 3: Teemo

- Awaken: readies `Teemo - Scout`.
- Beginning: holds `Bandle Tree` → scores 1 (1 → 2).
- Channel: 2 more Runes.
- Draw: `Evelynn - Entrancing`.
- Main:
  - Considered flipping `Blastcone Fae` (hideable since last turn was
    Teemo's own prior turn): its play effect must target a unit **at
    `Bandle Tree`** (rule 811.1.d.2), and the only unit there right now is
    `Teemo - Scout` itself — there's no enemy unit at that specific
    battlefield to debuff. Flipping it now would force a self-inflicted
    -2 Might. Held instead — see Findings.
  - Plays `Ember Monk` to base using 4 Energy. Enters exhausted. Its own
    "when you play a card from Hidden" trigger doesn't fire from playing
    itself normally.
- End state: score 2. Controls `Bandle Tree` (ready `Teemo - Scout`, 2
  hidden cards still down). Base: exhausted `Ember Monk`. Hand:
  `Tideturner`, `Keeper of Masks`, `Evelynn - Entrancing`.

### Turn 4: Lucian

- Awaken: readies `Veteran Poro` and `Sentinel Adept`.
- Beginning: holds `Forge of the Fluft` → scores 1 (2 → 3).
- Channel: 2 more Runes.
- Draw: `Rell - Magnetic`.
- Main:
  - Considered moving `Veteran Poro` and `Sentinel Adept` directly to
    `Bandle Tree` to pressure Teemo. Neither has `[Ganking]`, and Standard
    Move only goes Base↔Battlefield (rule 144.4.a-b) — a unit already at a
    battlefield can't Move directly to a *different* battlefield without
    it. Reaching `Bandle Tree` would take a Move to base this turn and a
    second Move next turn, costing tempo. Held that plan and developed
    instead.
  - Plays `Rell - Magnetic` to base using 4 Energy. Enters exhausted.
  - Plays `Boneshiver` to base using 3 Energy. Enters Ready, unattached
    (not yet activated).
- End state: score 3. Controls `Forge of the Fluft` (ready `Veteran Poro`
  with `Doran's Blade`, ready `Sentinel Adept` with `Long Sword`). Base:
  exhausted `Rell - Magnetic`, ready unattached `Boneshiver`. Hand:
  `Angle Shot`, `Strike Down`.

### Turn 4: Teemo

- Awaken: readies `Teemo - Scout` and `Ember Monk`.
- Beginning: holds `Bandle Tree` → scores 1 (2 → 3).
- Channel: 2 more Runes.
- Draw: `Consult the Past`.
- Main:
  - Moves ready `Ember Monk` from base to `Bandle Tree`, joining
    `Teemo - Scout` (same controller, no Contest, no Combat).
  - Still no enemy unit at `Bandle Tree`, so `Blastcone Fae` stays hidden
    rather than whiffing on a self-target.
  - `Bandle Tree`'s Facedown Zone is already at its raised cap of 2 (both
    slots filled), so `Consult the Past` can't be hidden there this turn —
    it's a `[Reaction]`, so it's held in hand for a good moment on Lucian's
    turn instead of being wasted on a spot that isn't available.
- End state: score 3. Controls `Bandle Tree` (ready `Teemo - Scout`, ready
  `Ember Monk`, 2 hidden cards). Hand: `Tideturner`, `Keeper of Masks`,
  `Evelynn - Entrancing`, `Consult the Past`.

## Score After 4 Rounds

- Lucian: 3.
- Teemo: 3.

Tied — neither side has attacked the other yet; both spent these four
rounds developing their own battlefield.

## Findings

### Deck File Finding — Teemo: Hidden Targeting Needs A Target

`Blastcone Fae`'s own reminder text already warns that its play effect must
target a unit at the battlefield where it was hidden, but this sim shows the
practical trap: if you hide it at a battlefield with **no enemy units**,
flipping it later forces you to target your own stuff (or leaves it dead if
somehow no target exists at all). The deck's Watch Outs should say this
explicitly: only hide `Blastcone Fae` (or `Edge of Night`, which has a
similar location lock) at a battlefield you expect an enemy to show up at,
or hold it until one does, rather than treating "it's hidden, it'll be
useful eventually" as automatic.

### Deck File Finding — Lucian: No Ganking Anywhere In The List

None of `Lucian - Merciless`, `Lucian - Gunslinger`, `Veteran Poro`,
`Sentinel Adept`, `Combat Chef`, `Armed Assailant`, `Jax - Unrelenting`,
`Yone - Blademaster`, or `Rell - Magnetic` have `[Ganking]`. That means once
this deck commits a board to one battlefield, contesting a second
battlefield always costs a full extra turn (recall to base, then move to
the new battlefield) rather than a single hop — a real tempo cost worth a
line in the deck's Watch Outs, since the deck's own How To Play doesn't
currently mention it.

### Rules Findings (New Since SIM-0001/0002/0003)

- **Hiding requires controlling a battlefield right now** — you can't hide
  a card before you control anywhere (rule 811.1.b). Prior sims never
  needed this because they never had a Hidden-heavy deck before its pilot
  controlled a battlefield.
- **A hidden card can't be revealed the same turn it's hidden** — earliest
  reveal is the hiding player's next turn (rule 811.1.b, "Beginning on the
  next turn, this gains [Reaction]").
- **A hidden permanent's targeting is locked to the battlefield where it
  was hidden** unless doing so would leave zero legal targets (rule
  811.1.d.2). This is the rule behind the finding above.
- **Facedown Zone capacity is per-battlefield, normally 1, and tied to
  Control**: `Bandle Tree` raises its own cap to 2, but losing Control of
  any battlefield removes whatever's hidden there during the next Cleanup
  (rule 107.3.d) — a hidden card is not "safe" just because it's face down.
- **Weaponmaster can re-target Equipment that's already attached elsewhere**
  ("even if it's already attached" is explicit card text, confirmed in
  live play by moving `Long Sword` off `Veteran Poro` and onto
  `Sentinel Adept` for free).
- **Standard Move never goes Battlefield-to-Battlefield without
  `[Ganking]`** (rule 144.4) — confirmed as a real tempo constraint, not
  just a rules footnote, when Lucian's board couldn't directly contest
  Teemo's battlefield.

## Recommended Next Step

Stop here; the sim already produced two real deck-file findings and
confirmed five distinct rules points about Hidden, Weaponmaster, and
movement. The board state is tied 3-3 with neither side having fought yet —
continuing would mostly test combat math this project has already verified
in SIM-0001/0002/0003, not new rules territory.

## Follow-Up

- Add a Watch Out to `decks/advanced/teemo-hidden-ambush-advanced.md`: only
  hide location-locked payoffs (`Blastcone Fae`, `Edge of Night`) at a
  battlefield you expect to have an enemy unit at, and remember losing
  Control of a battlefield destroys whatever's hidden there.
- Add a Watch Out to `decks/synergy/lucian-equipment-assault-synergy.md`:
  the deck has no Ganking, so contesting a second battlefield costs a full
  extra turn of recall-then-move — plan board commitments accordingly.