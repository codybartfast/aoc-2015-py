#  Day 22
#  ======
#
#  Part 1: 1269
#  Part 2: 1309
#
#  Timings
#  ---------------------
#    Parse:     0.000003
#   Part 1:     0.008398
#   Part 2:     0.006147
#  Elapsed:     0.014601


TURN = 0
P_HP = 1
P_ARM = 2
MANA = 3
MANA_SPENT = 4
B_HP = 5
B_DMG = 6
SHIELD_ENDS = 7
POISON_ENDS = 8
RECHARGE_ENDS = 9


def initial_game(p_hp, mana, b_hp, b_dmg):
    game = [0] * 10
    game[P_HP] = p_hp
    game[MANA] = mana
    game[B_HP] = b_hp
    game[B_DMG] = b_dmg
    game[SHIELD_ENDS] = -1
    game[POISON_ENDS] = -1
    game[RECHARGE_ENDS] = -1
    return game


def parse(text):
    return [int(line.split()[-1]) for line in text.splitlines()]


def spend(game, amount):
    if game[MANA] < amount:
        return False
    game[MANA] -= amount
    game[MANA_SPENT] += amount
    return True


def missile(game):
    if not spend(game, 53):
        return None
    game[B_HP] -= 4
    return game


def drain(game):
    if not spend(game, 73):
        return None
    game[P_HP] += 2
    game[B_HP] -= 2
    return game


def shield(game):
    if game[SHIELD_ENDS] > game[TURN] or not spend(game, 113):
        return None
    game[SHIELD_ENDS] = game[TURN] + 6
    return game


def poison(game):
    if game[POISON_ENDS] > game[TURN] or not spend(game, 173):
        return None
    game[POISON_ENDS] = game[TURN] + 6
    return game


def recharge(game):
    if game[RECHARGE_ENDS] > game[TURN] or not spend(game, 229):
        return None
    game[RECHARGE_ENDS] = game[TURN] + 5
    return game


spells = [missile, drain, shield, poison, recharge]


def apply_effects(game):
    game[P_ARM] = 7 if game[SHIELD_ENDS] > game[TURN] else 0
    if game[POISON_ENDS] > game[TURN]:
        game[B_HP] -= 3
    if game[RECHARGE_ENDS] > game[TURN]:
        game[MANA] += 101
    return game


def player_turn(game):
    game[TURN] += 1
    return (spelled for spell in spells if (spelled := spell(list(game))))


def boss_turn(game, is_hard):
    game[TURN] += 1
    damage = max(1, game[B_DMG] - game[P_ARM])
    if is_hard:
        damage = damage + 1
    game[P_HP] -= damage
    return game if game[P_HP] > 0 else None


def battle(games, is_hard):
    min_mana = 10**18
    while games:
        if games[0][TURN] % 2 == 0:
            next_games = [next for game in games for next in player_turn(game)]
        else:
            next_games = [next for game in games if (next := boss_turn(game, is_hard))]

        games = []
        for next in next_games:
            if next[MANA_SPENT] < min_mana:
                apply_effects(next)
                if next[B_HP] <= 0:
                    min_mana = next[MANA_SPENT]
                else:
                    games.append(next)
        games = sorted(games, key=lambda game: game[B_HP])[:1024]

    return min_mana


def part1(data):
    p_hp = 50
    mana = 500
    b_hp, b_dmg = data

    # p_hp = 10
    # mana = 250
    # b_hp, b_dmg = 14, 8

    game = initial_game(p_hp, mana, b_hp, b_dmg)

    return battle([game], False)


def part2(data, ans1=None):
    p_hp = 50
    mana = 500
    b_hp, b_dmg = data

    game = initial_game(p_hp, mana, b_hp, b_dmg)

    return battle([game], True)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
