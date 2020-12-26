import random
import matplotlib.pyplot as plt
import numpy as num

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vertex_set = set()
        self.cluster = None

n = 10
points = [P(random.randint(1, 100), random.randint(1, 100)) for i in range(n)]

colors = ['purple', 'salmon', 'olive', 'seagreen', 'thistle', 'lightpink']

def leng(x1, y1, x2, y2):
    return num.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

def SubMinDist(current, points):
    min_dist = None
    next = None
    for point in points:
        if point == current:
            continue
        candidate_dist = leng(current.x, current.y, point.x, point.y)
        if min_dist is None or candidate_dist < min_dist:
            next = point
            min_dist = candidate_dist
    return next

def MinDist(points):
    min_dist = None
    start = None
    neigh = None
    for point in points:
        next = SubMinDist(point, points)
        dist_tonext = leng(next.x, next.y, point.x, point.y)
        if min_dist is None or min_dist > dist_tonext:
            min_dist = dist_tonext
            start = point
            neigh = next
    start.vertex_set.add(neigh)
    neigh.vertex_set.add(start)
    return start


def CreateMinTree(points):
    now = MinDist(points)
    neigh = next(iter(now.vertex_set))
    pres_p = set()
    extra_p = set(points)
    pres_p.update([now, neigh])
    extra_p.remove(now)
    extra_p.remove(neigh)
    for extra in extra_p:
        new_neigh = SubMinDist(extra, pres_p)
        extra.vertex_set.add(new_neigh)
        new_neigh.vertex_set.add(extra)
        pres_p.add(extra)


def DeleteExtra(points, k):
    k -= 1
    distance_list = []
    used = set()
    for point in points:
        if used.__contains__(point):
            continue
        queue = [point]
        while len(queue) > 0:
            v = queue.pop(0)
            used.add(v)
            for vertex in v.vertex_set:
                if not used.__contains__(vertex):
                    distance_list.append(leng(v.x, v.y, vertex.x, vertex.y))
                    queue.append(vertex)
    distance_list.sort(reverse=True)
    for i in range(k):
        is_deleted = False
        for point in points:
            if is_deleted:
                break
            for neighbour in point.vertex_set:
                if leng(neighbour.x, neighbour.y, point.x, point.y) == distance_list[i]:
                    neighbour.vertex_set.remove(point)
                    point.vertex_set.remove(neighbour)
                    is_deleted = True
                    break


def ShowMinTree(points, save):
    used = set()
    x = []
    y = []
    now = [points[0]]
    while len(now) > 0:
        v = now.pop(len(now) - 1)
        if used.__contains__(v):
            continue
        used.add(v)
        for top in v.vertex_set:
            if used.__contains__(top):
                continue
            x.append(v.x)
            y.append(v.y)
            x.append(top.x)
            y.append(top.y)
            now.append(top)
    plt.plot(x, y, color="pink", marker="o")
    plt.show()

def Charts(points, save):
    clust = -1
    used = set()
    for point in points:
        if used.__contains__(point):
            continue
        clust += 1
        color = colors[clust]
        queue = [point]
        while len(queue) > 0:
            v = queue.pop(0)
            plt.scatter(v.x, v.y, color=color)
            used.add(v)
            for vertex in v.vertex_set:
                if not used.__contains__(vertex):
                    plt.scatter(vertex.x, vertex.y, color=color)
                    queue.append(vertex)
    plt.show()


CreateMinTree(points)
ShowMinTree(points, True)
DeleteExtra(points, 3)
Charts(points, True)
