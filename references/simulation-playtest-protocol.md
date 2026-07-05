# Simulation Playtest Protocol

Use this checklist before writing a simulated game artifact.

## Required State Tracking

- Name every card played, discarded, drawn, killed, moved, or recycled.
- Track score after every scoring event.
- Track ready/exhausted status for units, gear, and runes when it affects play.
- Track unit locations: base, battlefield name, trash, hand, Champion Zone.
- Track damage marked on units until end-of-turn or combat cleanup heals it.
- Track hand size and named hand contents whenever a discard/draw decision
  affects legality.
- Track battlefield control after every showdown, combat, and cleanup that could
  change it.

## Audit Rules

- Mark a result as `pending rules audit` until a rules agent reviews it.
- If any turn uses generic labels such as "a damage spell" or "a cheap unit,"
  the result may be useful for mechanics but not hard balance data.
- A hard balance result needs exact card names for every action so copy limits,
  energy affordability, domain legality, and card text can be checked.

## SIM-0001 Lessons

- Units entering exhausted creates a real tempo delay for beginner decks.
- A one-unit conquer can be correct if it starts a Hold clock, even when it does
  not trigger a legend payoff.
- Battlefield packages must be exact for 1v1: choose exactly three before setup,
  then randomly select one for the game.
- Rules audits should preserve caveats directly in the simulation file and
  simulation index.
