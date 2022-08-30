# Задание 1 Найти количество чисел , соседи которых отличаются более чем в 2 раза
# from random import randint

# n = int(input('Введите количество переменных n -- > '))

# x = [randint(1,20) for i in range(n)]
# print(f'Cгенерировался список x = {x} c {n} переменными')
# count = 0
# index_number =[]


# for i in range(1,len(x)-1):
#     if (x[i-1]/x[i+1]) >= 2 or ((x[i+1]/x[i-1])) > 2:
#         count += 1 
#         index_number.append({'index' : i, 'number': x[i]})

        

# print(f'Количество чисел у которых соседи отличаются более чем в 2 раза = {count}')
# print('Список этих чисел')
# for i in index_number:
#     print(i)

# Задание 2 Найдите количество чисел , каждое из которых равно сумме квадратов своих соседей и при этом не является большим в массиве

# x = [3,25,4,20,2,29,5,1,5,2]

# count = 0
# index_number =[]
# maximum = 0

# for i in x :
#     if i > maximum:
#         maximum = i

# for i in range(1,len(x)-1):
#     if x[i] == (x[i-1]**2 + x[i+1]**2) and x[i] < maximum  :
#         count += 1 
#         index_number.append({'index' : i, 'number': x[i]})

# print(count)
# print('Список этих чисел')
# for i in index_number:
#     print(i)

# Задание 3 Проверьте , содержит ли массив из n чисел все числа от 1 до n

# list_no_sort = [2,1,3,4,6,5,7,8,10,11,9]

# def includet(x):
#     x_sort = []
#     for i in range(1,len(x)+1):
#         x_sort.append(i)
#     c = 0
#     for i in x_sort :
#         if x.count(i) == 1:
#             c += 1
#     if c == len(x):
#         return print(f'Список {x} содержит все элементы от 1 до {len(x)}')
#     else:
#         return print(f'Список {x} не содержит все элементы от 1 до {len(x)}')
    
          
# includet(list_no_sort)


# Задание 4 Проверить , образуют ли элементы массива арифметическую или геометрическую прогрессии. Проверить является ли данный массив убывающим или возрастающим

# mass = [2,4,8,16]

# def type_progression(x):
#     b = 0
#     g = 0
#     d = x[1]-x[0]
#     f = x[1]/x[0]
#     type_arifmetic_progression = 'возрастающая'
#     if d < 0 :
#         type_arifmetic_progression = 'убывающая'
#     elif d == 0:
#         type_arifmetic_progression = 'стационарная'
    
#     if x[0] > 0 and f > 1:
#         type_geometrical_progression = 'возрастающая'
#     elif 0 < f < 1:
#         type_geometrical_progression = 'убывающая'
#     elif f < 0:
#         type_geometrical_progression = 'знакочередующаяся'
#     elif f == 1:
#         type_geometrical_progression = 'стационарная'
#     elif  x[0] < 0 and f > 1: 
#         return 'Это не прогрессия'  

#     for i in range(0,len(x)-1):
#         if x[i+1]-x[i] == d:
#             b += 1
#             if b == len(x)-1:
#                 return f'Арифметическая {type_arifmetic_progression} прогрессия со знаменателем {d}'
#     for i in range(0,len(x)-1):
#         if x[i+1]/x[i] == f:
#             g += 1  
#             if g == len(x)-1:
#                 return f'Геометрическая {type_geometrical_progression} прогрессия со знаменателем {f}'
#     return 'Это не прогрессия'

            
# print(type_progression(mass))

# Задача 5 Найдите количество различных элементов данного массива

# mass = [1,2,'d','a','d',4,5,5,4,1]
# a=[]

# for i in mass:
#     if i not in a:
#         a.append(i)    
 
# print(f'Количество различных элементов списка = {len(a)}')

# Задача 6 Определить количество перемен знаков элементов массива

# from random import randint


# mass = [randint(-20,20) for i in range(14)]
# count = 0


# for i in range(len(mass)-1):
#     if mass[i] < 0 :
#         if mass[i+1] > 0:
#             count +=1
#     elif mass[i] > 0 :
#         if mass[i+1] < 0:
#             count += 1

# print(f'Знак в списке {mass } изменился {count} раз')

# Задача 7 , 8  Найти максимальное количество элементов, найти наиболее часто встречающийся элемент в массиве целых чисел

# from optparse import Values
# from random import randint


# mass = [randint(0,5) for i in range(10)]
# a = 0
# count = 0

# for i in mass:
#     if mass.count(i) > count:
#         count = mass.count(i)
# for i in mass:
#     if mass.count(i) == count:
#         a = i

# print(f'Элемент {a} в списке {mass} встречается наиболее часто {count} раз ')

# Задача 9 Из словаря вывести все числа на экран


user = {
    'k': 1,
    2 : 2,
    'name' : 3,
    'login' : 4,
    'parents' : {'mather':[5,{'k':6},'7',[{'a':8}]],'father':'9'},
    'g':('10',{'p':11})}

var = '1234567891011121314'
for i in list(user):
    print(i)
    