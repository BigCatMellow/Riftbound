# Deck Index

Deck files are grouped by intended player experience and testing purpose.

Coverage: all 39 distinct Legends in `riftbound_cards_organized.md` have a
deck as of 2026-07-06 (one deck per Legend; some domain pairs have several
decks with deliberately different engines). Run
`python3 scripts/validate_decks.py` after any deck change.

## Beginner

| Deck | Legend | Domains | Plan |
|---|---|---|---|
| `beginner/garen-go-wide-beginner.md` | Garen - Might of Demacia - Starter | Body, Order | Make multiple units, conquer with four or more units, draw cards with Garen. |
| `beginner/annie-spell-burn-beginner.md` | Annie - Dark Child - Starter | Fury, Chaos | Use efficient damage spells, recur spells with Annie units, and close with boosted burn. |
| `beginner/leona-stun-and-buff-beginner.md` | Leona - Radiant Dawn | Calm, Order | Stun enemy units to shut off attacks/defense, buff your own units off the Legend's stun trigger, win fair fights with bigger bodies. |

## Synergy

| Deck | Legend | Domains | Plan |
|---|---|---|---|
| `synergy/jinx-discard-engine-synergy.md` | Jinx - Loose Cannon | Fury, Chaos | Discard on purpose to trigger `Jinx - Rebel` and other discard payoffs, refuel with draw-back effects, recur `Super Mega Death Rocket!` from the trash. |
| `synergy/rumble-mech-tribal-synergy.md` | Rumble - Mechanized Menace | Fury, Mind | Flood the board with Mech tokens, buff them as a type with Shield and the chosen champion's +1 Might, grind out combat with defenders that get stronger every fight. |
| `synergy/lucian-equipment-assault-synergy.md` | Lucian - Purifier | Fury, Body | Attach Equipment to [Weaponmaster] units for a discount, let the Legend turn every piece of Equipment into free Assault, recirculate gear with Angle Shot/Strike Down. |
| `synergy/yasuo-ganking-tempo-synergy.md` | Yasuo - Unforgiven | Calm, Chaos | Build around [Ganking] and "on move" payoffs on purpose (the gap Lucian's lack of Ganking exposed); reposition constantly for value and cash in a third move per turn with Yasuo - Windrider. |
| `synergy/lillia-sprite-swarm-synergy.md` | Lillia - Bashful Bloom | Calm, Mind | Flood the board with ready 3-Might Sprite tokens, buff them as a type, and win with board width — including the literal 7-units alt-win condition on The Grand Plaza. |
| `synergy/draven-assault-aggro-synergy.md` | Draven - Glorious Executioner | Fury, Chaos | Stack [Assault] to win combats cleanly, converting every win directly into cards (the Legend) and points (Draven - Audacious) — a combat-first identity distinct from Jinx's discard engine and Annie's spell burn in the same domain pair. |
| `synergy/volibear-mighty-tribal-synergy.md` | Volibear - Relentless Storm | Fury, Body | Get units to 5+ Might ("[Mighty]") by any means to trigger four separate payoffs keyed to that exact threshold: a free rune channel, a cost discount, and two card-draw effects. |
| `synergy/sett-buff-insurance-synergy.md` | Sett - The Boss | Body, Order | Spread cheap +1 Might buffs, then spend a dying unit's buff to save it from death entirely instead of losing it; Sett - Kingpin scales with how many buffed units share its battlefield. |
| `synergy/vi-excess-damage-aggro-synergy.md` | Vi - Piltover Enforcer | Fury, Order | Strip blockers with stuns/removal so attacks land as excess damage, then cash that excess damage in three times over: the Legend's free ready, Yeti Brawler's Gold gear tokens, and Tryndamere's scored point. |
| `synergy/fiora-mighty-threshold-synergy.md` | Fiora - Grand Duelist | Body, Order | Treat "becomes [Mighty]" as an event: every temporary pump that pushes a unit across 5 Might also channels a rune (Legend) and readies the unit (Fiora - Worthy) — even the counterspell (Riposte) pumps. |
| `synergy/pyke-revolving-door-synergy.md` | Pyke - Bloodharbor Ripper | Fury, Chaos | Nothing is played once: the Legend bounces a friendly unit every turn and mints Gold for it, so every on-play effect is a subscription — and Death from Below recurs itself. |
| `synergy/azir-standing-army-synergy.md` | Azir - Emperor of the Sands | Calm, Order | Tokens that wear swords: every Equipment mints a Sand Soldier (Legend), every soldier equips at a discount (Weaponmaster), Blade of the Ruined King eats spares, and Arise! turns the armory into an army. |
| `synergy/viktor-glorious-evolution-synergy.md` | Viktor - Herald of the Arcane | Mind, Order | An assembly line that never stops: the Legend prints a Recruit every turn, Zilean doubles one token play, Viktor - Innovator prints on the opponent's turn off nine reactions, and Soul Shepherd + Industrialist turn width into a ready 2-Might army. |
| `synergy/irelia-blade-dance-synergy.md` | Irelia - Blade Dancer | Calm, Chaos | Targeting your own units IS the engine: every pump also readies the target (Legend), grows it twice (Fervent triggers on chosen AND readied), draws cards (Jae Medarda, Spirit Wheel, Dreaming Tree), and got discounted (Graceful). |
| `synergy/missfortune-bounty-runners-synergy.md` | Miss Fortune - Bounty Hunter | Body, Chaos | Movement as income: the Legend grants Ganking on demand, the crew gets paid per move (XP, stat transfers, pumps, a free untap), Buccaneer deploys straight to open battlefields, and Bullet Time sweeps wherever the runners converge. |
| `synergy/leesin-buff-currency-synergy.md` | Lee Sin - Blind Monk | Calm, Body | Buffs as currency: the Legend mints one per turn, Ascetic banks unlimited coins, and half the deck spends them — Wallop's free ready, Kraken Hunter's discount, Fae Dragon's buff-to-Gold exchange, Monastery's card per conquest. |
| `synergy/ezreal-double-tap-synergy.md` | Ezreal - Prodigal Explorer | Mind, Chaos | Choose enemies twice a turn and the Legend draws: Orb of Regret + The List generate both taps for zero cards, combat abilities tap (Dashing, Icevale Archer), and Arcane Shift re-buys ETB units while tapping. |
| `synergy/jax-grandmaster-juggle-synergy.md` | Jax - Grandmaster at Arms | Calm, Body | One set of swords, many bearers: the Legend re-attaches Equipment at will, every attach to Jax - Unrelenting draws a card, Aphelios stops mint mana, and Akshan steals enemy gear into the rotation. |
| `synergy/sivir-gold-rush-synergy.md` | Sivir - Battle Mistress | Body, Chaos | Built on core rule 163.2.b: Basic Runes pay Power by recycling themselves, so every Power cost triggers the Legend's Gold mint — and enemy deaths re-ready her for more; On the Hunt readies the army for 1 Energy. |
| `synergy/rengar-pride-ambush-synergy.md` | Rengar - Pridestalker | Fury, Body | The Legend pumps a unit +1 on EVERY unit play, free — so units arrive at reaction speed (Ambush, Reaction-speed Pouncing, hidden Here to Help, Thrill of the Hunt replays) and every deploy is also a mid-combat trick. |
| `synergy/ivern-menagerie-synergy.md` | Ivern - Green Father | Calm, Order | A petting zoo with teeth: Poro/Bird swarm, the Legend terraforms conquests into Brush (+1 for animals), Friendship pays per tag type, and Daisy! discounts per tag to arrive early and ready. Tag data gap explicitly flagged. |

## Advanced

| Deck | Legend | Domains | Plan |
|---|---|---|---|
| `advanced/renata-gold-engine-advanced.md` | Renata Glasc - Chem-Baroness | Mind, Order | Generate Gold gear tokens from holds and deathknells, keep them ready with the chosen champion, and sequence when to crack them (especially near Victory Score, when Gold adds extra Energy). |
| `advanced/teemo-hidden-ambush-advanced.md` | Teemo - Swift Scout | Mind, Chaos | Play cards face down with [Hidden] for a cheap future reveal, flip them at the moment they're most disruptive, track deck density for Teemo - Strategist's damage payoff. |
| `advanced/darius-legion-tempo-advanced.md` | Darius - Hand of Noxus | Fury, Order | Sequence a cheap setup card before every [Legion] payoff each turn — the same removal spell (Noxian Guillotine) is either delayed or instant depending entirely on play order. |
| `advanced/leblanc-reflection-deathknell-advanced.md` | LeBlanc - Deceiver | Mind, Order | The Legend's [Temporary] Reflection token dies every Beginning Phase on schedule — so copy Deathknell units and the forced death IS the engine, doubled by Karthus and cashed by Wraith of Echoes, Viktor, and Shard of Undoing. |
| `advanced/jhin-four-act-spells-advanced.md` | Jhin - Virtuoso | Fury, Mind | Every core spell deliberately costs 4+ Energy so one cast pays five ways: the Legend's four-act banish clock, Prepared Neophyte's +4, Revna's untap, a one-rune Jhin - Meticulous Killer, and Forgotten Library's Predict. |
| `advanced/ahri-shrink-and-sweep-advanced.md` | Ahri - Nine-Tailed Fox | Calm, Mind | Never race, dissolve: the Legend shrinks every attacker, stacked -Might effects make 1-Might husks, and Fox-Fire's "total Might 4 or less" sweeps four of them at once while Ahri - Alluring scores off quiet holds. |
| `advanced/ornn-masterwork-forge-advanced.md` | Ornn - Fire Below the Mountain | Calm, Mind | The only deck whose 3 signature slots are 3 different cards (Ornn's Unique masterworks): the Legend's gear-only rune funds the forge, Gearhead doubles Equipment Might, and Forge God grows +1 per gear. |
| `advanced/vex-gloomhold-advanced.md` | Vex - Gloomist | Calm, Chaos | Stun as removal: stunned attackers deal nothing so defenders eat them free, Vex - Apathetic stuns and pins every reinforcement, Leona - Zealot gives stunned enemies -8, and the Legend draws a card per quiet hold. |
| `advanced/reksai-tunnel-cascade-advanced.md` | Rek'Sai - Void Burrower | Fury, Order | Attacking flips free cards into play: the Legend cascades on every conquer, Swarm Queen cascades on attack, Breacher gives cheated units Accelerate so they join the same fight, and Undertitan pays you 2 Energy just for being revealed. |
| `advanced/lux-final-spark-advanced.md` | Lux - Lady of Luminosity | Mind, Order | Every big spell replaces itself: the Legend draws off each 5+ cost spell (fifteen qualify), Crownguard banks 2 spell-Energy at reaction speed, Imperial Decree turns any ping into an execution, and The Academy doubles Final Spark. |
| `advanced/diana-moonlit-showdown-advanced.md` | Diana - Scorn of the Moon | Mind, Chaos | Fight only at night: the Legend banks showdown-only Energy, Moonfall drags an enemy into your trap battlefield, hidden cards spring for free, and Syndra gives every spell Repeat mid-showdown. |
| `advanced/poppy-hammer-time-advanced.md` | Poppy - Keeper of the Hammer | Body, Order | XP as a shared wallet with competing bills: holds deposit, and each turn you choose the bill — a card (Legend), a 3-Energy discount (Defender of the Meek), a one-sided sweep (Safety Inspector), or a ready (Blood Rose). |

## Overpowered

| Deck | Legend | Domains | Plan |
|---|---|---|---|
| `overpowered/master-yi-xp-snowball-overpowered.md` | Master Yi - Wuju Master | Calm, Body | Farm XP with [Hunt] units to hit the Legend's Level 6 (board-wide +1 Might) and Level 11 (units enter ready) thresholds, then land a cost-reduced, eventually removal-proof `Master Yi - Unstoppable`. |
| `overpowered/khazix-xp-burst-overpowered.md` | Kha'Zix - Voidreaver | Body, Chaos | Bank XP from combat wins and Hunt triggers, then cash it in for repeatable, unblockable direct damage or an outright unit steal via `Conscription`. |
| `overpowered/kaisa-icathian-barrage-overpowered.md` | Kai'Sa - Daughter of the Void | Fury, Mind | Bonus Damage multiplies per instance: Icathian Rain is six instances, so Annie - Fiery makes it 18 and Void Gate 24; the Legend adds a spell-only rune every turn and Evolutionary replays the Rain from trash on conquer. |
