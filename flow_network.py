from copy import deepcopy
from search import breadthFirstSearch


class FlowNetwork:

    def __init__(self, graph):
        self.G = graph
        self.Gf = deepcopy(graph)
        self.flow = 0

    def augment(self, P):
        vs, bottle_neck = P
        for i in range(len(vs) - 1):
            if vs[i + 1] in self.G.edges_dict[vs[i]]:
                edge = self.G.edges_dict[vs[i]][vs[i + 1]]
                edge.f += bottle_neck
            else:
                edge = self.G.edges_dict[vs[i + 1]][vs[i]]
                edge.f -= bottle_neck
        self.flow += bottle_neck

    def augmentingPath(self, method=breadthFirstSearch):
        vs = method(self.Gf)
        if vs == None:
            return None
        bottle_neck = float('inf')
        # print vs
        for i in range(len(vs) - 1):
            c = self.Gf.edges_dict[vs[i]][vs[i + 1]].c
            if bottle_neck > c:
                bottle_neck = c
        if bottle_neck == 0:
            return "augmentingPath found a null path"
        return vs, bottle_neck

    def updateResidualGraph(self):
        for v1, v1_dict in self.G.edges_dict.iteritems():
            for v2, ge in v1_dict.iteritems():
                fe = self.Gf.edges_dict[v1][v2]
                if v1 in self.Gf.edges_dict[v2]:
                    be = self.Gf.edges_dict[v2][v1]
                else:
                    be = self.Gf.edges_dict[v2][v1]
                    be.set(v2, v1)
                fe.c = ge.c - ge.f
                be.c = ge.f

    def fordFulkerson(self):
        Path = self.augmentingPath()
        while Path:
            self.augment(Path)
            self.updateResidualGraph()
            Path = self.augmentingPath()
        return self.flow
