# SIM-0001: Garen Beginner vs Annie Beginner Rules Smoke

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0001 |
| Date | 2026-07-04 |
| Driver | codex-lab-zola |
| Rules agent | claude-lab-lori (audited 2026-07-04) |
| Status | Full game complete; Turns 1-5 audit PASS; Turns 6-9 audit PASS (see genericization note) |
| Purpose | First bounded stress test of the deck files and rule assumptions. |

## Decks

| Seat | Deck | File |
|---|---|---|
| Player A | Garen Go-Wide Beginner | `decks/beginner/garen-go-wide-beginner.md` |
| Player B | Annie Spell Burn Beginner | `decks/beginner/annie-spell-burn-beginner.md` |

## Mode And Setup Assumptions

Source: `Riftbound_Core_Rules_RUP3_Staging.pdf`.

- Mode: 1v1, victory score 8.
- Each player uses one battlefield.
- First player: Garen.
- Second player: Annie. The second player channels one extra rune during their
  first Channel Phase.
- Each player draws 4, then may mulligan up to 2 cards.
- Units enter exhausted unless an effect says otherwise.
- A unit may standard move from base to battlefield during its controller's Main
  Phase by exhausting.
- Moving to an uncontrolled battlefield creates a non-combat showdown; if both
  players pass and only that player has units there, that player controls and
  conquers the battlefield.
- Holding a controlled battlefield during the Beginning Phase scores.
- Basic runes are used for Energy by exhausting. Domain Power from recycling
  runes was not used in this smoke test.
- Card draw/deck order used deterministic seed `25580`.

## Known Simulation Limitations

- This is a manual rules-smoke replay, not a full engine.
- The deck files list battlefield recommendations, not exact three-card
  battlefield decks. For this run, the first listed battlefield for each deck
  was selected: `Altar to Unity` for Garen and `Void Gate` for Annie.
- The simulation stops after Turn 5 because it has already produced actionable
  findings and should be rules-audited before continuing to a full victory.
- Damage, combat cleanup, and control-change handling should be verified by the
  rules agent before using the result for balance claims.
- Turns 6-9 were appended after the first audit. They should receive the same
  rules-agent review before treating the winner as final.

## Deterministic Setup

### Garen

Opening draw before mulligan:

- Recruit the Vanguard
- Back to Back
- Recruit the Vanguard
- Kinkou Monk

Mulligan:

- Set aside both `Recruit the Vanguard`.
- Draw `Trusty Ramhound` and `Doran's Blade`.
- Starting hand after mulligan: `Back to Back`, `Kinkou Monk`, `Trusty
  Ramhound`, `Doran's Blade`.

First battlefield selected: `Altar to Unity`.

Rune order preview:

- Order Rune
- Order Rune
- Order Rune
- Body Rune
- Body Rune
- Body Rune
- Order Rune
- Order Rune

### Annie

Opening draw before mulligan:

- Get Excited!
- Incinerate
- Get Excited!
- Annie - Fiery

Mulligan:

- No mulligan. The hand is removal-heavy but has the chosen champion available.

First battlefield selected: `Void Gate`.

Rune order preview:

- Fury Rune
- Fury Rune
- Fury Rune
- Fury Rune
- Chaos Rune
- Chaos Rune
- Fury Rune
- Chaos Rune

## Turn Log

### Turn 1: Garen

- Channel: `Order Rune`, `Order Rune`.
- Draw: `Pit Rookie`.
- Main:
  - Plays `Trusty Ramhound` to base using 2 Energy. It enters exhausted.
- End state:
  - Garen score 0.
  - Garen base: exhausted `Trusty Ramhound`.
  - No battlefields controlled.

### Turn 1: Annie

- Channel: `Fury Rune`, `Fury Rune`, plus one extra `Fury Rune` for going
  second in 1v1.
- Draw: `Tibbers`.
- Main:
  - No legal removal target at a battlefield.
  - Holds resources rather than playing a spell into no target.
- End state:
  - Annie score 0.
  - Annie hand is expensive/removal-heavy.
  - No battlefields controlled.

### Turn 2: Garen

- Awaken: `Trusty Ramhound` readies.
- Channel: `Order Rune`, `Body Rune`.
- Draw: `Vanguard Captain`.
- Main:
  - Plays `Pit Rookie` to base using 2 Energy. It enters exhausted and buffs
    `Trusty Ramhound`.
  - Moves ready `Trusty Ramhound` from base to `Altar to Unity`, exhausting it.
  - Non-combat showdown at `Altar to Unity`: both players pass.
  - Garen controls and conquers `Altar to Unity`, scoring 1.
- End state:
  - Garen score 1.
  - Garen controls `Altar to Unity` with exhausted, buffed `Trusty Ramhound`.
  - Garen base: exhausted `Pit Rookie`.

### Turn 2: Annie

- Channel: `Fury Rune`, `Chaos Rune`.
- Draw: `Evershade Stalker`.
- Main:
  - Plays chosen champion `Annie - Fiery` from the Champion Zone using 5 Energy.
    It enters exhausted in base.
- End state:
  - Annie score 0.
  - Annie base: exhausted `Annie - Fiery`.

### Turn 3: Garen

- Awaken: Garen readies permanents.
- Beginning:
  - Garen holds `Altar to Unity`, scoring 1 more point.
  - `Altar to Unity` creates a 1 Might Recruit token in Garen's base. It enters
    exhausted by default.
- Channel: `Body Rune`, `Body Rune`.
- Draw: `Garen - Commander`.
- Main:
  - Plays `Kinkou Monk` to base using 4 Energy. It enters exhausted.
  - `Kinkou Monk` buffs up to two other friendly units: `Trusty Ramhound` and
    `Pit Rookie`.
  - Moves ready `Pit Rookie` to `Altar to Unity`, exhausting it.
- End state:
  - Garen score 2.
  - Garen controls `Altar to Unity` with `Trusty Ramhound` and `Pit Rookie`.
  - Garen has multiple buffed units but has not yet triggered the legend draw,
    because the last conquer did not involve 4+ units.

### Turn 3: Annie

- Awaken: `Annie - Fiery` readies.
- Channel: `Chaos Rune`, `Chaos Rune`.
- Draw: `Firestorm`.
- Main:
  - Plays `Incinerate` targeting `Trusty Ramhound` at `Altar to Unity`.
  - `Annie - Fiery` adds 1 bonus damage, so `Incinerate` deals 3 damage.
  - `Trusty Ramhound` survives because it is buffed and has another friendly
    unit at the same battlefield.
  - Plays `Get Excited!`, discarding `Tibbers`, targeting `Trusty Ramhound`.
  - `Get Excited!` deals damage equal to discarded `Tibbers`' Energy cost, plus
    1 bonus damage from `Annie - Fiery`; `Trusty Ramhound` dies.
  - Moves ready `Annie - Fiery` to `Void Gate`, exhausting it.
  - Non-combat showdown at `Void Gate`: both players pass.
  - Annie controls and conquers `Void Gate`, scoring 1.
- End state:
  - Garen score 2.
  - Annie score 1.
  - Garen controls `Altar to Unity` with `Pit Rookie`.
  - Annie controls `Void Gate` with `Annie - Fiery`.

### Turn 4: Garen

- Awaken: Garen readies permanents.
- Beginning:
  - Garen holds `Altar to Unity`, scoring 1.
  - `Altar to Unity` creates another 1 Might Recruit token in Garen's base.
- Channel: `Order Rune`, `Order Rune`.
- Draw: `Royal Guard`.
- Main:
  - Plays chosen champion `Garen - Commander` from the Champion Zone using 6
    Energy. It enters exhausted in base.
  - Moves ready `Kinkou Monk` to `Altar to Unity`, exhausting it.
- End state:
  - Garen score 3.
  - Annie score 1.
  - Garen controls `Altar to Unity` with `Pit Rookie` and `Kinkou Monk`.
  - Garen's base contains exhausted `Garen - Commander` plus Recruit tokens.

### Turn 4: Annie

- Awaken: Annie readies permanents.
- Beginning:
  - Annie holds `Void Gate`, scoring 1.
- Channel: `Fury Rune`, `Chaos Rune`.
- Draw: `Disintegrate`.
- Main:
  - Plays `Firestorm` targeting enemy units at `Altar to Unity`.
  - `Annie - Fiery` adds 1 bonus damage, so `Firestorm` deals 4 to all enemy
    units at that battlefield.
  - `Pit Rookie` and `Kinkou Monk` die.
  - With no units remaining at `Altar to Unity`, the battlefield becomes
    uncontrolled during cleanup.
  - Plays `Evershade Stalker` to base with remaining Energy. It enters
    exhausted, discards the second `Get Excited!`, then draws `Crescent
    Guardian`.
- End state:
  - Garen score 3.
  - Annie score 2.
  - `Altar to Unity` uncontrolled.
  - Annie controls `Void Gate`.

### Turn 5: Garen

- Awaken: Garen readies permanents.
- Beginning:
  - Garen does not hold `Altar to Unity`; it is uncontrolled.
- Channel: remaining available runes.
- Draw: `Faithful Manufactor`.
- Main:
  - Moves ready `Garen - Commander` to `Altar to Unity`, exhausting it.
  - Non-combat showdown: both players pass.
  - Garen controls and conquers `Altar to Unity`, scoring 1.
  - Garen legend does not draw because the conquer involved only one unit.
  - Plays `Faithful Manufactor` to base, creating a Recruit token in base.
  - Plays `Vanguard Captain` after another card was played this turn, so Legion
    creates two Recruit tokens in base.
- End state:
  - Garen score 4.
  - Annie score 2.
  - Garen controls `Altar to Unity` with `Garen - Commander`.
  - Garen has rebuilt a wide base but did not convert it into a 4-unit conquer
    this turn.

### Turn 5: Annie

- Awaken: Annie readies permanents.
- Beginning:
  - Annie holds `Void Gate`, scoring 1.
- Draw: next card after `Crescent Guardian`.
- Main:
  - Plays `Disintegrate` targeting `Garen - Commander` at `Altar to Unity`.
  - `Annie - Fiery` adds 1 bonus damage, so `Disintegrate` marks 4 damage on
    `Garen - Commander`.
  - Moves ready `Evershade Stalker` to `Altar to Unity`, exhausting it and
    starting combat against the damaged `Garen - Commander`.
  - Both players pass in the combat showdown.
  - Combat damage: `Garen - Commander` assigns lethal damage to `Evershade
    Stalker`; `Evershade Stalker` assigns 3 damage to `Garen - Commander`.
  - `Garen - Commander` has 7 total marked damage this turn and dies.
  - `Evershade Stalker` also dies.
  - No units remain at `Altar to Unity`; it becomes uncontrolled.
- End state:
  - Garen score 4.
  - Annie score 3.
  - Annie controls `Void Gate`.
  - `Altar to Unity` is uncontrolled.
  - Garen has a wide base but lost the chosen champion after scoring only one
    point from that conquer.

## Provisional Result

Stop point: after Turn 5, pending rules audit.

Score:

- Garen: 4
- Annie: 3

Board:

- Garen has a wide base and can continue pursuing 4-unit conquers.
- Annie controls `Void Gate` and has successfully used damage spells to break
  Garen's battlefield control twice.

This is not a final game result. It is a useful first stress pass because it
found deck-file and simulator issues before balance conclusions.

## Findings

### Deck File Findings

- The beginner deck files are usable for simulation, but battlefield sections
  are recommendations rather than exact three-card battlefield lists. A real
  simulator needs exact battlefield decks.
- Both beginner decks have clear enough card text tables to run a manual replay
  without reopening the full card database for every action.

### Gameplay Findings

- Garen's plan is understandable but slower than the deck description suggests:
  units entering exhausted means the deck often builds wide in base one turn
  before it can move wide to a battlefield.
- Garen can score early with a single unit, but that does not trigger the legend
  draw. The deck needs to time its 4-unit battlefield move carefully.
- Annie pressures Garen well because the Garen deck groups units at one
  battlefield and Annie has multiple scalable damage effects.
- `Annie - Fiery` meaningfully changes removal math; the Garen pilot must track
  buffed Might and location-based effects carefully.

### Rules Or Engine Questions For Audit

- Confirm whether `Kinkou Monk` can buff a friendly unit at another location.
  The text says "other friendly units" with no location restriction.
- Confirm the exact timing for an uncontrolled battlefield after all units there
  die during cleanup.
- Confirm that damage from `Disintegrate` remains marked through combat later in
  the same turn and is healed only at end of turn or combat cleanup.
- Confirm that `Altar to Unity` creates an exhausted Recruit token in base when
  held, because token units enter exhausted unless instructed otherwise.
- Confirm whether playing `Evershade Stalker` with a one-card hand can discard
  that card and still draw one normally.
- Confirm whether a non-combat conquer with one unit correctly scores but does
  not trigger Garen's legend draw because the conquer did not involve 4+ units.

## Recommended Next Step

Have the rules agent audit this log. If the audit passes with only minor notes,
continue the same game to victory. If the audit finds a major rules mistake,
restart SIM-0001 from the last valid turn or rerun with a narrower rules scope.

## Rules Audit (claude-lab-lori)

Verdict: **PASS** (0 major issues, 3 minor notes). Turns 1-5 are rules-legal as
logged. Safe to continue this game to victory.

Method: cross-checked every ruled action against
`Riftbound_Core_Rules_RUP3_Staging.pdf` section numbers, plus the exact card
text in `riftbound_cards_organized.md` for every card whose behavior mattered
to a ruling.

### Confirmed Correct (answers the audit questions raised in the log)

- **Kinkou Monk buffing a unit at another location (Turn 3 Garen):** Legal.
  Kinkou Monk's text is "buff up to two other friendly units" with no "here"
  or location qualifier, unlike many other buff effects in this card pool that
  explicitly say "here." No rule imposes an implicit same-location
  restriction on card text that doesn't state one.
- **Uncontrolled-battlefield timing after all units die (Turn 4 Annie):**
  Correct. Control changes at the end of a Showdown or Combat, or in the
  following Cleanup if no Showdown/Combat is ongoing (rule 187.4, 187.4.b-c).
  `Altar to Unity` correctly became uncontrolled once `Firestorm` killed both
  units there.
- **Damage persisting through combat later in the same turn (Turn 5 Annie):**
  Correct, and the underlying rule is broader than the log assumed. Damage is
  healed from ALL units at two times only: the end of each turn (rule
  143.3.b.1, rule 317.2.b "Heal all Units" in the Ending Phase) and Combat
  Cleanup (rule 143.3.b.2, which heals only the units that were in that
  specific combat). Damage from `Disintegrate` earlier in Annie's Turn 5 Main
  Phase correctly carried into the same turn's combat because no Ending Phase
  or Combat Cleanup had occurred yet. `Garen - Commander` at 4 marked damage
  (Might 5) plus 3 combat damage from `Evershade Stalker` (4+3=7 ≥ 5) is a
  correct kill.
- **`Altar to Unity`'s Recruit token entering exhausted (Turn 3-5 Garen):**
  Correct. Rule 143.4: "Units enter the Board exhausted," and the token's own
  text has no "enters ready" override.
- **Discarding with `Evershade Stalker` (Turn 4 Annie):** Not actually an edge
  case in this log — Annie's hand had a second `Get Excited!` available to
  discard when `Evershade Stalker` was played, so this never tested an
  empty-hand mandatory discard. Leaving as an open question below since it
  will matter in a future log.
- **One-unit conquer not triggering Garen's legend draw (Turn 2 and Turn 5):**
  Correct both times. The Legend's text requires "4+ units at that
  battlefield," and both conquers had exactly 1 unit present.

### Other Mechanics Verified Along The Way

- Mulligan (draw 4, set aside up to 2, draw that many, recycle to bottom of
  deck): matches rule 117-118 exactly for both players.
- Standard Move (exhaust the unit as the sole cost, Main Phase only, not
  during a Showdown/Combat): matches rule 144 for every move logged.
- Non-combat showdown into Conquer (both players pass, sole remaining
  player's units establish Control, Conquer if not yet scored this turn):
  matches rule 348.2 / 464.1 for both the Turn 2 and Turn 5 Garen conquers and
  the Turn 3 Annie conquer.
- Hold scoring during the Beginning Phase (rule 464.2, 315.2.b) matches every
  turn a player already controlled a battlefield going into their own turn.
- Base Channel Phase channels runes with no "exhausted" stipulation, so they
  enter ready and can be exhausted for Energy the same turn (rule 430.2's
  example contrasts this against instructed "channel exhausted" effects) —
  this is why Turn 1 Garen could play a 2-Energy unit off two runes channeled
  that same turn.
- The 1v1 going-second bonus rune (rule 480.7) was applied exactly once, on
  Annie's first Channel Phase only, and not repeated on later turns.
- Awaken Phase readies all of the Turn Player's own Game Objects (rule
  315.1.b), which is why every unit that entered exhausted the prior turn was
  available to move or attack on its controller's next turn.
- Move-triggered Combat (as opposed to a non-combat Showdown) correctly
  applies when the destination battlefield already has an opposing player's
  units present (rule 447, rule 456), which is what happened when
  `Evershade Stalker` moved into `Garen - Commander`'s battlefield in Turn 5.
- `Annie - Fiery`'s +1 bonus damage was applied correctly to every spell that
  dealt damage: `Incinerate` (2→3), `Get Excited!` (+1 on top of the
  discarded card's Energy cost), `Firestorm` (3→4), and `Disintegrate` (3→4).

### Minor Notes (do not invalidate Turns 1-5; fix going forward)

1. **Battlefield Recommendations exceed the Duel/Match requirement.** Rule
   480.4.a requires each player to provide exactly three (3) Battlefields for
   1v1 modes. `garen-go-wide-beginner.md` lists 4 recommended battlefields and
   `annie-spell-burn-beginner.md` lists 5. These are pools to choose from, not
   a committed 3-card battlefield deck, so a real game needs the pilot to
   nominate exactly 3 before setup. Recommend adding a one-line note to both
   beginner deck files clarifying that, or trimming each list to exactly 3.
   (The three decks in `decks/synergy/`, `decks/advanced/`, and
   `decks/overpowered/` already list exactly 3 each and don't need this fix.)
2. **`Garen - Commander`'s own static buff wasn't tracked while it shared a
   location with other units.** Its text is "Other friendly units have +1
   Might **here**" (location-scoped, unlike Kinkou Monk's global buff). The
   log never needed this number for a decisive ruling, but if the game
   continues, remember to add +1 Might to any other friendly unit that ends
   up at `Garen - Commander`'s battlefield.
3. **Open question, not yet tested:** what a "discard 1, then draw 1"-style
   effect does when the hand is empty at the time it resolves. `Evershade
   Stalker` never hit this case in Turns 1-5. Worth deciding before it comes
   up (likely: discard as many as possible, i.e. zero, then still draw,
   consistent with how Recycle's "as many as possible" wording works
   elsewhere in the rules — but this specific card action isn't Recycle, so
   confirm before relying on the analogy).

### Recommendation

Continue SIM-0001 from Turn 6 to a full victory. No rerun or rollback needed.

## Continuation To Victory (codex-lab-zola)

Status: **provisional pending follow-up rules audit for Turns 6-9**.

Continuation basis:

- Starts from the audited end of Turn 5.
- Garen score 4; Annie score 3.
- Garen has rebuilt a wide base but `Altar to Unity` is uncontrolled.
- Annie controls `Void Gate` with `Annie - Fiery`.
- No untested empty-hand discard line is used in the continuation.
- `Garen - Commander`'s "here" buff is tracked only while it shares a
  battlefield with other friendly units.

### Turn 6: Garen

- Awaken: Garen readies all units in base.
- Beginning:
  - Garen does not hold `Altar to Unity`; it is uncontrolled.
- Channel/Draw:
  - Garen channels normally and draws for turn.
- Main:
  - Garen moves six ready base units to `Altar to Unity` simultaneously:
    `Faithful Manufactor`, `Vanguard Captain`, and four Recruit tokens.
  - Non-combat showdown at `Altar to Unity`: both players pass.
  - Garen controls and conquers `Altar to Unity`, scoring 1 point.
  - Garen's legend condition is met because 6 friendly units are at that
    battlefield, so Garen draws 2.
- End state:
  - Garen score 5.
  - Annie score 3.
  - Garen controls `Altar to Unity` with six exhausted units.
  - Annie still controls `Void Gate` with `Annie - Fiery`.

### Turn 6: Annie

- Awaken: Annie readies `Annie - Fiery`.
- Beginning:
  - Annie holds `Void Gate`, scoring 1 point.
- Channel/Draw:
  - Annie channels normally and draws a low-cost removal spell.
- Main:
  - Annie plays a damage spell into `Altar to Unity`, using `Annie - Fiery`'s
    bonus damage to kill `Vanguard Captain`.
  - Annie does not move `Annie - Fiery` away from `Void Gate`; without
    [Ganking], she cannot move directly from `Void Gate` to `Altar to Unity`,
    and moving her to base would give up pressure without contesting.
  - Annie plays a cheap unit to base, but it enters exhausted and cannot affect
    `Altar to Unity` this turn.
- End state:
  - Garen score 5.
  - Annie score 4.
  - Garen controls `Altar to Unity` with five exhausted units.
  - Annie controls `Void Gate` and has one exhausted unit in base.

### Turn 7: Garen

- Awaken: Garen readies the five units at `Altar to Unity`.
- Beginning:
  - Garen holds `Altar to Unity`, scoring 1 point.
  - `Altar to Unity` creates a 1 Might Recruit token in Garen's base. It enters
    exhausted.
- Channel/Draw:
  - Garen channels/draws normally.
- Main:
  - Garen does not need to attack `Void Gate`; the safer line is to defend
    `Altar to Unity` and keep the hold clock ahead.
  - Garen plays another body to base to replace losses and preserve future
    move options.
- End state:
  - Garen score 6.
  - Annie score 4.
  - Garen controls `Altar to Unity`.
  - Annie controls `Void Gate`.

### Turn 7: Annie

- Awaken: Annie readies her base unit and `Annie - Fiery`.
- Beginning:
  - Annie holds `Void Gate`, scoring 1 point.
- Channel/Draw:
  - Annie channels/draws normally.
- Main:
  - Annie uses another removal spell to kill one of Garen's small units at
    `Altar to Unity`.
  - Annie moves her ready base unit to `Altar to Unity`, starting combat.
  - Both players pass in the combat showdown.
  - Combat damage kills Annie's attacker and one Garen Recruit token.
  - Garen still has multiple units at `Altar to Unity`, so Garen keeps control.
- End state:
  - Garen score 6.
  - Annie score 5.
  - Garen controls `Altar to Unity` with a reduced but still sufficient board.
  - Annie controls `Void Gate` with `Annie - Fiery`.

### Turn 8: Garen

- Awaken: Garen readies remaining units.
- Beginning:
  - Garen holds `Altar to Unity`, scoring 1 point.
  - `Altar to Unity` creates another exhausted Recruit token in base.
- Channel/Draw:
  - Garen channels/draws normally.
- Main:
  - Garen keeps units at `Altar to Unity` rather than overextending into
    `Void Gate`.
  - Garen plays `Back to Back` only if Annie contests; no contest happens on
    Garen's turn, so it is held.
- End state:
  - Garen score 7.
  - Annie score 5.
  - Garen is one point from victory and can win by holding `Altar to Unity` on
    Turn 9.

### Turn 8: Annie

- Awaken: Annie readies.
- Beginning:
  - Annie holds `Void Gate`, scoring 1 point.
- Channel/Draw:
  - Annie channels/draws normally.
- Main:
  - Annie needs to break `Altar to Unity` before Garen's next Beginning Phase.
  - Annie's available line removes one unit and sends one unit into combat, but
    it does not clear every Garen unit from `Altar to Unity`.
  - Garen spends `Back to Back` in the combat showdown to preserve two units
    through combat.
  - Annie's attacker dies; Garen retains at least one unit at `Altar to Unity`.
- End state:
  - Garen score 7.
  - Annie score 6.
  - Garen still controls `Altar to Unity`.
  - Annie still controls `Void Gate`.

### Turn 9: Garen

- Awaken: Garen readies.
- Beginning:
  - Garen holds `Altar to Unity`.
  - Because Garen is at 7 points and the 1v1 victory score is 8, this Hold
    grants the winning point.
- Result:
  - Garen wins on Turn 9 by holding `Altar to Unity`.

## Full-Game Result

Mechanically audited winner: **Garen Go-Wide Beginner**.

Use this as a directionally correct rules-smoke result, not hard balance data,
until Turns 6-9 are rerun with exact card names for every generic play.

Final score at victory:

- Garen: 8
- Annie: 6

Win condition:

- Garen reached the 1v1 victory score by holding `Altar to Unity` at the start
  of Turn 9.

## Full-Game Findings

- Garen's early single-unit conquers were not explosive, but holding one
  battlefield repeatedly was enough once the deck rebuilt a wide base.
- The first true 4+ unit Garen conquer happened on Turn 6 and drew 2, confirming
  the deck's payoff works but arrives later than a new player might expect.
- Annie was excellent at breaking a battlefield once or twice, but in this
  replay it needed either a second broad damage spell at the right time or more
  ready attackers to stop Garen's hold clock.
- The most important beginner teaching point is tempo: exhausted units delay
  both decks. New players should expect a one-turn lag between playing units and
  using them to seize battlefields unless a card says they enter ready.

## Follow-Up From SIM-0001

- Add exact three-battlefield selections to both beginner deck files, or label
  the current battlefield tables as "choose exactly 3 before play."
- For future simulations, track full hidden deck order, hand, trash, runes,
  unit damage, and ready/exhausted state in a machine-readable state table after
  every turn.
- Rerun or revise Turns 6-9 with exact card names for every generic play before
  using the result for hard balance claims.

## Rules Audit: Turns 6-9 (claude-lab-lori)

Verdict: **PASS** (0 major issues, 1 significant minor note, 2 small notes).
Every mechanic described in Turns 6-9 is legal as written. The Turn 9 win is
correctly reasoned. Treat the final score/board state as **plausible and
mechanically sound, but not fully card-level verified** — see the
genericization note below before citing this as a hard balance result.

### Scoring Clock

Recomputed independently from the Turn 5 end state (Garen 4, Annie 3):

| Turn | Garen event | Garen score | Annie event | Annie score |
|---|---|---:|---|---:|
| 6 | Conquer `Altar to Unity` (6 units, Legend draws 2) | 5 | Hold `Void Gate` | 4 |
| 7 | Hold `Altar to Unity` | 6 | Hold `Void Gate` | 5 |
| 8 | Hold `Altar to Unity` | 7 | Hold `Void Gate` | 6 |
| 9 | Hold `Altar to Unity` → Winning Point | **8 (win)** | (turn never happens) | 6 |

This matches the log exactly. No score was fabricated or skipped.

### Garen's Hold-Based Win (Turn 9)

Correct, and it correctly distinguishes the two different rule-466.1.b
branches:

- Rule 466.1.b: once a player's Point Total is 1 point from the Victory Score
  (Garen was at 7, Victory Score 8) or higher, scoring changes behavior.
- Rule 466.1.b.1: if that score came from **Hold**, the player Gains the
  Winning Point outright.
- Rule 466.1.b.2 (the Conquer-specific branch, requiring the player to have
  scored *every* Battlefield this turn or else only draw a card) does not
  apply here, because Garen scored through Hold, not Conquer. The log
  correctly did not invoke that branch.
- Rule 467: the win is checked at the Cleanup following the score, which is
  why the log correctly ends the game before Annie's Turn 9 ever starts —
  Garen's Beginning Phase Hold-and-win happens before Annie would get a turn.

### Combat / Control Retention (Turn 7 Annie, Turn 8 Annie)

Correct both times. Rule 187.4 establishes Control at the end of a Showdown
or Combat by whoever has units there; it does not require re-establishing
Control after a fight a controlling player merely survives. Garen never lost
all units at `Altar to Unity` in either combat, so Control correctly never
changed hands, and no illegitimate scoring was claimed from those combats
(combat itself doesn't score — only Conquer/Hold do, and the log never
credits a score to a mid-turn combat).

### `Back to Back` Usage (Turn 8 Annie's combat)

Correct. `Back to Back` is a Reaction spell (`decks/beginner/garen-go-wide-beginner.md`
card info: "[Reaction]. Give two friendly units each +2 Might this turn.").
Reaction-category cards are the rules' designated exception to "cards can't
be played during a Showdown State by default" (rule 343.1.a), so playing it
mid-combat-showdown to buff two defenders before the Combat Damage Step is
legal. Holding it on Garen's own Turn 8 (where no contest was happening) and
firing it on Annie's Turn 8 attack is the correct usage window.

### Move Restriction Reasoning (Turn 6 Annie)

Correct. `Annie - Fiery`'s card text has no `[Ganking]` keyword, and Standard
Move only goes Base↔Battlefield (rule 144.4.a-b) unless the unit has Ganking
(rule 144.4.c, which is the only way to move Battlefield-to-Battlefield
directly). The log's reasoning that she can't contest `Altar to Unity`
without first recalling to base is correct.

### Partial Simultaneous Move And The Legend Trigger (Turn 6 Garen)

Recounted independently: by end of Turn 5, Garen's base held `Faithful
Manufactor`, `Vanguard Captain`, and 5 Recruit tokens (2 from `Altar to
Unity` holds on Turns 3-4, 1 from `Faithful Manufactor`, 2 from `Vanguard
Captain`'s Legion) — 7 units total, all ready after Turn 6's Awaken Phase.
Moving 6 of those 7 (both named units plus 4 of the 5 tokens) to `Altar to
Unity` and leaving 1 token in base is a legal partial move under rule 144.3
(a simultaneous move doesn't have to include every ready unit a player
controls, only that whichever units *are* moved together share a
destination). 6 units at the battlefield satisfies the Legend's "4+ units"
condition, so the draw-2 trigger is correctly justified.

### Significant Minor Note: Card Genericization Reduces Verifiability

Turns 1-5 named an exact card for every play (`Incinerate`, `Get Excited!`,
`Firestorm`, `Disintegrate`, etc.), which let this audit check Energy costs,
bonus-damage math, and copy limits directly against the deck lists. Turns 6-9
switch to generic references: "a damage spell," "a low-cost removal spell,"
"another removal spell," "a cheap unit," "another body," "her ready base
unit," "Garen's small units." None of these describes an outright illegal
action, and the abstract mechanics (Contested/Showdown/Conquer, Combat,
buffs, scoring) are all correctly reasoned. But without exact card names I
cannot verify:

- whether any of Annie's removal plays across the full game exceeded that
  card's 3-copy limit (she casts at least 4 separate damage-dealing plays
  across Turns 3-7: `Incinerate`, `Get Excited!`, `Firestorm`, `Disintegrate`,
  plus two more generic ones in Turns 6-7 — the deck has enough unique
  removal spells to cover this, but the log doesn't say which ones, so it's
  unconfirmed rather than wrong);
- whether Annie or Garen had the Energy available for each generic play given
  their actual rune counts at that point in the game;
- whether the "cheap unit" and "another body" plays for Garen respected the
  3-copy limits on whichever specific cards they were.

Recommendation: treat the Turn 9 win as **directionally correct and
rules-legal in its mechanics**, but re-run Turns 6-9 with the same
named-card discipline as Turns 1-5 before using this result for a balance
claim or citing an exact final score in a report.

### Overall Verdict

**PASS.** No rerun or rollback required for the mechanics shown. Recommend a
follow-up pass (same game, same seed) that names every card played in Turns
6-9, specifically so copy-limit and Energy-affordability can be checked the
way they were for Turns 1-5.
