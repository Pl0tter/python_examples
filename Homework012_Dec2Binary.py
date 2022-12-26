# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def input_value():
    while True:
        try:
            value_input = int(input("Введите десятичное число: "))
            return value_input
        except:
            print("Попробуй ещё раз")


value = input_value()
result = ""
while value > 1:
    result += str(value % 2)
    value //= 2
    if value < 2:
        result += str(value)

print(result[::-1])
