import numpy as np


def parse_input(input_data: str):

    m = []

    with open(input_data, "r", encoding="ascii") as file:
        for line in file:
            new_line = int(line.replace("R", "").replace("L", "-"))
            m.append(new_line)
    return m


def get_positions_and_next_move(m):
    m.insert(0, 50)
    m_pos = [int(a) for a in np.abs(np.cumsum(m) % 100)]
    return list(zip(m_pos, m[1:]))


def get_zero_count(start, delta):
    end = start + delta
    trend = np.linspace(start, end, num=abs(end - start) + 1, dtype=int)
    trend = trend % 100
    trend = trend[1:]
    return (trend == 0).sum()


def p1(m) -> int:

    # calculate positions and next move for each step
    shift_m = get_positions_and_next_move(m)

    # count 0 for current position
    count = [(a == 0) for (a, b) in shift_m]

    return int(np.sum(count))


def p2(m) -> int:

    # calculate positions and next move for each step
    shift_m = get_positions_and_next_move(m)

    # count 0 for any position crossed during the move
    count = [get_zero_count(u[0], u[1]) for u in shift_m]

    return int(np.sum(count))


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy()), p2(m.copy())
