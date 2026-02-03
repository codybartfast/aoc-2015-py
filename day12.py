import json
import re


def parse(text):
    return text


def part1(data):
    return sum(int(m) for m in re.findall(r"-?\d+", data))


def sum_nums(accts):
    match accts:
        case int():
            return accts
        case dict():
            if "red" not in accts.values():
                return sum(sum_nums(item) for item in accts.values())
            else:
                return 0
        case list():
            return sum(sum_nums(item) for item in accts)
        case str():
            return 0
        case _:
            raise RuntimeError(type(accts))


def part2(data, ans1=None):
    return sum_nums(json.loads(data))


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
