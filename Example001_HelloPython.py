# print('Hello world')

# --- типы данных и переменная
# --- int, float, boolean, str, list, None

# i = 123
# f = 1.23
# b = True
# s = "hello world"
# list = []
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(list))
# value = None
# print("Переменная value None", type(value))
# value = 12334
# print("Переменная value после присвоения значения", type(value))

# print(s)  # вывод строки
# print(i, f, s)
# print(i, "-", f, "-", s)
# print("{} - {} - {}".format(i, f, s)) # форматирование строки
# print("{1} - {2} - {0}".format(i, f, s)) # форматирование строки с переназначение порядка
# print(f"{i} - {f} - {s}") # интерполяция строки

# list = ["1", "2", "3"]
# col = ["hello", 1, 2, 4.5, True] # в списке возможно использовать разные типы данных
# print(list)
# print(col)

# --- Ввод и вывод данных
# --- print, input

# print("Введите a: ")
# a = input()
# print("Введите b: ")
# b = input()
# print(a, "+", b, "=", a + b)  # в данном случае складываются строки
# print(a, "+", b, "=", int(a) + int(b))  # в данном случае складываются целые числа
# print("{} {}".format(a, b))
# print(f"{a} {b}")

# --- Арифметические операции
# --- +, -, *, /, %, //, **
# --- Приоритет выполнения
# --- **, ⊕, ⊖, *, /, //, %, +, -
# --- (), Сокращенные операции

# a = 7
# b = 3
# print(a + b, a - b, a * b, a / b, a % b, a // b, a**b)
# c = round(a / b, 3)  # округление до 3 знаков
# print(c)

# --- Логические операции
# --- >, >=, <, <=, ==, !=
# --- not, and, or - не путать с &, |, ^
# --- is, is not, in, not in
# --- gen

# a = 3 <= 5
# # print(a)
# b = 1 > 4 and 5 > 2
# # print(b)
# f = [1, 2, 3, 4]
# print(2 in f)  # Проверка на наличие 2 in f
# print(not 2 in f)  # Проверка на отсутствие 2 in f

# is_odd = f[0] % 2 == 0
# is_odd = not f[0] % 2  # аналогично is_odd = f[0] % 2 == 0
# print(is_odd)

# --- Управляющие конструкции
# --- if, if-else

# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input("Введите имя: ")
# if username == "Маша":
#     print("Ура, это же МАША!")
# elif username == "Марина":
#     print("Я так ждала Вас, Марина!")
# elif username == "Ильнар":
#     print("Ильнар - топ)")
# else:
#     print("Привет, ", username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print("Пожалуй")
#     print("хватит )")
# print(inverted)

# --- Управляющие конструкции
# --- for

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i)

# r = range(5)
# for i in range(1, 10, 2):  # начало, конец диапазона, шаг
#     print(i)

# text = "съешь ещё этих мягких французских булок"
# print(len(text))  # 39
# print("ещё" in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace("ещё", "ЕЩЁ"))  #
# print(text[0])
# print(text[6:-25])  # срез строки от 6 элемента до 10 справа
# print(text[::2])  # вывод каждого второго символа начиная с первого

# for c in text:
#     print(c)

# --- Срезы строки

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])  # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2]  # ...

# --- Функции

# def f(x):
#     if x == 1:
#         return "Целое"
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 4
# print(f(arg))
# print(type(f(arg)))
