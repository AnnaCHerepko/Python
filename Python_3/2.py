# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

arr = [2, 3, 4, 5, 6]
size = len(arr)
arr2 = []

for i in range(len(arr)):
    while i < len(arr)/2 and size > len(arr)/2:
        size -= 1
        proiz = arr[i] * arr[size]
        arr2.append(proiz)
        i += 1

print(arr)
print(arr2)