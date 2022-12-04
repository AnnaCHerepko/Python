# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19           # 5 == 5.00?

# разница между дробной части максимального и минимального числа

# arr = [1.1, 1.2, 3.1, 5, 10.01]
# min = arr[0]
# max = 0

# for i in range(len(arr)):
    
#     if max < arr[i]:
#         max = arr[i]

#     if min > arr[i]:
#         min = arr[i]
# dif = (max - int(max)) - (min - int(min))

# print(arr)
# print(max, min)
# print(round(dif, 2))

# разница между максимальным и минимальным значением дробной части

arr = [1.1, 1.2, 3.1, 5, 10.01]
min = arr[0]
max = 0

for i in range(len(arr)):
    
    if max < arr[i] % 1:
        max = arr[i] % 1

    if min > arr[i] % 1:
        min = arr[i] % 1
dif = (max - int(max)) - (min - int(min))

print(arr)
print(round(max, 2), min)
print(round(dif, 2))