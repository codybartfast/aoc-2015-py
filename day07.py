MAX_INT = 1 << 16


class Gate:
    def __init__(self, board, op, args):
        self.board = board
        self.op = op
        self.args = args
        self._value = None

    def lookup(self, operand):
        if operand.isdigit():
            return int(operand)
        return self.board[operand].value()

    def calc(self):
        vals = tuple(map(self.lookup, self.args))
        return self.op(*vals)

    def value(self):
        if not self._value:
            self._value = self.calc()
        return self._value


def parse(input):
    return [
        [expr.split(), wire]
        for [expr, wire] in [line.split(" -> ") for line in input.splitlines()]
    ]


ops = {
    "ID": lambda a: a,
    "NOT": lambda a: (~a) % MAX_INT,
    "AND": lambda a, b: (a & b) % MAX_INT,
    "OR": lambda a, b: (a | b) % MAX_INT,
    "LSHIFT": lambda a, b: (a << b) % MAX_INT,
    "RSHIFT": lambda a, b: (a >> b) % MAX_INT,
}


def wire_board(wire_info, b_val=-1):
    board = {}

    for [parts, wire] in wire_info:
        if wire == "b" and b_val >= 0:
            board["b"] = Gate(board, ops["ID"], (str(b_val),))
            continue

        if len(parts) == 1:
            txt = parts[0]
            board[wire] = Gate(board, ops["ID"], (txt,))
        elif len(parts) == 2:
            a = parts[1]
            board[wire] = Gate(board, ops["NOT"], (a,))
        else:
            [a, op, b] = parts
            board[wire] = Gate(board, ops[op], (a, b))

    return board


def part1(wire_info):
    board = wire_board(wire_info)
    return board["a"].value()


def part2(wire_info, ans1=None):
    board = wire_board(wire_info, ans1)
    return board["a"].value()


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
