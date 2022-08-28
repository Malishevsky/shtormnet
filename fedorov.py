# a = pow(abs(-5)+abs(-3), round(5.8))
# print(a)

# def convert_to_cels(fahren):
#     return(fahren-32)*5/9
#
# print(convert_to_cels(80))

# def summ_degry(x):
#     return pow(x,4) + pow(4,x)
#
# print(summ_degry(2))
#
# def summ_degry2(x,y):
#     return  pow(y,4) + pow(4,x)
# print(summ_degry2(2,4))

# def celcy_to_farhen(celcy):
#     return 9/5*(celcy+32)
# print(celcy_to_farhen(31))

# def square(x,y):
#     return f'площадь квадрата = {x*y}\nпериметр квадрата = {2*(x+y)}'

# print(square(2,4))

# def three_mean(x,y,z):
#     return (x+y+z)/3
# print(three_mean(2,5,7))
#
# x = input('Введите своё имя')
# print('Привет ',x)

# s = 'Я вас люблю )'
#
# print( s[:6] +'не'+ s[5:])

# a = float(input('Введи 1 число '))
# b = float(input('Введи 2 число '))
# c = float(input('Введи 3 число '))
#
# print(f'Сумма введеных чисел = {a+b+c}')
# print(f'Произведение введеных чисел = {a*b*c}')

# pH = float(input("Введите pH: ")) # строку преобразовали к вещественному типу
# if pH == 7.0:
#  print(pH, "Вода")
# elif 7.36 < pH < 7.44:
#  print(pH, "Кровь")
# else:
#  print("Что это?!")

# value = input("Введите pH: ")
# if len(value) > 0:
#     pH = float (value)
#     if pH == 7.0:
#         print(pH, "Вода")
#     elif 7.36 < pH < 7.44:
#         print(pH, "Кровь")
#     else:
#         print("Что это?!")
# else:
#     print("Введите значение pH!")

# pH = float(input('Введите значение pH --> '))
#
# def pH_detected(pH):
#     if  2.9 < pH < 3.5 :
#         return 'Яблочный сок'
#     elif 4.5 < pH < 9:
#         return 'Шампунь'
#     elif 3 < pH < 4.5:
#         return 'Мыло'
#     else:
#         return 'Что это такое ?'
#
# print(pH_detected(pH))

# def maximum(x,y):
#     if x>y:
#         return x
#     elif x<y:
#         return y
#     else:
#         return 'Они равны'
#
# print(maximum(7,3))

# def even_number(x):
#     if x % 2 == 0:
#         return 'Четное'
#     return 'Нечетное'
#
# # print(even_number(4))


# def function():
#     x = float(input('Введите Х --->  '))
#     if -2.4 <= x <=5.7:
#         return f'f = {pow(x,2)}'
#     return f'f = 4'
#
# print(function())

# def cash_of_call():
#     x = int(input('Введите код города --->  '))
#     y = float(input('Введите количество минут --->  '))
#     if x == 343:
#         return f'Стоимость разговора = {y*15} руб'
#     elif x==381 :
#         return f'Стоимость разговора = {y * 18} руб'
#     elif x==473:
#         return f'Стоимость разговора = {y * 13} руб'
#     elif x==485:
#         return f'Стоимость разговора = {y * 11} руб'
#     return 'Не правильный код города'
# print(cash_of_call())

# def index_body_mass():
#     x = float(input('Введите рост --->  '))
#     y = int(input('Введите вес --->  '))
#     return y/pow(x/100,2)
#
# i = index_body_mass()
# def stadia_ojireniya():
#     if i < 25:
#         return 'Вы в норме'
#     elif 25 < i < 29.9:
#         return 'У вас избыточный вес'
#     elif 30 < i < 34.9:
#         return 'У вас 1 стадия ожирения'
#     elif 35 < i < 39.9:
#         return 'У вас 2 стадия ожирения'
#     else:
#         return 'У вас 3 стадия ожирения'
#
# def bolezni():
#     if i < 18.5:
#         return 'Пониженный вес , питайтесь лучше'
#     elif 18.5 < i < 24.9:
#         return 'Нормальная масса тела. Нет Рисков'
#     elif 25 < i < 29.9:
#         return 'Риск развития атеросклироза , сахарного диабета и др.'
#     elif 30 < i < 39.9:
#         return 'Увеличеные риски для здоровья'
#     else:
#         return 'Выраженая тучность .Огромные риски для здоровья'
#
# def info():
#     print(i)
#     print(bolezni())
#     print(stadia_ojireniya())
#
# info()
import math
print(help(__builtins__.exec))