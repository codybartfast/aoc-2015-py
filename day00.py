def parse(input):
    return input


def bells(input):
    data = parse(input)
    print(data, "\n")

    yield data

    yield None

    yield None


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
