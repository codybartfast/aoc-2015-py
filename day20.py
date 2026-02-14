import math


def parse(text):
    return int(text)


def find_factors(primes, known_factors, use_count, n):
    factors = known_factors.get(n, None)
    if not factors:
        factors = {1, n}
        max_factor = math.isqrt(n)
        for prime in primes:
            if prime > max_factor:
                break
            if n % prime == 0:
                factors.add(prime)
                factors |= find_factors(primes, known_factors, use_count, n // prime)
        if len(factors) == 2:
            primes.append(n)
        known_factors[n] = factors
    for factor in factors:
        use_count[factor] = use_count.get(factor, 0) + 1
    return factors


def part1(data):
    primes = []
    known_factors = {}
    use_count = {}
    for n in range(2, 10**18):
        if 10 * sum(find_factors(primes, known_factors, use_count, n)) >= data:
            return n


def part2(data, ans1=None):
    houses = [0] * data
    happy_house = 10**18
    elf = 1
    while elf < min(data, happy_house):
        for house in range(elf, min(data, elf + elf * 50), elf):
            present_count = houses[house] + 11 * elf
            if present_count >= data:
                happy_house = min(happy_house, house)
            houses[house] += 11 * elf
        elf += 1
    return happy_house


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
