def dl(a, b):
    if len(a) < len(b):
        a, b = b, a
    x = [[], [], []]
    global i_shift
    i_shift = 0
 
    def d(i, j):
        global i_shift
        if i < -1 or j < -1:
            return len(b) + len(a) + 1
        elif i == -1:
            return j + 1
        elif j == -1:
            return i + 1
 
        i -= i_shift
        return x[i][j]
 
    def d_new_line():
        global i_shift
        i_shift += 1
        x[0] = x[1]
        x[1] = x[2]
        x[2] = []
 
    def d_append(i, t):
        global i_shift
        i -= i_shift
        x[i].append(t)
 
    for i in range(len(a)):
        for j in range(len(b)):
            res = min(d(i - 1, j), d(i, j - 1)) + 1
            res = min(res, d(i - 1, j - 1) + 1)
            if a[i] == b[j]:
                res = min(res, d(i - 1, j - 1))
            if i > 0 and j > 0 and a[i - 1] == b[j] and a[i] == b[j - 1]:
                res = min(res, d(i - 2, j - 2) + 1)
            d_append(i, res)
        if i > 1:
            d_new_line()
    return d(len(a) - 1, len(b) - 1)
