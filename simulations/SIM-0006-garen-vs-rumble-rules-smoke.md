# SIM-0006: Garen Go-Wide vs Rumble Mech Tribal

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0006 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 4 rounds by design |
| Purpose | Sample-size batch; a beginner deck against a synergy deck that hadn't been paired yet. Runs at the same leaner pace as SIM-0005. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Garen. Second player: Rumble
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation, same documented deterministic
  shortcut as prior sims): `Altar to Unity` for Garen, `Marai Spire` for
  Rumble.
- Both opening hands kept. Garen: `Trusty Ramhound`, `Pit Rookie`,
  `Faithful Manufactor`, `Vanguard Captain` (plus draws). Rumble:
  `Forecaster`, `Icevale Archer`, `Danger Zone`, `Hextech Ray` (plus draws).

## Turn Log

### Turn 1

- **Garen**: Channels 2. Plays `Trusty Ramhound` for 2 Energy. Score 0.
- **Rumble**: Channels 3 (extra rune). Plays `Forecaster` for 2 Energy.
  Score 0.

### Turn 2

- **Garen**: Plays `Pit Rookie` for 2 Energy; its on-play buff targets
  `Trusty Ramhound` (Might 2 → 3, no buff yet). Moves `Trusty Ramhound`
  alone to `Altar to Unity` (uncontrolled → conquers, scores 1). Moving it
  alone drops its own "+1 Might while another unit is here" static, so it
  arrives at Might 3 (buffed value only, no companion bonus).
- **Rumble**: Plays `Bubble Bot` for 3 Energy — no actual Mech in play yet
  (same "support cards aren't Mechs" gap SIM-0003 found), so its
  ready-a-Mech trigger fizzles again. Moves `Forecaster` to `Marai Spire`
  (uncontrolled → conquers, scores 1).

Score: Garen 1, Rumble 1.

### Turn 3

- **Garen**: Holds `Altar to Unity` → scores 1 (1 → 2); its hold trigger
  makes a Recruit token in base. Plays `Kinkou Monk` for 4 Energy; its
  on-play buff (no location restriction, per the SIM-0001 finding) hits
  `Pit Rookie` (2 → 3) and the new Recruit token (1 → 2). Moves `Pit Rookie`
  to join `Trusty Ramhound` at `Altar to Unity` — now that another unit is
  there again, `Trusty Ramhound`'s static re-engages: Might 3 (buff) + 1
  (companion static) = 4. This is a clean demonstration that a static
  ability's condition is checked continuously, turning off and back on as
  the board changes, not locked in at the moment it was last true.
- **Rumble**: Holds `Marai Spire` → scores 1 (1 → 2). Plays `Assembly Rig`
  for 4 Energy — enters Ready (Gear). Tries to activate its ability, which
  costs "1 Energy + Fury Rune, Recycle a unit from your trash, Exhaust":
  **Rumble's trash is empty** (no unit has died yet), so the "recycle a
  unit from your trash" portion of the cost can't be paid at all. An
  Activated Ability's cost must be payable in full to activate it at all
  (the same principle as rule 422.3's Discard-as-a-cost example) — the
  ability simply can't be used this turn. Plays `Chakram Dancer` for 3
  Energy instead; its Shield-grant lands on `Bubble Bot`, wasted since
  nothing is defending this turn.

Score: Garen 2, Rumble 2.

### Turn 4

- **Garen**: Holds `Altar to Unity` → scores 1 (2 → 3); makes another
  Recruit token. Plays `Vanguard Captain` — first card this turn, so its
  `[Legion]` clause ("play two Recruit tokens") doesn't fire. Plays
  `Faithful Manufactor` second — its own token-making effect isn't
  Legion-gated, so it still makes a Recruit token normally regardless of
  play order.
- **Rumble**: Holds `Marai Spire` → scores 1 (2 → 3). Moves `Bubble Bot`
  (Might 3) and `Chakram Dancer` (Might 3) from base to `Altar to Unity`,
  contesting Garen's two units there (`Trusty Ramhound` Might 4,
  `Pit Rookie` Might 3) — Combat stages. Attacker (Rumble) sums 6 Might;
  Defender (Garen) sums 7.
  - Both pass. Combat Damage (rule 460.2): Rumble assigns 6 — 4 to
    `Trusty Ramhound` (lethal, dies), remaining 2 to `Pit Rookie` (needs 3
    for lethal, survives with 2 marked). Garen assigns 7 — 3 to
    `Bubble Bot` (lethal, dies), and since `Chakram Dancer` is the only
    unit left to receive the remaining 4, all 4 goes to it even though its
    own lethal threshold is only 3 (rule 460.2.c.4's "unless no further
    units remain" exception) — it dies too.
  - Combat Cleanup: Garen still has `Pit Rookie` there, Rumble has nothing
    — Garen retains Control (no new conquer, already controlled). Heals
    `Pit Rookie`'s 2 marked damage.

Score: Garen 3, Rumble 3 (Rumble's attack was fully repelled — both
attackers died, Garen kept a surviving defender).

## Findings

- **Static abilities re-check their condition continuously.** `Trusty
  Ramhound`'s "+1 Might while another unit is here" turned off when it
  moved alone and back on when `Pit Rookie` joined it — confirms these are
  live, re-evaluated conditions, not one-time snapshots.
- **An Activated Ability with an unpayable cost component can't be
  activated at all**, even if the rest of the cost is affordable. An empty
  trash blocked `Assembly Rig`'s "recycle a unit from your trash" clause
  entirely, not just reduced its effect.
- **`[Legion]` is checked per-card at the moment it's played, not
  retroactively** — playing the Legion card first in a turn genuinely
  misses its bonus, even if a second card is played moments later.
- **A 2-vs-2 attack with less total Might than the defense is a bad attack,
  not a coin flip.** Rumble's 6 Might split killed one defender but left
  the other alive to soak the rest, while Garen's 7 Might cleanly killed
  both attackers — total Might, not unit count, decided this fight.

## Recommended Next Step

Stop here; four solid findings in four rounds, all newly-confirmed
mechanics rather than repeats. No rerun needed.