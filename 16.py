# Координаты точки P
x, y = 0, 0

# Проверка попадания в круг
distance_to_center_circle = ((x - 1)** 2 + y **2) ** 0.5
if distance_to_center_circle <= 2:
    in_circle = True
else:
    in_circle = False

# Проверка попадания в прямоугольник
if (-2 < x < 2) and (-3 < y < 3):
    in_rectangle = True
else:
    in_rectangle = False

# Вывод результата
if in_circle and not in_rectangle:
    print("yes no")
elif in_rectangle and not in_circle:
    print("no yes")
elif in_circle and in_rectangle:
    print("yes yes")
else:
    print("no no")