INF = 10**18


def parse(text):
    contribs = {}
    for a, contrib, b in [
        (
            ord(parts[0][0]),
            (1 if parts[2] == "gain" else -1) * int(parts[3]),
            ord(parts[10][0]),
        )
        for parts in [line.split() for line in text.splitlines()]
    ]:
        new_contrib = contribs.get((a, b), 0) + contrib
        contribs[a, b] = new_contrib
        contribs[b, a] = new_contrib
    return contribs


def perms(set):
    if len(set) == 1:
        yield list(set)
    for item in set:
        for perm in perms(set - {item}):
            yield [item] + perm


def best_straight(contributions, plan):
    return sum(contributions[pair] for pair in zip(plan, plan[1:]))


def pursue_happiness(contributions, include_host):
    best = -INF
    diners = set(a for (a, b) in contributions.keys())

    for plan in perms(diners):
        happiness = best_straight(contributions, plan)
        if not include_host:
            happiness += contributions[plan[0], plan[-1]]

        if happiness > best:
            best = happiness

    return best


def part1(data):
    return pursue_happiness(data, False)


def part2(data, ans1=None):
    return pursue_happiness(data, True)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
