##Game Timer

def calculate_score(total_time, total_moves):
    return 500 - (total_time * 0.1 + total_moves * 1)


def display_final_time_and_moves(moves_count, timer):
    print("Finalna liczba ruchów: " + moves_count)
    print("Całkowity czas rozgrywki: " + timer)


def display_final_score(score, moves):
    print("Twój końcowy wynik to: " + calculate_score(score, moves) + '\n')


def display_score(time, moves):
    val = calculate_score(time, moves)
    print("Aktualna liczba punktów: " + str(val))