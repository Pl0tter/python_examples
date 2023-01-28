# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом
import random


def field_print(field):
    for i in range(len(field)):
        if i != 2 and i != 5 and i != 8:
            print(field[i], end=" | ")
        elif i == 2 or i == 5:
            print(field[i])
            print("---------")
        elif i == 8:
            print(field[i])


def turn_human():
    while True:
        try:
            turn = int(input('В какую клетку сделать ход? '))
            if 1 <= turn <= 9:
                if type(field[turn-1]) == str:
                    print("Ячейка занята")
                else:
                    return turn
            else:
                print(f"Нет такой ячейки")
        except:
            print(f"Необходимо ввести число")


def check_win():
    for line in wins:
        if field[line[0]] == field[line[1]] == field[line[2]] == "X":
            return 1
        elif field[line[0]] == field[line[1]] == field[line[2]] == "O":
            return 0
    draw = True
    for elem in field:
        if type(elem) == int:
            draw *= 0
    if draw == True:
        return 2


def turn_bot():
    for i in [2, 1, 0]:
        if i == 0:
            if type(field[4]) == int:
                return 5
            else:
                return 1
        for row in wins:
            count_O = 0
            count_X = 0

            for j in range(len(row)):
                if field[row[j]] == "O":
                    count_O += 1
                if field[row[j]] == "X":
                    count_X += 1
            if count_O == i or count_X == i:
                for l in range(len(row)):
                    if field[row[l]] != "O" and field[row[l]] != "X":
                        return row[l] + 1
            if i == 1 and type(field[4]) == int:
                return 5
            elif i == 1 and count_O == 0 and count_X == i:
                for l in range(len(row)):
                    if field[row[l]] != "O" and field[row[l]] != "X":
                        return row[l] + 1


field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

wins = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
        [1, 4, 7], [2, 5, 8]]

while True:
    play = int(input("Сыграем? 1 - да, 2 - нет: "))
    if play == 1:
        enemy = int(
            input("Выберите против кого будете играть, где 1 - это человек, 2 - бот: "))
        player = bool(random.randint(0, 1))
        print(f'Результат жеребьевки - первым ходит игрок {int(player)+1}')

        while True:
            field_print(field)
            if check_win() == 0:
                print("Выиграл игрок 1")
                break
            elif check_win() == 1:
                print("Выиграл игрок 2")
                break
            elif check_win() == 2:
                print("Ничья")
                break

            if enemy == 1:
                print(f"--- Ходит игрок {player+1}")
                turn = turn_human()
                if int(player) == 0:
                    field[turn-1] = "O"
                else:
                    field[turn-1] = "X"
                player = not player
            elif enemy == 2:
                if int(player) == 0:
                    turn = turn_human()
                    field[turn-1] = "O"
                else:
                    turn = turn_bot()
                    print(f"Бот ходит в клетку: {turn}")
                    field[turn-1] = "X"
                player = not player

    elif play == 2:
        break
