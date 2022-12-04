# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

arr = [2, 3, 5, 9, 3]
size = len(arr)
sum = 0
index = 0

while index < size:
    if index % 2 == 1:
        sum += arr[index]
    index += 1
print(sum)