###Logika menu
import os
import Dictionaries
import LeaderboardsLogic as leads
from termcolor import colored as color

difficulty_level = 2


def show_game_settings():
    global difficulty_level
    os.system('clear')
    print("Wybierz poziom trudności gry:")
    print('[1]Łatwy \n'
          '[2]Średni \n'
          '[3]Trudny \n'
          '[4]Wyjście \n'
          )

    print("Wybrany poziom trudności: " + Dictionaries.Difficulty.get(difficulty_level) + '\n')

    difficulty = input()
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
        print("Podano nieprawidłową wartość:")


def get_difficulty_level():
    return difficulty_level


def menu():
    os.system('clear')
    print("Main menu:")
    print('[1]Graj \n'
          '[2]Tablice wyników \n'
          '[3]Ustawienia \n'
          '[4]Sterowanie \n'
          '[5]Wyjście z gry \n'
          )
    val = input()
    if val == '1':
        os.system('clear')
        #play()
        print("Play")
    elif val == '2':
        os.system('clear')
        print("leaderboards")
        show_leaderboards()
    elif val == '3':
        os.system('clear')
        print("settings")
        show_game_settings()
    elif val == '4':
        os.system('clear')
        print("Sterowani")
        display_controls_view()
    elif val == '5':
        os.system('clear')
        print("Do zobaczenia następnym razem :D ")
        exit(0)
    else:
        print("Podano nieprawidłową wartość:")


def show_leaderboards():
    os.system('clear')
    print("Tablice wyników: ")

    print('[1]Łatwy \n'
          '[2]Średni \n'
          '[3]Trudny \n'
          '[4]Wyjście z gry \n'
          )

    val = input()
    if val == '1':
        os.system('clear')
        leads.display_leaderboards()
        fak_go_bak()
    elif val == '2':
        os.system('clear')
        print("leaderboards")
        leads.display_leaderboards()
        fak_go_bak()
    elif val == '3':
        os.system('clear')
        leads.display_leaderboards()
        fak_go_bak()
    elif val == '4':
        os.system('clear')
        show_leaderboards()
    else:
        print("Podano nieprawidłową wartość")


def display_controls_view():
    print("Sterowanie:")
    print('Do poruszania się po planszy gry należy używać przysków: {}, {}, {}, {}'
          .format(color('W', 'red',attrs=['bold']),
                  color('S', 'red',attrs=['bold']),
                  color('A', 'red',attrs=['bold']),
                  color('D', 'red',attrs=['bold'])
                  ))
    print('Aby potwierdzić wybór należy nacisnąć przycik: {}'
          .format(color('Enter', 'green',attrs=['bold'])
                  ))
    print('Rozgrywkę można opuścić w każdym momencie naciskając przycisk: {} \n\n'
          .format(color('E', 'yellow',attrs=['bold'])
                  ))
    fak_go_bak()


def fak_go_bak():
    print("[1] Exit")
    val = input()
    if val == '1':
        os.system('clear')
        show_leaderboards()


display_controls_view()