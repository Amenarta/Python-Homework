# Задача №1- Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# print('Введите цифру от 1 до 7: ')
# a = int(input())

# if (a > 7 or a <1):
#     print('Число выходит за рамки указанного диапозона')
# elif (a >= 1 <= 5):
#     print(a, '-', 'рабочий день.')
#     (a == 6 or a == 7)  
#     print(a, '-', 'выходной день.')


# Задача №2- Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Задача №3- Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# print('Введите значение точки Х: ')
# x = int(input())
# print('Введите значение точки Y: ')
# y = int(input())

# if (x > 0 and y > 0):
#     print("1 четверть координат.")
# elif (x < 0 and y > 0):
#     print("2 четверть координат.")
# elif (x < 0 and y < 0):
#     print("3 четверть координат.")
# elif (x > 0 and y < 0):
#     print("4 четверть координат.")


# Задача №4 - Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# print('Введите номер координатной четверти от 1 до 4: ')
# a = int(input())

# if a == 1:
#     print('Диапазон возможных координат точек в этой четверти: x > 0, y > 0)')
# elif a ==2:
#     print('Диапазон возможных координат точек в этой четверти: x < 0, y > 0)')
# elif a ==3:
#     print('Диапазон возможных координат точек в этой четверти: x < 0, y < 0)')
# elif a ==4:
#     print('Диапазон возможных координат точек в этой четверти: x > 0, y < 0)')
# elif (a < 1 or a > 4):
#     print('Данная цифра не может являться номером четверти координат')


# Задача №5- Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.

print('Введите координаты x1 точки А: ')
x1 = float(input())
print('Введите координаты y1 точки А: ')
y1 = float(input())
print('Введите координаты x2 точки B: ')
x2 = float(input())
print('Введите координаты y2 точки B: ')
y2 = float(input())


def Sqrt(x1, x2, y1, y2):
    import math
    sqrt = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print(sqrt)
    return(sqrt)

Sqrt(x1, x2, y1, y2)









    
