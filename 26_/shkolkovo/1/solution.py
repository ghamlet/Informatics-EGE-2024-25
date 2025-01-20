f = open("26_/shkolkovo/1/26_12__491va.txt")
number_detail = int(f.readline())

m = []
conveer_start = []
conveer_end = []
count_paint = 0


for ind in range(number_detail):
    t_grind, t_paint = map(int, f.readline().split())   # считываем время шлифовки и окрашивания
    
    # если максимальное число в этом упорядоченном списке – это время окрашивания конкретной детали, то деталь размещают на ленте транспортера на первое свободное место от ее начала;
    # если максимальное число – это время шлифовки, то деталь размещают на первое свободное место от конца ленты транспортера;
    if t_paint > t_grind:
        conveer_start.append([t_paint, "p", ind])
        count_paint +=1
        
    else: 
        conveer_end.append([t_grind, "g", ind])

conveer_start.sort()
conveer_end.sort()    

print(conveer_end[-1][2])  # какой номер будет иметь последняя отшлифованная деталь

conveer_full = conveer_start + conveer_end[::-1]    
# переворачиваем список так как деатли должны размещаться на первое свободное место от конца ленты транспортера

        
print(count_paint)
