import random
import numpy as np

n, K, E = 10, 3, 0.01
d, d0 = [], []

def comp_E(f_prev, f_cur, e):
    for i in range(len(f_prev)):
        for j in range(len(f_prev[i])):
            if abs(f_cur[i][j] - f_prev[i][j]) >= e:
                return True
    return False

def leng(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x = [random.randint(1, 100) for i in range(n)]
y = [random.randint(1, 100) for i in range(n)]
Xc = np.mean(x)
Yc = np.mean(y)
R = 0
for i in range(0, n):
    r = leng(Xc, Yc, x[i], y[i])
    if r > R:
        R = r
Xv = [R * np.cos(2 * np.pi * i / K) + Xc for i in range(K)]
Yv = [R * np.sin(2 * np.pi * i / K) + Yc for i in range(K)]
for k in range(K):
    clu = []
    for i in range(n):
        clu.append(leng(x[i], y[i], Xv[k], Yv[k]))
    d.append(clu)
for k in range(n):
    clu = []
    for i in range(K):
        sum = 0
        for j in range(K):
            sum += (d[i][k] / d[j][k]) ** (2 / (n - 1))
        clu.append(1 / sum)
    d0.append(clu)
f_prev = [[0 for i in range(K)] for j in range(n)]
f_cur = d0
count = 1
while (comp_E(f_prev, f_cur, E)):
    Xv = []
    Yv = []
    for i in range(K):
        sum = 0
        for j in range(n):
            sum += f_cur[j][i] ** n
        Xv.append((sum * x[i]) / sum)
        Yv.append((sum * y[i]) / sum)
    d = []
    for k in range(K):
        clu = []
        for i in range(n):
            clu.append(leng(x[i], y[i], Xv[k], Yv[k]))
        d.append(clu)
    d0 = []
    for k in range(n):
        clu = []
        for i in range(K):
            sum = 0
            for j in range(K):
                if d[j][k] != 0 & (n - 1) != 0:
                    sum += (d[i][k] / d[j][k]) ** (2 / (n - 1))
                if sum == 0:
                    sum = E
            clu.append(1 / sum)
        d0.append(clu)
    f_prev = f_cur
    f_cur = d0
    count += 1
print(count)
