def parse_line(line):
    return line
    parts = line.split()
    return parts


def parse(text):
    return [parse_line(line) for line in text.splitlines()]


def part1(data):
    print(f"{data}\n\n")
    return "ans1"


def part2(data, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
