import numpy as num
import matplotlib.pyplot as plt
import random

# Train data generator
def generateData(numberOfClassEl, numberOfClasses):
    data = []
    for classNum in range(numberOfClasses):
        # Choose random center of 2-dimensional gaussian
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        # Choose numberOfClassEl random nodes with RMS=0.5
        for rowNum in range(numberOfClassEl):
            data.append([[random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)], classNum])
    return data

def leng(x1, y1, x2, y2):
    return num.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

def cmp(a, b):
    return leng(a[0][0], a[0][1], x_new, y_new) - leng(b[0][0], b[0][1], x_new, y_new)

def cmp_to_key(cmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return cmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return cmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return cmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return cmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return cmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return cmp(self.obj, other.obj) != 0
    return K


n = 50
k = num.int(num.sqrt(n))
rec = []
rec = generateData(n, k)
x, y = [], []
for i in range(n):
    x.append(rec[i][0][0])
    y.append(rec[i][0][1])
plt.scatter(x, y)
min_x, max_x = num.min(x), num.max(x)
min_y, max_y = num.min(y), num.max(y)
x_new = min_x + num.random.random() * (max_x - min_x)
y_new = min_y + num.random.random() * (max_y - min_y)
plt.scatter(x_new, y_new, color='c')
plt.show()
sorted_data = sorted(rec, key=cmp_to_key(cmp))
dists = []
for i in range(len(sorted_data)):
    dists.append(leng(sorted_data[i][0][0], sorted_data[i][0][1], x_new, y_new))

