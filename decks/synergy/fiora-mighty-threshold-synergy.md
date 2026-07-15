# Fiora Mighty Threshold (Synergy)

## Snapshot

| Field | Value |
|---|---|
| Category | Synergy |
| Legend | Fiora - Grand Duelist |
| Domains | Body, Order |
| Chosen champion | Fiora - Victorious |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | `Riposte` (3) |
| Difficulty | Medium |
| Core plan | "Becomes [Mighty]" is an event, not a state — so every temporary pump that pushes a unit across 5 Might is also a trigger. The deck's combat tricks each do double duty: win the fight AND channel a rune (the Legend), ready the unit (`Fiora - Worthy`), or grant a keyword suite (`Fiora - Victorious`). Even the counterspell pumps. |

## Why This Is A Synergy Deck

Unlike the Volibear list (which wants units that *are* 5+ Might), this
deck cares about the moment a unit *crosses* the line. `Fiora - Grand
Duelist` channels a rune each time one of your units becomes Mighty, and
`Fiora - Worthy` readies that unit for an Order Rune — so a 1-cost
`Punch First` (+5 Might this turn) in combat is simultaneously:

- a combat trick that usually wins the fight;
- a rune channeled by the Legend;
- a fresh untap from `Fiora - Worthy`;
- a full keyword suite ([Deflect], [Ganking], [Shield]) if the target
  was `Fiora - Victorious`.

The trick fades at end of turn — which means the same unit can *become*
Mighty again tomorrow. Small bodies plus temporary pumps out-trigger big
bodies here, and `Riposte` is the purest expression of it: counter their
spell, and its Energy cost becomes Might on your duelist, often crossing
the threshold at reaction speed.

## Legality Notes

- Domain identity: Fiora - Grand Duelist is Body/Order. Every main deck
  card is single-domain Body, single-domain Order, or the Body/Order
  Signature card `Riposte`.
- Copy-limit check: `Fiora - Victorious` has 1 chosen-champion copy plus
  2 main deck copies (3 total, at the limit). No other card exceeds 3
  copies.
- Signature check: `Riposte` (SFD-206) is Fiora's own signature (printed
  directly after the Legend, SFD-205); 3 copies sit exactly at the
  3-signature limit and match the Legend's tag.
- Banned/errata check: no card used here is marked Banned in the local
  card database.
- Champion tag: `Fiora - Victorious`, `Fiora - Peerless`, and `Fiora -
  Worthy` are inferred to carry the `Fiora` champion tag from card name
  and the Legend's own name, per this project's convention. The source
  export has no explicit tag column — confirm the printed tag before
  tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Fiora - Grand Duelist | SFD-205 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Fiora - Victorious | OGN-232 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Fiora - Victorious | OGN-232 | Champion Unit | 4 |
| 3 | Fiora - Peerless | SFD-110 | Champion Unit | 3 |
| 3 | Fiora - Worthy | SFD-180 | Champion Unit | 3 |
| 2 | Qiyana - Victorious | OGN-155 | Champion Unit | 4 |
| 2 | Kinkou Monk | OGN-141 | Unit | 4 |
| 2 | Dauntless Vanguard | SFD-093 | Unit | 4 |
| 2 | Unsung Hero | SFD-167 | Unit | 2 |
| 2 | Kraken Hunter | OGN-150 | Unit | 3 |
| 2 | First Mate | OGN-132 | Unit | 3 |
| 3 | Punch First | SFD-097 | Spell | 1 |
| 2 | Primal Strength | OGN-154 | Spell | 4 |
| 3 | Bonds of Strength | SFD-151 | Spell | 2 |
| 2 | Back to Back | OGN-206 | Spell | 3 |
| 3 | Show of Strength | SFD-106 | Spell | 2 |
| 2 | Sacrifice | UNL-173 | Spell | 1 |
| 3 | Riposte | SFD-206 | Signature Spell | 2 |
| 2 | Mistfall | OGN-152 | Gear | 3 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 7 | Body Rune | OGN-126 |
| 5 | Order Rune | OGN-214 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Trifarian War Camp | OGN-294 | Units here have +1 Might — a 4-Might unit *becomes* Mighty just by arriving, and the aura keeps threshold math one point cheaper all game. |
| Sunken Temple | SFD-218 | Conquering with a Mighty unit pays 1 Energy for a card — the deck's natural attack pattern, monetized. |
| Navori Fighting Pit | OGN-283 | Hold-trigger buffs stack permanent +1s toward the threshold on the battlefield you're defending anyway. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Fiora - Grand Duelist | Legend | | | When one of your units becomes [Mighty], you may exhaust me to channel 1 rune exhausted. | Turns every threshold crossing into ramp — once per turn, so cross early. |
| Fiora - Victorious | Champion Unit | 4 | 4 | While [Mighty], I have [Deflect], [Ganking], and [Shield]. | Chosen champion; any pump makes her a protected, mobile 5+ threat for the turn. |
| Fiora - Peerless | Champion Unit | 3 | 3 | When I attack or defend one on one, double my Might this combat. | Crosses the threshold by herself every duel: 3 doubles to 6, triggering the whole suite. |
| Fiora - Worthy | Champion Unit | 3 | 3 | When a unit you control becomes [Mighty], you may pay Order Rune to ready it. | The other half of the engine: crossing the line untaps the crosser. |
| Qiyana - Victorious | Champion Unit | 4 | 4 | [Deflect]. When I conquer, draw 1 or channel 1 rune exhausted. | 4-Might body (one pump from Mighty) whose conquers keep the resources flowing. |
| Kinkou Monk | Unit | 4 | 4 | On play, buff up to two other friendly units. | Permanent +1s that put 4-Might bodies one temporary pump — or zero — from the line. |
| Dauntless Vanguard | Unit | 4 | 4 | Can be played to an occupied enemy battlefield. | Starts duels on your terms; a `Punch First` makes the ambush lethal. |
| Unsung Hero | Unit | 2 | 2 | [Deathknell] — If I was [Mighty], draw 2. | Dies pumped, draws 2 — a trick spent on a doomed blocker isn't wasted. |
| Kraken Hunter | Unit | 3 | 5 | [Accelerate]. [Assault]. Spend buffs to reduce my cost. | Natively 5 Might (see Watch Outs on entry timing); attacks as a 6. |
| First Mate | Unit | 3 | 3 | On play, ready another unit. | A second untap effect that doesn't need the threshold at all. |
| Punch First | Spell | 1 | | [Action]. Give a unit +5 Might this turn. | The signature trick: one Energy converts any body into a Mighty event. |
| Primal Strength | Spell | 4 | | [Action]. Give a unit +7 Might this turn. | The haymaker version — 2-Might chump becomes a 9. |
| Bonds of Strength | Spell | 2 | | [Reaction]. [Repeat] 2 Energy. Give two friendly units each +1 Might this turn. | Precision tool: pushes two 4-Might units across at once, at reaction speed, repeatably. |
| Back to Back | Spell | 3 | | [Reaction]. Give two friendly units each +2 Might this turn. | Two crossings in one card when the board has 3-4 Might bodies. |
| Show of Strength | Spell | 2 | | [Reaction]. Draw 1 for each of your [Mighty] units. | The payoff spell — cast it inside combat, after the pumps, for a fistful of cards. |
| Sacrifice | Spell | 1 | | [Reaction]. Kill a friendly [Mighty] unit: draw 2 and channel 1 rune. | Spend a unit that's about to die anyway — the pump that saved nothing still buys 2 cards and a rune. |
| Riposte | Signature Spell | 2 | | [Reaction]. Counter a spell; give a friendly unit +Might equal to that spell's Energy cost this turn. | Counterspell as threshold trigger: countering a 5-drop makes almost anything Mighty. |
| Mistfall | Gear | 3 | | When you buff a friendly unit, pay Body Rune + exhaust: ready it. | A third untap engine, running off the permanent buffs from Kinkou Monk and the Fighting Pit. |

## How To Play

1. Deploy 3-4 Might bodies early and pick fights — `Fiora - Peerless`
   into a lone defender is the ideal turn-2/3 play, since her double is
   a free threshold crossing.
2. Spend one cheap trick per combat, not three: each unit can only
   *become* Mighty once per pump, and the Legend exhausts for its
   channel — spread crossings across turns to maximize total ramp.
3. With `Fiora - Worthy` down, sequence pumps during your attack: the
   untap means one unit can fight at two battlefields, or attack and
   still defend.
4. `Riposte` is best held against removal aimed at your pumped attacker
   — countering it protects the unit AND pushes it further up.
5. Cast `Show of Strength` inside a showdown after your tricks resolve;
   two or three Mighty units at that moment is a normal outcome.
6. `Sacrifice` converts a doomed pumped unit into resources — with
   `Unsung Hero` it's a 4-card swing (2 from Sacrifice, 2 from the
   Deathknell).

## Mulligan

Keep:

- two cheap bodies, at least one a Fiora (`Peerless` or `Worthy`);
- one cheap pump (`Punch First`, `Bonds of Strength`);
- `Riposte` if you already have a body and a pump.

Avoid keeping `Primal Strength` or `Mistfall` in openers with no bodies
— the deck's worst hands are all payoff, no duelist.

## Watch Outs

- **Entry ambiguity, flagged not resolved:** whether a unit that enters
  play at 5+ printed Might (`Kraken Hunter`) "becomes" Mighty on entry
  is not settled by the local rules extract — the Legend and `Fiora -
  Worthy` say "becomes," while the Volibear Legend says "when you play a
  Mighty unit," implying the wordings differ on purpose. This deck is
  built so nothing depends on the entry ruling: every trigger can be
  produced by a temporary pump instead. Play conservatively (no trigger
  on entry) until confirmed, per this project's explicit-ambiguity
  practice.
- The Legend is once per turn in practice (it exhausts) — a second
  crossing the same turn channels nothing. `Fiora - Worthy` is the
  repeatable half, gated by Order Runes.
- A unit that is already Mighty does not "become" Mighty again from a
  second pump — it must drop below 5 (end of turn) and cross again.
- `Sacrifice` needs the unit Mighty *as you pay the cost* — you can't
  respond to your own trick fading at end of turn.
- `Riposte`'s pump equals the countered spell's Energy cost: countering
  a cheap 1-cost trick barely moves the needle; save it for real spells.

## Upgrade Paths

- `Overt Operation` (5: spend buffs to ready everyone, then buff all) is
  a strong finisher if the deck drifts toward permanent buffs.
- `Gentlemen's Duel` and `Challenge` add fight-based removal that the
  pumps convert into one-sided kills.
- `Jaull-Fish` (costs 2 less per Mighty unit) is a budget top-end that
  rewards the deck for doing what it already does.
- If the entry ruling is confirmed *in favor* of entry triggers, add a
  second `Kraken Hunter` and consider `Petty Officer`-class 5-Might
  bodies — every deployment becomes ramp.
