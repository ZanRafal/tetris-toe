##Leaderboards
import os


def is_on_podium(player_score):
    separated_list = []
    for element in read_from_file():
        separated_list.append(element.split())

    score = []
    for element in separated_list:
        score.append(float(element[3]))

    if player_score < score[2]:
        return False
    return True


def validate_score(player_name, game_time, number_of_moves, player_score):
    buffer = player_name + " " + str(number_of_moves) + " " + str(game_time) + " " + str(player_score)
    list = read_from_file()

    separated_list = []
    for element in list:
        separated_list.append(element.split())

    score = []
    for element in separated_list:
        score.append(float(element[3]))

    for i in range(len(score)):
        if score[i] < int(player_score):
            list.insert(i, buffer)
            break
    else:
        list.append(buffer)
    save_to_file(list)


def save_to_file(list_of_items):
    file = open("leaderboards_db.txt", "w")
    if capacity_not_exceeded(list_of_items):
        file.write('\n'.join(list_of_items))
    else:
        list_of_items.pop(-1)
        file.write('\n'.join(list_of_items))
    file.close()


def capacity_not_exceeded(list):
    return True if len(list) < 6 else False


def read_from_file():
    with open("leaderboards_db.txt", "r") as file:
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


def display_leaderboards():
    field_names = ('Name', "Time", "Moves", "Score")
    contestants = read_from_file()
    # os.system('clear')
    buffer =  ' X   '
    for el in field_names:
        buffer += el + '       '
    buffer += '\n----'
    for i in range(len(field_names)):
        buffer += '-----------'
    buffer += '\n'

    i = 0
    for line in contestants:
        buffer += ' ' + str(i + 1) + '   '
        i += 1
        for element in line.split():
            if '.' in element: buffer += '\t'
            buffer += element + '   \t'
            if ':' in element: buffer += '\t'

        buffer += '\n'

    print(buffer)
