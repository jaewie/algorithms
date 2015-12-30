def get_shortest_path(in_nodes, start, dest):
    shortest_paths = {start: (0, [start])}

    def _get_shortest(dest, shortest_paths=shortest_paths):
        if dest not in shortest_paths:
            incoming_edges = in_nodes[dest]

            shortest_path, shortest_cost = None, None

            for in_node, cost in incoming_edges:
                # incoming shortest path cost and path
                in_cost, in_short = _get_shortest(in_node)

                if shortest_cost is None or in_cost + cost < shortest_cost:
                    shortest_path = in_short
                    shortest_cost = in_cost + cost
            shortest_paths[dest] = (shortest_cost, shortest_path + [dest])

        return shortest_paths[dest]

    return _get_shortest(dest)


def get_incoming_edges(adj_lst):
    res = {}
    for node_from, edges in adj_lst.items():
        for node_to, cost in edges:
            res[node_to] = res.get(node_to, []) + [((node_from, cost))]
    return res

if __name__ == "__main__":
    out_nodes = {'a': [('c', 3), ('b', 2)],
                 'b': [('d', 4)],
                 'c': [('e', 6), ('d', 5)],
                 'd': [('f', 2), ('g', 3)],
                 'e': [('f', 1)],
                 'f': [('h', 15)],
                 'g': [('h', 10)],
                 'h': []}

    in_nodes = get_incoming_edges(out_nodes)

    print get_shortest_path(in_nodes, 'a', 'h')
