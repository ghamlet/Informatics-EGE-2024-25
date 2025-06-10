from math import  dist

f = open("27_3__615w5.txt")
trash = f.readline()

CLUSTERS = [[] for i in range(3)]

for line in f:
    line = line.replace(",", ".")
    x,y,z = map(float, line.split())
    star = [x,y,z]

    if x < -5: CLUSTERS[0].append(star)
    elif x < 5: CLUSTERS[1].append(star)
    else: CLUSTERS[2].append(star)

Px = Py = Pz = 0

for cluster in CLUSTERS:
    min_dist = 999999999999

    for main_star in cluster:
        summa_dist = sum(dist(main_star, star) for star in cluster)

        if summa_dist < min_dist:
            min_dist = summa_dist
            centroid = main_star

    Px += centroid[0]
    Py += centroid[1]
    Pz += centroid[2]

print(int(Px / len(CLUSTERS) * 1000))
print(int(Py / len(CLUSTERS) * 1000))
print(int(Pz / len(CLUSTERS) * 1000))

