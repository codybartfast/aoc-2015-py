def parse(text):
    joys = {}
    for a, b, joy in [
        (
            parts[0],
            parts[10][:-1],
            (1 if parts[2] == "gain" else -1) * int(parts[3]),
        )
        for parts in [line.split() for line in text.splitlines()]
    ]:
        joys[a, b] = joys.get((a, b), 0) + joy
        joys[b, a] = joys[a, b]
    return joys


def perms(set):
    if len(set) == 1:
        yield list(set)
    for item in set:
        for perm in perms(set - {item}):
            yield [item] + perm


def arrange_seating(joys, skip_host):
    return max(
        sum(joys[pair] for pair in zip(plan, plan[1:]))
        + (joys[plan[0], plan[-1]] if skip_host else 0)
        for plan in perms(set(a for (a, b) in joys.keys()))
    )


def part1(joys):
    return arrange_seating(joys, True)


def part2(joys, ans1=None):
    return arrange_seating(joys, False)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
