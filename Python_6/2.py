# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Введите вещественное число: ')
sum = sum(map(int, num.replace('.', ' ')))
print (sum)