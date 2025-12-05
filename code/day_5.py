import numpy as np


def parse_input(input_data: str):

    m_1 = []
    m_2 = []

    with open(input_data, "r") as file:
        first = True

        for line in file:
            if line == "\n":
                first = False

            v = line.replace("\n", "")
            if v == "":
                continue
            if first:
                m_1.append(line.replace("\n", ""))
            else:
                m_2.append(int(line.replace("\n", "")))

    return np.array(m_1), np.array(m_2)


def p1(m1, m2) -> int:

    fresh_id = []
    count = 0
    for v in m1:
        v1, v2 = int(v.split("-")[0]), int(v.split("-")[1])
        fresh_id += [(v1, v2)]

    for v in m2:
        for p in fresh_id:
            if p[0] <= v <= p[1]:
                count += 1
                break

    return count


def p2(m1, m2) -> int:

    fresh_id = []
    count = 0
    for v in m1:

        v1, v2 = int(v.split("-")[0]), int(v.split("-")[1])
        fresh_id += [(v1, v2)]

    fresh_id_sorted = sorted(fresh_id, key=lambda x: x[0])

    new_fresh = []
    to_be_added = fresh_id_sorted[0]

    for t in fresh_id_sorted:

        if (t[0] <= to_be_added[1]) and (t[1] > to_be_added[1]):
            to_be_added = (to_be_added[0], t[1])
            continue
        if t[0] > to_be_added[1]:
            new_fresh += [to_be_added]
            to_be_added = t

    new_fresh += [to_be_added]

    count = 0

    for v in new_fresh:
        count += v[1] - v[0] + 1

    return count


def main(input_data):

    m1, m2 = parse_input(input_data)

    p1_result = p1(m1.copy(), m2.copy())

    p2_result = p2(m1.copy(), m2.copy())

    return p1_result, p2_result
