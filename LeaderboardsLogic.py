##Leaderboards
import os
import MenuLogic



def show_leaderboards():
    os.system('clear')
    print("Tablice wyników")


    exit =  input()
    print("[1]Wyjście")
    if exit == '1':
        MenuLogic.menu()


def save_to_leaderboards(player_name, game_time, number_of_moves,  player_score):
    buffer = player_name + " " + str(number_of_moves) + " " + str(game_time) + " " + str(player_score)
    if capacity_not_exceeded():
        file = open("leaderboards_db.txt", "a+")
        file.write(buffer)
        file.close()


def capacity_not_exceeded():
    pass

def read_from_file():
    pass


def save_to_file():
    file = open("leaderboards_db.txt", "w+")
