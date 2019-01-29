class Topological:
    def __init__(self, v, graph):
        self.v = v
        self.total_nodes = set(range(self.v))
        self.graph = graph

    def print_nodes(self):
        print(self.total_nodes)

    def indegree_zero(self):
        child_nodes = []
        for k, v in self.graph.items():
            child_nodes.extend(v)
        indegree_nodes = set(child_nodes)
        return self.total_nodes - indegree_nodes

    def outdegree_zero(self):
        parent_nodes = graph.keys()
        return self.total_nodes - parent_nodes

    def indegree(self):
        pass

    def outdegree(self):
        pass

    def topological_sorting(self):
        topological_order = []
        indegree_zero_nodes = self.indegree_zero()
        for node in indegree_zero_nodes:
            self.graph.pop(node)
        print(self.graph)


if __name__ == "__main__":

    graph = {
        0: [1, 2, 3],
        1: [4],
        2: [5],
        3: [1, 4, 5, 7, 8],
        4: [8],
        5: [6],
        6: [7, 10],
        7: [8, 9],
        8: [9],
        10: [9, 11]
    }

    v = 12
    obj = Topological(v, graph)
    obj.topological_sorting()
    obj.print_nodes()
    print(obj.indegree_zero())
    print(obj.outdegree_zero())