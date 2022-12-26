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
                for i in range(len(row_input)):
                    row_input[i] = int(row_input[i])
                return row_input
        except:
            print("Это не целые числа. Попробуй ещё раз")


row_main = input_row()
sum = 0
for i in range(1, len(row_main), 2):
    sum += row_main[i]
print("Сумма нечётных элементов:".upper())
print("на нечётных позициях элементы", end=" ")
for j in range(1, len(row_main), 2):
    print(f"{row_main[j]},", end=" ")
print(f"ответ: {sum}")
