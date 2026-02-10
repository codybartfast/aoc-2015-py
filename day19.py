import re


def parse(text):
    repl_txt, molecule = text.split("\n\n")
    replacements = {}
    for line in repl_txt.splitlines():
        parts = line.split()
        replacements.setdefault(parts[0], []).append(parts[2])
    return molecule, replacements


def replace(molecule, replacements):
    for match in re.finditer(r"[A-Z][a-z]|[A-Z]", molecule):
        prefix = molecule[: match.start()]
        suffix = molecule[match.end() :]
        for repl in replacements.get(match.group(), []):
            yield prefix + repl + suffix


def part1(data):
    return len(set(replace(*data)))


def part2(data, ans1=None):
    return "ans2"


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
