def parse(input):
    return input


def part1(data):
    print(f"{data}\n\n")
    return "ans1"


def part2(data, ans1):
    return "ans2"


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
