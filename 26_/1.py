# № 19256 ЕГКР 21.12.24 (Уровень: Базовый)


file = open("26_/1/26_19256.txt")
N = int(file.readline())

students = {}


def check_tasks(tasks:list):
    mx_count = 1
    
    tasks = sorted(set(tasks))
    
    for i in range(len(tasks)-1):
        if tasks[i+1] - tasks[i] ==1:
            mx_count+=1
        else:
            mx_count = 1
            
    return mx_count
        
        

for i in range(N):
    student_id, number_task = map(int, file.readline().split())
    
    if student_id not in students.keys():
        students[student_id] = []
        
    students[student_id].append(number_task)


mx_c = 0
ans =[]

for ind, tasks in students.items():

    count_soluted_tasks = check_tasks(tasks)
    students[ind] = count_soluted_tasks
    
    if count_soluted_tasks >= mx_c:
        mx_c = count_soluted_tasks
        ans.append([ind, count_soluted_tasks])
        
ans.sort(key=lambda x:x[1], reverse=True)
ans.sort(key=lambda x:x[0])

print(ans[0])