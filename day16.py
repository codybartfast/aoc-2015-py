MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse(text):
    aunts = {}
    for line in text.splitlines():
        name_numb, kvps = line.split(": ", 1)
        numb = int(name_numb.split()[1])
        aunts[numb] = {
            key: int(value)
            for (key, value) in [kvp.split(": ") for kvp in kvps.split(", ")]
        }
    return aunts


def equality_match(key, scanVal, auntVal):
    return scanVal == auntVal


def turbo_match(key, scanVal, auntVal):
    if key in ["cats", "trees"]:
        return scanVal <= auntVal
    if key in ["goldfish", "pomeranians"]:
        return scanVal >= auntVal
    return auntVal == scanVal


def find_matches(MFCSAM, aunts, is_match):
    return [
        number
        for number, aunt in aunts.items()
        if all(is_match(key, MFCSAM[key], aunt[key]) for key in aunt.keys())
    ]


def part1(aunts):
    return find_matches(MFCSAM, aunts, equality_match)[0]


def part2(aunts, ans1=None):
    return find_matches(MFCSAM, aunts, turbo_match)[0]


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
