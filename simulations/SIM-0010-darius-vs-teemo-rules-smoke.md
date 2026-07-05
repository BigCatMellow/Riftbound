# SIM-0010: Darius Legion Tempo vs Teemo Hidden Ambush

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0010 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 4 rounds by design |
| Purpose | First test for the new Darius deck. Gave a concrete, costly demonstration of the Hidden-card-loss-on-Control-loss finding from SIM-0004, this time actually removing real cards instead of just being a hypothetical risk. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Darius. Second player: Teemo
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation, same documented deterministic
  shortcut as prior sims): `Trifarian War Camp` for Darius, `Bandle Tree`
  for Teemo.
- Both opening hands kept. Darius: `Legion Rearguard`,
  `Trifarian Gloryseeker`, `Hextech Ray`, `Daring Poro` (plus draws).
  Teemo: `Teemo - Scout`, `Blastcone Fae`, `Wages of Pain`, `Ember Monk`
  (plus draws).

## Turn Log

### Turn 1

- **Darius**: Channels 2. Plays `Legion Rearguard` for 2 Energy — first
  card this turn, Legion inactive. Score 0.
- **Teemo**: Channels 3 (extra rune). Plays `Teemo - Scout` face up (no
  battlefield controlled yet, so Hiding isn't available) for 2 Energy. On
  play +3 Might this turn. Score 0.

### Turn 2

- **Darius**: Plays `Trifarian Gloryseeker` (first card, Legion inactive,
  no buff), then `Daring Poro` (second card — Legion is now active for the
  rest of the turn, though `Daring Poro` itself has no Legion clause to use
  it). Moves `Legion Rearguard` to `Trifarian War Camp` (uncontrolled →
  conquers, scores 1; the battlefield's own "+1 Might here" passive brings
  it to Might 3).
- **Teemo**: `Teemo - Scout`'s +3 Might expired at end of Turn 1. Moves it
  to `Bandle Tree` (uncontrolled → conquers, scores 1). Now controlling a
  battlefield, hides `Blastcone Fae` and `Wages of Pain` there (2 Energy
  via the Legend's discount, `Bandle Tree`'s own raised cap of 2).

Score: Darius 1, Teemo 1.

### Turn 3

- **Darius**: Holds `Trifarian War Camp` → scores 1 (1 → 2). Plays
  `Hextech Ray` (first card, Legion inactive) targeting `Teemo - Scout`
  (Might 1, the only enemy unit on the board) for 3 damage — dies. Tries to
  play `Noxian Guillotine` next, but **there is no legal enemy unit left
  anywhere on the board** to target — a removal spell with zero valid
  targets can't be played at all, the same "no legal target" principle
  confirmed for `[Hidden]` cards in SIM-0004, now shown for an ordinary
  removal spell too. Plays `Vanguard Captain` instead (Legion is active
  from `Hextech Ray`, but `Vanguard Captain`'s own `[Legion]` still
  requires it specifically: makes two 1 Might Recruit tokens on play).
- **Teemo**: `Teemo - Scout` died last turn, so `Bandle Tree` was already
  lost — **and everything hidden there is removed at the next Cleanup**
  once Control is lost (rule 107.3.d, confirmed again here, this time with
  real stakes): both `Blastcone Fae` and `Wages of Pain` are gone from the
  game, straight to the trash, with no reveal and no refund. Plays
  `Pyke - Returned` face up (no battlefield controlled) for 3 Energy.

Score: Darius 2, Teemo 1 — and Teemo is down two real cards for nothing.

### Turn 4

- **Darius**: Holds `Trifarian War Camp` → scores 1 (2 → 3). Plays `Cleave`
  first (Legion now active), then `Noxian Guillotine` targeting
  `Pyke - Returned` (Might 3, Teemo's only unit) — with Legion active, its
  `[Legion]` clause kills it **immediately** instead of only "the next time
  it takes damage this turn." Same card, and this time the sequencing paid
  off: an instant kill instead of a conditional one.
- **Teemo**: No battlefield, no score. Plays `Ember Monk` for 4 Energy.

Score: Darius 3, Teemo 1.

## Findings

### Costly Confirmation — Hidden Cards Are Truly Gone When Their Battlefield Is Lost

SIM-0004 flagged this as a risk in the abstract; this game shows the actual
cost. Teemo lost `Teemo - Scout` to a 1-cost removal spell on Turn 3, which
also destroyed two hidden cards (`Blastcone Fae`, `Wages of Pain`) that
had nothing to do with the fight that killed their battlefield's only
unit — they were just sitting safely, as far as the pilot might assume,
until the battlefield itself became uncontrolled. This is a sharp
reminder that "hidden" does not mean "protected"; it means "tied to a
specific piece of board state that can be taken away by any means,
including a cheap removal spell aimed at something else entirely."

### Rules Finding — A Spell With Zero Legal Targets On The Board Cannot Be Played

`Noxian Guillotine` couldn't be played on Turn 3 immediately after
`Hextech Ray` cleared the only enemy unit, because there was nothing left
to target. This is the same "no valid target, can't be played" principle
SIM-0004 found for `[Hidden]` cards (rule 811.1.d), shown here applying to
an ordinary targeted removal spell with no Hidden component at all — a
general targeting rule, not something specific to Hidden cards.

### Rules Finding — Legion's Instant-Kill Mode Rewards Correct Sequencing, Concretely

Turn 4 showed the exact contrast the Darius deck file's How To Play already
described in the abstract: the same `Noxian Guillotine` card, played after
a Legion-setup card, killed its target immediately instead of only setting
up a conditional kill. This is the clearest single-turn demonstration yet
of why this deck is rated Advanced — the card's own effectiveness literally
doubles based on play order within the same turn.

## Recommended Next Step

Stop here; the Hidden-card-loss finding recurring with real stakes (rather
than only a hypothetical) is a strong enough signal on its own. No
additional deck-file fix needed — the existing Teemo Watch Out already
covers this; this sim is further confirmation of an already-documented
risk, not a new gap.