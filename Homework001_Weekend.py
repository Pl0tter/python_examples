# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input("Введите число дня недели: "))
if 1 <= number <= 5:
    print("нет")
elif 6 <= number <= 7:
    print("да")
else:
    print("такого дня нет")
