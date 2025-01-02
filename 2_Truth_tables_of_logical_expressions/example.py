from itertools import product, permutations

def f(a,b,c,d):
    return ((a <= b) == c) or d

for x1, x2, x3, x4 in product([0,1], repeat = 4):
    table = [
             (1, 0, 1, x1, 0),
             (1, 0, x2, 1, 0), 
             (x3, x4, 0, 0, 0)
            ]
    
    if len(table) == len(set(table)):
        for permutation in permutations('abcd', r = 4):
            
            # Произвольное количество именованных аргументов **kwargs
            # Как уже было отмечено выше, именованные аргументы передаются в функцию в виде пар ключ=значение:

                    
            # def my_function(cat1, cat2, cat3):
            #     print(f'Младший кот: {cat1}, старший кот: {cat2}')
            # my_function(cat1='Том', cat2='Барсик', cat3='Полосатик') 


            if all(f(**dict(zip(permutation, row))) == row[-1] for row in table):
                print(*permutation)
                print(table)
                exit()




# TODO : добавить базовый способ решения через фор , указать прелесть нового спобога что он выводит все возможные способы и если значение функции в таблице разные то не надо в коденичего менять