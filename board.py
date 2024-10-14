class Board:
    board = ["#", 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self) -> None:
        self.WIN_CONDITIONS = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),  # Rows
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),  # Column
            (1, 5, 9),
            (3, 5, 7),
        )  # Diagonals
        self.PLAYER_1 = ""
        self.PLAYER_2 = ""
        self.PLAY_GAME = True

    def display_board(self, board):
        print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
        print("-----+-----+-----")
        print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
        print("-----+-----+-----")
        print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")

    def make_move(self, board):
        player_input = input("What position will you play?\n")
        board[int(player_input)] = "X"
        self.display_board(self.board)

    def check_winner(self, board):
        for condition in self.WIN_CONDITIONS:
            a, b, c = condition
            if board[a] == board[b] == board[c]:
                print("We have a Winner, great job!")
                PLAY_GAME = False


test1 = Board()
test1.display_board(test1.board)
test1.make_move(test1.board)
