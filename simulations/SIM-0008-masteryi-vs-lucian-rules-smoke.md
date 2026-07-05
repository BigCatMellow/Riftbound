# SIM-0008: Master Yi XP Snowball vs Lucian Equipment Assault

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0008 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 4 rounds by design |
| Purpose | Sample-size batch; both decks share the Body domain. Surfaced a genuine rules ambiguity worth flagging rather than resolving with false confidence. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Master Yi. Second player: Lucian
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation, same documented deterministic
  shortcut as prior sims): `Reckoner's Arena` for Master Yi,
  `Forge of the Fluft` for Lucian.
- Both opening hands kept. Master Yi: `Gemhand Hunter`, `Mosstomper`,
  `Master Yi - Tempered`, `Combat Experience` (plus draws). Lucian:
  `Veteran Poro`, `Long Sword`, `Doran's Blade`, `Sentinel Adept` (plus
  draws).

## Turn Log

### Turn 1

- **Master Yi**: Channels 2. Plays `Gemhand Hunter` for 2 Energy. Score 0,
  XP 0.
- **Lucian**: Channels 3 (extra rune). Plays `Veteran Poro` for 2 Energy —
  no Equipment yet, so `[Weaponmaster]`'s trigger fizzles.

### Turn 2

- **Master Yi**: Plays `Mosstomper` for 3 Energy. Moves `Gemhand Hunter` to
  `Reckoner's Arena` (uncontrolled → conquers, scores 1; `[Hunt]` gains 1
  XP → 1).
- **Lucian**: Plays `Long Sword` for 2 Energy — enters Ready, `[Quick-Draw]`
  auto-attaches it to `Veteran Poro` (Might 2 + 2 = 4, plus the Legend's
  Assault-while-attacking). Moves `Veteran Poro` to `Forge of the Fluft`
  (uncontrolled → conquers, scores 1).

Score: Master Yi 1, Lucian 1.

### Turn 3

- **Master Yi**: Holds `Reckoner's Arena` → scores 1 (1 → 2). **Open
  rules question, played conservatively — see Findings**:
  `Reckoner's Arena`'s own text is "When you hold here, activate the
  conquer effects of units here," and `Gemhand Hunter`'s `[Hunt]` is
  phrased as a single combined ability, "(When I conquer or hold, gain 1
  XP.)" It's genuinely unclear whether the battlefield's "activate the
  conquer effects" clause fires a *second*, independent instance of that
  gain on top of the ability's own natural hold-trigger, or whether Hunt
  has no separable "conquer effect" distinct from its "hold" branch for
  this battlefield to re-trigger. Played this conservatively as firing
  once (the natural hold trigger only) rather than asserting a resolution.
  Plays `Herald of Spring` for 4 Energy — its on-play "gain 2 XP" is
  unconditional, not Hunt-gated, so no ambiguity there: XP 1 → 3.
- **Lucian**: Holds `Forge of the Fluft` → scores 1 (1 → 2). Plays
  `Sentinel Adept` for 3 Energy; `[Weaponmaster]`'s "even if already
  attached" clause moves `Long Sword` off `Veteran Poro` onto it instead,
  for free (Weaponmaster's discount fully covers the cost). `Veteran Poro`
  reverts to Might 2; `Sentinel Adept` becomes Might 3 + 2 = 5. Plays
  `Doran's Blade` for 2 Energy, then activates its own `[Equip] Body Rune`
  (Recycling a Body Rune) to attach it to `Veteran Poro`, bringing it back
  to Might 2 + 2 = 4.

Score: Master Yi 2, Lucian 2.

### Turn 4

- **Master Yi**: Holds `Reckoner's Arena` → scores 1 (2 → 3). Same
  conservative reading applies to both units there this time:
  `Mosstomper`'s `[Hunt 2]` fires once from the hold (XP 3 → 5);
  `Gemhand Hunter`'s `[Hunt]` fires once from the hold (XP 5 → **6**).
  Crossing 6 XP activates `Master Yi - Wuju Master`'s Level 6 clause
  ("Your units have +1 Might") immediately and continuously for as long as
  XP holds at 6+. **This stacks independently with a unit's own matching
  Level 6 text** — `Gemhand Hunter`'s own "[Level 6] I have +1 Might" is a
  *separate* source from the Legend's blanket buff (a different object
  granting a different instance of +1 Might), so it gets both: Might 2 → 4.
  `Mosstomper` has no such self-buff text, so it only gets the Legend's
  +1: Might 3 → 4. This is a different rule than the Buff *keyword*, which
  is capped at one application per unit (confirmed in SIM-0005) — plain
  stat-boost text from two different sources stacks normally. Plays
  `Master Yi - Tempered` for 4 Energy; because Level 6 is already active
  when it enters, it immediately gets the Legend's +1 Might (Might 4 → 5)
  *and* its own printed Level 6 clause (Deflect and Ganking) the moment
  it's on board — confirming these are continuously-checked conditions,
  not "must already be in play when XP crossed the threshold."
- **Lucian**: Holds `Forge of the Fluft` → scores 1 (2 → 3). Plays
  `Rell - Magnetic` for 4 Energy.

Score: Master Yi 3, Lucian 3.

## Findings

### Genuine Rules Ambiguity — Not Resolved, Flagged For Review

`Reckoner's Arena`'s "activate the conquer effects of units here" (a Hold
trigger) interacting with `[Hunt]`-style abilities that are printed as a
single combined "conquer or hold" clause is genuinely unclear from the
extracted rules text alone: does the battlefield's clause fire a second,
independent instance of the gain on a hold, or does it have nothing to
re-activate because Hunt's hold-branch already covers the same event on its
own? This sim played it conservatively (once per hold), which likely
*understates* `Reckoner's Arena`'s value if the more generous reading is
correct. Recommend either finding the disambiguating rules-glossary entry
for "conquer effects" as a defined term, or treating this as a genuine
rules question for the publisher/community rather than guessing further.

### Rules Findings (Confirmed, Not Ambiguous)

- **A card's own stat-boost text stacks independently with a separate,
  differently-sourced stat-boost**, even when both trigger off the exact
  same condition (here, both keyed to 6+ XP). This is meaningfully
  different from the Buff *keyword*, which SIM-0005 confirmed caps at one
  application per unit regardless of how many sources try to grant it —
  the cap is specific to Buff, not a general rule about stacking.
- **Level-gated abilities are continuously checked, not locked in at the
  moment a threshold is crossed.** A unit played *after* XP already reached
  6 gets every Level 6 benefit immediately, both from the Legend and from
  its own card text, with no "grandfathering" gap.

## Recommended Next Step

Stop here. Score is tied 3-3 with the game's central mechanical questions
already answered (or explicitly flagged as unresolved). No rerun needed;
the Reckoner's Arena ambiguity is a documentation gap to research
separately, not something more play-testing alone will resolve.