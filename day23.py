REG_PC = 0
REG_A = 1
REG_B = 2


def parse_line(line):
    reg_names = {"a": REG_A, "a,": REG_A, "b": REG_B, "b,": REG_B}
    [instr, p2, *rest] = line.split()
    match instr:
        case "jmp":
            return (instr, int(p2))
        case "jie" | "jio":
            return (instr, reg_names[p2], int(rest[0]))
        case _:
            return (instr, reg_names[p2])


def parse(text):
    return [parse_line(line) for line in text.splitlines()]


def run(program):
    regs = [0] * 3
    while regs[REG_PC] < len(program):
        instr = program[regs[REG_PC]]
        match instr:
            case ["hlf", reg]:
                regs[reg] //= 2
                regs[REG_PC] += 1
            case ["tpl", reg]:
                regs[reg] *= 3
                regs[REG_PC] += 1
            case ["inc", reg]:
                regs[reg] += 1
                regs[REG_PC] += 1
            case ["jmp", off]:
                regs[REG_PC] += off
            case ["jie", reg, off]:
                if regs[reg] % 2 == 0:
                    regs[REG_PC] += off
                else:
                    regs[REG_PC] += 1
            case ["jio", reg, off]:
                if regs[reg] == 1:
                    regs[REG_PC] += off
                else:
                    regs[REG_PC] += 1
            case _:
                raise RuntimeError(f"oops {instr}")
    return regs
                

def part1(program):
    return run(program)[REG_B]


def part2(program, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
