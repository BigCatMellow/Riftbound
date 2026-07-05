# SIM-0011: Lillia Sprite Swarm vs Kha'Zix XP Burst

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0011 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 4 rounds by design |
| Purpose | Second test for Lillia, first cross-domain test against Kha'Zix. Contains a mid-sim self-correction (see Turn 2) and a genuinely new Zilean - Time Mage timing finding. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Lillia. Second player: Kha'Zix
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation, same documented deterministic
  shortcut as prior sims): `The Grand Plaza` for Lillia, `Sunken Temple`
  for Kha'Zix.
- Both opening hands kept. Lillia: `Sprite Fountain`, `Trevor Snoozebottom`,
  `Desert's Call`, `Ahri - Inquisitive` (plus draws). Kha'Zix:
  `Gemhand Hunter`, `Voracious Gromp`, `Grim Resolve`, `Crowd Favorite`
  (plus draws).

## Turn Log

### Turn 1

- **Lillia**: Channels 2. Plays `Sprite Fountain` for 2 Energy — enters
  Ready (Gear), makes a ready 3 Might Sprite token to base. Score 0.
- **Kha'Zix**: Channels 3 (extra rune). Plays `Gemhand Hunter` for 2
  Energy. Score 0, XP 0.

### Turn 2 (includes a self-correction)

**Correction, made while writing this turn:** the Sprite token created on
Turn 1's Main Phase dies at the start of the **very next** Beginning
Phase, before scoring (rule 315.2.a-b, the same timing SIM-0009 already
established) — that's Lillia's own Turn 2 Beginning Phase, not Turn 3's.
An earlier draft of this turn incorrectly had the token surviving to be
moved during Turn 2's Main Phase. Corrected below: the token is already
dead by the time Turn 2's Main Phase happens.

- **Lillia**: Awaken (nothing new to ready). Beginning: the Turn 1 Sprite
  token dies now — no battlefield was controlled yet, so this doesn't cost
  a hold. Plays `Trevor Snoozebottom` directly to `The Grand Plaza`
  (uncontrolled → Contested the same way a Move would be, per SIM-0009 →
  conquers, scores 1). 1 Energy left, nothing else affordable.
- **Kha'Zix**: Plays `Voracious Gromp` for 5 Energy. Moves `Gemhand Hunter`
  to `Sunken Temple` (uncontrolled → conquers, scores 1; `[Hunt]` gains 1
  XP → 1).

Score: Lillia 1, Kha'Zix 1.

### Turn 3

- **Lillia**: Holds `The Grand Plaza` → scores 1 (1 → 2).
  `Trevor Snoozebottom` (not Temporary itself, so no repeat of the SIM-0009
  hold-loss trap) triggers its own "on hold, play a ready 3 Might Sprite
  token here" — makes a new token. Plays `Zilean - Time Mage` to
  `The Grand Plaza` for 5 Energy.
- **Kha'Zix**: Holds `Sunken Temple` → scores 1 (1 → 2). Plays the chosen
  champion `Kha'Zix - Evolving Hunter` from the Champion Zone for 5
  Energy. Moves `Voracious Gromp` (Might 5) to `The Grand Plaza`, contesting
  `Trevor Snoozebottom` (`[Shield]`, Might 3 + 1 = 4 while defending) and
  the fresh Sprite token (Might 3) — Combat stages. Both pass. Combat
  Damage: Kha'Zix (5) assigns 3 to the Sprite token (lethal, dies), the
  remaining 2 to `Trevor Snoozebottom` (needs 4 for lethal, survives).
  Lillia (4 + 3 = 7) assigns all 7 to the lone `Voracious Gromp` — dies.
  Cleanup: Lillia still has `Trevor Snoozebottom` there — retains Control
  (no new conquer, already hers). Heals `Trevor Snoozebottom`'s 2 damage.

Score: Lillia 2, Kha'Zix 2 (Kha'Zix's attack was repelled).

### Turn 4

- **Lillia**: Holds `The Grand Plaza` → scores 1 (2 → 3).
  `Trevor Snoozebottom`'s hold trigger makes another Sprite token — and
  this is the **first token play of the turn**, so `Zilean - Time Mage`'s
  "once each turn" doubling applies to it: the Beginning Phase hold
  trigger produces **two** ready Sprite tokens instead of one, since a
  Beginning-Phase token creation is still "playing a token unit" for
  Zilean's purposes (rule 176 — tokens can still be Played even though
  they aren't cards). Plays `Sprite Mother` to `The Grand Plaza` for 4
  Energy in the Main Phase — its own on-play token doesn't get doubled,
  since Zilean's once-per-turn effect was already used up by the earlier
  hold trigger. `The Grand Plaza` now has 6 units total (`Trevor
  Snoozebottom`, `Zilean - Time Mage`, two Sprite tokens from the doubled
  hold, `Sprite Mother`, and its own fresh Sprite token) — one short of
  the battlefield's own 7-unit win condition.
- **Kha'Zix**: Holds `Sunken Temple` → scores 1 (2 → 3). Plays
  `Crowd Favorite` for 3 Energy.

Score: Lillia 3, Kha'Zix 3.

## Findings

### Process Note — Temporary Token Timing Is Easy To Get Wrong, Even Having Just Confirmed The Rule

This sim's own first draft of Turn 2 made exactly the mistake SIM-0009 had
just finished establishing the rule against: it let a Temporary token
survive one Beginning Phase too many. Catching and correcting it here
rather than letting it stand is the point of self-auditing inline, but it's
worth recording plainly that even a rule confirmed one game prior is easy
to mis-time in the next one — this is a good argument for a future sim
(or an actual engine) tracking token "expires at start of turn N" as an
explicit per-token field rather than re-deriving it from memory each time.

### New Finding — "Once Each Turn" Replacement Effects Can Fire On A Trigger You Don't Choose The Timing Of

`Zilean - Time Mage`'s token-doubling is a once-per-turn effect, but the
first qualifying token play of a turn can be an automatic Beginning-Phase
hold trigger (like `Trevor Snoozebottom`'s), which happens before the
player has made any Main Phase choices at all. That means the doubling
can get "spent" on whatever the hold trigger happens to make, rather than
saved for a bigger token play the pilot would have preferred to double
later that same turn. This is a genuine sequencing consideration for the
Lillia deck that its file doesn't currently mention.

### Confirmed, Consistent With Prior Sims

- Playing a card directly to an uncontrolled battlefield applies Contested
  the same way moving there does (re-confirmed from SIM-0009).
- Multi-unit Combat Damage assignment and Shield's defense-only bonus both
  behaved exactly as established in SIM-0003/0006/0008 — no new wrinkle
  here, just consistent behavior.

## Recommended Next Step

Stop here. Add the Zilean timing finding to the Lillia deck file; no other
deck-file fix needed. Continue toward the 7-unit win condition in a future
sim only if the alternate-win-condition claim specifically needs a
demonstrated finish.

## Follow-Up

- Add a note to `decks/synergy/lillia-sprite-swarm-synergy.md`: if
  `Zilean - Time Mage` is at a battlefield with a hold-trigger token-maker
  (like `Trevor Snoozebottom`) also there, its once-per-turn doubling will
  apply to that automatic Beginning Phase token first, before any Main
  Phase token play that turn — plan around the doubling landing on the
  hold trigger, not a bigger card you'd rather double.