# Далее, пусть есть координаты точки
# point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

from math import sqrt

x, y, r = 23, 34, 42
point_1 = sqrt(x ** 2 + y ** 2)
print("Расстояние до точки от начала координат равно %.2f" % point_1)
if point_1 > r:
    print("False - точка лежит вовне круга")
else:
    print("True - точка внутри круга")