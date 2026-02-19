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


def initial_state(p_hp, mana, b_hp, b_dmg):
    state = [0] * 10
    state[P_HP] = p_hp
    state[MANA] = mana
    state[B_HP] = b_hp
    state[B_DMG] = b_dmg
    state[SHIELD_ENDS] = -1
    state[POISON_ENDS] = -1
    state[RECHARGE_ENDS] = -1
    return state


def parse(text):
    return [int(line.split()[-1]) for line in text.splitlines()]


def spend(state, amount):
    if state[MANA] < amount:
        return False
    state[MANA] -= amount
    state[MANA_SPENT] += amount
    return True


def missile(state):
    if not spend(state, 53):
        return None
    state[B_HP] -= 4
    return state


def drain(state):
    if not spend(state, 73):
        return None
    state[P_HP] += 2
    state[B_HP] -= 2
    return state


def shield(state):
    if state[SHIELD_ENDS] > state[TURN] or not spend(state, 113):
        return None
    state[SHIELD_ENDS] = state[TURN] + 6
    return state


def poison(state):
    if state[POISON_ENDS] > state[TURN] or not spend(state, 173):
        return None
    state[POISON_ENDS] = state[TURN] + 6
    return state


def recharge(state):
    if state[RECHARGE_ENDS] > state[TURN] or not spend(state, 229):
        return None
    state[RECHARGE_ENDS] = state[TURN] + 5
    return state


spells = [missile, drain, shield, poison, recharge]


def apply_effects(state):
    state[P_ARM] = 7 if state[SHIELD_ENDS] > state[TURN] else 0
    if state[POISON_ENDS] > state[TURN]:
        state[B_HP] -= 3
    if state[RECHARGE_ENDS] > state[TURN]:
        state[MANA] += 101
    return state


def player_turn(state):
    state[TURN] += 1
    return (spelled for spell in spells if (spelled := spell(list(state))))


def boss_turn(state, is_hard):
    state[TURN] += 1
    damage = max(1, state[B_DMG] - state[P_ARM])
    if is_hard:
        damage = damage + 1
    state[P_HP] -= damage
    return state if state[P_HP] > 0 else None


def battle(states, is_hard):
    best_cost = 10**18
    while states:
        if states[0][TURN] % 2 == 0:
            next_states = [next for state in states for next in player_turn(state)]
        else:
            next_states = [
                next for state in states if (next := boss_turn(state, is_hard))
            ]

        states = []
        for next in next_states:
            if next[MANA_SPENT] < best_cost:
                apply_effects(next)
                if next[B_HP] <= 0:
                    best_cost = next[MANA_SPENT]
                else:
                    states.append(next)
    return best_cost


def part1(data):
    p_hp = 50
    mana = 500
    b_hp, b_dmg = data

    # p_hp = 10
    # mana = 250
    # b_hp, b_dmg = 14, 8

    initial = initial_state(p_hp, mana, b_hp, b_dmg)

    return battle([initial], False)


def part2(data, ans1=None):
    p_hp = 50
    mana = 500
    b_hp, b_dmg = data
    initial = initial_state(p_hp, mana, b_hp, b_dmg)

    return battle([initial], True)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
