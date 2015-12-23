import math
import random
 
class RMQ:
    def __init__(self, a):
        self.inf = max(a)
        self.len = 2 ** int(math.log(len(a), 2) + 1) - 1
        self.a = [self.inf] * self.len
        self.a += a
        self.a += [self.inf] * (self.len + 1 - len(a))
        for i in range(len(self.a) - 1, 0, -1):
            self.a[(i - 1) // 2] = min(self.a[(i - 1) // 2], self.a[i])
 
    def m(self, l, r):
        if l + 1 >= r:
            return min(self.a[l], self.a[r])
        res = self.inf
        if l % 2 == 0:
            res = min(res, self.a[l])
            l += 1
        if r % 2 == 1:
            res = min(res, self.a[r])
            r -= 1
        return min(res, self.m((l - 1) // 2, (r - 1) // 2))
 
 
    def min(self, l, r):
        return self.m(l + self.len, r + self.len)
 
class LCA:
    def __init__(self, g, r):
        a = []
        mn = [3 * len(g) for i in range(len(g))]
        mx = [-1 for i in range(len(g))]
        def dfs(v, d):
            mx[v] = len(a)
            mn[v] = mx[v]
            a.append((d, v))
            for u in g[v]:
                if mx[u] == -1:
                    dfs(u, d + 1)
                    mx[v] = len(a)
                    a.append((d, v))
        dfs(r, 0)
        self.rmq = RMQ(a)
        self.mn = mn
        self.mx = mx
    def lca(self, v1, v2):
        if self.mn[v1] < self.mx[v2]:
            return self.rmq.min(self.mn[v1], self.mx[v2])[1]
        else:
            return self.rmq.min(self.mn[v2], self.mx[v1])[1]        
