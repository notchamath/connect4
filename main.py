import numpy as np

# Size of board
ROWS = 6
COLS = 7


# Create board using numpy
def create_board():
    return np.zeros((ROWS, COLS), "int32")


# Add piece to location chosen by player
def drop_piece(board, row, col, player):
    board[row][col] = player


# Check if column is full
def is_valid_location(board, col):
    return board[0][col] == 0


# Get which row to add piece to
def get_next_open_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 0:
            return row


# Check for winning move
def winning_move(board, player):
    # Horizontal
    for col in range(COLS - 3):
        for row in range(ROWS):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # Vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # Negative Sloped Diagonal
    for col in range(COLS - 3):
        for row in range(ROWS - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Positive Sloped Diagonal
    for col in range(COLS - 3):
        for row in range(3, ROWS):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True


# Print board
def print_board():
    print("\n")
    print(board)


board = create_board()
game_over = False
turn = 0

while not game_over:
    print_board()

    # Check for errors
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

            if winning_move(board, player):
                game_over = True
                print_board()
                print(f"Game over! Player {player} wins!")

            turn += 1
        else:
            print("That column is already filled!")

