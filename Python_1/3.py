# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

x = int(input())
y = int(input())

if x == 0:
    print('x не должен равняться 0')
if y == 0:
    print('y не должен равняться 0')

elif x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
else:
    print('Четвертая четверть')