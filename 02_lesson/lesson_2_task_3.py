# Площадь квадрата

import math
def square(num):
    return math.ceil(num * num)

sq_num = int(input("Сторона квадрата равна: "))
sq = square(sq_num)
print(f"Площадь квадрата: {sq}")
