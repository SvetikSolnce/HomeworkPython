# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input('Введите число: ')
sum = 0
for i in number:
    if i.isdigit():
        sum = sum + int(i)
print(f'{number} -> {sum}')

