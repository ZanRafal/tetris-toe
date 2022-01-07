from termcolor import colored as color

import Dictionaries
import LeaderboardsLogic as leads
from modules.getChar import *
import os
import main


def show_game_settings():
    global difficulty_level
    difficulty_level = 2
    os.system('clear')
    print("Wybierz poziom trudności gry:")
    print('[1] Łatwy \n'
          '[2] Średni \n'
          '[3] Trudny \n'
          '[4] Wyjście \n'
          )

    print("Wybrany poziom trudności: " + Dictionaries.Difficulty.get(difficulty_level) + '\n')

    difficulty = get_char()
    if difficulty == '1':
        difficulty_level = 1
        show_game_settings()
    elif difficulty == '2':
        difficulty_level = 2
        show_game_settings()
    elif difficulty == '3':
        difficulty_level = 3
        show_game_settings()
    elif difficulty == '4':
        os.system('clear')
        menu()
    else:
        print(Dictionaries.INVALID_VALUE)


def menu():
    global difficulty_level
    os.system('clear')
    print("Main menu:")
    print('[1] Graj \n'
          '[2] Tablice wyników \n'
          '[3] Ustawienia \n'
          '[4] Sterowanie \n'
          '[5] Wyjście z gry \n'
          )

    val = get_char()

    if val == '1':
        os.system('clear')
        player_name = input_name()
        main.play(player_name)
    elif val == '2':
        os.system('clear')
        show_leaderboards()
    elif val == '3':
        os.system('clear')
        show_game_settings()
    elif val == '4':
        os.system('clear')
        display_controls_view()
    elif val == '5':
        os.system('clear')
        print(Dictionaries.EXIT_MESSAGE)
        exit(0)
    else:
        print(Dictionaries.INVALID_VALUE)


def show_leaderboards():
    os.system('clear')
    print("Tablice wyników: ")

    print('[1]Łatwy \n'
          '[2]Średni \n'
          '[3]Trudny \n'
          '[4]Powrót \n'
          )

    val = get_char()
    if val == '1':
        os.system('clear')
        leads.display_leaderboards(Dictionaries.easy_db)
        fak_go_bak()
    elif val == '2':
        os.system('clear')
        print("leaderboards")
        leads.display_leaderboards(Dictionaries.medium_db)
        fak_go_bak()
    elif val == '3':
        os.system('clear')
        leads.display_leaderboards(Dictionaries.hard_db)
        fak_go_bak()
    elif val == '4':
        os.system('clear')
        menu()
    else:
        print(Dictionaries.INVALID_VALUE)


def display_controls_view():
    print("Sterowanie:")
    print('Do poruszania się po planszy gry należy używać przysków: {}, {}, {}, {}'
          .format(color('W', 'red', attrs=['bold']),
                  color('S', 'red', attrs=['bold']),
                  color('A', 'red', attrs=['bold']),
                  color('D', 'red', attrs=['bold'])
                  ))
    print('Aby potwierdzić wybór należy nacisnąć przycik: {}'
          .format(color('Enter', 'green', attrs=['bold'])
                  ))
    print('Rozgrywkę można opuścić w każdym momencie naciskając przycisk: {} \n\n'
          .format(color('E', 'yellow', attrs=['bold'])
                  ))
    print("[1]Exit")
    val = get_char()
    if val == '1':
        menu()


def fak_go_bak():
    pass
    print("[1] Exit")
    val = get_char()
    if val == '1':
        os.system('clear')
        show_leaderboards()


def get_char():
    while True:
        ch = get_nonblock_char(0.5)
        if ch != '':
            return ch


def input_name():
    print('Podaj imię gracza: ')
    player_name = ''
    while True:
        ch = get_nonblock_char(0.5)
        if ch != '' and ch != '':
            os.system('clear')
            player_name += ch
            print('Podaj imię gracza: {}'.format(player_name))
        if ch == '':
            os.system('clear')
            player_name = player_name[:-1]
            print('Podaj imię gracza: {}'.format(player_name))
        if ch == '\n':
            return player_name


def get_application_properties():
    with open(Dictionaries.app_properties, "r") as file:
        properties = file.read()
    return properties


def set_application_properties(value):
    with open(Dictionaries.app_properties, "w") as file:
        file.write(value)