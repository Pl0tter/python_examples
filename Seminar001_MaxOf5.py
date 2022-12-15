# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

list = []

for i in range(5):
    list.append(int(input(f"Введите {i+1} число: ")))
print(list)

max = list[0]

for i in range(1, len(list)):
    if max < list[i]:
        max = list[i]

print(max)

# Получение случайного значения
# import random
# random.randint(0,5)
