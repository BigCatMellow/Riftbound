# Riftbound Deck Lab

Working notes and deck files for building Riftbound decks from the local rules
PDF and card database.

## Source Files

- `Riftbound_Core_Rules_RUP3_Staging.pdf` - rules source used for deck
  construction constraints and gameplay assumptions.
- `riftbound_cards_organized.md` - local card database generated from the
  organized spreadsheet. Check this before adding card text to a deck file.

## Folder Layout

| Path | Purpose |
|---|---|
| `references/` | Rules summaries and source-derived constraints. |
| `templates/` | Reusable deck profile format. |
| `decks/beginner/` | Low-complexity decks with clear play patterns. |
| `decks/synergy/` | Focused archetype decks built around strong card interactions. |
| `decks/advanced/` | Higher-complexity decks with sequencing, reactions, or layered engines. |
| `decks/overpowered/` | Pushed or intentionally high-power builds for testing ceilings. |

## Key References

| File | Purpose |
|---|---|
| `references/rules-and-deckbuilding.md` | Deck construction constraints extracted from the rules PDF. |
| `references/simulation-playtest-protocol.md` | Required tracking and audit practices for simulated games. |

## Deck File Expectations

Each deck profile should include:

- legality snapshot;
- legend and chosen champion;
- main deck list with exact counts;
- 12-card rune deck;
- battlefield recommendations;
- card information for every card used;
- how to play the deck;
- mulligan and sequencing notes;
- watch-outs, weaknesses, and upgrade paths.

Start with `templates/deck-profile-template.md` when adding a new list.
