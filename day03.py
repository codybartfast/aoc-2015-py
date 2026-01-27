def parse(input):
    return input


def next_house(house, dir):
    x, y = house
    match dir:
        case "^":
            return x, y - 1
        case ">":
            return x + 1, y
        case "v":
            return x, y + 1
        case "<":
            return x - 1, y
    assert False


def route(directions):
    house = 0,0
    yield house
    for dir in directions:
        yield (house := next_house(house, dir))
    

def part1(directions):
    print(f"{directions}\n\n")
    return len(set(route(directions)))


def part2(data, ans1):
    return "ans2"


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
