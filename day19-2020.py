# This is a recreation of solution I originally wrote in 2020 in F#
# https://git.sr.ht/~codybartfast/aoc15/tree/main/item/Day19.fs
#
# Because the main solution feels a bit of "cheat" (just counting 'Ar's and
# 'Y's) I thought I'd try a more general solution.  I remembered this problem
# which usually means I sweated some blood on the original solution.

import re


def parse(text):
    elem_rx = re.compile(r"[A-Z][a-z]|[A-Z]")
    repl_txt, molecule = text.split("\n\n")
    replacements = {}
    for line in repl_txt.splitlines():
        parts = line.split()
        replacements.setdefault(parts[0], []).append(tuple(elem_rx.findall(parts[2])))
    return tuple(elem_rx.findall(molecule)), replacements


# let altheads right =
#     let replace n =
#         let right' = List.skip n right
#         lookup (List.take n right)
#         |>  List.map ((fun sub -> combine sub right'))
#     match right with
#     | [] -> Seq.empty
#     | [_] -> replace 1 |> List.toSeq
#     | _ -> Seq.concat [replace 1; replace 2]


def alt_heads(replacements, right):
    if not right:
        return
    el, rest = right[0], right[1:]
    for sub in replacements.get(el, ()):
        yield sub + rest


# let splits list =
#     let rec iter left right = seq {
#         yield left, right
#         match right with [] -> () | a::right -> yield! iter (a::left) right }
#     iter [] list


def splits(molecule):
    for i in range(len(molecule)):
        yield (molecule[:i], molecule[i:])


# let allchildren =
#     splits >> Seq.collect (fun (l, r) -> r |> altheads |> Seq.map (combine l))


def all_children(replacements, molecule):
    for left, right in splits(molecule):
        yield from (
            tuple(left + alt_head) for alt_head in alt_heads(replacements, right)
        )


# let nextsources ((tlen, target), source) = seq{
#     match target, source with
#     | [], _ | _, [] -> ()
#     | t::ts, s::ss ->
#         if t = s then
#             yield (tlen - 1, ts), ss
#         yield! source |> altheads |> Seq.map (fun src -> (tlen, target), src) }


def next_sources(replacements, source):
    target, molecule = source
    if not target or not molecule:
        return
    [t, *ts] = target
    [m, *ms] = molecule
    if t == m:
        yield ts, ms
    yield from ((target, mole) for mole in alt_heads(replacements, molecule))


# let sort =
#     Seq.distinct >> Seq.groupBy (fst>>fst) >> Seq.sortBy fst >> Seq.collect snd


def _sort(sources):
    sources = tuple(sources)
    for source in sources:
        print(source)
    return sorted(set(sources), key=lambda targ_mole: len(targ_mole[0]))


# let fabricate molecule source maxtrials =
#     let rec fab steps sources =
#         let next = sources |> Seq.collect nextsources
#         let sorted = next |> sort |> Seq.truncate maxtrials |> Seq.toList
#         match sorted with
#         | ((0,_),_)::_ -> steps
#         | _ -> fab (steps + 1) sorted
#     let len = List.length molecule
#     fab 1 [((len, molecule), source)]
#     |> (fun steps -> steps - len)


def fabricate(replacements, molecule, source, max_trials):
    def fab(steps, sources):
        # print(f"FAB!  sources:{sources}")
        nexts = (
            next for source in sources for next in next_sources(replacements, source)
        )
        sorted_sources = tuple(_sort(nexts)[:max_trials])
        # print("SORTED_SOURCES:", sorted_sources)
        match sorted_sources:
            case (((), _), *_):
                return steps
            case _:
                fab(steps + 1, sorted_sources)

    return fab(1, ((molecule, source),))


def part1(data):
    medicine, replacements = data
    return len(set(all_children(replacements, medicine)))


def part2(data, ans1=None):
    medicine, replacements = data
    return fabricate(replacements, medicine, ("e",), 100)


def jingle(filename=None, filepath=None, text=None):
    import sack

    text = text if text else sack.read_input(filename, filepath)
    sack.present(text, parse, part1, part2)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    jingle(filename=filename)
