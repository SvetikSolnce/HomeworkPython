# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Введите число '))
fib_list2 =[]
fib_list1 = []
fib_list = []
fib1, fib2 = 1, 1
for i in range (k):
    fib_list1.append(fib1)
    fib1, fib2 = fib2, fib1 + fib2
fib3, fib4 = 0, 1
for i in range (k+1):
    fib_list2.append(fib3)
    fib3, fib4 = fib4, fib3 - fib4
fib_list2.reverse()
fib_list = fib_list2 + fib_list1
print(f'для k = {k} список будет выглядеть так: {fib_list}')




    


