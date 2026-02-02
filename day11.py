CHARS = "abcdefghjkmnpqrstuvwxyz"


def parse(text):
    return text


def to_nums(password):
    return list([CHARS.index(char) for char in password])


def from_nums(numbers):
    return "".join(CHARS[n] for n in numbers)


def enum_nums(nums):
    idx = len(nums) - 1
    while True:
        nums[idx] = (nums[idx] + 1) % len(CHARS)
        if nums[idx] != 0:
            yield nums
            idx = len(nums) - 1
        else:
            idx -= 1


def happy_security_elf(nums):
    got_asc = False
    asc_count = 0
    doubles = 0
    prev_asc = -2
    prev_dub = None
    for n in nums:
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
    nums = to_nums(password)
    for ns in enum_nums(nums):
        if happy_security_elf(ns):
            return from_nums(ns)


def part1(data):
    return find_next(data)


def part2(data, ans1=None):
    return find_next(ans1)



def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
