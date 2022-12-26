# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def input_value():
    while True:
        try:
            value_input = int(input("Введите число Фибоначчи: "))
            return value_input
        except:
            print("Попробуй ещё раз")


def fib_neg_pos(n: int):
    if n == 0:
        return 0
    if n == 1 or n == -1:
        return 1
    if n < -1:
        return fib_neg_pos(n + 2) - fib_neg_pos(n + 1)
    if n > 1:
        return fib_neg_pos(n - 2) + fib_neg_pos(n - 1)


k = input_value()
row_fibo = []

for e in range(-k, k + 1):
    row_fibo.append(fib_neg_pos(e))

print(row_fibo)
