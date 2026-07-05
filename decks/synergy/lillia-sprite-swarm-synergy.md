# Lillia Sprite Swarm (Synergy)

## Snapshot

| Field | Value |
|---|---|
| Category | Synergy |
| Legend | Lillia - Bashful Bloom |
| Domains | Calm, Mind |
| Chosen champion | Lillia - Protector of Dreams |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | None |
| Difficulty | Medium |
| Core plan | Flood the board with 3-Might Sprite tokens that enter **ready** (not exhausted — the token effects explicitly override the default), buff them as a type, and win with sheer board width, including the literal alternate win condition on `The Grand Plaza`. |

## Why This Is A Synergy Deck — And A Genuine Type Identity Check

Learned from `simulations/SIM-0003-rumble-vs-khazix-rules-smoke.md`: before
building a tribal deck, verify the support cards actually produce the named
type, rather than assuming "sounds thematic" means "is thematic." Every
token-producing card here is confirmed to make an actual `Sprite`, `Bird`,
`Recruit`, `Sand Soldier`, or `Reflection` token (the same generic token
types seen throughout this card pool), and `Lillia - Protector of Dreams`
and `Soul Shepherd`'s bonuses key off "token unit," a broader category that
includes all of them — not a narrower one this deck might accidentally miss.

## Legality Notes

- Domain identity: Lillia - Bashful Bloom is Calm/Mind. Every main deck card
  is single-domain Calm or single-domain Mind.
- Copy-limit check: `Lillia - Protector of Dreams` has 1 chosen-champion
  copy plus 2 main deck copies (3 total). No other card exceeds 3 copies.
- Signature check: no signature cards are included.
- Banned/errata check: no card used here is marked banned in the local card
  database.
- Champion tag: `Lillia - Protector of Dreams` is inferred to carry the
  `Lillia` champion tag from card name and the Legend's own name. The
  source export has no explicit tag column — confirm the printed tag before
  tournament play.
- Token note: the Sprite, Bird, Recruit, Sand Soldier, and Reflection tokens
  this deck creates are not Main Deck cards and are not counted in the 40 —
  they're created during play per rule 176 (Tokens). Several of them
  explicitly say "play a **ready**" token, an intentional override of the
  rule 143.4/181.1 default that tokens (like units generally) enter
  exhausted.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Lillia - Bashful Bloom | UNL-189 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Lillia - Protector of Dreams | UNL-058 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Lillia - Protector of Dreams | UNL-058 | Champion Unit | 5 |
| 3 | Trevor Snoozebottom | UNL-048 | Unit | 3 |
| 3 | Frisky Hunter | UNL-033 | Unit | 4 |
| 2 | Sprite Mother | OGN-106 | Unit | 4 |
| 1 | Sprite Queen | UNL-084 | Unit | 7 |
| 2 | Zilean - Time Mage | UNL-086 | Champion Unit | 5 |
| 2 | Soul Shepherd | UNL-077 | Unit | 5 |
| 3 | Sprite Fountain | UNL-078 | Gear | 2 |
| 3 | Desert's Call | SFD-031 | Spell | 2 |
| 2 | Flurry of Feathers | UNL-044 | Spell | 4 |
| 3 | Sprite Call | OGN-094 | Spell | 3 |
| 2 | Sprite Burst | UNL-069 | Spell | 5 |
| 2 | Viktor - Innovator | OGN-117 | Champion Unit | 4 |
| 2 | Keeper of Masks | UNL-081 | Unit | 2 |
| 2 | Ahri - Inquisitive | OGN-119 | Champion Unit | 3 |
| 2 | Gutter Palace | UNL-088 | Gear | 4 |
| 2 | Pickpocket | SFD-074 | Unit | 3 |
| 2 | Card Sharp | SFD-081 | Unit | 3 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 6 | Calm Rune | OGN-042 |
| 6 | Mind Rune | OGN-089 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| The Grand Plaza | OGN-293 | Direct alternate win condition at 7+ units here — exactly what a token-flood deck is trying to build toward anyway. |
| Bandle Tree | OGN-278 | An extra Hidden slot for `Sprite Call`, letting it sit ready for a surprise token drop. |
| Windswept Hillock | OGN-297 | Grants Ganking to units here, letting the deck's already-ready Sprite tokens hop straight into contesting a second battlefield. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Lillia - Bashful Bloom | Legend | | | 4 Energy, Exhaust: play a ready 3 Might Sprite token with Temporary. Costs 1 less per friendly Temporary unit. | A repeatable token generator that gets cheaper the more Temporary tokens are already out. |
| Lillia - Protector of Dreams | Champion Unit | 5 | 4 | On token play, +1 Might this turn. Token units have Tank. | Chosen champion; grows every time a token hits the board and makes the whole token board absorb combat damage first. |
| Trevor Snoozebottom | Unit | 3 | 3 | [Shield]. On hold, play a ready 3 Might Sprite token here. | A defender that generates another ready attacker just by holding. |
| Frisky Hunter | Unit | 4 | 3 | On play, a 1 Might Deflect Bird token here. | Cheap extra body with built-in protection from targeted removal. |
| Sprite Mother | Unit | 4 | 3 | On play, a ready 3 Might Sprite token here. | Immediate extra attacker the turn it's played. |
| Sprite Queen | Unit | 7 | 6 | On play or every Beginning Phase, a ready 3 Might Sprite token to base. | Top-end engine that keeps making bodies every turn it survives. |
| Zilean - Time Mage | Champion Unit | 5 | 5 | Once a turn, doubles a token play while it's at that battlefield. | Turns any single token-making card into two tokens for the turn. |
| Soul Shepherd | Unit | 5 | 3 | Token units have +1 Might. | Blanket buff that makes every 3-Might Sprite a 4-Might Sprite. |
| Sprite Fountain | Gear | 2 | | On play, a ready 3 Might Sprite token. [Deathknell] repeats its own play effect. | Makes a token twice across its lifetime — once on play, once on death. |
| Desert's Call | Spell | 2 | | [Repeat] 2 Energy. Play a 2 Might Sand Soldier token. | Cheap, repeatable token generation. |
| Flurry of Feathers | Spell | 4 | | [Reaction]. Counter a spell, or make four 1 Might Deflect Bird tokens. | Flexible — either protects the board plan or floods it in one card. |
| Sprite Call | Spell | 3 | | [Hidden], [Action]. Play a ready 3 Might Sprite token. | Can be banked face down for a surprise token drop later. |
| Sprite Burst | Spell | 5 | | Play two ready 3 Might Sprite tokens. | Big one-card burst toward the 7-unit win condition. |
| Viktor - Innovator | Champion Unit | 4 | 3 | Playing a card on the opponent's turn makes a Recruit token. | Rewards holding up Reactions instead of dumping the whole hand on your own turn. |
| Keeper of Masks | Unit | 2 | 1 | [Hidden], [Temporary]. On play, two Reflection copies of itself here. | Turns one flip into three bodies for the turn. |
| Ahri - Inquisitive | Champion Unit | 3 | 3 | On attack/defend, -2 Might to an enemy unit here. | Combat-math support that helps a token actually win its fight. |
| Gutter Palace | Gear | 4 | | Win at your Beginning Phase with exactly 4 cards in hand and exactly 4 units at battlefields. Otherwise, discard 1, exhaust: make a Deflect Bird token. | A precise alternate win condition, plus a steady token trickle when the exact numbers aren't lined up. |
| Pickpocket | Unit | 3 | 3 | On play, may kill a cheap gear for a Gold token. | Filler body with minor resource upside. |
| Card Sharp | Unit | 3 | 3 | Offers both players a Gold token; extra for you if they take it. | Filler body, upside depends on the opponent. |

## How To Play

1. Play cheap token-makers early (`Sprite Mother`, `Sprite Fountain`,
   `Desert's Call`) to build width fast — remember these tokens enter
   **ready**, so they can move or fight the same turn they're made.
2. Land `Lillia - Protector of Dreams` once tokens are flowing — every
   future token play buffs it, and Tank on all your tokens means they
   soak combat damage before your bigger bodies do.
3. Use `Zilean - Time Mage` at a battlefield where you're about to make a
   token — doubling `Sprite Burst` or `Sprite Fountain`'s output is a huge
   tempo swing.
4. Track your total unit count at battlefields — `The Grand Plaza` wins
   outright at 7+ units there, and `Gutter Palace` wins on a precise
   4-card-hand/4-unit board state, so both are real, reachable win
   conditions this deck can aim for directly instead of only combat.
5. Use `Viktor - Innovator` to get extra value from Reaction-speed plays
   like `Flurry of Feathers` on the opponent's turn.

## Mulligan

Keep:

- one cheap token-maker: `Sprite Mother`, `Sprite Fountain`, or
  `Desert's Call`;
- one payoff: `Lillia - Protector of Dreams` or `Soul Shepherd`, only with
  an early token-maker to support it;
- one flexible card: `Flurry of Feathers` or `Ahri - Inquisitive`.

Avoid keeping `Sprite Queen` or `Gutter Palace` without any early
token-makers already in hand — both want the board already developing.

## Watch Outs

- Sprite tokens (and the Reflection tokens from `Keeper of Masks`) are
  `[Temporary]` — they die at the start of their controller's next
  Beginning Phase, before scoring. Use them the turn they're made or the
  turn right after; don't expect them to stick around as a long-term board.
- **A lone Temporary token can never hold a battlefield into its own
  controller's next scoring tick.** Its death happens in the Beginning
  Step, strictly before the Scoring Step in the same Beginning Phase
  (rule 315.2.a-b) — so by the time holds are checked, it's already dead
  and Control of that battlefield is already lost if nothing else is there.
  Confirmed directly in
  `simulations/SIM-0009-yasuo-vs-lillia-rules-smoke.md`. Treat Temporary
  tokens as conquer tools and combat bodies for the turn they're made, not
  a way to bank a hold — pair any battlefield you want to hold across turns
  with a non-Temporary unit (`Lillia - Protector of Dreams`, `Sprite
  Mother` itself, `Frisky Hunter`'s Bird token is not Temporary either, or
  any other permanent body) before relying on it.
- `The Grand Plaza`'s win condition needs 7+ units specifically **at that
  battlefield** during your hold — spreading tokens across multiple
  battlefields for individual conquers works against this particular win
  line, even though it's still fine for normal scoring.
- `Gutter Palace`'s win condition is exact ("exactly 4... exactly 4"), not
  "at least" — overshooting either number misses it entirely.
- `Zilean - Time Mage` only doubles a token play while it's physically at
  the same battlefield as the card being played — moving it away turns the
  effect off.
- `Zilean - Time Mage`'s doubling is once per turn and fires on the
  **first** qualifying token play that turn — including an automatic
  Beginning Phase hold trigger like `Trevor Snoozebottom`'s, which happens
  before you've made any Main Phase choices. If both are at the same
  battlefield, expect the doubling to land on whatever the hold trigger
  makes, not a bigger token play you'd rather double later that turn.
  Confirmed in `simulations/SIM-0011-lillia-vs-khazix-rules-smoke.md`.

## Upgrade Paths

- Add `Lillia - Fae Fawn` (Mind) as a second Sprite-generating body that
  also has Ganking-adjacent movement to spread tokens across battlefields.
- Add more Reaction-speed cards to get full value from `Viktor - Innovator`.
- For a more advanced version, build explicitly around `The Grand Plaza`
  and `Gutter Palace`'s alternate win conditions as the primary plan instead
  of a backup, which asks for careful unit-count tracking every turn.
