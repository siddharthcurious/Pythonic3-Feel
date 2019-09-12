class GraphColoring:

    def __init__(self, gmatrix, V):
        self.gmatrix = gmatrix
        self.V = V

    def __isSafe(self, v, color, c):
        for i in range(self.V):
            if self.gmatrix[v][i] == 1 and color[i] == c:
                return False
        return True

    def color_graph(self, m):
        color = [0] * self.V
        def ismColored(m, color, v):
            if v == self.V:
                return True
            for c in range(0, m):
                if self.__isSafe(v, color, c) == True:
                    color[v] = c
                    if ismColored(m, color, v+1) == True:
                        return True
                    color[v] = 0

        return ismColored(m, color, 0)

if __name__ == "__main__":

    matrix = [
        [0,1,1,0,0,0,0,0],
        [1,0,1,0,0,0,0,0],
        [1,1,0,0,1,1,0,0],
        [0,1,0,0,1,0,0,1],
        [0,1,1,1,0,0,1,0],
        [0,0,1,0,0,0,1,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,1,0,0,1,0]
    ]

    matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    m = 3
    V = 8
    gc = GraphColoring(matrix, V)
    r = gc.color_graph(m)
    if r == None:
        print("The graph is not {} colorable".format(m))
    else:
        print("This graph is {} colorable".format(m))
