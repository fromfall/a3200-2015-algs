def palin(s):
    d = []
    for i in range(len(s) + 1):
        d.append([])
        for j in range(len(s) + 1):
            d[i].append(0)
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[len(s) - j - 1]:
                d[i + 1][j + 1] = d[i][j] + 1
            elif d[i][j + 1] < d[i + 1][j]:
                d[i + 1][j + 1] = d[i + 1][j]
            else:
                d[i + 1][j + 1] = d[i][j + 1]
    res = ''
    i = len(s)
    j = len(s)
    while i > 0 and j > 0:
        if s[i - 1] == s[len(s) - j]:
            res += s[i - 1]
            i -= 1
            j -= 1
        elif d[i][j - 1] <= d[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return res
