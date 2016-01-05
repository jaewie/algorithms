from copy import deepcopy
from graph import Graph
from collection.priority_queue import PriorityQueue


def kruskals(adj_list):
    '''Return a minimum spanning tree of adj_list using Kruskal's algo.'''

    adj_list = deepcopy(adj_list)  # Since we need to modify adj_list
    expected_mst_edges = (len(adj_list.keys()) - 1) * 2
    mst = {k: [] for k in adj_list}
    for node in adj_list:
        adj_list[node].sort(key=lambda x: x[1])  # Sort by weight edge

    while get_edge_num(mst) < expected_mst_edges:
        min_edge = get_min_weight_edge(adj_list)
        first_node = min_edge[0]
        sec_node = min_edge[1]
        weight = min_edge[2]

        if not does_create_cycle(mst, min_edge):  # Then include edge in MST
            edge_first_node = (sec_node, weight)
            edge_sec_node = (first_node, weight)
            mst[first_node].append(edge_first_node)
            mst[sec_node].append(edge_sec_node)

        del adj_list[first_node][0]
        del adj_list[sec_node][0]
    return mst


def get_min_weight_edge(adj_list):
    '''Return the edge with minimum weight in adj_list.'''

    min_edge = None
    for key in adj_list:
        if adj_list[key]:  # If this node has edges
            cur_edge = [key] + list(adj_list[key][0])
            if min_edge is None:
                min_edge = [key] + list(cur_edge)
        min_edge = min(min_edge, cur_edge, key=lambda x: x[2])
    return min_edge


def does_create_cycle(adj_list, edge):
    '''Return whether edge creates a cycle in adj_list.'''

    return is_connected(adj_list, edge[0]) and is_connected(adj_list, edge[1])


def is_connected(adj_list, node):
    ''' Return whether there is an edge in adj_list connected to node.'''

    return any(node in adj_list[key] for key in adj_list)


def get_edge_num(adj_list):
    ''' Return the total number of edges in the graph (adj_list).'''

    return sum((len(v) for k, v in adj_list.iteritems()))


def prims(adj_list):
    '''Return a minimum spanning tree of adj_list using Prim's algo.'''

    adj_list = deepcopy(adj_list)  # Since we need to modify adj_list
    expected_mst_edges = (len(adj_list.keys()) - 1) * 2
    mst = {adj_list.iterkeys().next(): []}  # Choose any one node
    for node in adj_list:
        adj_list[node].sort(key=lambda x: x[1])  # Sort by weight edge

    while get_edge_num(mst) < expected_mst_edges:
        copy = {}

        for node in mst:  # Get the minimum edge among nodes in mst
            copy[node] = adj_list[node]
        min_edge = get_min_weight_edge(copy)

        first_node = min_edge[0]
        sec_node = min_edge[1]
        weight = min_edge[2]
        if not does_create_cycle(mst, min_edge):  # Then include edge in MST
            edge_first_node = (sec_node, weight)
            edge_sec_node = (first_node, weight)
            mst[first_node] = mst.get(first_node, []) + [(edge_first_node)]
            mst[sec_node] = mst.get(sec_node, []) + [(edge_sec_node)]
        adj_list[first_node].remove((sec_node, weight))
        adj_list[sec_node].remove((first_node, weight))
    return mst


def a_star(start, end, coords):
    '''Return the shortest route from start coord to end coord using A*
    algorithm'''

    coords = deepcopy(coords)  # Since we have to modify the coordinates
    start = deepcopy(start)
    start["g_score"], start["h_score"], start["f_score"] = 0, 0, 0
    start["prev"] = []
    visited = []
    to_discover = [start]

    while to_discover:
        cur_node = get_min_fscore_coord(to_discover)
        to_discover.remove(cur_node)
        is_end = cur_node["is_end"]
        x, y = cur_node['x'], cur_node['y']

        if is_end:  # Found finishing node
            return cur_node["prev"] + [(x, y)]

        to_discover += get_valid_neighbors(cur_node, end, coords, visited)
        visited += [(x, y)]
    return None


def get_min_fscore_coord(to_discover):
    '''Return the coord with minimum f score in list to_discover '''

    f_score = min(coord['f_score'] for coord in to_discover)

    for coord in to_discover:
        if coord['f_score'] == f_score:
            return coord
    return None


def get_valid_neighbors(cur_node, end, coords, visited):
    ''' Return list of valid neighbors for cur_node.'''

    x, y = cur_node['x'], cur_node['y']
    is_wall = cur_node["is_wall"]
    valid_neighbors = []

    to_check = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for c in to_check:
        if is_in_board_and_not_visited(c, coords, visited):
            coord = get_coord(c, coords)
            coord['prev'] = cur_node['prev'] + [(x, y)]
            update_scores(coord, cur_node, end)
            valid_neighbors += [coord]
    return valid_neighbors


def is_in_board_and_not_visited(coord, coords, visited):
    '''Return if coord is inside the board, not a wall, and was not visited.'''

    viable_coords = [(c['x'], c['y']) for c in coords if not c["is_wall"]]
    return coord in viable_coords and coord not in visited


def get_coord(c, coordinates):
    '''Return the dictionary coord for tuple c inside coordinates.'''

    for coord in coordinates:
        if coord['x'] == c[0] and coord['y'] == c[1]:
            return coord
    return None


def calculate_hscore(cur_node, end_node):
    '''Return the h score of cur_node.'''

    x_dist = abs(cur_node['x'] - end_node['x'])
    y_dist = abs(cur_node['y'] - end_node['y'])
    return x_dist + y_dist


def update_scores(coord, visiting_coord, end_node):
    '''Update h score for coord.'''

    coord['g_score'] = visiting_coord['g_score'] + 1
    coord['h_score'] = calculate_hscore(coord, end_node)
    coord['f_score'] = coord['g_score'] + coord['h_score']


def topological_sort(prereq_task):
    def get_task_prereq(prereq_task):
        task_prereq = {c: [] for c in prereq_task}

        for prereq, rely_prereq in prereq_task.iteritems():
            for task in rely_prereq:
                task_prereq[task].append(prereq)

        return task_prereq

    task_prereq = get_task_prereq(prereq_task)

    todo = [c for c, deps in task_prereq.iteritems() if not deps]
    order = []

    while todo:
        prereq = todo.pop()
        order.append(prereq)

        for t in prereq_task[prereq]:  # These tasks rely on pre-req

            task_prereq[t].remove(prereq)

            if not task_prereq[t]:
                todo.append(t)
    return order


def shortest_paths(graph, start):
    # Dijkstra's algorithm for single source shortest paths
    # O(|V| log |V| + |E| log |V|)
    paths = {node: None for node in graph}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = PriorityQueue()
    for node in graph:
        if node == start:
            pq.put(node, 0)
        else:
            pq.put(node, float('inf'))

    while not pq.empty():
        node, distance = pq.get()

        for neighbour, edge_cost in graph[node]:
            new_cost = distance + edge_cost

            if new_cost < distances[neighbour]:
                distances[neighbour] = new_cost
                paths[neighbour] = node

                pq.update(neighbour, new_cost)


    return paths, distances
