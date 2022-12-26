# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def input_row():
    while True:
        try:
            row_input = input(
                "Введите список вещественных чисел через пробел: ").split()
            for i in range(len(row_input)):
                row_input[i] = float(row_input[i])
            return row_input
        except:
            print("Попробуй ещё раз")


row_main = input_row()
min = max = row_main[0] - int(row_main[0])
for j in range(1, len(row_main)):
    rest = row_main[j] - int(row_main[j])
    if min == 0:
        min = rest
    if 0 < rest < min:
        min = rest
    if 0 < rest > max:
        max = rest
diff = round(max - min, 2)
print(diff)
