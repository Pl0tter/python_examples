# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

valid = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            left = not (x or y or z)
            right = not x and not y and not z
            if left != right:
                valid = False

if valid == True:
    print("Утверждение истинно")
else:
    print("Утверждение не истинно")
