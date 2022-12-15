# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# # Работа как с числом
number = float(input("Введите дробное число: "))
rest = (number * 10) % 10
if number == int(number):
    print("нет")
else:
    print(round(rest))

# # Работа как со строкой
# number = input("Введите дробное число: ")
# number = number.split(".")
# if len(number) < 2:
#     print("нет")
# else:
#     print(number[1][0])
