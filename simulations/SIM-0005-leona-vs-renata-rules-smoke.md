# SIM-0005: Leona Stun And Buff vs Renata Gold Engine

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0005 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline) |
| Status | Stopped after 4 rounds by design |
| Purpose | First test for both of these decks (neither had been simulated yet); part of a wider batch run for sample size. Runs leaner than SIM-0002-0004: established mechanics (non-combat showdown/conquer, Awaken readying, "this turn" expiry, mandatory discard) are applied without re-deriving their rule numbers every time; only genuinely new rulings are cited in full. |

## Mode And Setup

- 1v1 Duel, Victory Score 8. First player: Leona. Second player: Renata
  (extra Rune, first Channel Phase only).
- Battlefields (first-listed recommendation from each deck file, per the
  same documented deterministic-shortcut limitation as SIM-0002/0003/0004):
  `Navori Fighting Pit` for Leona, `Treasure Hoard` for Renata.
- Both opening hands kept, no mulligan. Leona: `Trifarian Gloryseeker`,
  `Solari Shieldbearer`, `Rune Prison`, `Wizened Elder`, `Facebreaker` (draw
  included). Renata: `Plundering Poro`, `Honest Broker`, `Blood Money`,
  `Trifarian Gloryseeker`, `Watchful Sentry` (draw included).

## Turn Log

### Turn 1

- **Leona**: Channels 2. Plays `Trifarian Gloryseeker` to base for 2 Energy
  (Legion inactive — it's the first card this turn). Score 0.
- **Renata**: Channels 3 (extra rune). Plays `Plundering Poro` to base for 2
  Energy. Score 0.

### Turn 2

- **Leona**: Plays `Solari Shieldbearer` for 3 Energy; its on-play stun has
  no "at a battlefield" restriction in its text, so it can target
  `Plundering Poro` sitting in Renata's base. Stunning it triggers
  `Leona - Radiant Dawn`'s Legend ability: buff a friendly unit —
  `Trifarian Gloryseeker` gets +1 Might (Might 2 → 3). Moves ready
  `Trifarian Gloryseeker` to `Navori Fighting Pit` (uncontrolled → conquers,
  scores 1).
- **Renata**: `Plundering Poro`'s stun expired at end of Turn 1 (a "this
  turn" effect, rule 317.2.c). Plays `Honest Broker` for 2 Energy. Moves
  ready `Plundering Poro` to `Treasure Hoard` (uncontrolled → conquers,
  scores 1; its own "on conquer, play a Gold gear token exhausted" fires).

Score: Leona 1, Renata 1.

### Turn 3

- **Leona**: Holds `Navori Fighting Pit` → scores 1 (1 → 2). `Navori
  Fighting Pit`'s own hold trigger ("buff a unit here") looks for a target —
  `Trifarian Gloryseeker` is the only unit there and **already has a buff**
  from last turn's Legend trigger. "Buff" grants +1 Might only "if it
  doesn't already have one" (a hard cap, not a refreshable resource), so
  this fizzles. Plays `Wizened Elder` to base for 4 Energy (not buffed yet,
  so no bonus from its own "extra +1 Might while buffed" clause).
- **Renata**: Holds `Treasure Hoard` → scores 1 (1 → 2). Its own hold
  trigger ("pay 1 Energy to play a Gold gear token exhausted") is paid
  during the Beginning Phase, **before this turn's own Channel Phase has
  happened** — confirming a player can spend previously-channeled, already-
  ready Energy at any point in their turn, not only after that turn's own
  Channel Phase resolves. Plays `Trifarian Gloryseeker` (Legion inactive,
  first play) and `Card Sharp` for 2 + 3 Energy. `Card Sharp`'s "you and
  each opponent may play a Gold gear token exhausted; for each opponent who
  did, you play one too" offers Leona the option — Leona declines (no use
  for a Gold token in this deck), so Renata's own bonus token from that
  clause doesn't trigger either. `Card Sharp`'s upside is genuinely
  opponent-dependent.

Score: Leona 2, Renata 2.

### Turn 4

- **Leona**: Holds `Navori Fighting Pit` → scores 1 (2 → 3). Same fizzle as
  last turn — still only the already-buffed `Trifarian Gloryseeker` there.
  Moves `Wizened Elder` from base to join it at `Navori Fighting Pit` (no
  combat, same controller). Plays `Enthusiastic Promoter` for 3 Energy.
- **Renata**: Holds `Treasure Hoard` → scores 1 (2 → 3); pays 1 Energy for
  another Gold token (2 total banked). Plays `Blood Money` — its "kill a
  unit at a battlefield with 2 Might or less" finds **no legal enemy
  target**: both Leona units at `Navori Fighting Pit` are Might 3+ from the
  buff plan, above the threshold. Turns the spell on her own
  `Plundering Poro` (Might 2, a legal friendly target) instead for the
  "if friendly, play two Gold tokens" mode — nets 2 more Gold but removes
  Renata's only unit at `Treasure Hoard`, so **`Treasure Hoard` becomes
  uncontrolled** the same way it would from enemy removal. Plays
  `Watchful Sentry` for 2 Energy.

Score: Leona 3, Renata 3.

## Findings

- **Buffs are a hard cap, not a refreshable resource.** `Navori Fighting
  Pit`'s "buff a unit here" fizzled twice in a row once its only target
  already had a buff — a good demonstration that stacking multiple buff
  *sources* onto the same unit does nothing past the first without a card
  like `Wizened Elder` that explicitly grants more.
- **Beginning Phase costs can be paid from already-ready resources before
  that turn's Channel Phase.** Nothing requires waiting for the current
  turn's own Channel Phase to spend Energy on a Beginning Phase trigger.
- **`Blood Money`'s Might-or-less restriction is real defensive tech
  against a buff deck** — once Leona's units cross the threshold, this
  entire removal spell can't target them at all, not just "deals less
  damage." Worth noting as a strength of the Leona deck's plan against
  small-unit removal.
- **Self-inflicted removal costs Control the same as enemy removal does.**
  Killing your own last unit at a battlefield you control loses that
  battlefield immediately — there's no exemption for self-targeted effects.

## Recommended Next Step

Stop here; produced four independent findings in four rounds, none of which
needed re-deriving previously-established rules. No rerun needed.