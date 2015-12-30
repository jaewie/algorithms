class Graph(object):

    def __init__(self, value):
        self.adjacecy_list = defaultdict(set)

    def add_edge(self, start, destination):
        self.adjacency_list[start].add(destination)
        self.adjacency_list[destination].add(start)

    def edges(self, node):
        return self.adjacency_list(node)

    @property
    def nodes(self):
        return self.adjacency_list.iterkeys()
