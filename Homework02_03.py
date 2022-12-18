# 3. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

import random

n = int(input('Введите число: '))
my_list = []
for i in range (n):
    my_list.append(random.randint(0, 100))
new_list = my_list[:]
for i in range (len(new_list)):
    index_list = random.randint(0, len(new_list) - 1)
    temp = new_list[i]
    new_list[i] = new_list[index_list] 
    new_list[index_list] = temp
print(f'Случайный список: {my_list}')
print(f'Перемешанный список: {new_list}')
