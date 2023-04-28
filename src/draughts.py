# Checker Game in Python

# Constants
EMPTY = "-"
BLACK = "b"
WHITE = "w"
KING_BLACK = "B"
KING_WHITE = "W"

# Board representation
board = [
    [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
    [BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY],
    [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
    [EMPTY] * 8,
    [EMPTY] * 8,
    [WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY],
    [EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE],
    [WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY]
]

# Helper function to display the board
def display_board():
    print("  0 1 2 3 4 5 6 7")
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            row += board[i][j] + " "
        print(str(i) + " " + row)

# Function to get a move from the user
def get_move(player):
    while True:
        try:
            # Prompt the user to enter the row and column of the piece they want to move
            start_row, start_col = map(int, input(f"Player {player}'s turn. Enter the row and column of the piece you want to move (e.g. 1 2): ").split())
            # Prompt the user to enter the row and column of the destination cell
            end_row, end_col = map(int, input("Enter the row and column of the destination cell: ").split())
            # Check if the move is valid
            if is_valid_move(start_row, start_col, end_row, end_col, player):
                # If the move is valid, return it as a tuple
                return (start_row, start_col, end_row, end_col)
            else:
                # If the move is not valid, print an error message and prompt the user to enter a valid move
                print("Invalid move. Please enter a valid move.")
        except ValueError:
            # If the user enters invalid input, print an error message and prompt them to enter valid input
            print("Invalid input. Please enter valid input.")

# Function to check if a move is valid
def is_valid_move(start_row, start_col, end_row, end_col, player):
    # Check if start and end coordinates are valid
    if board[start_row][start_col] != player:
        return False
    if end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
        return False
    if board[end_row][end_col] != EMPTY:
        return False

    # Check if move is diagonal
    if abs(end_row - start_row) != 1 or abs(end_col - start_col) != 1:
        # Check for jump move
        if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
            jumped_row = (end_row + start_row) // 2
            jumped_col = (end_col + start_col) // 2
            if board[jumped_row][jumped_col] in [player, player.upper()]:
                return False
        else:
            return False

    # Check if player is moving in the right direction
    if player == BLACK and end_row < start_row:
        return False
    elif player == WHITE and end_row > start_row:
        return False

    # Valid move
    return True

# Function to make a move
def make_move(player, start_row,
                start_col, end_row, end_col):
        # Make move
        board[start_row][start_col] = EMPTY
        board[end_row][end_col] = player

        # Check if piece should be kinged
        if player == BLACK and end_row == 7:
            board[end_row][end_col] = KING_BLACK
        elif player == WHITE and end_row == 0:
            board[end_row][end_col] = KING_WHITE

        # Check for jump move
        if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
            jumped_row = (end_row + start_row) // 2
            jumped_col = (end_col + start_col) // 2
            board[jumped_row][jumped_col] = EMPTY

# Function to check if a player has won
def has_won(player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in [player, player.upper()]:
                return False
    return True

# Function to get all valid moves for a player
def get_valid_moves(player):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player:
                # Check forward moves
                if player == BLACK or board[row][col] == KING_BLACK:
                    if row < 7:
                        if col > 0 and board[row+1][col-1] == EMPTY:
                            moves.append((row, col, row+1, col-1))
                        if col < 7 and board[row+1][col+1] == EMPTY:
                            moves.append((row, col, row+1, col+1))
                if player == WHITE or board[row][col] == KING_WHITE:
                    if row > 0:
                        if col > 0 and board[row-1][col-1] == EMPTY:
                            moves.append((row, col, row-1, col-1))
                        if col < 7 and board[row-1][col+1] == EMPTY:
                            moves.append((row, col, row-1, col+1))
                # Check jump moves
                if board[row][col] in [player.upper(), KING_BLACK, KING_WHITE]:
                    if row < 6 and col > 1 and board[row+1][col-1] in [WHITE, KING_WHITE] and board[row+2][col-2] == EMPTY:
                        moves.append((row, col, row+2, col-2))
                    if row < 6 and col < 6 and board[row+1][col+1] in [WHITE, KING_WHITE] and board[row+2][col+2] == EMPTY:
                        moves.append((row, col, row+2, col+2))
                    if row > 1 and col > 1 and board[row-1][col-1] in [BLACK, KING_BLACK] and board[row-2][col-2] == EMPTY:
                        moves.append((row, col, row-2, col-2))
                    if row > 1 and col < 6 and board[row-1][col+1] in [BLACK, KING_BLACK] and board[row-2][col+2] == EMPTY:
                        moves.append((row, col, row-2, col+2))
    return moves



# Main function
def main():
    #Ask if the user wants to play against a human or a computer
    bot = True
    print("Welcome to Draughts!")
    print("Would you like to play against a human or a computer?")
    print("1. Human")
    print("2. Computer")
    choice = input("Enter your choice: ")
    while choice not in ["1", "2"]:
        choice = input("Invalid input. Please enter 1 or 2: ")
    if choice == "1":
        bot = False

    # Get the difficulty of the bot
    if bot:
        print("Please select a difficulty for the bot:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter your choice: ")
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid input. Please enter 1, 2 or 3: ")
        if choice == "1":
            difficulty = 1
        elif choice == "2":
            difficulty = 2
        else:
            difficulty = 3


    # Initialize variables
    player = BLACK
    game_over = False

    # Main game loop
    while not game_over:
        # Display board
        display_board()

        # Get move from player
        valid_moves = get_valid_moves(player)
        if len(valid_moves) == 0:
            print("No valid moves left. " + player + " loses!")
            game_over = True
            continue
        print("Valid moves: " + str(valid_moves))
        start_row, start_col, end_row, end_col = get_move(player)
        while not is_valid_move(start_row, start_col, end_row, end_col, player):
            print("Invalid move, please try again.")
            start_row, start_col, end_row, end_col = get_move(player)

        # Make move
        make_move(player, start_row, start_col, end_row, end_col)

        # Check if player has won
        if has_won(player):
            print(player + " wins!")
            game_over = True

        # Switch players
        if player == BLACK:
            player = WHITE
        else:
            player = BLACK

# Run the game
if __name__ == "__main__":
    main()