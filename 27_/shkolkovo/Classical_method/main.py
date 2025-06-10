from math import dist

f = open("demo_2025_27_Б__4v457.txt")   # открываем файл
trash = f.readline()    # считываем первую строку в которой написано X Y

# формируем кластеры
CLUSTERS = [[] for i in range(3)]  # 3 кластера

# проходимся по строкам
for line in f:    # могут быть мусорные данные по типу 3,2076336787822dE которые дадут ошибку
    line = line.replace(",", ".")  # заменяем запятые на точки если нужно

    # ------------------------------------------
    # проверка что все символы это цифры
    x, y = line.split()
    if not (x + y).replace(".", "").isdigit():
        continue
    #--------------------------------------------


    x, y = map(float, line.split())  # разбиваем строку на x y и переводим их во FLOAT !!!
    star = [x,y]  # важно добавлять звезды в виде массивов

    # производим кластеризацию с помощью прямых
    if x < 3 and y < 4: CLUSTERS[0].append(star)
    elif x < 5 and y > 6:CLUSTERS[1].append(star)
    elif x >5: CLUSTERS[2].append(star)


# проверка кластеризации: можно добавить turtle
print(list(len(cluster) for cluster in CLUSTERS))

# ищем центроиды
summa_X = 0
summa_Y = 0

for cluster in CLUSTERS: # перебираем кластеры
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
    summa_X += centroid[0]
    summa_Y += centroid[1]

    # Дополнительно
    # Радиус кластера - максимальное расстояние от центра кластера до его точки
    radius = max(dist(centroid, star) for star in cluster)
    print(radius)


# прошлись по всем кластерам и накопили суммы абсцисс и ординат центроидов
# находим среднее арифметическое

sr_X = int((summa_X / len(CLUSTERS)) *  10_000)  # среднее арифметическое абсцисс центров кластеров
sr_Y = int((summa_Y / len(CLUSTERS)) * 10_000)   # среднее арифметическое ординат центров кластеров

print(sr_X, sr_Y)


# визуализация
from turtle import  *
from random import  random

colors = ["green", "red", "blue"]
m = 50
tracer(0)
penup()
screensize(2000, 2000)

for i, cluster in enumerate(CLUSTERS):
    color = colors[i]
    # color = random(), random(), random()
    for x, y in cluster:
        goto(x*m, y*m)
        dot(4, color)

done()