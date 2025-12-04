import itertools
import re
import numpy as np
import time
from functools import cache


def parse_input(input_data: str):

    m = []

    with open(input_data, "r") as file:
        for line in file:
            if "\n" in line:
                l = [c for c in line[:-1]]
            else:
                l = [c for c in line]

            m.append(l)

    return np.array(m)


def p1(m) -> int:
    max_i, max_j = m.shape[0], m.shape[1]
    m_final = m.copy()
    total = 0
    for i in range(max_i):
        for j in range(max_j):
            if m[i, j] == "@":
                count = 0
                for di, dj in [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, 1),
                    (1, 0),
                    (1, -1),
                ]:
                    if (i == 0) and (di == -1):
                        continue
                    if (j == 0) and (dj == -1):
                        continue
                    if (i == max_i - 1) and (di == 1):
                        continue
                    if (j == max_j - 1) and (dj == 1):
                        continue
                    # print(i,j,di,dj)
                    n_m = m[i + di, j + dj]

                    if n_m == "@":
                        count += 1
                        # print(i,j,di,dj)
                if count < 4:
                    m_final[i, j] = "."
                    total += 1

    return total, m_final


def p2(m) -> int:
    init_count = len([c for c in m.flatten() if c == "@"])
    current_count = init_count
    for i in range(10000):
        _, m = p1(m)
        print(current_count)

        new_count = len([c for c in m.flatten() if c == "@"])
        if new_count == current_count:
            break

        current_count = len([c for c in m.flatten() if c == "@"])

    return init_count - current_count


def main(input_data):

    m = parse_input(input_data)
    print(m)
    p1_result = p1(m.copy())

    p2_result = p2(m.copy())

    return p1_result, p2_result
