def parse_input(input_data: str):

    m = []

    with open(input_data, "r", encoding="ascii") as file:
        for line in file:
            new_line = line.split(",")
            if "\n" in new_line:
                new_line.remove("\n")
            m.append(new_line)

    return [item for sublist in m for item in sublist]


def check_simetry(a: str) -> bool:
    if len(a) % 2 == 1:
        return False
    if a[0] == "0":
        return False
    if a[: len(a) // 2] == a[len(a) // 2 :]:
        return True
    return False


def check_repeated_pattern(a: str) -> bool:
    half_len = len(a) // 2
    for i in range(1, half_len + 1):

        block = a[:i]

        for r in range(1, len(a) // len(block) + 1):
            if block * r == a:
                print("detected", a, block, r)
                return True

    return False


def p1(m) -> int:

    count = []
    for pair in m:

        start = int(pair.split("-")[0])
        end = int(pair.split("-")[1])
        for i in range(int(start), int(end) + 1):
            if check_simetry(str(i)):
                count.append(i)

    return sum(count)


def p2(m) -> int:

    count = []
    for pair in m:

        start = int(pair.split("-")[0])
        end = int(pair.split("-")[1])
        for i in range(int(start), int(end) + 1):
            if check_repeated_pattern(str(i)):
                count.append(i)

    return sum(count)


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy()), p2(m.copy())
