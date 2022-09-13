# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];    [2, 3, 5, 6] => [12, 15]

numbers = [2, 3, 4, 5, 6]
mult = []
for i in range ((len(numbers)) // 2):
    a = numbers[i] * numbers[-1 - i]
    mult.append(a)
if len(numbers) % 2 != 0:
    b = (numbers[len(numbers) // 2])**2
    mult.append(b)
print(mult)