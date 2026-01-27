def parse(input):
    return input



def bells(input):
    data = parse(input)
    print("[", data, "]", "\n")

    yield data

    open_parens = sum(1 for char in data if char == "(")

    yield open_parens - (len(data) - open_parens)

    floor = 0
    for idx, char in enumerate(data):
        floor += 1 if char == "(" else -1
        if floor == -1:
            yield idx + 1

    yield None


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
