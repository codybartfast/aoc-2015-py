def parse(text):
    return tuple(sorted((int(line) for line in text.splitlines()), reverse=True))


def pack(pkgs, picked, remaining, max_pick_lst):
    if remaining == 0:
        max_pick_lst[0] = min(max_pick_lst[0], len(picked))
        yield picked, pkgs
    if remaining < 0 or not pkgs or len(picked) >= max_pick_lst[0]:
        return
    pkg, *rest = pkgs
    new_picked = list(picked)
    new_picked.append(pkg)
    yield from pack(rest, new_picked, remaining - pkg, max_pick_lst)
    yield from pack(rest, picked, remaining, max_pick_lst)


def mul(values):
    result = 1
    for value in values:
        result *= value
    return result


def find_balance(packages, split):
    full_load = sum(packages)
    target = full_load / split
    max_pick_lst = [10**8]

    picks = [
        (pick, unused)
        for pick, unused in list(pack(packages, [], target, max_pick_lst))
        if len(pick) == max_pick_lst[0]
    ]
    return min(
        [mul(pick) for pick, unused in picks if pack(unused, [], target, [10**18])]
    )


def part1(packages):
    return find_balance(packages, 3)


def part2(packages, ans1=None):
    return find_balance(packages, 4)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
