class Gate:
    def __init__(self, spec):
        self.spec = spec
        self.value = None


def parse(input):
    return {
        out_wire: Gate(expr.split())
        for [expr, out_wire] in [line.split(" -> ") for line in input.splitlines()]
    }


def output(device, operand):
    if operand.isdigit():
        return int(operand)

    gate = device[operand]
    if gate.value is not None:
        return gate.value

    match gate.spec:
        case [wire_id]:
            gate.value = output(device, wire_id)
        case ["NOT", a]:
            gate.value = ~ output(device, a)
        case [a, "AND", b]:
            gate.value = output(device, a) & output(device, b)
        case [a, "OR", b]:
            gate.value = output(device, a) | output(device, b)
        case [a, "LSHIFT", b]:
            gate.value = output(device, a) << output(device, b)
        case [a, "RSHIFT", b]:
            gate.value = output(device, a) >> output(device, b)
    return gate.value


def part1(device):
    return output(device, "a")


def part2(device, ans1=None):
    for gate in device.values():
        gate.value = None
    device["b"].spec = [str(ans1)]
    return output(device, "a")


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
