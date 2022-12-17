# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int

from random import randint

l = 10
list_origin = []
for i in range(l):
    list_origin.append(randint(10, 99))
print("Исходный список:")
print(list_origin)

for j in range(len(list_origin)):
    list_origin.insert(j, list_origin.pop(randint(j, len(list_origin) - 1)))
print("Перемешанный методами insert&pop список:")
print(list_origin)

# ----
list_index = []
list_shuffle = []

for k in range(len(list_origin)):
    item = randint(0, len(list_origin) - 1)
    while item in list_index:
        item = randint(0, len(list_origin) - 1)
    list_shuffle.append(list_origin[item])
    list_index.append(item)
print("Перемешанный список без использования методов списка:")
print(list_shuffle)
