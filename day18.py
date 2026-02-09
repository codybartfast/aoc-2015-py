# Using bits is overkill given size but I wanted to try it :-)

# Assumes lights is square in a couple of places


def parse(text):
    lights = [0]
    for line in text.splitlines():
        row = 0
        for char in line:
            if char == "#":
                row |= 1
            row <<= 1
        lights.append(row)
    lights.append(0)
    return lights


def step(lights):
    # This flips the lights horizontally (vert. axis) on each call.
    width = len(lights) - 2
    count_mask = 0b111
    on_mask = 0b010

    next = [0] * len(lights)

    for _ in range(width):
        for row in range(1, len(lights) - 1):
            count = (
                (lights[row - 1] & count_mask).bit_count()
                + (lights[row] & count_mask).bit_count()
                + (lights[row + 1] & count_mask).bit_count()
            )
            if count == 3 or (count == 4 and (lights[row] & on_mask)):
                next[row] |= 1
            next[row] <<= 1
        count_mask <<= 1
        on_mask <<= 1

    return next


def set_corners(lights):
    corner_mask = (1 << len(lights) - 2) | 0b10
    lights[1] |= corner_mask
    lights[len(lights) - 2] |= corner_mask
    return lights


def part1(lights):
    for _ in range(100):
        lights = step(lights)
    return sum(row.bit_count() for row in lights)


def part2(lights, ans1=None):
    set_corners(lights)
    for _ in range(100):
        lights = set_corners(step(lights))
    return sum(row.bit_count() for row in lights)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
