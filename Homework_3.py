# Задача №1 - Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# list_numbers = [5, 3, 7, 10, 11]
# print(list_numbers)

# def numbers_sum(list_numbers):    
#     sum = 0
#     for i in range(1, len(list_numbers), 2):
#         sum = sum + list_numbers[i]
#         print(sum)
#     return sum
        
    
# print(numbers_sum)
# print('Сумма чисел на нечетных позициях равна: ', numbers_sum(list_numbers))

# Задача №2: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import math

# my_list = [1, 3, 10, 5, 8, 9]
# print(my_list)
# len_list = math.ceil(len(my_list)/2)
# new_list = []

# for i in range (len_list):
#     new_list.append(my_list[i]*my_list[-i-1])

# print(f'Произведение пар: \r\n{new_list}')



# Задача №3: Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# my_list = [1.1, 2.5, 7.9, 5.4]
# min = int(str(my_list[0]).split('.')[1])
# max = int(str(my_list[0]).split('.')[1])

# for i in range (len(my_list)):
#     temp_val = int(str(my_list[i]).split('.')[1])
#     if (min > temp_val):
#         min = temp_val
#     if (max < temp_val):
#         max = temp_val

# print(f"Наибольшее: {max} \r\n Наименьшее: {min}")
# print(f'Разница между наибольшим и наименьшим: {max - min}')

# Задача №4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# def binary_num(text):
#     int_num = True
#     while int_num:
#         a = input(f'{text}')
#         if a.isdigit():
#             a = int(a)
#             if a <=0:
#                 print('Введите число больше 0')
#             else:
#                 int_num = False
#         else:
#             print('Не число, попробуйте еще раз')
#     return a
# a = binary_num('Введите число: ')
# num = ' '

# while a > 0:
#     num = str(a%2) + num
#     a = a // 2
# print(f'Двоичное число: {a}')


# Задача №5:  Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# def fib(a):
#     if (a <= 0):
#         return a
#     else:
#         return(fib(a-1) + fib(a-2))
# a = int(input('Введите число последовательности: '))
# possitive_fib = []
# for i in range(a):
#     possitive_fib.append(fib(i))
# print(f'положительное Фибоначи: \n {possitive_fib}')

# negative_fib = []
# my_list = possitive_fib
# for i in range(1, len(my_list)):
#     negative_fib.append(my_list[i]*((-1)**(i+1)))
# negative_fib.reverse()

# print(f'Отрицательное Фибоначи: \n {negative_fib + my_list}')
    