# Day 20
# ======
#
# Part 1: 786240
# Part 2: 831600
#
# Timings
# ---------------------
#   Parse:     0.000001
#  Part 1:     0.901876
#  Part 2:     0.240317
# Elapsed:     1.142269
#
# Originally did Part 1 with factorisation but Part 2 method is about 3x faster


def parse(text):
    return int(text)


def deliver(reqd_presents, present_factor, max_deliveries, n_houses):
    houses = [0] * n_houses
    max_house = n_houses
    elf = 1
    while elf < max_house:
        deliveries = max_deliveries
        house = elf
        while house < max_house and deliveries:
            houses[house] = (presents := (houses[house] + present_factor * elf))
            if presents >= reqd_presents and house < max_house:
                max_house = house
            house += elf
            deliveries -= 1
        elf += 1
    return max_house


def part1(reqd_presents):
    return deliver(reqd_presents, 10, 1 << 20, 1 << 20)


def part2(reqd_presents, ans1=None):
    return deliver(reqd_presents, 11, 50, 1 << 20)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
