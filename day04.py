import hashlib


def parse(input):
    return input


def md5(key, number):
    text = key + str(number)
    return hashlib.md5(text.encode("ascii")).hexdigest()


def search(key, nzero):
    zero_str = "0" * nzero
    n = 0
    while not md5(key, n).startswith(zero_str):
        n += 1
    return n


def part1(key):
    return search(key, 5)


def part2(key, ans1=None):
    return search(key, 6)


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
