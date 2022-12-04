# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Введите число: '))
list = [(1+1/n)**n for n in range(1, n+1)]
print(list)
summa = 0

for n in range(n):
    n += 1
    summa += (1+1/n)**n
    print(summa) 