f = open("26_/shkolkovo/2/2_26_conf__3uznp.txt")
n = int(f.readline())

periods = []
completed_confs = []

for i in range(n):
    start, end = map(int, f.readline().split())
    periods.append([start, end])
    
# Чтобы проводить как можно больше мероприятий, нужно выбирать те, которые заканчиваются раньше. Это позволит минимизировать время простоя
periods.sort(key=lambda x:x[1])


completed_confs.append(periods.pop(0))  # чтобы в списке был "последний" элемент

for period in periods:
    cur_start_time = period[0]
    prev_end_time = completed_confs[-1][1]
    
    if cur_start_time >= prev_end_time:
        completed_confs.append(period)


# Время окончания пред-предпоследнего мероприятия    
last_end_time = completed_confs[-3][1]
print(last_end_time)
minn = float("inf")

print(periods)
# Цикл начиная со следующего после пред-предпоследнего
for ind in range(periods.index(completed_confs[-3]) + 1, len(periods)):
    cur_start_time, cur_end_time = periods[ind]
    # Если текущее может стать предпоследним
    if cur_start_time >= last_end_time:
        # Все возможные варианты последнего для текущего предпоследнего
        variants = [i[0] for i in periods[ind + 1:] if i[0] >= cur_end_time]
        # Если есть хоть один вариант - обновляем минимальную разность между
        # началом последнего и концом предпоследнего
        if variants:
            minn = min(minn, abs(min(variants) - cur_end_time))

print( minn)

