from itertools import cycle
from math import hypot
from numpy import random
import matplotlib.pyplot as plt
import numpy as np
import random

def dbscan_naive(P, eps, m, distance):

    NOISE = 0
    C = 0

    visited_points = set()
    clustered_points = set()
    clusters = {NOISE: []}

    def region_query(p):
        return [q for q in P if distance(p, q) < eps]

    def expand_cluster(p, neighbours):
        if C not in clusters:
            clusters[C] = []
            
        clusters[C].append(p)
        clustered_points.add(p)
        while neighbours:
            q = neighbours.pop()
            if q not in visited_points:
                visited_points.add(q)
                neighbourz = region_query(q)
                if len(neighbourz) > m:
                    neighbours.extend(neighbourz)
            if q not in clustered_points:
                clustered_points.add(q)
                clusters[C].append(q)
                if q in clusters[NOISE]:
                    clusters[NOISE].remove(q)

    for p in P:
        if p in visited_points:
            continue
        visited_points.add(p)
        neighbours = region_query(p)
        
        if len(neighbours) < m:
            clusters[NOISE].append(p)
        else:
            C += 1
            expand_cluster(p, neighbours)

    return clusters



if __name__ == "__main__":
    
    f = open("27_/19567/27.13.B_19567.txt")
    trash_data = f.readline()
    
    STARS = [tuple(map(float, (line.replace(",", ".").split()))) for line in f]    
    
    
   
    
    colors="bgry"
    
    clusters = dbscan_naive(STARS, 0.4, 2, lambda x, y: hypot(x[0] - y[0], x[1] - y[1]))
    for c, points in zip(colors, clusters.values()):
        X = [p[0] for p in points]
        Y = [p[1] for p in points]
        plt.scatter(X, Y, c=c)
    plt.show()


