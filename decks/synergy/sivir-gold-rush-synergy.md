# Sivir Gold Rush (Synergy)

## Snapshot

| Field | Value |
|---|---|
| Category | Synergy |
| Legend | Sivir - Battle Mistress |
| Domains | Body, Chaos |
| Chosen champion | Sivir - Mercenary |
| Main deck size | 40 |
| Rune deck | 12 |
| Signature cards | `On the Hunt` (3) |
| Difficulty | Medium |
| Core plan | Hidden in the core rules (163.2.b): every Basic Rune pays Power by **recycling itself** — so "when you recycle a rune" is not a niche trigger, it's *every time you pay a Power cost*. The Legend converts that into a Gold token, and her second line readies her whenever enemy units die — so in a removal-heavy turn she mints Gold repeatedly. `Twisted Fate - Gambler` recycles a rune from the top of the rune deck on every attack, and `On the Hunt` readies the whole army for one Energy. |

## Why This Is A Synergy Deck

Three rules interlock:

- **Core rule 163.2.b** (verified in the rules PDF): a Basic Rune's
  Power ability reads "Recycle this: Add [domain]" — paying any Power
  cost recycles a rune, which triggers `Sivir - Battle Mistress`;
- the Legend **exhausts** per Gold, but "when one or more enemy units
  die, ready me" — this deck's fight suite (`Challenge`, `Marching
  Orders`, `Carnivorous Snapvine`, `Clash of Giants`, combat itself)
  keeps re-arming her mid-turn;
- Gold tokens add **Any Rune** — which pays the Power costs of the
  next spell, which recycles nothing extra (Gold is killed, not
  recycled — no loop) but *frees your real runes* to keep cycling.

`Twisted Fate - Gambler` is the deck's metronome: each attack reveals
and recycles the top rune of the rune deck (a Legend trigger, plus his
domain-keyed modal bonus). `Sivir - Mercenary` gets +2 and [Ganking]
any turn you've spent two runes — in this deck, that's every turn. And
`On the Hunt`, Sivir's own signature, is one Energy for a full army
untap: attack, ready, defend anyway.

## Legality Notes

- Domain identity: Sivir - Battle Mistress is Body/Chaos. Every main
  deck card is single-domain Body, single-domain Chaos, or the
  Body/Chaos Signature card `On the Hunt`.
- Copy-limit check: `Sivir - Mercenary` has 1 chosen-champion copy plus
  2 main deck copies (3 total, at the limit). `Sivir - Ambitious` is a
  different card name. No other card exceeds 3 copies.
- Signature check: `On the Hunt` (SFD-204) is Sivir's own signature
  (printed directly after the Legend, SFD-203); 3 copies sit exactly at
  the 3-signature limit and match the Legend's tag. (The lab's Kha'Zix
  deck once ran this card illegally — see that file's changelog note.)
- Banned/errata check: no card used here is marked Banned in the local
  card database.
- Champion tag: `Sivir - Mercenary` and `Sivir - Ambitious` are
  inferred to carry the `Sivir` champion tag from card name and the
  Legend's own name, per this project's convention. The source export
  has no explicit tag column — confirm the printed tag before
  tournament play.

## Deck List

### Legend

| Count | Card | Card ID |
|---:|---|---|
| 1 | Sivir - Battle Mistress | SFD-203 |

### Chosen Champion

| Count | Card | Card ID |
|---:|---|---|
| 1 | Sivir - Mercenary | SFD-143 |

### Main Deck

| Count | Card | Card ID | Type | Cost |
|---:|---|---|---|---:|
| 2 | Sivir - Mercenary | SFD-143 | Champion Unit | 4 |
| 2 | Sivir - Ambitious | SFD-120 | Champion Unit | 6 |
| 3 | Twisted Fate - Gambler | OGN-200 | Champion Unit | 4 |
| 2 | Treasure Hunter | SFD-130 | Unit | 2 |
| 2 | Carnivorous Snapvine | OGN-149 | Unit | 5 |
| 2 | Dauntless Vanguard | SFD-093 | Unit | 4 |
| 2 | Dune Drake | OGN-131 | Unit | 5 |
| 2 | Anivia - Primal | OGN-148 | Champion Unit | 7 |
| 1 | Elder Dragon | UNL-118 | Unit | 12 |
| 3 | On the Hunt | SFD-204 | Signature Spell | 1 |
| 3 | Challenge | OGN-128 | Spell | 2 |
| 2 | Marching Orders | SFD-114 | Spell | 3 |
| 1 | Clash of Giants | UNL-110 | Spell | 6 |
| 2 | Punch First | SFD-097 | Spell | 1 |
| 2 | Catalyst of Aeons | OGN-138 | Spell | 4 |
| 2 | Mobilize | OGN-134 | Spell | 2 |
| 2 | Spoils of War | OGN-144 | Spell | 4 |
| 2 | Stacked Deck | OGN-183 | Spell | 1 |
| 1 | Gust | OGN-169 | Spell | 1 |
| 2 | Ancient Henge | SFD-117 | Gear | 2 |

Main deck total: **40**

### Rune Deck

| Count | Card | Card ID |
|---:|---|---|
| 8 | Body Rune | OGN-126 |
| 4 | Chaos Rune | OGN-166 |

Rune deck total: **12**

### Battlefield Recommendations

| Card | Card ID | Why it fits |
|---|---|---|
| Sigil of the Storm | OGN-287 | Conquering forces a rune recycle — a guaranteed Legend trigger stapled to the deck's attack plan. |
| Treasure Hoard | SFD-220 | Conquer, pay 1, another Gold token — the second mint. |
| Targon's Peak | OGN-289 | Conquering readies 2 runes at end of turn — more runes to recycle tomorrow. |

## Card Info

| Card | Type | Cost | Might | Text | Role |
|---|---:|---:|---:|---|---|
| Sivir - Battle Mistress | Legend | | | When you recycle a rune, exhaust me: play a Gold gear token exhausted. When one or more enemy units die, ready me. | Ordinary spending mints Gold; killing re-arms the mint. |
| Sivir - Mercenary | Champion Unit | 4 | 4 | [Accelerate]. If you've spent 2+ runes this turn, +2 Might and [Ganking]. | Chosen champion; a 6-Might roamer on any normal turn. |
| Sivir - Ambitious | Champion Unit | 6 | 7 | [Deflect 2]. On conquer after attack with 5+ excess damage, deal that much to an enemy unit. | The top-end body whose conquests echo into their board. |
| Twisted Fate - Gambler | Champion Unit | 4 | 4 | On attack: reveal and recycle the top rune of the rune deck; get an effect by its domain (Fury: damage / Mind: draw / Order: stun). | The metronome — every attack is a Legend trigger plus a bonus. |
| Treasure Hunter | Unit | 2 | 1 | When I move, play a Gold token exhausted. | The third mint. |
| Carnivorous Snapvine | Unit | 5 | 6 | On play, fight an enemy unit at a battlefield. | Removal that readies Sivir when the victim dies. |
| Dauntless Vanguard | Unit | 4 | 4 | Can be played to an occupied enemy battlefield. | Starts fights where the Gold gets spent. |
| Dune Drake | Unit | 5 | 5 | On attack, +2 if a ready enemy unit is here. | Honest pressure that punishes untapped blockers. |
| Anivia - Primal | Champion Unit | 7 | 8 | On attack, deal 3 to all enemy units here. | Multi-kill attacks re-ready the Legend mid-swing. |
| Elder Dragon | Unit | 12 | 10 | Any of your damage kills. On play, deal 1 to up to one enemy at each location. | The Gold sink: the deck's ramp has to go somewhere magnificent. |
| On the Hunt | Signature Spell | 1 | | Ready your units. | One Energy: attack with everything, then defend anyway. |
| Challenge | Spell | 2 | | [Action]. A friendly and an enemy unit fight. | Kills on demand — which is Gold on demand. |
| Marching Orders | Spell | 3 | | [Action]. [Repeat] 3 Energy. A friendly unit anywhere fights an enemy at a battlefield. | Repeatable fights from the safety of base. |
| Clash of Giants | Spell | 6 | | Two units fight each other. | The heavyweight double-kill. |
| Punch First | Spell | 1 | | [Action]. +5 Might this turn. | Wins the fights the deck keeps starting. |
| Catalyst of Aeons | Spell | 4 | | Channel 2 runes exhausted (draw 1 if you can't). | More runes in play = more recycles available. |
| Mobilize | Spell | 2 | | Channel 1 exhausted (draw 1 if you can't). | Same, smaller. |
| Spoils of War | Spell | 4 | | [Reaction]. 2 cheaper if an enemy died this turn. Draw 2. | The deck's kills discount its refuel. |
| Stacked Deck | Spell | 1 | | [Action]. Look at top 3, draw 1, recycle the rest. | Digs for fights or bodies. |
| Gust | Spell | 1 | | [Reaction]. Bounce a ≤3-Might unit at a battlefield. | Cheap interaction. |
| Ancient Henge | Gear | 2 | | Exhaust: [Reaction] — pay any amount of Energy: Add that much Any Rune. | Converts spare Energy into Power — see Watch Outs. |

## How To Play

1. Spend Power every turn and take the Gold: with the Legend ready,
   your first rune-paid cost each turn mints a token. It's free money
   for playing the game normally.
2. `Twisted Fate - Gambler` attacks whenever safe — the top-rune
   recycle triggers the Legend even when nothing else does, and Order
   flips stun his own blocker.
3. Fight, don't trade politely: every enemy death readies Sivir, so a
   `Challenge` + combat turn can mint two or three Gold.
4. Bank Gold toward the curve-toppers: `Anivia - Primal` at 7 and
   `Elder Dragon` at 12 both arrive turns early off token ramp.
5. `On the Hunt` after your attack step is the deck's dirtiest single
   Energy — full army ready to defend, or a second combat wave with
   `Sivir - Mercenary` Ganking between battlefields.
6. `Sivir - Ambitious` wants a stunned or shrunken blocker (via TF's
   Order flip) to convert overkill into reach.

## Mulligan

Keep:

- one 2-drop (`Treasure Hunter`) or `Stacked Deck` opener;
- `Twisted Fate - Gambler` (the engine's best early body);
- one fight spell (`Challenge`, `Punch First`).

Avoid keeping `Elder Dragon`, `Anivia`, or `Clash of Giants` in openers
— the Gold has to exist before the sinks do.

## Watch Outs

- **The core-rule reading is the deck's spine**: rule 163.2.b gives
  every Basic Rune "Recycle this: Add [domain]" — paying Power with the
  *recycle* ability triggers the Legend, but paying with a rune's
  exhaust ability ("[E]: Add 1" produces Energy, not Power) does not
  recycle anything. Know which ability you're using.
- The Legend exhausts per Gold: one mint until something dies. Front-
  load a kill if you want two mints in a turn.
- Gold tokens are **killed** when used (their text), not recycled — no
  Gold-into-Gold loop exists; the token's Any Rune also isn't a rune
  recycle.
- `Ancient Henge` adds Power without recycling runes — it's ramp that
  deliberately *doesn't* trigger the Legend; use it when the mint is
  already exhausted.
- `On the Hunt` readies units only — not runes, not the Legend.
- `Twisted Fate`'s modal effect is dictated by the revealed rune's
  domain — an 8/4 Body/Chaos rune deck means his Fury/Mind/Order modes
  almost never fire; his value here is the recycle itself. (His flip
  effects list Fury/Mind/Order only — with this rune base, expect *no*
  modal bonus most attacks; he is played for the trigger.)

## Upgrade Paths

- `Void Assault` is Kha'Zix's signature and stays in that deck; `Bullet
  Time` is Miss Fortune's — Body/Chaos is signature-crowded, and this
  shell's identity is the only one built on the recycle rule.
- Splashier rune bases (adding Fury or Order runes) turn on Twisted
  Fate's modal hits at the cost of Power consistency — worth testing
  in a simulation.
- `Vicious Snapjaws` (XP per friendly death) plus `Cull the Weak`
  effects would add a self-sacrifice angle to the ready-Sivir line.
- `Baron Nashor` is the vanity Gold sink if Elder Dragon isn't enough.
