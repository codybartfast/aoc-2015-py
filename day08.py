def parse(input):
    return input.splitlines()


def part1(lines):
    return sum(len(line) - len(eval(line)) for line in lines)


def part2(data, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
