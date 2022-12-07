# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = list(map(int, input("Введите числа:\n").split()))
new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)