# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from functools import reduce
A = list(map(int, input('Введите координаты точки A: ').split())) 
B = list(map(int, input('Введите координаты точки B: ').split()))
def dot_range(A, B):
     res = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(A, B))))
     return round(res, 2)
print(dot_range(A, B))