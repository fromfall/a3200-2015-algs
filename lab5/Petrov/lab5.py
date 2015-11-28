from random import *
from sys import stdin
a = list(map(int, stdin.readline().split()))
 
def partition(l, r):
    x = a[randint(l, r)]
    i = l
    j = r
    while 1:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            return j
           
def quickSort(l, r):
    if l < r:
        q = partition(l, r)
        quickSort(l, q)
        quickSort(q + 1, r)
    return a
   
b = quickSort(0, len(a) - 1)
 
for i in range(len(b)):
    print(b[i], end = ' ')
