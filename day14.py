def parse(text):
    return [
        (int(parts[3]), int(parts[6]), int(parts[13]))
        for parts in [line.split() for line in text.splitlines()]
    ]

def distance(deer, time):
    speed, sprint, rest = deer
    full = time // (sprint + rest)
    rmndr = time % (sprint + rest)
    flight_time = full * sprint + min(sprint, rmndr)
    return flight_time * speed
    
def part1(reindeer):
    print(f"{reindeer}\n\n")

    return max(distance(deer, 2503) for deer in reindeer)


def part2(reindeer, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
