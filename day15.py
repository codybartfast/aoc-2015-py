from math import prod


def parse(text):
    return [
        tuple(int(prop_val.split()[1]) for prop_val in prop_vals)
        for prop_vals in [line.split(": ")[1].split(", ") for line in text.splitlines()]
    ]


def add_ingredient(properties, ingredient, spoons):
    return [
        properties[idx] + spoons * ingredient[idx] for idx in range(len(properties))
    ]


def recipes(properties, ingredients, remaining_spoons):
    if len(ingredients) == 1:
        yield add_ingredient(properties, ingredients[0], remaining_spoons)
    else:
        for spoons in range(remaining_spoons + 1):
            yield from recipes(
                add_ingredient(properties, ingredients[0], spoons),
                ingredients[1:],
                remaining_spoons - spoons,
            )


def score(properties, need_500=False):
    [*props, cals] = properties
    if ((not need_500) or (need_500 and cals == 500)) and all(a > 0 for a in props):
        return prod(props)
    else:
        return 0


def part1(properties):
    return max(map(score, recipes([0] * len(properties[0]), properties, 100)))


def part2(properties, ans1=None):
    return max(
        score(atts, True) for atts in recipes([0] * len(properties[0]), properties, 100)
    )


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
