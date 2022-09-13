# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.

numbers = [1.1, 1.2, 3.1, 5, 10.01]
new_numbers =[]
import math
for i in range (len(numbers)):
    residue = round((numbers[i] - math.trunc(numbers[i])),3)
    new_numbers.append(residue)
print(new_numbers)
print(max(new_numbers) - min(new_numbers))

