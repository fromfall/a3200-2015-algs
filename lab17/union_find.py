from random import randint


class DSU:
    def __init__(self, size = 0):
        self.p = []
        for i in range(size):
            self.p.append(i)

    def append(self):
        self.p.append(len(self.p))

    def find(self, v):
        if v == self.p[v]:
            return v
        else:
            self.p[v] = self.find(self.p[v])
            return self.p[v]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if randint(0, 1) == 0:
            a, b = b, a
        if a != b:
            self.p[a] = b
