# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
n = int(input('Введите число: '))
my_list = []
new_list = []
for i in range (n):
    my_list.append(random.randint(0, 100))
for i in range (round(len(my_list) / 2)):
    new_list.append(my_list[i] * my_list[- i - 1] )
print(f'{my_list} => {new_list}')


