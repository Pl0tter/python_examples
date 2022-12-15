# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:*
#     5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

n = int(input("Введите число N: "))
my_str = ""
my_list = []

for i in range(-n, n + 1):
    if i < n:
        my_str += str(i) + ", "
    else:
        my_str += str(i)
    my_list.append(i)

print(my_str)
# раскрытие списка * (вывод без [] и запятых) с разделителем sep ", "
print(*my_list, sep=", ")
