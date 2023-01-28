# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# ---LIST COMPREHENSION & ENUMERATE
# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введите число n: '))
sum = 0
result = [round((1 + 1/x)**x, 2) for x in range(1, n+1)]
for i, item in enumerate(result):
    sum += item
print(f'Для n={n} -> {result}')
print(f'Сумма {round(sum,2)}')

# ---LIST COMPREHENSION & ENUMERATE & LAMBDA & MAP
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def input_row():
    while True:
        try:
            row_input = input(
                "Введите список из нескольких чисел через пробел: ").split()
            if len(row_input) < 2:
                print("Это не список. Попробуй ещё раз")
            else:
                row_input = list(map(int, row_input))
                return row_input
        except:
            print("Это не целые числа. Попробуй ещё раз")


row_main = input_row()
sum = 0
row_main = enumerate(row_main)
row_main = filter(lambda item: item[0] % 2, row_main)

for i, item in row_main:
    sum += item
print(f"Ответ: {sum}")
