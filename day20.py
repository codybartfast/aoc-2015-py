import math


def parse(text):
    return int(text)


def find_factors(primes, known_factors, n):
    factors = known_factors.get(n, None)
    if factors:
        return factors
    factors = {1, n}
    max_factor = math.isqrt(n)
    for prime in primes:
        if prime > max_factor:
            break
        if n % prime == 0:
            factors.add(prime)
            factors |= find_factors(primes, known_factors, n // prime)
    if len(factors) == 2:
        primes.append(n)
    known_factors[n] = factors
    return factors


def part1(data):
    assert data % 10 == 0
    data //= 10
    primes = []
    known_factors = {}
    for n in range(2, 10**18):
        if sum(find_factors(primes, known_factors, n)) >= data:
            return n


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
