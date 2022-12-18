# 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
number = int(input('Введите число: '))
my_list = []
new_list = []
sum = 0
for n in range(1, number+1):
    my_list.append((1+1/n)**n)
    for i in range(len(my_list)):
        p = round(my_list[i], 2)
    new_list.append(p)
    sum = sum + p
print(f'Для n={n} -> {new_list}')
print(f'Сумма {sum}')