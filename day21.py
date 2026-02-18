#  Day 21
#  ======
#
#  Part 1: 78
#  Part 2: 148
#
#  Timings
#  ---------------------
#    Parse:     0.000018
#   Part 1:     0.000469
#   Part 2:     0.000452
#  Elapsed:     0.000984
#

shop_text = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


def parse_shop_text(shop_text):
    def parse_shop_chunk(chunk):
        return [tuple(map(int, line.split()[-3:])) for line in chunk.splitlines()[1:]]

    shop = [parse_shop_chunk(chunk) for chunk in shop_text.split("\n\n")]
    shop[1].insert(0, (0, 0, 0))
    shop[2].insert(0, (0, 0, 0))
    shop[2].insert(0, (0, 0, 0))
    return shop


def parse(text):
    def parse_line(line):
        return int(line.split()[-1])

    boss = tuple(parse_line(line) for line in text.splitlines())
    return boss, parse_shop_text(shop_text)


def player_wins(player, boss):
    p_hp, p_damage, p_armour = player
    b_hp, b_damage, b_armour = boss
    p_effect = max(0, p_damage - b_armour)
    b_effect = max(0, b_damage - p_armour)

    if not p_effect:
        return False

    p_turns, rem = divmod(b_hp, p_effect)
    p_turns += rem > 0
    return (p_turns - 1) * b_effect < p_hp


def equip_choices(shop):
    weapons, armours, rings = shop
    for r1 in range(len(rings) - 1):
        ring1 = rings[r1]
        for ring2 in rings[r1 + 1 :]:
            for armour in armours:
                for weapon in weapons:
                    yield map(sum, zip(ring1, ring2, armour, weapon))


def equip_outcomes(p_hp, shop, boss):
    for cost, damage, armour in equip_choices(shop):
        yield player_wins((p_hp, damage, armour), boss), cost


def part1(data):
    boss, shop = data
    outcomes = equip_outcomes(100, shop, boss)
    return min(oc[1] for oc in outcomes if oc[0])


def part2(data, ans1=None):
    boss, shop = data
    outcomes = equip_outcomes(100, shop, boss)
    return max(oc[1] for oc in outcomes if not oc[0])


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
