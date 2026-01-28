def parse(input):
    return input.splitlines()


def is_nice(string):
    prev = ""
    vowels = 0
    has_double = False
    for char in string:
        if char in "aeiou":
            vowels += 1
        if char == prev:
            has_double = True
        if prev + char in ["ab", "cd", "pq", "xy"]:
            return False
        prev = char
    return vowels >= 3 and has_double


def part1(strings):
    return sum(is_nice(string) for string in strings)


def part2(strings, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
