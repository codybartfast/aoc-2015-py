import re


def parse(input):
    return input.splitlines()


def is_nice(string):
    prev = "\n"
    vowels = 0
    has_double = False
    for char in string:
        if char in "aeiou":
            vowels += 1
        if char == prev:
            has_double = True
        if (idx := "acpx".find(prev)) >= 0 and "bdqy"[idx] == char:
            return False
        prev = char
    return vowels >= 3 and has_double


repeated_pair_rx = re.compile(r"(..).*\1")
split_pair_rx = re.compile(r"(.).\1")


def is_nicer(string):
    return bool(repeated_pair_rx.search(string)) and bool(split_pair_rx.search(string))


def part1(strings):
    return sum(is_nice(string) for string in strings)


def part2(strings, ans1=None):
    return sum(is_nicer(string) for string in strings)


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
