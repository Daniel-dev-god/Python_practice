from board import WIN_CONDITIONS, PLAYER_1, PLAYER_2, PLAY_GAME


def set_player_symbol():
    choice = input("Player 1 choose: O or X\n").upper()
    while choice.upper() != "X" and choice != "O":
        choice = input("Incorrect input, Player 1 choose: O or X\n")
    PLAYER_1 = choice
    if PLAYER_1 == "X":
        PLAYER_2 = "O"
    else:
        PLAYER_2 = "X"
    print(f"Player 1 will be {choice}")


def tic_tac_toe():
    pass
