#Leaderboards
import os

import Dictionaries
import MenuLogic


def place_in_leaderboards(player_name, game_time, number_of_moves, player_score):
    if MenuLogic.get_difficulty_level() == 1:
        if is_on_podium(player_score, Dictionaries.easy_db):
            validate_score(player_name,
                           game_time,
                           number_of_moves,
                           player_score,
                           Dictionaries.easy_db)
    if MenuLogic.get_difficulty_level() == 2:
        if is_on_podium(player_score, Dictionaries.medium_db):
            validate_score(player_name,
                           game_time,
                           number_of_moves,
                           player_score,
                           Dictionaries.medium_db)
    if MenuLogic.get_difficulty_level() == 3:
        if is_on_podium(player_score, Dictionaries.hard_db):
            validate_score(player_name,
                           game_time,
                           number_of_moves,
                           player_score,
                           Dictionaries.hard_db)


def is_on_podium(player_score, file_name):
    separated_list = []
    for element in read_from_file(file_name):
        separated_list.append(element.split())

    score = []
    for element in separated_list:
        score.append(float(element[3]))

    if player_score < score[2]:
        return False
    return True


def validate_score(player_name, game_time, number_of_moves, player_score, file_name):
    buffer = player_name + " " + str(number_of_moves) + " " + str(game_time) + " " + str(player_score)
    contestants = read_from_file(file_name)

    separated_list = []
    for element in contestants:
        separated_list.append(element.split())

    score = []
    for element in separated_list:
        score.append(float(element[3]))

    for i in range(len(score)):
        if score[i] < int(player_score):
            contestants.insert(i, buffer)
            break
    else:
        contestants.append(buffer)
    save_to_file(contestants, file_name)


def save_to_file(list_of_items, file_name):
    file = open(file_name, "w")
    if capacity_not_exceeded(list_of_items):
        file.write('\n'.join(list_of_items))
    else:
        list_of_items.pop(-1)
        file.write('\n'.join(list_of_items))
    file.close()


def capacity_not_exceeded(number_of_contestants):
    return True if len(number_of_contestants) < 6 else False


def read_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
    return lines


# def display_leaderboards():
#     field_names = ('Name', "Time", "Moves", "Score")
#
#     contestants = read_from_file()
#     os.system('clear')
#
#     buffer = '┏━━━'
#     for i in range(len(field_names)):
#         buffer += '┳━━━━━━━━━━━━'
#     buffer += '┓\n'
#
#     buffer += '┃' + ' ╳ ' + '┃'
#
#     for i in field_names:
#         buffer += '    ' + str(i) + '    ┃'
#
#     buffer += '\n┣━━━┫'
#     for i in range(len(field_names)):
#         buffer += '━━━━━━━━━━━┫'
#     buffer += '\n'
#
#     i = 0
#     for line in contestants:
#         buffer += '┃ ' + str(i + 1) + ' ┃'
#         i += 1
#         for element in line.split():
#             if len(element) > 3:
#                 buffer += '\t' + str(element) + '\t┃'
#             else:
#                 buffer += '\t' + str(element) + '\t\t┃'
#         if i < len(contestants):
#             buffer += '\n┣━━━'
#             for _ in range(len(contestants) - 1):
#                 buffer += '╋━━━━━━━━━━━'
#             buffer += '┫'
#             buffer += '\n'
#     buffer += '\n┗━━━'
#     for _ in range(len(field_names)):
#         buffer += '┻━━━━━━━━━━━'
#     buffer += '┛\n'
#     print(buffer)


def display_leaderboards(file_name):
    field_names = ('Name', "Time", "Moves", "Score")
    contestants = read_from_file(file_name)
    os.system('clear')
    buffer = ' X   '
    for el in field_names:
        buffer += el + '       '
    buffer += '\n----'
    for i in range(len(field_names)):
        buffer += '----------'
    buffer += '\n'

    i = 1
    for line in contestants:
        buffer += ' ' + str(i) + '   '
        i += 1
        for element in line.split():
            buffer += element + '\t'
            if ':' in element:
                buffer += '\t'

        buffer += '\n'

    print(buffer)
