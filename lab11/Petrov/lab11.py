from sys import stdin
#a = list(map(int, stdin.readline().split()))

def f(A):
    res = 0
    c = -1
    s = 0
    for i in range(len(A)):
        if A[i] >= c:
            res = max(res, s)
            s = 0
            c = A[i]
        else:
            s += c - A[i]
    c = -1
    s = 0
    for i in range(0, len(A), -1):
        if A[i] >= c:
            res = max(res, s)
            s = 0
            c = A[i]
        else:
            s += c - A[i]
    return res

#print(f(a))
