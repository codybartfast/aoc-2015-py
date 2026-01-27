def apply(instrs):
    floor = 0
    for instr in instrs:
        floor += 1 if instr == "(" else -1
        yield floor


def bells(instrs):
    yield "Just for timing"

    floors = list(apply(instrs))

    yield floors[-1]
    yield floors.index(-1) + 1


def jingle(input_filename=None):
    import sack

    input = sack.read_input(input_filename)
    sack.present(lambda: bells(input))


if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(input_filename)
