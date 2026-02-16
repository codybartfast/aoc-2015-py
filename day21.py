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


def parse_shop_chunk(chunk):
    return [tuple(map(int, line.split()[-3:])) for line in chunk.splitlines()[1:]]


def parse_shop_text(shop_text):
    shop = [parse_shop_chunk(chunk) for chunk in shop_text.split("\n\n")]
    shop[1].insert(0, (0, 0, 0))
    shop[2].insert(0, (0, 0, 0))
    shop[2].insert(0, (0, 0, 0))
    return shop


def parse_line(line):
    return int(line.split()[-1])


def parse(text):
    return tuple(parse_line(line) for line in text.splitlines())


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


def cheap_victory(p_hp, shop, boss):
    best_cost = 10**18
    for cost, damage, armour in equip_choices(shop):
        if cost < best_cost and player_wins((p_hp, damage, armour), boss):
            best_cost = cost
    return best_cost


def part1(boss):
    shop = parse_shop_text(shop_text)
    return cheap_victory(100, shop, boss)


def part2(data, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
