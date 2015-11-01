from sys import stdin

def f(A):
    if len(A) == 0:
        return []
    A.sort()
    b = []
    for i in A:
        if not i in b:
            b.append(i)
    A = b
    res = 0
    for c in A:
        l = len(A) - 1
        for a in A:
            while (l > 0 and c ** 2 - a ** 2 < A[l] ** 2):
                l -= 1
            if (c ** 2 - a ** 2 == A[l] ** 2 and A[l] < a):
                res += 1
    return res
