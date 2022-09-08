#Задача 1 Найти наиболее часто встречающийся элемент в массиве целых чисел

# from random import randint
# a = int(input('Введите длину массива\n --->>> '))

# b = [randint(0,10) for i in range(a)]

# count = 0 
# elem = 0
# for i in b:
#     if b.count(i) > count:
#         count = b.count(i)
#         elem = i


# print(f'В списке {b} элемент {elem} встречается {count} раз(а)')


#Задача 2 Вычислить номер минимального элемента и сумму элементов массива расположеных между перым и вторым отриц. числами
# from random import randint
# a = int(input('Введите длину массива\n --->>> '))

# b = [randint(-4,20) for i in range(a)]

# count = 0 
# elem = []
# minimum = b[0]
# for i in b: # ищем минимальный элемент без sort
#     if i < minimum:
#         print(i)
#         minimum = i


# for i in range(len(b)): # добавляем в cписок elem индексы 2х первых отрицательных чисел
#         if b[i] < 0 and len(elem)<2:
#             elem.append(i)

# if len(elem) ==2: # Проверка есть ли 2 отрицательных элемента в списке, если да считаем сумму
#     for i in range(elem[0]+1,elem[1]):
#         count += b[i]
# else:
#     print('Нет 2х отрицательный элементов')       
# print(f'Сгенерированный список {b}')
# print(f'Минимальное число в списке = {minimum}')
# print(f'Сумма элементов между первым {b[elem[0]]} и вторым {b[elem[1]]} отрицательными элементами = {count}')

#Задача 3 Вводит с клавиатуры не пустой массив и выводит не локальный максимум

# lst = []
# lst_local_max = []
# print("Для завершения введите >>>>> 666 <<<<<")
# while True:
#     try:
#         inp = int(input('\nВведите новый элемент списка: '))
#         lst.append(inp)
#         if inp == 666 and len(lst)>2:
#             lst.pop(-1)
#             print(f'Введенный список {lst}')
#             break
#     except:
#         print('Введено не число ')
# if lst[0] > lst[1]:
#         lst_local_max.append(lst[0])
# for i in range(1,len(lst)-1):
#     if lst[i]>lst[i-1] and lst[i]>lst[i+1]:
#         lst_local_max.append(lst[i])
# if lst[-1] > lst[-2]:
#     lst_local_max.append(lst[-1])
# print(f'Список локальных максимумов {lst_local_max}')

# Задача 4 В данном массиве найдите 2 наименьших элемента

# from random import randint
# a = int(input('Введите длину массива\n --->>> '))

# b = [randint(-10,20) for i in range(a)]
# b1 = b.copy()
# count = 0 
# elem = []
# minimum1 = b[0]
# for i in b: # ищем первый минимальный элемент без sort
#     if i < minimum1:
#         minimum1 = i
# b.remove(minimum1)
# minimum2 = b[0]
# for i in b: # ищем второй минимальный элемент без sort
#     if i < minimum2:
#         minimum2 = i        
# print(f'Минимальное числа в массиве {b1} \n1 = {minimum1}\n2 = {minimum2}')

# Задача 5 Определить есть ли в массиве повторяющеися элементы

# from random import randint
# a = int(input('Введите длину массива\n --->>> '))

# b = [randint(-10,20) for i in range(a)]

# if len(b)==len(set(b)):
#     print(f'В массиве {b} нет повторяющихся элементов')
# else:
#     print(f'В массиве {b} -->>  {len(b)-len(set(b))} повторяющиxся элемента')

# Задача 6 В данном массиве найдите наибольшую серию подряд идущих элементов , расположенных по возрастанию

from random import randint
a = int(input('Введите длину массива\n --->>> '))

b = [randint(0,6) for i in range(a)]

count = 0
count_lst = []
for i in range(len(b)-3):
    if b[i] != b[i+1] and b[i+1] != b[i+2] and b[i+2] != b[i+3]:
        count += 1
        count_lst.append(str(b[i])+str(b[i+1])+str(b[i+2])+str(b[i+3]))

print(f'Сгенерированный массив {b}')
print(f'Количество неповторяющихся четверок = {count}')
print(f'Серии из четверок {count_lst}')