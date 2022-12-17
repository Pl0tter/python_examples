# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите вещественное число: ')
sum = 0
for char in number:
    if char.isdigit():
        sum += int(char)
print("Решение через строку:")
print(f'{number} -> {sum}')

sum = 0
number_list = number.split('.')
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
    while number_list[i] > 10:
        sum += number_list[i] % 10
        number_list[i] //= 10
    sum += number_list[i]
print("Решение арифметически:")
print(f'{number} -> {sum}')
