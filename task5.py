# 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  

n = int(input('введите целое положительное число больше двух: N= '))

fib1 = []
for i in range(0,n+1):
    if i == 0:
        a = 0
        fib1.append(a)
    elif i == 1:
        a = 1
        fib1.append(a)
    else:
        a = fib1[i-1] + fib1[i-2]
        fib1.append(a)

fib2 = []
for i in range(n):
    if i == 0:
        a = 1
        fib2.append(a)
    elif i == 1:
        a = -1
        fib2.append(a)
    else:
        a = fib2[i-2] - fib2[i-1]
        fib2.append(a)

fib2.reverse()
print(fib2 + fib1)
    
