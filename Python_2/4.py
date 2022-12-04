# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

from random import randint

N = int(input('Введите число: '))
list = []

for i in range(-N, N - 1):
    list.append(randint(-N, N - 1))
print(list)

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

for i in range(len(list)):
    proiz = list[num1 - 1] * list[num2 - 1]
print(f'Произведение = {proiz}')