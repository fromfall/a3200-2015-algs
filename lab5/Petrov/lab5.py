from random import *
from sys import stdin
a = list(map(int, stdin.readline().split()))
 
def quickSort(a):
    if len(a) <= 1:
        return a
    less = []
    more = []
    p = choice(a)
    for i in a:
        if i < p:
            less.append(i)
        if i > p:
            more.append(i)
    less = quickSort(less)
    more = quickSort(more)
    return less + [p] * a.count(p) + more
    
b = quickSort(a)
 
for i in range(len(b)):
    print(b[i], end = ' ')
