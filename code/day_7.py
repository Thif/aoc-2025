import numpy as np
import pandas as pd
from functools import cache


def parse_input(input_data: str):

    m = []

    with open(input_data, "r", encoding="ascii") as file:
        for line in file:
            new_line = [c for c in line]
            if "\n" in new_line:
                new_line = [c for c in line[:-1]]
            m.append(new_line)

    return np.array(m)


def get_next_nodes(m, node):

    if int(node[0]) == 0:
        return [(int(node[0]) + 2, int(node[1]))]
    if (
        int(node[0]) == m.shape[0] - 1
        or int(node[1]) == 0
        or int(node[1]) == m.shape[1] - 1
    ):
        return []
    next_nodes = []
    array_right = m[int(node[0]) :, int(node[1]) + 1]
    array_left = m[int(node[0]) :, int(node[1]) - 1]

    match_right = np.where(array_right == "^")[0]
    match_left = np.where(array_left == "^")[0]

    if len(match_left) != 0:
        next_nodes += [(int(node[0]) + int(match_left[0]), node[1] - 1)]
    if len(match_right) != 0:
        next_nodes += [(int(node[0]) + int(match_right[0]), node[1] + 1)]
    return next_nodes


def get_network(m, start_node, net={}):

    next_nodes = get_next_nodes(m, start_node)

    if len(next_nodes) != 0:
        net[start_node] = next_nodes

        for node in get_next_nodes(m, start_node):
            if node not in net.keys():
                net = get_network(m, node, net)

    return net


def p1(m) -> int:
    m = np.append(m, [["^"] * m.shape[1]], axis=0)
    print(m)
    start_i, start_j = np.where(m == "S")
    net = get_network(m, (int(start_i), int(start_j)))

    return len(net.keys())-1 #remove first node !


def p2(m) -> int:

    # add chevron on last row to capture beams
    m = np.append(m, [["^"] * m.shape[1]], axis=0)

    start_i, start_j = np.where(m == "S")
    net = get_network(m, (int(start_i), int(start_j)))

    @cache
    def get_n_possibilities(node, start_node=False):
        print("Checking", node)

        # If the node is not in the network, return 2
        if node not in net:

            return 1

        # If the node has only one connection
        if len(net[node]) == 1:

            return get_n_possibilities(net[node][0], start_node)

        # If the node has two connections
        elif len(net[node]) == 2:

            return get_n_possibilities(net[node][0], start_node) + get_n_possibilities(
                net[node][1], start_node
            )

        # If the node has no connections, add the path to the list
        if len(net[node]) == 0:

            return 1  # Return 1 to count this path

        return 0  # Default return value

    n = get_n_possibilities((int(start_i), int(start_j)), start_node=True)

    return n


def main(input_data):

    m = parse_input(input_data)

    return p1(m.copy()), p2(m.copy())
