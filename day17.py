def parse(text):
    return tuple(sorted(map(int, (text.splitlines())), reverse=True))


def solution_count(all, idx, remaining, used_counts, used):
    if remaining == 0:
        used_counts.append(used)
        return 1

    if idx >= len(all):
        return 0

    if remaining < 0:
        return 0

    capacity = sum(all[idx:])
    if capacity < remaining:
        return 0

    count = sum(
        solution_count(all, i + 1, remaining - all[i], used_counts, used + 1)
        for i in range(idx, len(all))
    )
    return count


def part1(data):
    print(f"{data}\n\n")
    return solution_count(data, 0, 150, [], 0)


def part2(data, ans1=None):
    used_counts = []
    solution_count(data, 0, 150, used_counts, 0)
    min_used = min(used_counts)
    return used_counts.count(min_used)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
