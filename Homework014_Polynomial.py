# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

from random import randint


def input_value():
    while True:
        try:
            value_input = int(input("Введите число: "))
            return value_input
        except:
            print("Попробуй ещё раз")


def fill_ratio(degree: int, start: int, stop: int):
    ratio_dict = {}
    for n in range(degree + 1):
        ratio_dict[n] = randint(start, stop)
        while n == degree and ratio_dict[n] == 0:
            ratio_dict[n] = randint(start, stop)
    return ratio_dict


def make_polynomial(ratio_dict: dict):
    polynomial = ""
    degree = 0
    for k in ratio_dict.keys():
        if k > degree:
            degree = k

    for m in range(degree, -1, -1):
        if ratio_dict.get(m, 0) > 0:
            if m != degree:
                polynomial += f" + {ratio_dict[m]}"
            else:
                polynomial += f"{ratio_dict[m]}"
        elif ratio_dict.get(m, 0) < 0:
            if m != degree:
                polynomial += f" - {abs(ratio_dict[m])}"
            else:
                polynomial += f"-{abs(ratio_dict[m])}"
        if m != 1 and m != 0 and ratio_dict.get(m) != None:
            polynomial += f"*x**{m}"
        elif m == 1 and ratio_dict.get(m) != None:
            polynomial += "*x"
        elif m == 0:
            polynomial += " = 0"
    return polynomial


def parsing_polynomial(exist_polynomial: str):
    exist_polynomial = (exist_polynomial.replace(' ', '').replace('-', '+-').replace('*',
                                                                                     '').replace('x+', 'x1+').lstrip('+').rstrip('=0') + "x0").split("+")
    ratio_poly = {}
    for i in range(len(exist_polynomial)):
        exist_polynomial[i] = exist_polynomial[i].split('x')
        ratio_poly[int(exist_polynomial[i][1])] = int(exist_polynomial[i][0])
    return ratio_poly


k = input_value()
ratio = fill_ratio(k, -100, 100)
print("Словарь случайных коэффициентов многочлена:")
print(ratio)

polynomial = make_polynomial(ratio)
print("Получившийся многочлен:")
print(polynomial)

path_poly_write = 'Python/Examples/Homework014_Polynomial.txt'
path_poly_A = 'Python/Examples/Homework014_Polynomial_A.txt'
path_poly_B = 'Python/Examples/Homework014_Polynomial_B.txt'
path_poly_sum = 'Python/Examples/Homework014_Polynomial_Sum.txt'

data = open(path_poly_write, 'w')
data.write(f'{polynomial}\n')
data.close()

data = open(path_poly_A, 'r')
poly_A = data.readline().rstrip('\n')
data.close()

data = open(path_poly_B, 'r')
poly_B = data.readline().rstrip('\n')
data.close()

print("Многочлен из первого файла:")
print(poly_A)
ratio_poly_A = parsing_polynomial(poly_A)

print("Многочлен из второго файла:")
print(poly_B)
ratio_poly_B = parsing_polynomial(poly_B)

ratio_poly_sum = ratio_poly_A
for k in ratio_poly_B.keys():
    ratio_poly_sum[k] = ratio_poly_sum.get(k, 0) + ratio_poly_B.get(k, 0)

print("Сумма первого и второго многочлена:")
print(make_polynomial(ratio_poly_sum))

data = open(path_poly_sum, 'w')
data.write(make_polynomial(ratio_poly_sum))
data.close()
