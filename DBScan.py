import matplotlib.pyplot as plt
import numpy as np

def leng(x1, y1, x2, y2):
    return np.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

n = 100
e, minC = 6, 3
color_list = []
for i in range(n):
    color_list.append('black')

colors = ['lavenderblush', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'darkmagenta', 'darkorange', 'maroon',
          'pink', 'crimson', 'lime', 'red', 'gray', 'olive', 'dodgerblue', 'skyblue']

x = [np.random.randint(1, 50) for i in range(n)]
y = [np.random.randint(1, 50) for i in range(n)]
pen = []
for i in range(0, n):
    neig = 0
    for j in range(0, n):
        if leng(x[i], y[i], x[j], y[j]) <= e:
            neig += 1
    if neig > minC:
        pen.append('m')
    else:
        pen.append('c')

for i in range(0, n):
    if pen[i] == 'c':
        for j in range(0, n):
            if pen[j] == 'm':
                if leng(x[i], y[i], x[j], y[j]) <= e:
                    pen[i] = 'b'
cluster = []

for i in range(n):
    cluster.append(0)

c = 1
for i in range(0, n):
    if pen[i] == 'm':
        for j in range(0, n):
            if leng(x[i], y[i], x[j], y[j]) <= e:
                if pen[j] == 'm':
                    if cluster[i] == 0 and cluster[j] == 0:
                        cluster[i] = c
                        cluster[j] = c
                        c += 1
                    elif cluster[i] == 0 and cluster[j] != 0:
                        cluster[i] = cluster[j]
                    elif cluster[j] == 0 and cluster[i] != 0:
                        cluster[j] = cluster[i]
                    elif cluster[i] != 0 and cluster[j] != 0:
                        if cluster[i] < cluster[j]:
                            cluster[j] = cluster[i]
                        else:
                            cluster[i] = cluster[j]
                elif pen[j] == 'b':
                    if cluster[i] == 0:
                        cluster[i] = c
                        c += 1

for i in range(0, n):
    if pen[i] == 'b':
        for j in range(0, n):
            if pen[j] == 'm':
                if leng(x[i], y[i], x[j], y[j]) <= e and cluster[j] != 0:
                    cluster[i] = cluster[j]

for i in range(n):
    for j in range(len(colors)):
        if cluster[i] == j:
            color_list[i] = colors[j]


cluster.sort()
print(cluster)

for i in range(0, n):
    plt.scatter(x[i], y[i], color=pen[i])
plt.show()

for i in range(0, n):
    plt.scatter(x[i], y[i], color=color_list[i])
plt.show()