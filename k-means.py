import matplotlib.pyplot as plt
import numpy as num

k, n = 500,5
x = [num.random.randint(1, k) for i in range(n)]
y = [num.random.randint(1, k) for i in range(n)]
x_c = num.mean(x)
y_c = num.mean(y)

def len(x1, y1, x2, y2):
    return num.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

def dot_and_clu(x, y, x_cc, y_cc, l):
    clu = []
    for i in range(0, n):
        dist = len(x[i], y[i], x_cc[0], y_cc[0])
        c = 0
        for j in range(0, l):
            if len(x[i], y[i], x_cc[j], y_cc[j]) < dist:
                dist = len(x[i], y[i], x_cc[j], y_cc[j])
                c = j
        clu.append(c)
    return clu

def k_means(l):
    R = 0
    for i in range(0, n):
        d = len(x_c, y_c, x[i], y[i])
        if d > R:
            R = d
    x_cc = [R * num.cos(2 * num.pi * i / l) + x_c for i in range(l)]
    y_cc = [R * num.sin(2 * num.pi * i / l) + y_c for i in range(l)]
    cluster = dot_and_clu(x, y, x_cc, y_cc, l)
    dist_s = 0
    for i in range(0, n):
        sum = 0
        for k_count in range(0, l):
            if cluster[i] == k_count:
                sum += pow((x_cc[k_count] - x[i]), 2)
        dist_s += sum
    return dist_s

dist_s = []
opt_k_count = 1
min_k_count = 2
max_k_count = 8
for i in range(min_k_count, max_k_count):
    dist_s.append(k_means(i))
min_sum = dist_s[0]
for i in range(0, max_k_count-min_k_count):
    if (dist_s[i] < min_sum):
        min_sum = dist_s[i]
        opt_k_count = i+min_k_count+1
print("Оптимальное кол-во кластеров =", opt_k_count)

R = 0
for i in range(0, n):
    d = len(x_c, y_c, x[i], y[i])
    if d > R:
        R = d
x_cc = [R * num.cos(2 * num.pi * i / opt_k_count) + x_c for i in range(opt_k_count)]
y_cc = [R * num.sin(2 * num.pi * i / opt_k_count) + y_c for i in range(opt_k_count)]
colors = ["red", "green", "blue", "purple", "pink", "yellow", "gray", "orange"]
dots = dot_and_clu(x, y, x_cc, y_cc, opt_k_count)
for i in range(0, n - 1):
    plt.scatter(x[i], y[i], color=colors[dots[i]])
for i in range(0, opt_k_count):
    plt.scatter(x_cc[i], y_cc[i], color='black')
plt.show()