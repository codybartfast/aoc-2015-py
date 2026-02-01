def parse(text):
    routes = {
        (parts[0], parts[2]): int(parts[4])
        for parts in map(str.split, text.splitlines())
    }
    returns = {
        (end, start): distance for (start, end), distance in routes.items()
    }
    return routes | returns


def locations(routes):
    return set(key[0] for key in routes)
    

def permutations(locations):
    if len(locations) == 1:
        yield list(locations)
    for loc in locations:
        for perm in permutations(locations - {loc}):
            yield [loc] + perm


def route_length(distances, route):
    return sum(distances[leg] for leg in zip(route, route[1:]))
    

def part1(distances):
    locs = locations(distances)
    routes = permutations(locs)
    return min(route_length(distances, route) for route in routes)


def part2(distances, ans1=None):
    locs = locations(distances)
    routes = permutations(locs)
    return max(route_length(distances, route) for route in routes)



def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
