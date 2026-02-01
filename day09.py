def parse(text):
    routes = {}
    for [start, _, end, _, dist] in map(str.split, text.splitlines()):
        routes[(start, end)] = int(dist)
        routes[(end, start)] = int(dist)
    return routes


def perms(locations):
    if len(locations) == 1:
        yield list(locations)
    for loc in locations:
        for perm in perms(locations - {loc}):
            yield [loc] + perm


def route_length(distances, route):
    return sum(distances[leg] for leg in zip(route, route[1:]))


def all_lengths(distances):
    locations = set(key[0] for key in distances)
    return (route_length(distances, route) for route in perms(locations))


def part1(distances):
    return min(all_lengths(distances))


def part2(distances, ans1=None):
    return max(all_lengths(distances))


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
