from collections import defaultdict
from edge import Edge


class Graph:

    def __init__(self, number_of_vertices, edges_list=None):
        self.number_of_vertices = number_of_vertices
        self.edges_dict = self.listToDict(edges_list)
        self.s = 0
        self.t = number_of_vertices - 1

    def listToDict(self, list):
        a = defaultdict((lambda: defaultdict((lambda: Edge()))))
        for edge in list:
            (i, j, c) = edge
            a[i][j].set(i, j, c, 0)
        return a

    def getSuccessors(self, v):
        return filter((lambda x: self.edges_dict[v][x].c > 0), self.edges_dict[v].keys())

    def isGoalState(self, s):
        return self.t == s

    def print_edges(self):
        for v1, v1_dict in self.edges_dict.iteritems():
            for v2, edge in v1_dict.iteritems():
                edge.print_state()
