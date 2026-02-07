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
    aunts = []
    for line in text.splitlines():
        name_numb, kvps = line.split(": ", 1)
        name, numb = name_numb.split()
        aunt = {name: numb} | {
            key: int(value)
            for (key, value) in [kvp.split(": ") for kvp in kvps.split(", ")]
        }
        aunts.append(aunt)
    return aunts


def part1(aunts):
    matches = [
        aunt["Sue"]
        for aunt in aunts
        if all(aunt[key] == MFCSAM[key] for key in aunt.keys() if key != "Sue")
    ]
    return matches[0]


def part2(aunts, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
