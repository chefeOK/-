# Tic-Tac-Toe Game

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    print('---------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('---------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('---------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('---------')

# Function to check if the game is over
def is_game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    # Check if the board is full
    if ' ' not in board:
        return True
    return False

# Function to make a move
def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    else:
        return False

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    current_player = 'X'
    while not is_game_over():
        position = int(input(f"Player {current_player}, enter your move (0-8): "))
        if make_move(current_player, position):
            print_board()
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("Invalid move. Try again.")
    print("Game over!")

# Start the game
play_game()