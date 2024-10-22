class Board:
    board = ["#", 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self) -> None:
        self.WIN_CONDITIONS = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),  # Rows
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),  # Columns
            (1, 5, 9),
            (3, 5, 7),
        )  # Diagonals
        self.PLAYER_1 = ""
        self.PLAYER_2 = ""
        self.PLAY_GAME = True
        self.MOVES_MADE = 0

    def display_board(self, board):
        print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
        print("-----+-----+-----")
        print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
        print("-----+-----+-----")
        print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")

    def set_player_symbol(self):
        choice = input("Player 1 choose: O or X\n").upper()
        while choice.upper() != "X" and choice != "O":
            choice = input("Incorrect input, Player 1 choose: O or X\n").upper()
        self.PLAYER_1 = choice
        if self.PLAYER_1 == "X":
            self.PLAYER_2 = "O"
        else:
            self.PLAYER_2 = "X"
        print(f"Player 1 will be {choice}")

    def make_move(self, board):
        self.MOVES_MADE += 1
        player_input = input("What position will you play?\n")
        if self.MOVES_MADE % 2 == 1:
            board[int(player_input)] = self.PLAYER_1
        else:
            board[int(player_input)] = self.PLAYER_2

        self.display_board(self.board)

    def check_winner(self, board):
        for condition in self.WIN_CONDITIONS:
            a, b, c = condition
            if board[a] == board[b] == board[c]:
                print("We have a Winner, great job!")
                PLAY_GAME = False
