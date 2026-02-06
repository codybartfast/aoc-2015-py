from math import prod


def parse(text):
    return [
        tuple(int(attr_val.split()[1]) for attr_val in attr_vals)
        for attr_vals in [line.split(": ")[1].split(", ") for line in text.splitlines()]
    ]


def add_ingredient(attributes, ingredient, spoons):
    return [
        attributes[idx] + spoons * ingredient[idx] for idx in range(len(attributes))
    ]


def recipes(attributes, ingredients, remaining_spoons):
    if len(ingredients) == 1:
        yield add_ingredient(attributes, ingredients[0], remaining_spoons)
    else:
        for spoons in range(remaining_spoons + 1):
            yield from recipes(
                add_ingredient(attributes, ingredients[0], spoons),
                ingredients[1:],
                remaining_spoons - spoons,
            )


def score(attributes):
    attributes = attributes[:-1]
    return prod(attributes) if all(a > 0 for a in attributes) else 0


def part1(data):
    return max(map(score, recipes([0] * len(data[0]), data, 100)))


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
