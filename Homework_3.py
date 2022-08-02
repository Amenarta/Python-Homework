# Задача №1 - Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list_numbers = [5, 3, 7, 10, 11]
print(list_numbers)

def numbers_sum(list_numbers):    
    sum = 0
    for i in range(len(list_numbers)):
        if list_numbers[i+1]:
            sum = sum + list_numbers[i+1]
            print(sum)
        return sum
    
print(numbers_sum)
print('Сумма чисел на нечетных позициях равна: ', numbers_sum(list_numbers))
