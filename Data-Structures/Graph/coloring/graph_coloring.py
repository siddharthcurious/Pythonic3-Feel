from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, source, dest):
        self.graph[source].append(dest)

class GraphColoring:
    def __init__(self, V):
        self.V = V

    def color_graph(self, graph):
        result = [-1] * (self.V)
        available = [True] * self.V

        for u in range(self.V):
            neigh = graph.get(u)
            if neigh:
                for e in neigh:
                    if result[e] != -1:
                        available[result[e]] = False
            color = -1
            for i in range(self.V):
                if available[i] == True:
                    color = i
                    break
            result[u] = color
            available = [True] * self.V
        print(result)

if __name__ == "__main__":

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 7)
    g.add_edge(4, 6)
    g.add_edge(5, 6)
    g.add_edge(6, 7)

    g.add_edge(1, 0)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(3, 1)
    g.add_edge(4, 1)
    g.add_edge(5, 2)
    g.add_edge(4, 2)
    g.add_edge(4, 3)
    g.add_edge(7, 3)
    g.add_edge(6, 4)
    g.add_edge(6, 5)
    g.add_edge(7, 6)

    gc = GraphColoring(8)
    gc.color_graph(g.graph)


