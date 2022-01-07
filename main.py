# Rafał Zan
# 311 214
import time
from termcolor import colored
import Board
import Dictionaries
import MenuLogic as gameMenu
import Shapes
import TimerLogic as tl
import LeaderboardsLogic as leaderboards
from modules.getChar import *


def main():
    gameMenu.menu()


def play(player_name):
    my_board = Board.init_board(gameMenu.get_difficulty_level())
    start = time.time()
    moves_count = 0
    row = col = 4
    new_figure = Shapes.get_shape(gameMenu.get_difficulty_level())
    Board.display_board(my_board.copy())
    while Board.number_of_x(my_board) != 0:
        ch = get_nonblock_char(0.5)
        time.sleep(0.01)
        if ch != '':
            row, col = change_position(ch, row, col)
            if ch == '\n':
                moves_count += 1
                Shapes.choose_from_set(row, col, new_figure, my_board)
                new_figure = Shapes.get_shape(gameMenu.get_difficulty_level())
                row = col = 4
        display_on_game(time.time() - start, new_figure, row, col, my_board, moves_count)
    init_last_step(moves_count, time.time() - start)


def display_on_game(timer, new_figure, row, col, my_board, moves_count):
    Board.update_display(row, col, new_figure, my_board)
    display_current_moves_count(moves_count)
    display_time(int(timer))
    tl.display_score(int(timer), moves_count)


def change_position(var, row, col):
    tmp = 8 + (gameMenu.get_difficulty_level() - 1) * 4

    if var == 'w':
        return row % tmp, (col - 1) % tmp
    elif var == 'a':
        return (row - 1) % tmp, col % tmp
    elif var == 's':
        return row % tmp, (col + 1) % tmp
    elif var == 'd':
        return (row + 1) % tmp, col % tmp
    elif var == 'e':
        gameMenu.menu()
    return row, col


def display_current_moves_count(moves_count):
    print("Aktualna liczba ruchów: {}".format(moves_count))


def display_win_message():
    print(Dictionaries.WIN_MESSAGE)


def display_time(value):
    seconds = value % 60
    minutes = value // 60
    if seconds <= 9:
        print('Czas rozgrywki: {} : 0{}'.format(minutes, seconds))
    else:
        print('{} : {}'.format(minutes, seconds))


def init_last_step(moves_count, total_time, player_name):
    display_win_message()
    tl.display_final_time_and_moves(moves_count, total_time)
    final_score = tl.calculate_score(total_time, moves_count)
    tl.display_final_score(moves_count, final_score)
    leaderboards.place_in_leaderboards(player_name, total_time, moves_count, final_score)
    display_credits()


def display_credits():
    print('\n\n\n\n \t\t\t\t\t\t\t\t Game created by {}'
          .format(colored('Rafał Zan', 'yellow', attrs=['bold'])))
    print(' \t\t\t\t\t\t\t\t Student of {}'
          .format(colored('Warsaw University of Technology', 'yellow', attrs=['bold'])))
    print(' \t\t\t\t\t\t\t\t Thank you for playing {}'
          .format(colored('<3', 'red', attrs=['bold'])))


if __name__ == "__main__":
    main()
