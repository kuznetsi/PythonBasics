import random
# Задание 4
# Решение 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
def ager(name, age, city):
    print(f'{name}, {age} год(а), проживает в городе {city}')
name = input('Введие имя: ')
age = input('Введие возраст: ')
city = input('Введие город проживания человека: ')
ager(name, age, city)

# Решение 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
# numbers = []
# for i in range(3):
#     number = int(input('Введие число: '))
#     numbers.append(number)
# print(f'Исходный список: {numbers}')
# print(f'Наибольшее число в списке: {max(numbers)}')

# Решение 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
# 4: Давайте усложним предыдущее задание.
# Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание.
# Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

# Бойцовкий клуб (Fight club)
player_1 = {
    'name': input('Введите имя 1-го игрока: '),
    'health': 100,
    'damage': random.randint(1, 50),
    'armor': 1.2
}
player_2 = {
    'name': input('Введите имя 2-го игрока: '),
    'health': 100,
    'damage': random.randint(1, 50),
    'armor': 1.2
}

# Функции для отрисовки таблицы
# Функция высчитывания длины ключа
def max_len_name_key(dictionary):
    len_col = 0
    for key in dictionary.keys():
        # print(len(key))
        if len(str(key)) > len_col:
            len_col = len(key)
    return len_col

# Функция высчитывания длины значения ключа
def max_len_name_val(dictionary):
    len_val = 0
    for val in dictionary.values():
        # len_val = len(str(val))
        if len(str(val)) > len_val:
            len_val = len(str(val))
            # print(f'{val} = {len_val}')
        else:
            len_val = len_val
    # print('len_val=', len_val)
    return len_val

# Функция добавления пробелов для отрисовки таблицы
def print_sep(key, len_str):
    len_space = int(len_str) - len(str(key))
    # print(len_space)
    str_space = ''
    while len_space != 0:
        str_space = str_space + ' '
        len_space -= 1
    return str_space

# Выбираем того, кто будет бить первым
start_game = random.randint(1, 2)

if start_game == 1:
    player = player_1
    enemy = player_2
else:
    player = player_2
    enemy = player_1

# Вывод информации об играках
def players_opt(player, enemy):
    print(f'Характеристки игроков')
    for key in player.keys():
        print(f'|{key}{print_sep(key,max_len_name_key(player) )}'
              f'|{player[key]}{print_sep(player[key],max_len_name_val(player))}'
              f'|{enemy[key]}{print_sep(enemy[key],max_len_name_val(enemy))}'
              f'|')
    print('\nБой начинается...\n')
    print(f'Начинает игрок под номером {start_game}: {player["name"]}')

players_opt(player_1, player_2)

# Функция атаки игрока
def attack(player, enemy):
    enemy['health'] = enemy['health'] - player['damage']
    # t = float(enemy['health'])-float(armor_attack(player['damage'], enemy['armor']))
    # print(f'{player["name"]}({enemy["health"]})')
    print(f'Урон {player["damage"]}')

# Функция применения щита
def armor_attack(player_damage, enemy_armor):
    enemy_damage = player_damage['damage'] / enemy_armor['armor']
    enemy['health'] = round(enemy['health'] - enemy_damage, 3)
    print(f'Урон {round(enemy_damage, 3)}')
    return enemy_damage

is_winner = False
winner_name = None

while not is_winner:
    print(f'{player["name"]}({player["health"]}) бьёт -> {enemy["name"]}({enemy["health"]}) ')
    block = random.randint(1, 2)
    # Если 1, то без блокировки
    # Если 2, то с блокировкой
    if block == 1:
        print(f'{enemy["name"]} не успел выставить блок')
        attack(player, enemy)

    else:
        print(f'{enemy["name"]} успел выставить блок')
        armor_attack(player, enemy)
    if player["health"] <= 0:
        print(f'Победил {enemy["name"]}({enemy["health"]})')
        is_winner = True
        break
    elif enemy["health"] <= 0:
        print(f'Победил {player["name"]}({player["health"]})')
        is_winner = True
        break

    buffer_player = player
    buffer_enemy = enemy
    player = buffer_enemy
    enemy = buffer_player