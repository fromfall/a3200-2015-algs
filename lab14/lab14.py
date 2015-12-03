class Graph:
    def __init__(self):
        self.vertices = {}
        self.ids = []
        self.edges = []        
   
    def add_vertex(self, v):
        self.edges.append([])
        self.ids.append(v)
        self.vertices[v] = len(self.vertices)
           
    def add_directed_link(self, v1, v2):
        v1 = self.vertices[v1]
        v2 = self.vertices[v2]
        self.edges[v1].append(v2)
           
    def dfs(self, v, res, used):
        used[v] = 1
        circle = False
        for to in self.edges[v]:
            if used[to] == 0:
                circle = circle or self.dfs(to, res, used)
            elif used[to] == 1:
                return True
        res.append(v)
        used[v] = 2
        return circle
           
    def topological_sort(self):
        used = []
        for i in range(len(self.vertices)):
            used.append(0)
        res = []
        for i in range(len(self.vertices)):
            if (used[i] == 0):
                if self.dfs(i, res, used):
                    return None
        for i in range(len(res)):
            res[i] = self.ids[res[i]]
        return res[::-1]
