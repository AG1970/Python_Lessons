__author__ = 'Александр Гайкалов'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random # для генерации номеров бочонков
import copy #для вывода карточки

#Константы игры
total_barrels = 90 # всего бочонков с номерами
lines_in_card = 3 #строк в карточке
columns_in_card = 9 # колонок (разрядов!) в карточке, ячеек в строке 
numerals_in_line = 5 #номеров в строке
total_numerals = 15 #всего номеров в карточке
max_numerals_in_column = 2 #чисел в разряде; строгое правило классической игры; не сумел реализовать:(


def make_card():
    """Генерация карточки"""
    num_sequence = random.sample(range(1, total_barrels + 1), total_numerals)
    card = [sorted(num_sequence[i:i + numerals_in_line]) for i in range(0, len(num_sequence), numerals_in_line)]
    return card

def display_card(card):
    """Вывод карточки на экран"""
    card = copy.deepcopy(card)  # пользуемся модулем copy для сохранения исходной карточки
    add_space = " ".join(["{:>2}" for i in range(columns_in_card)])  # дополняем ячейки и колонки до необходимого количества
    for line in card:
        for space in " " * (columns_in_card - numerals_in_line):
            line.insert(random.randint(0, len(line) - 1), space)  # Вставляем недостающие пропуски
    return [add_space.format(*line) for line in card]


def make_num_list():
    """Генерирация произвольной последовательности бочонков"""
    numbers = list(range(1, total_barrels + 1))
    random.shuffle(numbers)
    return numbers

def show_barrel(num_list):
    """Выдача очередного бочонка"""
    x = random.randrange(1, len(num_list))
    num_list[-1], num_list[x] = num_list[x], num_list[-1]
    return num_list.pop()

def del_num(card, barrel):
    """Вычёркивание: замена цифры в карте на прочерк, если цифра совпала с номером бочонка"""
    for line in card:
        yield ["-" if x == barrel else x for x in line]

def card_is_empty(card):
    """Проверка; остались ли еще цифры в карточке"""
    for line in card:
        for elt in line:
            if elt != "-":
                return False
    return True

def num_in_card(card, barrel):
    """Проверка: содержится ли номер бочонка в карточке"""
    return barrel in [barrel for line in card for barrel in line]

def game():
    """ Основной цикл игры"""
    player_card = make_card()
    computer_card = make_card()
    barrels = make_num_list()

    while True:
        next_barrel = show_barrel(barrels)
        print("Выпал бочонок №{} (осталось: {})\n".format(next_barrel, len(barrels)))
        print("{0} Ваша карточка {0}\n{1}\n{2}\n{3}\n".format("-" * 6, *display_card(player_card)))
        print("{0} Карточка компьютера {0}\n{1}\n{2}\n{3}".format("-" * 5, *display_card(computer_card)))
        answer = "a"
        while answer not in "ynw":
            answer = input("\nЗачеркнуть цифру?(y/n) (Enter - сразу сдаться, w - победить)\n"
                         "\t? --> ")
        if answer == "w":
            print("Вы победили!!!!!! Так держать!!!! Ура!!!!!!!!!!!!!")
            break
        elif (answer == "y" and num_in_card(player_card, next_barrel)) or (answer == "n" and not num_in_card(player_card, next_barrel)):
            print("\nИгра продолжается...............")
        else:
            print("Вы проиграли")
            break

        player_card = list(del_num(player_card, next_barrel))
        computer_card = list(del_num(computer_card, next_barrel))

        if card_is_empty(player_card):
            print("Победа! Вы заполнили всю карточку!")
            break

        if card_is_empty(computer_card):
            print("Вы проиграли: компьютер заполнил карточку")
            break
        
print("Игра началась!")
game()

