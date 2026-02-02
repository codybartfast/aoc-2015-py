CHARS = "abcdefghijklmnopqrstuvwxyz"


def parse(text):
    return text


def to_numeric(password):
    return list([CHARS.index(char) for char in password])


def from_numeric(numbers):
    return "".join(CHARS[n] for n in numbers)


def enum_numeric_passwords(npwd):
    # This will overflow if no password is found
    idx = len(npwd) - 1
    while True:
        npwd[idx] = (npwd[idx] + 1) % len(CHARS)
        if npwd[idx] != 0:
            yield npwd
            idx = len(npwd) - 1
        else:
            idx -= 1


def happy_security_elf(illegal, npwd):
    got_asc = False
    asc_count = 0
    doubles = 0
    prev_asc = -2
    prev_dub = None
    for n in npwd:
        if n in illegal:
            return False

        if n == prev_asc + 1:
            asc_count += 1
            if asc_count == 2:
                got_asc = True
        else:
            asc_count = 0
        prev_asc = n

        if n == prev_dub:
            doubles += 1
            prev_dub = None
        else:
            prev_dub = n

    return got_asc and doubles >= 2


def find_next(password):
    illegal = to_numeric("ilo")
    npwd = to_numeric(password)
    for npwd in enum_numeric_passwords(npwd):
        if happy_security_elf(illegal, npwd):
            return from_numeric(npwd)


def part1(password):
    return find_next(password)


def part2(_, ans1=None):
    return find_next(ans1)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
