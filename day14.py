def parse(text):
    return [
        (int(parts[3]), int(parts[6]), int(parts[13]))
        for parts in [line.split() for line in text.splitlines()]
    ]


def distance(deer, duration):
    speed, sprint, rest = deer
    full = duration // (sprint + rest)
    remaindeer = duration % (sprint + rest)
    flight_time = full * sprint + min(sprint, remaindeer)
    return flight_time * speed


def award_points(reindeer, duration):
    scores = [0] * len(reindeer)
    for time in range(1, duration + 1):
        distances = [distance(deer, time) for deer in reindeer]
        max_dist = max(distances)
        for idx in range(len(distances)):
            if distances[idx] == max_dist:
                scores[idx] += 1
    return max(scores)


def part1(reindeer):
    return max(distance(deer, 2503) for deer in reindeer)


def part2(reindeer, ans1=None):
    return award_points(reindeer, 2503)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
