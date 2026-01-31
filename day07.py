MAX_INT = 1 << 16


def parse(input):
    return [
        [expr.split(), wire]
        for [expr, wire] in [line.split(" -> ") for line in input.splitlines()]
    ]


def memo(cicuit):
    values = {}

    def get(id):
        if id not in values:
            values[id] = cicuit[id]()
        return values[id]

    return get


def wire_circuit(wire_info, b_val=-1):
    circuit = {}
    memo_get = memo(circuit)

    def val_getter(txt):
        if txt.isdigit():
            val = int(txt)
            return lambda val=val: val
        else:
            return lambda id=txt: memo_get(id)

    for [parts, wire] in wire_info:
        if wire == "b" and b_val >= 0:
            circuit["b"] = lambda: b_val
            continue

        if len(parts) == 1:
            txt = parts[0]
            circuit[wire] = val_getter(txt)
        elif len(parts) == 2:
            a = parts[1]
            circuit[wire] = lambda a=a: (~circuit[a]()) % MAX_INT
        else:
            [a, op, b] = parts
            get_a, get_b = val_getter(a), val_getter(b)
            match parts[1]:
                case "AND":
                    circuit[wire] = (
                        lambda get_a=get_a, get_b=get_b: (get_a() & get_b()) % MAX_INT
                    )
                case "OR":
                    circuit[wire] = (
                        lambda get_a=get_a, get_b=get_b: (get_a() | get_b()) % MAX_INT
                    )
                case "LSHIFT":
                    circuit[wire] = (
                        lambda get_a=get_a, get_b=get_b: (get_a() << get_b()) % MAX_INT
                    )
                case "RSHIFT":
                    circuit[wire] = lambda get_a=get_a, get_b=get_b: get_a() >> get_b()
    return circuit


def part1(wire_info):
    circuit = wire_circuit(wire_info)
    return circuit["a"]()


def part2(wire_info, ans1=None):
    circuit = wire_circuit(wire_info, ans1)
    return circuit["a"]()


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
