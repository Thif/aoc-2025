import numpy as np
import pandas as pd


def parse_input(input_data: str, prob=1):

    m = []

    with open(input_data, "r") as file:

        if prob == 1:
            for line in file:
                elements = [
                    c.replace("\n", "")
                    for c in line.split(" ")
                    if c != "\n" and c != ""
                ]

                m.append(elements)
        if prob == 2:
            for line in file:
                elements = [c for c in line if c != "\n"]
                m.append(elements)

                # Pad the last row with spaces
                m[-1] += [" "] * (len(m[0]) - len(m[-1]))

    return np.array(m)


def p1(m) -> int:

    mt = m.T
    values = mt[:, : mt.shape[1] - 1]
    signs = mt[:, mt.shape[1] - 1]

    grand_tot = 0
    for v, s in zip(values, signs):
        tot = 0 if s == "+" else 1
        for vi in v:
            if s == "*":
                tot *= int(vi)
            elif s == "+":
                tot += int(vi)

        grand_tot += tot

    return grand_tot


def fill_signs(m):

    df = pd.DataFrame(m)
    df.iloc[:, -1] = df.iloc[:, -1].replace(" ", np.nan).bfill()
    return df.to_numpy()


def p2(m) -> int:

    m = np.rot90(m)
    m = fill_signs(m)

    sums = []
    first_value = True
    for v in m:
        val = "".join(
            [vi for vi in v if vi != "" and vi != "+" and vi != "*" and vi != " "]
        )

        if val == "":
            first_value = True
            sums += [current_sum]
            continue

        if "+" in v:
            current_sign = "+"
            if first_value:
                current_sum = 0

        if "*" in v:
            current_sign = "*"
            if first_value:
                current_sum = 1

        if current_sign == "+":
            current_sum += int(val)
            first_value = False
        else:
            current_sum *= int(val)
            first_value = False

    sums += [current_sum]
    return sum(sums)


def main(input_data):

    m = parse_input(input_data, 1)

    return p1(m.copy()), p2(m.copy())
