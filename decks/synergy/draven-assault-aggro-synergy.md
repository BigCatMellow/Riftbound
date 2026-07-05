# Draven Assault Aggro (Synergy)

## Snapshot

| Field | Value |
|---|---|
| Category | Synergy |
| Legend | Draven - Glorious Executioner |
| Domains | Fury, Chaos |
| Chosen champion | Draven - Audacious |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | None |
| Difficulty | Medium |
| Core plan | Stack `[Assault]` onto attackers to win combats cleanly, then convert every win directly into cards (the Legend) and points (`Draven - Audacious`) — a combat-first identity distinct from this project's other two Fury/Chaos decks (`Jinx`'s discard engine and `Annie`'s spell burn). |

## Why This Is A Synergy Deck

`Draven - Glorious Executioner`'s "When you win a combat, draw 1" and
`Draven - Audacious`'s "The first time I win a combat each turn, you score
1 point" both key off the same event — winning a fight, not just attacking
or dealing damage — so every `[Assault]` buff in this list is pulling
double duty: it helps win the fight, and winning the fight is the payoff
condition for two separate cards at once. `Corrupt Enforcer`'s own
"When I win a combat, draw 1" stacks a third copy of that exact payoff.

## Legality Notes

- Domain identity: Draven - Glorious Executioner is Fury/Chaos. Every main
  deck card is single-domain Fury or single-domain Chaos.
- Copy-limit check: `Draven - Audacious` has 1 chosen-champion copy plus 2
  main deck copies (3 total). No other card exceeds 3 copies.
- Signature check: no signature cards are included.
- Banned/errata check: `Draven - Vanquisher` (SFD-020) is marked **Banned**
  in the local card database and is intentionally excluded —
  `Draven - Audacious` fills the Chosen Champion slot instead. No other
  card used here is banned.
- Champion tag: `Draven - Audacious` is inferred to carry the `Draven`
  champion tag from card name and the Legend's own name; `Draven -
  Showboat` is included as a generic Fury unit, not the Chosen Champion.
  The source export has no explicit tag column — confirm the printed tag
  before tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Draven - Glorious Executioner | SFD-185 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Draven - Audacious | SFD-148 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Draven - Audacious | SFD-148 | Champion Unit | 6 |
| 2 | Rengar - Pouncing | SFD-025 | Champion Unit | 3 |
| 2 | Rengar - Unseen | UNL-024 | Champion Unit | 4 |
| 2 | Vayne - Hunter | OGN-035 | Champion Unit | 4 |
| 2 | Captain Farron | OGN-015 | Unit | 4 |
| 2 | Lord Broadmane | UNL-012 | Unit | 5 |
| 3 | Chemtech Enforcer | OGN-003 | Unit | 2 |
| 2 | Inferna | UNL-002 | Unit | 2 |
| 2 | Sharkling | UNL-006 | Unit | 3 |
| 3 | Towering Pairofant | UNL-008 | Unit | 6 |
| 3 | Corrupt Enforcer | SFD-123 | Unit | 3 |
| 3 | Ancient Warmonger | SFD-131 | Unit | 5 |
| 3 | Blood Rush | SFD-003 | Spell | 1 |
| 3 | Cleave | OGN-004 | Spell | 1 |
| 3 | Vault Breaker | UNL-010 | Spell | 1 |
| 1 | Square Up | UNL-017 | Spell | 4 |
| 2 | Draven - Showboat | OGN-028 | Champion Unit | 5 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 6 | Fury Rune | OGN-007 |
| 6 | Chaos Rune | OGN-166 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Trifarian War Camp | OGN-294 | A flat Might buff for units here stacks directly with every Assault buff, making combats easier to win outright. |
| Void Gate | OGN-296 | Bonus damage to spell/ability effects here — note this does **not** boost Combat damage itself (confirmed in `simulations/SIM-0007-annie-vs-khazix-rules-smoke.md`, rule 417.6.c), only this deck's few damage-dealing effects, if any are added later. |
| The Grand Plaza | OGN-293 | A wide, aggressive board of cheap Assault units can reach the 7-units-here alternate win condition as a side effect of just attacking normally. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Draven - Glorious Executioner | Legend | | | Win a combat, draw 1. | Turns every won fight into a card, no matter which unit won it. |
| Draven - Audacious | Champion Unit | 6 | 6 | [Deflect]. First combat win each turn scores 1 point. Dying in combat gives an opponent a point. | Chosen champion; converts the deck's own combat-first plan directly into points. |
| Rengar - Pouncing | Champion Unit | 3 | 3 | [Reaction]. [Assault 2]. Can be played to a battlefield you're already attacking. | Reinforces a fight already in progress instead of waiting for the next turn. |
| Rengar - Unseen | Champion Unit | 4 | 4 | [Accelerate]. [Assault 2]. [Deflect]. [Ganking]. | A well-rounded attacker that's hard to remove and can reposition. |
| Vayne - Hunter | Champion Unit | 4 | 2 | [Assault 3]. Enters ready if the opponent controls a battlefield. May bounce itself on conquer for 1 Energy. | Big swing Might while attacking, often ready the turn it's played. |
| Captain Farron | Unit | 4 | 5 | Other friendly units here have Assault. | A local anthem that turns every ally at its battlefield into an attacker threat. |
| Lord Broadmane | Unit | 5 | 5 | [Ambush]. On play, other units here get Assault this turn. | A one-turn version of Captain Farron's effect, timed to land right before a big attack. |
| Chemtech Enforcer | Unit | 2 | 2 | [Assault 2]. On play, discard 1. | Cheap attacker; the discard is a minor cost, not a payoff in this build. |
| Inferna | Unit | 2 | 1 | [Ambush]. [Assault 2]. | Cheap surprise attacker. |
| Sharkling | Unit | 3 | 1 | [Accelerate]. [Assault 4]. | Huge Might swing while attacking off a cheap body. |
| Towering Pairofant | Unit | 6 | 6 | [Assault]. Enters ready if a unit died this turn. | Big body that often arrives ready given how much combat this deck picks. |
| Corrupt Enforcer | Unit | 3 | 4 | On move to a battlefield, discard 1. On combat win, draw 1. | A third source of the Legend's exact payoff condition. |
| Ancient Warmonger | Unit | 5 | 4 | [Accelerate]. Assault equal to the number of enemy units here. | Scales hardest into a crowded battlefield, the opposite of most Assault cards. |
| Blood Rush | Spell | 1 | | [Action], [Repeat] 1 Energy. Assault 2 this turn. | Cheap, repeatable combat trick. |
| Cleave | Spell | 1 | | [Action]. Assault 3 this turn. | Efficient one-shot Might swing. |
| Vault Breaker | Spell | 1 | | [Action]. Assault 2 and Ganking this turn. | Combat trick that also lets the target reposition after winning. |
| Square Up | Spell | 4 | | [Repeat] — discard 1. Assault 4 this turn. | Big, repeatable Might swing for a deck with card advantage to spend. |
| Draven - Showboat | Champion Unit | 5 | 3 | My Might is increased by your points. | Scales automatically as the deck's own scoring plan progresses. |

## How To Play

1. Play cheap Assault attackers early (`Chemtech Enforcer`, `Inferna`,
   `Sharkling`) and start picking fights you can win outright.
2. Every combat win triggers the Legend's draw — and `Corrupt Enforcer`'s
   own copy of the same trigger if it's the one winning — so favor
   attacking with a unit that will actually win the fight over a riskier
   attacker.
3. Play `Draven - Audacious` once the deck is already winning fights
   regularly; its score-on-win clause only needs the *first* win of the
   turn, so it doesn't need to win every fight itself.
4. Use `Lord Broadmane` or `Captain Farron` right before a big attack to
   push several units over the line in the same combat.
5. Hold cheap Assault spells (`Blood Rush`, `Cleave`, `Vault Breaker`) as
   insurance to win a fight that would otherwise be close or lost.
6. `Draven - Showboat` gets better automatically as the game goes on — it's
   a fine mid-game play but a genuine threat once the deck has banked a
   few points already.

## Mulligan

Keep:

- one cheap Assault attacker: `Chemtech Enforcer`, `Inferna`, or
  `Sharkling`;
- one cheap Assault spell: `Blood Rush`, `Cleave`, or `Vault Breaker`;
- one payoff or anthem: `Corrupt Enforcer`, `Captain Farron`, or
  `Draven - Audacious` only with an early attacker to support it.

Avoid keeping `Towering Pairofant` or `Ancient Warmonger` without any early
attackers — both want the board already fighting to be at their best.

## Watch Outs

- Winning a combat requires only your units to remain after it (per the
  Legend's own reminder text) — a mutual trade where both sides lose units
  does **not** count as a win, so it won't trigger the Legend's draw or
  `Draven - Audacious`'s score.
- `Ancient Warmonger`'s Assault scales with *enemy* units at its
  battlefield, so it's weakest exactly when you're picking a clean 1-on-1
  fight and strongest when the opponent has stacked up defenders.
- `Vayne - Hunter`'s enters-ready clause depends on the opponent
  controlling a battlefield at all — it won't be ready if they don't
  control anything yet.
- `Draven - Audacious`'s score-on-win is capped at the *first* win each
  turn — stacking multiple wins in one turn doesn't score extra points from
  it, only the Legend's draw and `Corrupt Enforcer`'s draw scale
  per-win.

## Upgrade Paths

- Add `Draven - Vanquisher`'s effect via a proxy discussion only if your
  playgroup's banned list differs from this project's source data — it is
  currently banned here and intentionally excluded.
- Add more removal if the deck struggles to find combats it can cleanly
  win rather than trade into.
- For a lower-complexity version, cut `Ancient Warmonger` and
  `Vayne - Hunter` (both have conditional stat lines that need board-state
  awareness) and keep only the flat Assault-granting cards.
