# SIM-0002: Jinx Discard Synergy vs Master Yi XP Snowball

## Status

| Field | Value |
|---|---|
| Simulation ID | SIM-0002 |
| Date | 2026-07-04 |
| Driver | claude-lab-lori |
| Rules agent | claude-lab-lori (self-audited inline, same session as driver) |
| Status | Stopped after 5 full rounds (Turns 1-5 each) by design — see Recommended Next Step |
| Purpose | Apply SIM-0001's lessons (name every card, cite rules inline, watch for location-scoped statics) to a stress test of a different deck pair. |

## Why This Pairing And Why Inline Self-Audit

- Different combination per the operator's request: `decks/synergy/jinx-discard-engine-synergy.md`
  (Fury/Chaos) vs `decks/overpowered/master-yi-xp-snowball-overpowered.md`
  (Calm/Body) — no domain overlap, no shared cards, and it tests two very
  different engines (discard-payoff aggro vs a shared player-level XP
  counter that buffs the whole board).
- SIM-0001 found that genericizing card names in later turns broke
  verifiability. Every card played below is named exactly and cross-checked
  against `riftbound_cards_organized.md`'s card text at the time it mattered.
- Unlike SIM-0001, I am both driver and rules agent in the same pass, citing
  the specific rule number for every non-obvious ruling as it happens instead
  of a separate later audit. This is a deliberate process change based on the
  first sim, not a shortcut: naming rules inline as each ruling occurs is
  what made SIM-0001 Turns 1-5 fully auditable, so this log does that from
  the start instead of retrofitting it.
- Neither deck has a location-scoped ("...here") static like
  `Garen - Commander`'s. Checked both decks' Card Info tables for "here" in
  ability text before starting — none found — so no equivalent tracking gap
  is expected, but combat and battlefield location are still tracked
  explicitly below in case a future card added to either list has one.

## Mode And Setup Assumptions

Source: `Riftbound_Core_Rules_RUP3_Staging.pdf`.

- Mode: 1v1 Duel, Victory Score 8, Battlefield Count 2 (rule 480.3-480.4: one
  battlefield contributed and used per player, not "each player uses 2").
- First player: Jinx. Second player: Master Yi — channels one extra rune
  during their first Channel Phase only (rule 480.7).
- Each player draws 4, then may set aside up to 2 and draw that many
  (rule 117-118). Both hands below are kept as drawn; no mulligan needed.
- Units and tokens enter the board exhausted unless a card says otherwise
  (rule 143.4). Channeled runes enter ready by default because the base
  Channel Phase task (rule 315.3.b) does not say "exhausted" (contrast with
  rule 430.2's example of an effect that explicitly channels a rune
  exhausted).
- Runes ready every Awaken Phase (rule 315.1.b: "readies all Game Objects
  [the Turn Player] controls"), so the pool of usable Energy grows turn over
  turn as more runes are channeled and none are Recycled away.
- Numeric Energy costs can be paid by Energy from any rune regardless of its
  Domain (rule 162.1.a: "Energy has no Domain"). Only cards with an explicit
  domain-specific Power cost (e.g. Accelerate's "1 Energy + Fury Rune") need
  a matching-domain rune, and this sim avoids Accelerate's paid option
  entirely to sidestep an unresolved question about how "Fury Rune" as a bare
  cost (as opposed to the "[C]" Power symbol) actually gets paid — see Known
  Simulation Limitations.
- Battlefields chosen: `Zaun Warrens` (OGN-298) for Jinx, `Reckoner's Arena`
  (OGN-286) for Master Yi — the first-listed recommendation in each deck
  file. Both start uncontrolled by anyone regardless of who brought them
  (matches SIM-0001 precedent, confirmed again by rule 445: a Battlefield
  becomes Contested, and thus needs a Showdown to establish Control, the
  first time *any* unit moves there — ownership of the card itself doesn't
  grant starting Control).

## Known Simulation Limitations

- Manual replay, not a full engine, same as SIM-0001.
- Battlefield selection used each deck file's first-listed recommendation
  deterministically rather than `references/simulation-playtest-protocol.md`'s
  documented method (choose exactly three, then randomly select one). Both
  deck files already list exactly three battlefields, so this is a
  documented shortcut for reproducibility, not a rules violation — a real
  game should still randomize among the three.
- This sim intentionally avoids any card's paid Accelerate option (e.g.
  `Jinx - Demolitionist`'s "1 Energy + Fury Rune" enter-ready cost). The
  rules distinguish a Basic Rune's plain Energy ability ("[E]: Reaction —
  Add [1]", paid by exhausting the rune) from its Domain Power ability
  ("Recycle this: Reaction — Add [C]", paid by permanently recycling the
  rune). Text like "1 Energy + Fury Rune" as a bare cost (not printed as
  "[C]") sits between these two documented abilities, and this sim did not
  need to resolve that ambiguity to reach its findings. Flagging it as an
  open rules question rather than guessing.
- Stops after 5 rounds (10 individual turns) by design, once it had produced
  a clean set of findings, rather than being forced to a full 8 points. See
  Recommended Next Step for why continuing further wasn't necessary to
  answer the question this sim was run for.

## Deterministic Setup

### Jinx (Fury, Chaos)

Opening hand (kept, no mulligan):

- `Chemtech Enforcer`
- `Get Excited!`
- `Jinx - Demolitionist`
- `Evershade Stalker`

Battlefield: `Zaun Warrens`.

### Master Yi (Calm, Body)

Opening hand (kept, no mulligan):

- `Gemhand Hunter`
- `Combat Experience`
- `Mosstomper`
- `Master Yi - Tempered`

Battlefield: `Reckoner's Arena`.

## Turn Log

### Turn 1: Jinx

- Channel: `Fury Rune`, `Fury Rune` (rule 315.3.b — base 2 for the Turn
  Player).
- Draw: `Corrupt Enforcer`.
- Main:
  - Plays `Chemtech Enforcer` to base using 2 Energy. Enters exhausted
    (rule 143.4).
  - `Chemtech Enforcer`'s "When you play me, discard 1" is mandatory
    (rule 422.2.a). Discards `Get Excited!` — no synergy card in hand yet to
    make this discard matter beyond paying the cost.
- End state:
  - Jinx score 0.
  - Jinx base: exhausted `Chemtech Enforcer`.
  - Hand: `Jinx - Demolitionist`, `Evershade Stalker`, `Corrupt Enforcer`.
  - No battlefields controlled.

### Turn 1: Master Yi

- Channel: `Calm Rune`, `Calm Rune`, `Body Rune` (2 base + 1 for going second
  in 1v1, rule 480.7, applies only to this first Channel Phase).
- Draw: `Voracious Gromp`.
- Main:
  - Plays `Gemhand Hunter` to base using 2 Energy (of 3 available). Enters
    exhausted. `[Hunt]` is dormant — it triggers on conquer or hold, and this
    unit isn't at a battlefield yet.
- End state:
  - Master Yi score 0, XP 0.
  - Master Yi base: exhausted `Gemhand Hunter`.
  - Hand: `Combat Experience`, `Mosstomper`, `Master Yi - Tempered`,
    `Voracious Gromp`.
  - No battlefields controlled.

### Turn 2: Jinx

- Awaken: readies `Chemtech Enforcer` and both channeled Runes
  (rule 315.1.b — all of Jinx's Game Objects, runes included).
- Channel: `Chaos Rune`, `Chaos Rune`. 4 total runes on board, all ready = up
  to 4 Energy this Main Phase.
- Draw: `Bewitching Spirit`.
- Main:
  - Plays `Jinx - Demolitionist` using 3 Energy (not paying Accelerate's
    additional cost — see Known Simulation Limitations). Enters exhausted.
  - "When you play me, discard 2" is mandatory as far as it can be paid
    (rule 422.4). Hand has 3 cards (`Evershade Stalker`, `Corrupt Enforcer`,
    `Bewitching Spirit`); discards `Corrupt Enforcer` and
    `Evershade Stalker`, keeping `Bewitching Spirit`.
  - Moves ready `Chemtech Enforcer` from base to `Zaun Warrens`, exhausting
    it. `Zaun Warrens` is uncontrolled, so this applies Contested
    (rule 445); no opposing units are present, so a Non-Combat Showdown
    opens (rule 344). Both players pass (rule 348) → Jinx is the sole
    remaining player's units there → Jinx establishes Control
    (rule 348.2.a) → not yet scored this battlefield this turn → Conquer
    (rule 348.2.a.1, rule 464.1) → Jinx scores 1.
  - `Zaun Warrens`' Conquer trigger ("discard 1, then draw 1") fires
    (rule 466.2.a). Discards the only card in hand, `Bewitching Spirit`
    (hand now empty), then draws 1 regardless of how many were actually
    discarded (rule 422.4's Undercover Agent example is the exact precedent
    for this: draw the stated amount even if the discard portion did less
    than instructed). Draws `Undercover Agent`.
- End state:
  - Jinx score 1.
  - Jinx controls `Zaun Warrens` with exhausted `Chemtech Enforcer`.
  - Jinx base: exhausted `Jinx - Demolitionist`.
  - Hand: `Undercover Agent`.
  - Trash: `Get Excited!`, `Corrupt Enforcer`, `Evershade Stalker`,
    `Bewitching Spirit`.

**Finding, flagged live rather than after the fact:** two discard-heavy plays
back to back stripped Jinx's hand to 1 card by Turn 2, before
`Jinx - Rebel` (the actual payoff for discarding) is even affordable. This
matches the Watch Outs already written in the deck file ("track how many
cards you have left"), now demonstrated directly.

### Turn 3: Master Yi

- Awaken: readies `Gemhand Hunter` and channeled Runes.
- Channel: `Body Rune`, `Calm Rune`. 5 total runes ready.
- Draw: `Kha'Zix - Evolving Hunter`.
- Main:
  - Plays `Master Yi - Tempered` using 4 Energy. Enters exhausted. `[Hunt 2]`
    dormant (not at a battlefield).
  - Moves ready `Gemhand Hunter` from base to `Reckoner's Arena`, exhausting
    it (1 Energy left over, unused). Uncontrolled → Contested → Non-Combat
    Showdown → both pass → Master Yi conquers, scores 1.
  - `Gemhand Hunter`'s `[Hunt]` triggers on this conquer: gain 1 XP
    (0 → 1). `Reckoner's Arena`'s own ability ("When you hold here, activate
    the conquer effects of units here") is Hold-triggered, not
    Conquer-triggered, so it does **not** fire on this initial conquer —
    only on a future Beginning-Phase hold. Noted explicitly to avoid
    double-triggering it here.
- End state:
  - Master Yi score 1, XP 1.
  - Master Yi controls `Reckoner's Arena` with exhausted `Gemhand Hunter`.
  - Master Yi base: exhausted `Master Yi - Tempered`.
  - Hand: `Combat Experience`, `Mosstomper`, `Voracious Gromp`,
    `Kha'Zix - Evolving Hunter`.

### Turn 3: Jinx

- Awaken: readies `Chemtech Enforcer` (at `Zaun Warrens`) and
  `Jinx - Demolitionist` (at base).
- Beginning: Jinx holds `Zaun Warrens` (rule 464.2, 315.2.b) → scores 1.
  `Zaun Warrens`' own ability is Conquer-triggered, not Hold-triggered, so
  holding does not re-fire the discard/draw. Score 1 → 2.
- Channel: `Fury Rune`, `Chaos Rune`. 6 total runes ready.
- Draw: `Traveling Merchant`.
- Main:
  - Plays `Undercover Agent` using 5 Energy (of 6). Enters exhausted. No ETB
    (its ability is `[Deathknell]`, dormant while alive). 1 Energy left,
    not enough for `Traveling Merchant` (cost 2); it stays in hand.
  - Moves ready `Jinx - Demolitionist` from base to `Reckoner's Arena`,
    exhausting it. `Reckoner's Arena` is controlled by Master Yi and already
    has `Gemhand Hunter` there, so this Move stages Combat instead of a
    plain Showdown (rule 447, rule 456: Combat applies when units controlled
    by two opposing players are both present). Attacker = Jinx (applied
    Contested, rule 459.2.b.1); Defender = Master Yi.
  - Both players pass in the Combat Showdown (rule 348.1 → proceed to the
    Combat Damage Step). `Jinx - Demolitionist` (Might 4, `[Assault 2]` = +2
    Might while attacking = 6 effective) deals 6 to `Gemhand Hunter`
    (Might 2) → dies (6 ≥ 2). `Gemhand Hunter` deals its Might (2, no
    attacker-only bonus applies to a defender) to `Jinx - Demolitionist` → 2
    marked, survives (2 < 4).
  - Combat Cleanup (rule 461.1, "Step 3: Resolution Step"): only Jinx's unit
    remains at `Reckoner's Arena`, and Jinx has not yet scored this
    battlefield this turn, so this is a Conquer (rule 464.1, taken from
    Master Yi) — Jinx scores 1 more. Score 2 → 3.
  - `Reckoner's Arena`'s ability doesn't fire (Hold-triggered, not
    Conquer-triggered — same reasoning as Turn 3 Master Yi).
  - Combat Cleanup also inserts "Heal all Units" (rule 461.1.a.1) — this is
    a *second, separate* healing trigger from the end-of-turn one SIM-0001
    found (rule 317.2.b); it fires immediately after every Combat resolves,
    not only at end of turn. This heals the 2 damage marked on
    `Jinx - Demolitionist` right now, back to full Might.
- End state:
  - Jinx score 3.
  - Jinx controls `Zaun Warrens` (ready `Chemtech Enforcer`, didn't act this
    turn) and `Reckoner's Arena` (exhausted, healed `Jinx - Demolitionist`).
  - Jinx base: exhausted `Undercover Agent`.
  - Hand: `Traveling Merchant`.

**Rules refinement worth carrying into future sims:** damage doesn't only
heal at end of turn (rule 317.2.b, found in SIM-0001) — it also heals
immediately after every individual Combat's own cleanup (rule 461.1.a.1).
In practice this means marked damage almost never survives past the specific
Combat that caused it, unless the damage was dealt *outside* combat (like a
spell) and no combat has happened yet that turn — exactly the situation that
made SIM-0001's Turn 5 `Disintegrate`-into-combat sequence legal.

### Turn 4: Master Yi

- Awaken: readies `Master Yi - Tempered` and channeled Runes.
- Beginning: no battlefield controlled (lost `Reckoner's Arena` last turn),
  no score.
- Channel: 2 more Runes. 7 total ready.
- Draw: `Herald of Spring`.
- Main:
  - Plays `Voracious Gromp` using 5 Energy (of 7). Enters exhausted.
    `[Hunt 3]` dormant.
  - Moves ready `Master Yi - Tempered` from base to `Reckoner's Arena`,
    exhausting it (2 Energy left over, unused). `Jinx - Demolitionist` is
    there, currently **exhausted** (it hasn't been readied since Jinx's own
    last Awaken Phase, and it is not yet Jinx's turn) — an exhausted unit
    can still be a Combat participant and take/deal combat damage; only
    Standard Move and being declared an attacker require a unit to
    exhaust as a cost, not defending. This Move stages Combat (rule 447,
    456). Attacker = Master Yi; Defender = Jinx.
  - Both pass. Combat Damage Step: `Master Yi - Tempered` (Might 4, no
    Assault/Shield) deals 4 to `Jinx - Demolitionist` (Might 4) → 4 ≥ 4,
    dies. `Jinx - Demolitionist` deals 4 back to `Master Yi - Tempered`
    (Might 4) → 4 ≥ 4, also dies. A clean mutual trade with no combat
    tricks involved.
  - Combat Cleanup: **neither** player has units remaining at
    `Reckoner's Arena` (rule 348.2.a requires exactly one player's units to
    remain for anyone to establish Control) — the battlefield becomes
    uncontrolled. Nobody scores from this combat.
  - 2 Energy left, nothing affordable worth playing (`Herald of Spring` is
    4, `Mosstomper` is 3, `Kha'Zix - Evolving Hunter` is 5,
    `Combat Experience` is 1 but has no clear target); holds the rest of the
    hand.
- End state:
  - Master Yi score 1 (unchanged), XP 1 (unchanged).
  - `Reckoner's Arena` uncontrolled (empty).
  - Master Yi base: exhausted `Voracious Gromp`.
  - Hand: `Combat Experience`, `Mosstomper`, `Kha'Zix - Evolving Hunter`,
    `Herald of Spring`.

### Turn 4: Jinx

- Awaken: readies `Undercover Agent` (`Jinx - Demolitionist` died last turn;
  `Chemtech Enforcer` was already ready and untouched).
- Beginning: Jinx holds `Zaun Warrens` → scores 1. Score 3 → 4.
- Channel: 2 more Runes. 8 total ready.
- Draw: `Get Excited!` (a second copy; 1 of 3 total is already in the trash
  from Turn 1).
- Main:
  - Plays `Traveling Merchant` to base using 2 Energy. Enters exhausted. No
    ETB (its ability triggers on Move, not on play).
  - Considered playing `Get Excited!` (cost 2, 6 Energy left over): after
    playing it, hand would be **empty** at the moment "Discard 1" resolves,
    since `Get Excited!` itself already left the hand as part of being
    played. Per rule 422.4, discarding 0 cards is legal (discard as many as
    possible), but "Deal its Energy cost as damage" then has no discarded
    card to reference — no valid amount of damage exists to Deal
    (rule 417.1.e requires a positive integer). This would be a complete
    whiff: 2 Energy spent, nothing discarded, no damage dealt. Held instead
    of playing it into a dead trigger.
  - Moves ready `Undercover Agent` from base to the now-uncontrolled
    `Reckoner's Arena`, exhausting it. No opposing units present → Non-Combat
    Showdown → both pass → Jinx conquers, scores 1. Score 4 → 5.
- End state:
  - Jinx score 5.
  - Jinx controls `Zaun Warrens` (ready `Chemtech Enforcer`) and
    `Reckoner's Arena` (exhausted `Undercover Agent`).
  - Jinx base: exhausted `Traveling Merchant`.
  - Hand: `Get Excited!`.

**Finding, flagged live:** a discard-payoff spell (`Get Excited!`) is a dead
card whenever it would be the last card in hand when played, because it
discards itself out of existence before its own "discard 1" clause resolves.
Worth a line in the deck file's Watch Outs (see Follow-Up below).

### Turn 5: Master Yi

- Awaken: readies `Voracious Gromp`.
- Beginning: no battlefield controlled, no score.
- Channel: 2 more Runes.
- Draw: `Alpha Strike`.
- Main:
  - Plays `Herald of Spring` using 4 Energy. Enters exhausted. Its "When you
    play me, gain 2 XP" fires immediately on play — this is not conditional
    on being at a battlefield, unlike `[Hunt]`. XP 1 → 3.
  - Plays `Mosstomper` using 3 Energy. Enters exhausted. `[Hunt 2]` dormant.
  - Moves ready `Voracious Gromp` (Body, Might 5, `[Hunt 3]`) from base to
    `Zaun Warrens`, exhausting it. `Chemtech Enforcer` (ready, Might 2) is
    there. Stages Combat: Attacker = Master Yi, Defender = Jinx.
  - Both pass. Combat Damage: `Voracious Gromp` deals 5 to
    `Chemtech Enforcer` (Might 2) → dies. `Chemtech Enforcer` deals 2 to
    `Voracious Gromp` (Might 5) → survives.
  - Combat Cleanup: only Master Yi's unit remains → Master Yi conquers
    `Zaun Warrens` (taken from Jinx), scores 1. Score 1 → 2.
    `Voracious Gromp`'s `[Hunt 3]` triggers on this conquer: gain 3 XP.
    XP 3 → **6**.
  - Crossing 6 XP activates `Master Yi - Wuju Master`'s Level 6 clause:
    "Your units have +1 Might" (a continuously-checked static, per the
    reminder text pattern used across this card pool — "While you have 6+
    XP, get the effect" — not a one-time trigger). This applies immediately
    and for as long as XP stays at 6+: `Voracious Gromp` is now effectively
    Might 6, `Herald of Spring` Might 5, `Mosstomper` Might 4, and so on for
    every current and future Master Yi unit.
  - `Zaun Warrens`' Conquer trigger now belongs to Master Yi (it fires for
    whoever conquers, not the original controller): discard 1 (discards
    `Combat Experience`, keeping `Kha'Zix - Evolving Hunter` and
    `Alpha Strike`), then draw 1 → draws `Wily Newtfish`.
  - Combat Cleanup's "Heal all Units" clears `Voracious Gromp`'s 2 marked
    damage.
- End state:
  - Master Yi score 2, XP 6 (Level 6 active — every Master Yi unit is
    permanently +1 Might from here on, as long as XP holds at 6+).
  - Master Yi controls `Zaun Warrens` (exhausted `Voracious Gromp`, now
    effectively Might 6).
  - Master Yi base: exhausted `Herald of Spring` (now Might 5), exhausted
    `Mosstomper` (now Might 4).
  - Hand: `Kha'Zix - Evolving Hunter`, `Alpha Strike`, `Wily Newtfish`.

### Turn 5: Jinx

- Awaken: readies `Undercover Agent` (at `Reckoner's Arena`).
- Beginning: `Zaun Warrens` was lost last turn, no hold there.
  `Reckoner's Arena` still controlled → holds, scores 1. Score 5 → 6.
- Channel: 2 more Runes.
- Draw: `Scrapyard Champion`.
- Main:
  - Plays `Scrapyard Champion` using 5 Energy. Enters exhausted. Its
    `[Legion]` clause ("When you play me, discard 2, then draw 2") needs
    another card to have been played this turn *first* — this is the first
    card played this turn, so Legion's condition isn't met and nothing
    triggers. Correctly dormant, not an omission.
  - Considered playing `Get Excited!` again: hand would again be empty
    (only card left) at the moment it resolves — same whiff as Turn 4. Held
    instead.
  - Chose not to attack into `Zaun Warrens` this turn: `Voracious Gromp` now
    defends at effective Might 6 (post-Level-6 buff), which would lose to
    `Undercover Agent`'s Might 5 in a straight trade. Held position instead
    of a bad attack.
- End state:
  - Jinx score 6.
  - Jinx controls `Reckoner's Arena` (ready `Undercover Agent`, didn't act).
  - Jinx base: exhausted `Scrapyard Champion`.
  - Hand: `Get Excited!`.

## Score After 5 Rounds

- Jinx: 6 (needs 2 more to win).
- Master Yi: 2, XP 6 (Level 6 buff active; Level 11 not yet reached).

## Findings

### Deck File / Card-Interaction Findings

- `Get Excited!` and any other "discard 1, then [do something with the
  discarded card]" spell is a dead card whenever it's the last card in hand
  — it discards itself out of hand before its own discard clause can find a
  target (rule 422.4: discard as many as possible, which is 0 here; a
  damage or other effect that depends on the discarded card's properties
  then has nothing to reference). This is a real sequencing trap, not just a
  Watch Outs bullet — recommend adding it explicitly to
  `decks/synergy/jinx-discard-engine-synergy.md`'s Watch Outs.
- Aggressive early discard outlets (`Chemtech Enforcer` into
  `Jinx - Demolitionist`) can strip the Jinx deck's hand to near-zero before
  `Jinx - Rebel` (the actual payoff) is affordable at 5 Energy. The deck's
  own Watch Outs already warns about this in general terms; this sim gives a
  concrete example (hand at 1 card by Turn 2, before the payoff piece is
  even close to castable).
- Even Might-for-Might combat with no combat tricks in play produces a
  mutual kill (`Jinx - Demolitionist` vs `Master Yi - Tempered`, both
  Might 4). Neither deck's early units are durable enough to win a fair
  fight outright without a buff or keyword advantage — expected for a
  beginner-adjacent midrange curve, but worth knowing when picking which
  unit to commit to an even fight.
- `Master Yi - Wuju Master`'s Level 6 threshold triggered naturally by
  Turn 5 in this line, entirely off two `[Hunt]`-tagged conquers plus one
  on-play XP burst from `Herald of Spring`. The overpowered deck file's own
  claim that the buff is reachable at a normal pace holds up.

### Balance Signal (Read With Care — Single Test)

- At the 5-round mark, Jinx leads 6-2 and Master Yi's Level 6 threshold just
  came online, not Level 11 (the "units enter ready" clause) or
  `Master Yi - Unstoppable`'s own late-game safety clause. This is
  consistent with what `master-yi-xp-snowball-overpowered.md`'s own Watch
  Outs already says: "a fast aggressive opponent can race it before XP
  accumulates" and "removal that hits before Level 6 is much more effective
  ... than removal that arrives after." This single line does not contradict
  the deck's documented ceiling — it shows the documented early-game
  weakness playing out as described, in a race that hasn't reached the late
  game yet.
- This is one deterministic line with hand-picked (not randomized) draws and
  battlefield choices, run by a single pilot on both sides. It is a
  plausibility check on the card interactions, not a balance verdict — don't
  cite the 6-2 score as proof either deck is over- or under-tuned without a
  few more independent lines, ideally ones that let Master Yi reach Level
  11 or land `Master Yi - Unstoppable` before drawing a conclusion about the
  "overpowered" label.

### Rules Findings (New Since SIM-0001)

- Damage heals after **every** Combat's own Cleanup (rule 461.1.a.1: "Heal
  all Units" is inserted as part of Step 3, the Resolution Step), not only
  at end of turn (rule 317.2.b, found in SIM-0001). In practice, marked
  damage essentially never survives past whichever specific Combat caused
  it, unless the damage was dealt outside of combat (e.g. by a spell) before
  any Combat has happened yet that turn.
- Confirmed (was an open question in SIM-0001): when a "discard X, then
  [effect]" instruction can't fully be paid because the hand has fewer than
  X cards, the player discards as many as they can (including 0), and the
  "then [effect]" portion still happens in full afterward (rule 422.4, using
  the rules' own `Undercover Agent` example almost verbatim — that card is
  in this deck). This resolves SIM-0001's open question 3 outright.
- A card's own "when I do X" trigger belongs to whichever player controls it
  at the time X happens, not the deck's original pilot — `Zaun Warrens`'
  Conquer trigger fired for Master Yi on Turn 5 once *he* was the one who
  conquered it, exactly the same as it fired for Jinx earlier. Battlefields
  and their triggers are not deck-bound; whoever conquers or holds them gets
  the effect.
- Confirmed a Move can stage Combat (not just a Non-Combat Showdown) even
  when the unit moving in is up against an **exhausted** defender — only the
  mover needs to exhaust as the cost of the Move itself; defenders don't
  need to be ready to participate in Combat.
- Open question, not yet resolved (flagged rather than guessed): how "1
  Energy + Fury Rune" as a bare additional cost (distinct from the "[C]"
  Domain Power symbol) is actually paid — via the Basic Rune's plain Energy
  ability, its Recycle-for-Power ability, or some other mechanism not yet
  located in the extracted rules text. This sim avoided every card with that
  cost pattern (`Jinx - Demolitionist`'s Accelerate, several others) rather
  than guess. Worth a dedicated rules-text pass before a sim needs to use
  Accelerate's paid option.

## Follow-Up From SIM-0002

- Add a line to `decks/synergy/jinx-discard-engine-synergy.md`'s Watch Outs:
  don't play a "discard 1, then ..." spell when it would be the last card in
  hand — it discards itself out of the hand first and the follow-up effect
  then has nothing to act on.
- Resolve the Accelerate "1 Energy + [Domain] Rune" payment mechanism against
  the rules text before a future sim uses it, rather than avoiding it again.
- If a future sim wants to test `master-yi-xp-snowball-overpowered.md`'s
  actual ceiling claim, run it long enough to reach Level 11 or land
  `Master Yi - Unstoppable`, since this run stopped at Level 6.
- Continue this specific game to a real winner only if a balance claim needs
  to rest on it; the findings this sim was run for (card genericization
  discipline, a new discard deck's real sequencing trap, and the Combat-heal
  rule refinement) were already produced by Turn 5.