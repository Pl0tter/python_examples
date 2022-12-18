# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.

text = "Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую."
print(text)
subtext = input("Введите строку: ")

text_list = text.split()
count = 0
for i in text_list:
    if subtext in i:
        count += 1
print(f"Количество слов с вхождением: {count}")

count_func = text.count(subtext)
print(f"Количество вхождений подсчитанных методом count: {count_func}")

count_char = 0
for char in text:
    if subtext == char:
        count_char += 1
print(f"Количество вхождений символа: {count_char}")

count_cut = 0
for j in range(len(text)):
    if subtext == text[j:j+len(subtext)]:
        count_cut += 1
print(f"Количество вхождений подсчитанных срезом строки: {count_cut}")

text_count = text.split(subtext)
print(
    f"Количество вхождений подсчитанных сплитом по вхождению: {len(text_count)-1}")
