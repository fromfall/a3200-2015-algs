from sys import stdin

if __name__ == '__main__':
    n = int(input())
    num = list(map(int, stdin.readline().split()))

def solve(n, num):
    nmax = 1000003
    cur = nmax * [0]
    pt = []
    res = 0
    
    for x in range(len(num)):
        cur[num[x]] += 1
    
    for i in range(nmax - 3, 1, -1):
        for j in range((((cur[i + 1] % 2) + cur[i]) // 2)):
            pt.append(i)
        if cur[i] > 0:
            cur[i] += cur[i + 1] % 2
            
    for i in range(1, len(pt), 2):
        res += pt[i - 1] * pt[i]
    return res
    
if __name__ == '__main__':
    print(solve(n, num))
