# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

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
row_result = []
product = 0
for i in range(len(row_main) // 2 + len(row_main) % 2):
    row_result.append(int(row_main[i]) * int(row_main[len(row_main) - 1 - i]))
print(row_result)
