from math import  dist
from turtle import  *

f = open("27_b__5shxn.txt")
trash = f.readline()

stars = [list(map(float, line.replace(",", ".").split())) for line in f]


def dbscan(stars: list, R: float):
    CLUSTERS = []
    cur_ind = 0

    # пока есть нерассмотренные звезды
    while stars:
        # в списке кластеров создаем новый кластер куда помещаем новую звезду
        CLUSTERS.append([stars.pop(0)])

        #  рассматриваем все возможные пары звезд из текущего кластера и нераспределенных звезд
        for main_star in CLUSTERS[cur_ind]:
            for star in stars:
                # если расстояние между парой звезд меньше ограничения, значит они расположены рядом и относятся к одному кластеру
                if dist(main_star, star) <= R:
                    CLUSTERS[cur_ind].append(star)  # добавляем в текущий кластер новую звезду
                    stars.remove(star)   # удаляем добавленную звезду из нерассмотренных
        cur_ind+=1

    return  CLUSTERS


clusters = dbscan(stars, 0.2) # разбиение по кластерам R =0.2 из условия

# отбираем кластеры в которых более 10 звезд, чтобы отсеить одиночные звезды которые образуют отдельные кластеры
clusters = [cluster for cluster in clusters if len(cluster) > 10]
print(len(clusters))


# # Визуализация
# tracer(0)
# screensize(2000, 2000)
# m = 20
# penup()
#
# colors = ["green", "red", "purple", "blue"]
# for i, cl in enumerate(clusters):
#     for x, y in cl:
#         goto(x*m, y*m)
#         dot(4, colors[i])
#
# done()



# Поиск двойной звездной системы
t = 0.05 # максимальное расстояние между ближайшими звездами

for cluster in clusters:
    stars_groups = dbscan(cluster, t)  # разбиение каждого кластера на группы в которых расстояние между ближайшими звездами меньше 0.05

    # по условию задачи нужны группы где только 2 звезды
    need_groups = [group for group in stars_groups if len(group) == 2]
    # print(need_groups)

    # надо найти максимальное расстояние между двойными звездами
    max_dist = 0
    for twin_stars in need_groups:
        star1, star2 = twin_stars[0], twin_stars[1]

        cur_dist = dist(star1, star2)  # расстояние между звездами
        if cur_dist > max_dist:
            max_dist = cur_dist
            need_twin_stars = twin_stars

    print(need_twin_stars)


