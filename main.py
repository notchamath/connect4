import numpy as np

ROWS = 6
COLS = 7


def create_board():
    return np.zeros((ROWS, COLS), "int32")


def drop_piece(board, row, col, player):
    board[row][col] = player


def is_valid_location(board, col):
    return board[0][col] == 0


def get_next_open_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 0:
            return row


def winning_move(board, player):
    pass


board = create_board()
game_over = False
turn = 0

while not game_over:
    print("\n")
    print(board)

    try:
        # Player 1 input
        if turn % 2 == 0:
            col = int(input("Player 1 make your selection (0-6): "))
        # Player 2 input
        else:
            col = int(input("Player 2 make your selection (0-6): "))

        if col >= COLS:
            raise IndexError

    except ValueError:
        print("Not a number")
    except IndexError:
        print("Pick a number between 0 and 6")

    else:

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            player = turn % 2 + 1
            drop_piece(board, row, col, player)

            turn += 1
        else:
            print("That column is already filled!")

