def parse(text):
    return list(map(int, text))


def see_and_say(seq):
    prev = None
    count = 0
    for n in seq:
        if prev is None:
            prev = n
            count = 1
        elif n == prev:
            count += 1
        else:
            yield count
            yield prev
            prev = n
            count = 1
    yield count
    yield prev


def repeat(n, func, arg):
    if n == 1:
        return func(arg)
    return func(repeat(n - 1, func, arg))


def part1(seq):
    return sum(1 for _ in repeat(40, see_and_say, seq))


def part2(seq, ans1=None):
    return sum(1 for _ in repeat(50, see_and_say, seq))


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
