def parse(input):
    return input


dir_deltas = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def route(directions):
    x, y = 0, 0
    yield x, y
    for dir in directions:
        dx, dy = dir_deltas[dir]
        x += dx
        y += dy
        yield x, y


def part1(directions):
    return len(set(route(directions)))


def part2(directions, ans1):
    santa = route(directions[::2])
    robo_santa = route(directions[1::2])
    visited = set(santa)
    visited.update(robo_santa)
    return len(visited)


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
