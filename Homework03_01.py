# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
import random

n = int(input('Введите число: '))
my_list = []
sum = 0
for i in range (n):
    my_list.append(random.randint(0, 100))
for i in range(len(my_list)):
    if i%2 != 0:
        sum = sum + my_list[i]
print(f'{my_list} -> ответ: {sum}')