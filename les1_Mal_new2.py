# Задание 1
# def soldier():
#
#     try:
#         age = int(input('Сколько тебе лет? '))
#         if age >= 18 and age <= 27:
#             return 'В боты ))'
#         elif age > 27:
#             return 'Стариков не берем'
#         else:
#             return 'Ты еще салага )))'
#     except:
#         return 'Ошибка ввода'
#
#
# print(soldier())

# Задание 2 (Определить содержет ли массив число х)

# l = [1,3,6,4,8,13,15,3,3,3,124,123,13]
# x = int(input('Введите число ''X'' --->'))
# l = l.count(x)
# if l >0:
#     print(f'Число Х встречается в списке {l} раз(а) ')
# elif l == 0 :
#     print('Числа "Х" нет в списке')

# Задание 3 (Найти количество четных чисел в массиве)

# l = [1,3,6,4,8,13,15,3,3,3,124,122,13]
# count = 0
#
# for n in l:
#     if n % 2 == 0:
#         count += 1
#
# print(f'В данном списке четных чисел --> {count}')

# Задание 4 (Найти количество чисел в массиве которые делятся на 3 ,но не делятся на 7)

# l = (1,3,6,21,8,13,15,44,124,122,13,44,14,15)
# count = 0

# for n in l:
#      if n % 3 == 0 and n % 7 != 0:
#          count += 1

# print(count)

# Задание 5 (Определить каких чисел больше , которые делятся на первый или последний элемент массива)

# l = [5,2,4,5,6,7,8,9,10,14,8,3]
# count_beginning = 0
# count_end = 0

# for n in l:
#     if n % l[0] == 0 :
#         count_beginning += 1
#     elif n % l[-1] == 0:
#         count_end += 1

# if count_beginning > count_end:
#     print ('Чисел которые делятся на первый элемент больше')
# elif count_beginning < count_end:
#     print ('Чисел которые делятся на последний элемент больше')
# else : print('Поровну')

# Задание 6 (Найдите сумму и произведение чисел массива)

# l = [5,2,4,3]

# sum = 0
# mult = 1

# for i in l:
#     sum += i
#     mult *= i

# print(f'Произведение чисел = {mult} \nCумма чисел = {sum}')

# Задание 7 (Найдите сумму четных чисел массива)

# l = [1,3,6,4,8,13,15,3,3,3,13]
# summ_even = 0

# for n in l:
#     if n % 2 == 0:
#         summ_even += n

# print(f'Сумма четных чисел = {summ_even}') 

# Задание 8 (Найти сумму нечетных чисел массива которые не превосходят 11)

# l = [1,3,6,4,8,13,15,3,3,3,13,9,21]
# summ_odd = 0

# for n in l:
#     if n % 2 != 0 and n < 11:
#         summ_odd += n

# print(f'Сумма нечетных чисел = {summ_odd}') 

# Задание 9 (Найти сумму чисел массива , которые расположены до первого четного числа ,
# если четных чисел в массиве нет то найти сумму чисел за исключением крайних)

# l = [3,9,11,15,3,3,2,13]
# count = 0
# summ = 0

# for n in l:
#     if n % 2 == 0 :
#         count += 1

# if count >= 1 : #добавил равенство
#     for n in l:
#         if n % 2 != 0 : #исправил
#           summ += n 
#         elif n % 2 == 0: #исправил
#             break
# else:
#     summ = sum(l[1:-1])          
           
# print(f'Сумма чисел = {summ}') 

# Задание 10 (Найти сумму чисел массива которые стоят на четных местах)

# l = [3,11,7,15,3,3,3,13,3]
# x = 0
# for i in range(1,len(l)+1): # исправил
#     if i % 2 == 0 :
#         x += l[i-1] # исправил

# print (f'Сумма чисел на нечетных местах = {x}')


# Задание 11 (Найди сумму чисел массива, которые стоят на нечетных местах и при этом
# превосходят сумму крайних элементов массива)

# l = [1,4,7,19,14,1,5,5,7]
# summ = 0
# extr = l[0] + l[-1]

# for i in range(len(l)):

#     if i % 2 == 0 and l[i] > extr:
#         print(l[i])
#         summ += l[i]
        

# print(f'Сумма равна = {summ}')

# Задание 12 (задан массив x  из n элементов. x1 - x2 +x3 - x4)

# from random import randint
#
# n = int(input('Введите количество переменных n -- > '))
#
# x = [randint(1,20) for i in range(n)]
# result = 0
# q = 1
# print(f'Cгенерировался список x = {x} c {n} переменными')
#
# for i in x:
#     result += i*q
#     q *= -1
#
# print((f'Результат x[1]-x[2]+x[3].....-x[n-1]+x[n] = {result}'))

# Задание 13 (задан массив x  из n элементов. x1xn+x2xn-1....)

# from random import randint
#
# n = int(input('Введите количество переменных n -- > '))
#
# q = n
#
# x = [randint(1,10) for i in range(n)]
#
# result = 0
#
# print ( f'Cгенерировался список x = {x} c {n} переменными')
#
# while q > 0:
#
#     for i in x:
#         q += -1
#         result += (i*x[q])
#
# print(f"Результат (x[1]*x[n])+(x[2]*x[n-1]....+x[n]*x[1]) = {result}")


# Задание 14 (задан массив x  из n элементов. xn(xn+xn-1)(xn+xn-1+xn-2))

# from random import randint
#
# n = int(input('Введите количество переменных n -- > '))
#
# q = n
#
# x = [randint(1,10) for i in range(n)]
#
# result = 1
#
# print ( f'Cгенерировался список x = {x} c {n} переменными' )
#
# d = x[-1]
# while q > 0:
#
#     for i in x:
#         q += -1
#         result *= d
#         d += x[q-1]
# print(f'Результат x[n]*(x[n]+x[n-1])*(x[n]+x[n-1]+x[n-2])... = {result}')

# Задание 15 (Найти наибольший элемент массива)

# from random import randint
#
# n = int(input('Введите количество переменных n -- > '))
# x = [randint(1,10) for i in range(n)]
# print(f'Cгенерировался список x = {x} c {n} переменными')
# maximum = 0
#
# for i in x:
#     if i > maximum:
#         maximum = i
#
# print(f'Наибольший элемент массива = {maximum}')

# Задание 16 (Найти сумму наибольшего и наименьшего элементов массива)

from random import randint

n = int(input('Введите количество переменных n -- > '))
x = [randint(-5,25) for i in range(n)]
print(f'Cгенерировался список x = {x} c {n} переменными')
maximum = 0
minimum = x[0]
for i in x:
    if i > maximum:
        maximum = i
for i in x:
    if i < minimum:
        minimum = i
print(f'Cумма наибольшего и наименьшего элементов массива = {maximum+minimum}')
