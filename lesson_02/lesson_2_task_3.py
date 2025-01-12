import math


def square(side):
    side = math.ceil(side)
    res = side * side
    return res


side = float(input("Введите сторону квадрата: "))
print(square(side))
