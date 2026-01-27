def parse(input):
    return [tuple(map(int, line.split("x"))) for line in input.splitlines()]


def wrapping(dimensions):
    d1, d2, d3 = sorted(dimensions)
    s1, s2, s3 = d1 * d2, d2 * d3, d1 * d3
    return s1 + 2 * (s1 + s2 + s3)


def ribbon(dimensions):
    d1, d2, d3 = sorted(dimensions)
    return 2 * (d1 + d2) + (d1 * d2 * d3)


def part1(data):
    return sum(map(wrapping, data))


def part2(data, ans1):
    return sum(map(ribbon, data))


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
