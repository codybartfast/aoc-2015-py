#  Day 25
#  ======
#
#  Part 1: 8997277
#  Part 2: Meryy Christmas
#
#  Timings
#  ---------------------
#    Parse:     0.000003
#   Part 1:     0.000003
#   Part 2:     0.000000
#  Elapsed:     0.000044


def parse(text):
    parts = text.split()
    return int(parts[-1][:-1]), int(parts[-3][:-1])


def part1(cell):
    x, y = cell
    line = x + y
    index = x + ((line - 1) * (line - 2) // 2)
    code = 20151125
    # for _ in range(1, n):
    #     code = (code * 252533) % 33554393
    #
    # pow(_, _, modulus) found with a little ai help
    return code * pow(252533, index - 1, 33554393) % 33554393


def part2(data, ans1=None):
    return "Meryy Christmas"


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
