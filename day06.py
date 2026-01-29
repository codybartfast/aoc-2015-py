def parse(input):
    return [
        (
            parts[-4],
            tuple(map(int, parts[-3].split(","))),
            tuple(map(int, parts[-1].split(","))),
        )
        for parts in [line.split() for line in input.splitlines()]
    ]


def apply(instruction, lights, turn_on, turn_off, toggle):
    (op, (x1, y1), (x2, y2)) = instruction
    match op:
        case "on":
            adjust = turn_on
        case "off":
            adjust = turn_off
        case "toggle":
            adjust = toggle
    for y in range(y1, y2 + 1):
        row = lights[y]
        for x in range(x1, x2 + 1):
            row[x] = adjust(row[x])


def part1(instructions):
    lights = [[0] * 1000 for _ in range(1000)]
    for instr in instructions:
        apply(instr, lights, lambda n: 1, lambda n: 0, lambda n: not n)
    return sum(sum(row) for row in lights)


def part2(instructions, ans1=None):
    lights = [[0] * 1000 for _ in range(1000)]
    for instr in instructions:
        apply(instr, lights, lambda n: n + 1, lambda n: max(0, n - 1), lambda n: n + 2)
    return sum(sum(row) for row in lights)


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
