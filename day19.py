import re


def parse(text):
    elem_rx = re.compile(r"[A-Z][a-z]|[A-Z]")
    repl_txt, molecule = text.split("\n\n")
    replacements = {}
    for line in repl_txt.splitlines():
        parts = line.split()
        replacements.setdefault(parts[0], []).append(elem_rx.findall(parts[2]))
    return elem_rx.findall(molecule), replacements


def replace_all(molecule, replacements):
    return (
        "".join(molecule[:idx] + repl + molecule[idx + 1 :])
        for idx in range(len(molecule))
        for repl in replacements.get(molecule[idx], [])
    )


def part1(data):
    return len(set(replace_all(*data)))


def part2(data, ans1=None):
    med, _ = data
    remaining = len(med)
    steps = 0

    n_ar = med.count("Ar")
    remaining -= 3 * n_ar
    steps += n_ar

    remaining -= 2 * med.count("Y")

    return steps + remaining - 1


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
