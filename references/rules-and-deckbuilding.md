# Rules And Deckbuilding Reference

Source: `Riftbound_Core_Rules_RUP3_Staging.pdf`, section 101-103.

## Deck Construction

- A player brings a Champion Legend, a Main Deck, a Rune Deck, and battlefields.
- The Champion Legend starts in the Legend Zone and defines the deck's Domain
  Identity.
- Cards in the Main Deck and Rune Deck must fit the Champion Legend's domains.
- A single-domain card is legal if that domain is in the legend identity.
- A multi-domain card is legal only if all of its domains are in the legend
  identity.
- The Main Deck has at least 40 cards.
- The Chosen Champion starts in the Champion Zone.
- The Chosen Champion must be a champion unit with a champion tag matching the
  Champion Legend.
- The Main Deck can include up to 3 copies of the same named card. This copy
  limit includes the chosen champion card.
- A deck may contain only 3 total Signature cards, regardless of signature card
  name, and all signature cards must match the Champion Legend's tag.
- The Rune Deck contains exactly 12 rune cards and is kept separate from the Main
  Deck.
- Battlefields are mode-dependent. If more than one battlefield is required,
  do not include more than one battlefield with the same name.

## Local Card Database Checks

Use `riftbound_cards_organized.md` before finalizing a list:

- Confirm every card's domain fits the legend.
- Check the `Banned Errata` section for banned status or current text.
- Prefer the non-promo card row unless a promo is the only available printing.
- Record card text in deck files from the card database so a player can use the
  deck file without re-opening the full card list.

## Practical Deck File Convention

Deck profiles in this folder treat the chosen champion as separate from the
40-card Main Deck. Additional copies of that champion may be included in the Main
Deck, but the chosen copy plus main-deck copies must not exceed 3 total copies by
name.
