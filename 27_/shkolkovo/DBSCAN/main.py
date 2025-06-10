from math import dist

f = open("/home/arrma/PROGRAMMS/Informatics-EGE-2024-25/27_/shkolkovo/Classical_method/demo_2025_27_Б__4v457.txt")
trash = f.readline()    # считываем первую строку в которой написано X Y

# считываем все звезды из файла
stars = [list(map(float, line.replace(",", ".").split())) for line in f]
print(len(stars))


def dbscan(stars: list, R: float):
    CLUSTERS = []
    cur_ind = 0

    # пока есть нерассмотренные звезды
    while stars:
        # в списке кластеров создаем новый кластер куда помещаем новую звезду
        CLUSTERS.append([stars.pop(0)])

        #  рассматриваем все возможные пары звезд из текущего кластера и нераспределенных звезд
        for main_star in CLUSTERS[cur_ind]:
            for star in stars[:]:
                # если расстояние между парой звезд меньше ограничения, значит они расположены рядом и относятся к одному кластеру
                if dist(main_star, star) <= R: # на случай если у звезды есть 3 параметра то main_star[:2], star[:2]
                    CLUSTERS[cur_ind].append(star)  # добавляем в текущий кластер новую звезду
                    stars.remove(star)   # удаляем добавленную звезду из нерассмотренных
        cur_ind+=1

    return  CLUSTERS




if __name__ == "__main__":

    R = 0.7 # максимальное расстояние между звездами одного кластера
    clusters = dbscan(stars, R) # разбиение по кластерам R =0.2 из условия
    [print(len(cluster)) for cluster in clusters]

    #--------------------Визуализация----------------------------------------
    from turtle import *
    from random import random

    m = 50
    tracer(0)
    penup()
    screensize(2000, 2000)

    for i, cluster in enumerate(clusters):
        color = random(), random(), random()
        for x, y in cluster:
            goto(x * m, y * m)
            dot(4, color)

    done()

    #--------------------------------------------------------


    # отбираем кластеры в которых более 10 звезд, чтобы отсеить одиночные звезды которые образуют отдельные кластеры
    clusters = [cluster for cluster in clusters if len(cluster) > 10]
    print(len(clusters))

    summa_X = 0
    summa_Y = 0

    for cluster in clusters:  # перебираем кластеры
        min_dist = 999999  # !!! при рассмотрении каждого кластера надо вводить заново минимальную дистанцию

        for main_star in cluster:  # перебираем все звезды текущего кластера
            # находим сумму расстояний от текущей звезды до всех остальных звезд в этом кластере

            # summa_dists = sum(((star[0] - main_star[0]) **2 + (star[1] - main_star[1]) **2) ** 0.5  for star in cluster)
            summa_dists = sum(dist(main_star, star) for star in cluster)

            # если сумма расстояний меньше меньшего значения
            if summa_dists < min_dist:
                min_dist = summa_dists  # обновляем наименьшую сумму расстояний
                centroid = main_star  # новый кандидат на центроид

        # после того как пройдемся по всем звездам кластера, в centroid будут координаты точки с наименьшей суммой расстояний до других звезд
        print(centroid)

        # Радиус кластера - максимальное расстояние от центра кластера до его точки
        radius = max(dist(centroid, star) for star in cluster)
        print(radius)

        summa_X += centroid[0]
        summa_Y += centroid[1]

    # прошлись по всем кластерам и накопили суммы абсцисс и ординат центроидов
    # находим среднее арифметическое

    sr_X = int((summa_X / len(clusters)) * 10_000)  # среднее арифметическое абсцисс центров кластеров
    sr_Y = int((summa_Y / len(clusters)) * 10_000)  # среднее арифметическое ординат центров кластеров

    print(sr_X, sr_Y)