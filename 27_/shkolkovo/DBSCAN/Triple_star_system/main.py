from math import dist

f = open("27-1b__5t7yn.txt")
trash = f.readline()

stars = [list(map(float, line.replace(",", ".").split())) for line in f]


def dbscan(stars:list, R:float):
    CLUSTERS = []
    cur_ind = 0

    while stars:
        CLUSTERS.append([stars.pop(0)])

        for main_star in CLUSTERS[cur_ind]:
            for star in stars:
                if dist(main_star, star) <= R:
                    CLUSTERS[cur_ind].append(star)
                    stars.remove(star)

        cur_ind+=1

    return  CLUSTERS


if __name__ == "__main__":
    R = 0.5
    clusters = dbscan(stars, R)
    clusters = [cluster for cluster in clusters if len(cluster) > 10]

    d = 0.01

    for cluster in clusters:
        stars_groups = dbscan(cluster,d )
        stars_groups = [group for group in stars_groups if len(group) ==3]
        # print(stars_groups)

        max_perimetr = 0
        for group in stars_groups: # перебираем тройки
            # print(group)

            dist1 = dist(group[0], group[1])
            dist2 = dist(group[1], group[2])
            dist3 = dist(group[0], group[2])

            if dist1 < d and dist2 < d and dist3 < d:
                cur_perimetr = dist1 + dist2 + dist3

                if cur_perimetr > max_perimetr:
                    max_perimetr = cur_perimetr
                    need_triple_stars = group

        print(need_triple_stars)



