# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random
max_take = 28


def take_human():
    while True:
        try:
            take = int(input(f"Сколько конфет берет игрок: "))
            if 0 < take <= max_take:
                return take
            else:
                print(f"Необходимо взять от 1 до {max_take} конфет")
        except:
            print(f"Необходимо ввести число")


def take_bot():
    if candies % (max_take + 1) == 0:
        take = random.randint(1, max_take)
    else:
        take = candies % (max_take + 1)
    print(f"Сколько конфет берет бот: {take}")
    return take


while True:
    play = int(input("Сыграем? 1 - да, 2 - нет: "))
    if play == 1:
        candies = int(input("Введите количество конфет: "))
        enemy = int(
            input("Выберите против кого будете играть, где 1 - это человек, 2 - бот: "))
        
        turn = bool(random.randint(0, 1))
        if enemy == 1:
            print(f'Результат жеребьевки - первым ходит игрок {int(turn)+1}')
        elif enemy == 2 and turn == 0:
            print("Результат жеребьевки - первым ходит игрок")
        elif enemy == 2 and turn == 1:
            print("Результат жеребьевки - первым ходит бот")

        while candies > max_take:
            if enemy == 1:
                print(f"--- Ходит игрок {int(turn)+1}")
                candies -= take_human()
            elif enemy == 2:
                if turn == 0:
                    print(f"--- Ходит игрок")
                    candies -= take_human()
                else:
                    print(f"--- Ходит бот")
                    candies -= take_bot()
            print(f"### На столе осталось конфет: {candies}")
            turn = not turn

        if enemy == 1:
            print(f"!!! Выиграл игрок {int(turn)+1}")
        elif enemy == 2 and turn == 0:
            print("!!! Выиграл игрок")
        elif enemy == 2 and turn == 1:
            print("!!! Выиграл бот")
    elif play == 2:
        break
