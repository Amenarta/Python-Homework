# Задача №1 - Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# a = 4561
# figure = str(a) # переводим число в строку
# figure = figure.replace('.', ' ') # производим замену десятичного разделителя, если оно есть
# figure_str = list(figure) # меняем строку с числом в список строк с цифрами
# number_lst = map(int, figure_str) # преобразовываем каждый элемент
# numbers_sum = sum(number_lst) # считаем сумму
# print(numbers_sum)

# Задача №2 - Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# from math import factorial

# print ('Введите число: ')
# N = int(input())
# mult = 1

# for i in range(1, N+1):
#     mult = factorial(i)
#     print(mult, end=' ')

# 3 - Задайте список из n чисел последовательности (1+1/n)**n 
# и выведите на экран их сумму.

# print ('Введите число N: ')
# N = int(input())
# roster = {}
# sum = 0

# for i in range(1, N+1):
#     roster[i] = (1+1/N)**N
#     sum += roster[i] 
# print(roster)
# print(sum)








