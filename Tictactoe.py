#Generate a basic tic tac toe game
# Importing the random module
import random
# Function to print the board

#Create a class for the game
class wrongcode():
    print("This is a wrong code")

def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the game is over
def is_game_over(board):
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to get the available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

# Function to make a move
def make_move(board, row, col, player):
    if board[row][col] != " ":
        raise ValueError("The cell is already occupied.")
    board[row][col] = player
    
# Function to get the computer's move
def get_computer_move(board):
    moves = get_available_moves(board)
    if moves:
        return random.choice(moves)
    return None
# Function to play the game

def play_game():
    """
    Plays a game of Tic Tac Toe between a human player and the computer.

    The game alternates turns between the human player ('X') and the computer ('O').
    The board is displayed after each move, and the game ends when there is a winner
    or the board is full, resulting in a draw. The human player inputs their move
    by specifying the row and column, while the computer selects its move randomly.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            while True:
                try:
                    move = get_computer_move(board)
                    if move is None:
                        print("No moves available for the computer.")
                        break
                    row, col = move
                    print(f"Computer chose: {row} {col}")
                    break
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")
        else:
            row, col = get_computer_move(board)
            print(f"Computer chose: {row} {col}")
        make_move(board, row, col, current_player)
        if is_game_over(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        player_switch = {"X": "O", "O": "X"}
        current_player = player_switch[current_player]

# Main function to start the game
if __name__ == "__main__":
    play_game()
# This code implements a simple Tic Tac Toe game where a player can play against the computer.
# The player is represented by "X" and the computer by "O". The game checks for wins, draws, and available moves.
# The player inputs their move by specifying the row and column, and the computer randomly selects its move from the available options.
# The game continues until there is a winner or the board is full, resulting in a draw.
# The board is printed after each move, showing the current state of the game.
# The game is played in a console environment, and the player interacts with it through text input.

