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
        vals = map(self.lookup, self.args)
        return self.op(*vals)

    def value(self):
        if not self._value:
            self._value = self.calc()
        return self._value


ops = {
    "ID": lambda a: a,
    "NOT": lambda a: ~a,
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "LSHIFT": lambda a, b: a << b,
    "RSHIFT": lambda a, b: a >> b,
}


def parse(input):
    return [
        [expr.split(), wire]
        for [expr, wire] in [line.split(" -> ") for line in input.splitlines()]
    ]


def wire_board(wire_info, b_val=-1):
    board = {}
    for [parts, wire] in wire_info:
        if len(parts) == 1:
            board[wire] = Gate(board, ops["ID"], (parts[0],))
        elif len(parts) == 2:
            board[wire] = Gate(board, ops["NOT"], (parts[1],))
        else:
            [a, op, b] = parts
            board[wire] = Gate(board, ops[op], (a, b))
    return board


def part1(wire_info):
    board = wire_board(wire_info)
    return board["a"].value()


def part2(wire_info, ans1=None):
    board = wire_board(wire_info, ans1)
    board["b"] = Gate(board, ops["ID"], (str(ans1),))
    return board["a"].value()


def jingle(filename=None, filepath=None, input=None):
    import sack

    input = input if input else sack.read_input(filename, filepath)
    sack.present(input, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
