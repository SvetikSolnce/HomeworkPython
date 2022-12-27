# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
import random
n = int(input('Введите число: '))
my_list = []
nums = []
for i in range (n):
    my_list.append(round(random.uniform(0, 100), 2))
for i in range(len(my_list)):
    nums.append(round(my_list[i] - int(my_list[i]), 2))
for n in range(len(nums)):
    my_max = nums[0]
    my_min = nums[0]
    if nums[n] > my_max and nums[n] != 0:
        my_max = nums[n]
    if nums[n] < my_min and nums[n] != 0:
        my_min = nums[n]
    res = my_max - my_min
print(f'{my_list} => {round(res, 2)}')
    
    

