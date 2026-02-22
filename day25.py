def parse(text):
    parts = text.split()
    return int(parts[-1][:-1]), int(parts[-3][:-1])

def part1(cell):
    x, y = cell
    line = x + y
    n = x + ((line - 1) * (line - 2) // 2)
    code = 20151125
    for _ in range(1, n):
        code = (code * 252533) % 33554393
    return code


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
