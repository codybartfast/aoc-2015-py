from pathlib import Path
import sys

def _day():
    filepath = sys._getframe(2).f_code.co_filename
    day = filepath[-5:-3]
    return day
 
def read_input(input_filename = None):
    if input_filename is None:
        input_filename = "input"    
    if "." not in input_filename:
        input_filename += ".txt"
    day = _day()
    input_path = Path(__file__).resolve().parent / "input" / "2025"
    input_path = input_path / f"day{day}" / f"{input_filename}"
    with open(input_path, encoding="utf-8") as f:
         input = f.read()
    return input 


def present(solver_action, title=None):
    import time
    pc_start = time.perf_counter()
    day = _day()

    if title is None:
        title = f"Day {day}"

    print()
    print(title)
    print("=" * len(title))
    print()

    solve_it=solver_action()
    
    pc_parse_before = time.perf_counter()
    next(solve_it)
    pc_parse_after = time.perf_counter()
    
    pc_part1_before = time.perf_counter()
    ans1 = next(solve_it)
    pc_part1_after = time.perf_counter()
    print(f"Part 1: {ans1}")

    pc_part2_before = time.perf_counter()
    ans2 = next(solve_it)
    pc_part2_after = time.perf_counter()
    print(f"Part 2: {ans2}")

    pc_stop = time.perf_counter()

    print()
    print("Timings")
    print("---------------------")
    print(f"  Parse: {pc_parse_after - pc_parse_before:12.6f}")
    print(f" Part 1: {pc_part1_after - pc_part1_before:12.6f}")
    print(f" Part 2: {pc_part2_after - pc_part2_before:12.6f}")
    print(f"Elapsed: {pc_stop - pc_start:12.6f}")
    print()
     
