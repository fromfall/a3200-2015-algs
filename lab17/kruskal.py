import operator
from union_find import DSU

class WeightedGraph:
    def __init__(self, vertices=0):
        self.e = []
        self.vertices = vertices

    def add_vertex(self, v):
        self.vertices += 1

    def add_directed_link(self, v1, v2, w):
        self.e.append([v1, v2, w])

    def get_links(self, v):
        res = []
        for edge in self.e:
            if edge[0] == v:
                res.append(edge)
        return res

    def min_tree(self):
        e = sorted(self.e, key=operator.itemgetter(2))
        dsu = DSU(self.vertices)
        res = WeightedGraph(self.vertices)
        for edge in e:
            if dsu.find(edge[0]) != dsu.find(edge[1]):
                dsu.unite(edge[0], edge[1])
                res.add_directed_link(edge[0], edge[1], edge[2])
        return res
