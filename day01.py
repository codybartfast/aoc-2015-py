def parse(input):
    return input


def apply(instrs):
    floor = 0
    for instr in instrs:
        floor += 1 if instr == "(" else -1
        yield floor


def part1(data):
    return list(apply(data))[-1]


def part2(data, ans1=None):
    return list(apply(data)).index(-1) + 1


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
