def parse(input):
    return [
        (
            parts[-4],
            tuple(map(int, parts[-3].split(","))),
            tuple(map(int, parts[-1].split(","))),
        )
        for parts in [line.split() for line in input.splitlines()]
    ]


def make_lights(size = 1000):
    return [[False] * size for _ in range(size)]

def turn_on(n):
    return True

def turn_off(n):
    return False

def toggle(n):
    return not n

def apply(instruction, lights):
    (op, (x1, y1), (x2, y2)) = instruction
    match op:
        case "on":
            set = turn_on
        case "off":
            set = turn_off
        case "toggle":
            set = toggle
    for y in range(y1, y2 + 1):
        row = lights[y]
        for x in range(x1, x2 + 1):
            row[x] = set(row[x])
    
    
def part1(instructions):
    lights = make_lights()
    for instr in instructions:
        apply(instr, lights)
    return sum(sum(row) for row in lights)


def part2(instructions, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
