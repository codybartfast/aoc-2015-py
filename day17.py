def parse(text):
    return tuple(sorted(map(int, (text.splitlines())), reverse=True))


def solution_count(all, idx, remaining, known):
    if remaining == 0:
        return 1

    if idx >= len(all):
        return 0

    if remaining < 0:
        return 0

    key = (remaining, idx)
    if key in known:
        return known[key]

    def remember(count):
        known[key] = count
        return count

    capacity = sum(all[idx:])
    if capacity < remaining:
        return remember(0)

    count = sum(
        solution_count(all, i + 1, remaining - all[i], known)
        for i in range(idx, len(all))
    )
    return remember(count)


def part1(data):
    print(f"{data}\n\n")
    return solution_count(data, 0, 150, {})


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
