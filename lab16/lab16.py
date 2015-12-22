import heapq
 
class WeightedGraph:
    def __init__(self):
        self.g = []
        self.v_to_id = {}
        self.id_to_v = []
 
    def add_vertex(self, v):
        self.g.append([])
        self.v_to_id[v] = len(self.v_to_id)
        self.id_to_v.append(v)
 
    def add_direct_link(self, v1, v2, weight):
        v1 = self.v_to_id[v1]
        v2 = self.v_to_id[v2]
        self.g[v1].append((v2, weight))
 
    def paths(self, v):
        v = self.v_to_id[v]
        d = []
        f = []
        for i in range(len(self.g)):
            d.append(1000000000000000000)
            f.append(True)
        d[v] = 0
        q = []
        heapq.heappush(q, (0, v))
        while len(q) > 0:
            _, a = heapq.heappop(q)
            if f[a] == False:
                continue;
            f[a] = False
            for b, ab in self.g[a]:
                if d[b] > d[a] + ab:
                    d[b] = d[a] + ab
                    heapq.heappush(q, (d[b], b))
        res = {}
        for i in range(len(d)):
            res[self.id_to_v[i]] = d[i]
        return res
