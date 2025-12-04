import itertools
import re
import numpy as np
import time
from functools import cache


def parse_input(input_data: str):

    m = []

    with open(input_data, "r", encoding="ascii") as file:
        for line in file:
            new_line = line
            if "\n" in new_line:
                new_line = new_line[:-1]
            m.append(new_line)

    return m


@cache
def get_max(s, l):

    if l == 1:
        return str(np.max([int(c) for c in s]))

    current_max = np.max([int(c) for c in s[: -l + 1]])
    index_max = s[: -l + 1].index(str(current_max))

    return "".join(str(current_max) + get_max(s[index_max + 1 :], l - 1))


def p1(m) -> int:
    sol = 0
    for seq in m:
        sol += int(get_max(seq, 2))

    return sol


def p2(m) -> int:
    sol = 0
    for seq in m:
        sol += int(get_max(seq, 12))

    return sol


def main(input_data):
    t0 = time.perf_counter()
    m = parse_input(input_data)
    p1_result = p1(m.copy())
    t1 = time.perf_counter()
    p2_result = p2(m.copy())
    t2 = time.perf_counter()

    print(f"Day 3 ({input_data}) - Part 1: {p1_result} in {t1-t0:.6f}s")
    print(f"Day 3 ({input_data}) - Part 2: {p2_result} in {t2-t1:.6f}s")
    return p1_result, p2_result
