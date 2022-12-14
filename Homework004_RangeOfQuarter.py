# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти: "))

if quarter == 1:
    print("Координаты X и Y лежат в интервале [(0;∞);(0;∞)]")
elif quarter == 2:
    print("Координаты X и Y лежат в интервале [(∞;0);(0;∞)]")
elif quarter == 3:
    print("Координаты X и Y лежат в интервале [(∞;0);(∞;0)]")
elif quarter == 4:
    print("Координаты X и Y лежат в интервале [(0;∞);(∞;0)]")
else:
    print("Такой четверти не существует")
