import random

# Задание словаря
my_dict = {"key1": 1, "key3": 3, "keyA": "A", 4: 4,
           345: 345, 'keyABC': {"A", "B", "C"}, 456: {4, 5, 6}}
print(my_dict)
print(my_dict[345])
# при отсутствии элемента get выдаст None, в отличии от my_dict[] когда программа выдаст ошибку
print(my_dict.get(456))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
# my_dict.keys() - обращение к ключу
# my_dict.values() - обращение к значению
# my_dict.items() - обращение и к ключу, и к значению
for item in my_dict.values():
    print(item)
# my_dict.pop - удаление ключа
test_dict = {}
for i in range(10):
    test_dict[i] = random.random() * 10
print(test_dict)
