from math import dist


def separation(x, y, brightness):
    """Разделение на кластеры"""

    if brightness > 45 and brightness < 98:   # дополнительное условие, чтобы яркость звезды была в диапозоне от 45 до 98
        
        if x <0 and y < -60:
            CLUSTERS[0].append([x,y, brightness])
            
        elif x<0 and -60< y<-20:
            CLUSTERS[1].append([x,y, brightness])
            
        elif x<0 and y>0:
            CLUSTERS[2].append([x,y,brightness])
            
        elif x>0 and y < -50:
            CLUSTERS[3].append([x,y,brightness])
            
        elif x >0 and y > -50:
            CLUSTERS[4].append([x,y,brightness])
    
    
    

def find_center_of_cluster(cluster: list[float, float]) -> list[float, float]:
    """Нахождение центроида кластера"""
    
    m = []      # массив для хранения расстояний 
    
    for main_star in cluster:           # перебираем все звезды кластера
        sum_dist = sum(dist(main_star, slave_star) for slave_star in cluster)     # находим расстояние от данной точки main_star до всех точек кластера и суммируем значения
        m.append([sum_dist, main_star])       # сохраняем координаты данной точки и сумму расстояний от нее

    dist, coordinates_center_point = min(m)    # находим минимальную сумму расстояний и оставляем только координаты этой центральной точки
    return coordinates_center_point
        
   

CLUSTERS = [[], [], [], [] ,[]] 

def main():
    file = open("27_/shkolkovo/1/3B__5gsq6.txt")
    [separation(*map(float, line.replace(",", ".").split())) for line in file]  # проходимся по всем строкам файла, заменяем запятые на точки, разделяем по пробелу, превращаем в float тип и передаем значения из данной строки в функцию для распределния на кластеры
    
    centers = [find_center_of_cluster(cluster) for cluster in CLUSTERS]   # для каждого из 5 кластеров находим координаты центральной звезды
    
    Px = int(sum(center[0] for center in centers) / (len(centers)))   # среднее арифметическое абсцисс кластеров
    Py = int(sum(center[1] for center in centers) / (len(centers)))    # среднее арифметическое ординат кластеров
    print(Px, Py)
    
    
if __name__ == "__main__":
    main()