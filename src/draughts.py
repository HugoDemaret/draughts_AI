import random

# Checker Game in Python


class Board:
    """
    Class to represent a checker board
    :param board: The board representation.
    :param game_over: A boolean to indicate if the game is over.
    :param EMPTY: A constant to represent an empty cell.
    :param BLACK: A constant to represent a black piece.
    :param WHITE: A constant to represent a white piece.
    :param KING_BLACK: A constant to represent a black king.
    :param KING_WHITE: A constant to represent a white king.
    """

    #constructor
    def __init__(self):
        """
        Initializes the board.
        :return: None
        """
        # Constants
        self.EMPTY = "-"
        self.BLACK = "b"
        self.WHITE = "w"
        self.KING_BLACK = "B"
        self.KING_WHITE = "W"
        self.game_over = False
        # Board representation (the same as board but with self)
        self.board = [
            [self.EMPTY, self.BLACK, self.EMPTY, self.BLACK, self.EMPTY, self.BLACK, self.EMPTY, self.BLACK],
            [self.BLACK, self.EMPTY, self.BLACK, self.EMPTY, self.BLACK, self.EMPTY, self.BLACK, self.EMPTY],
            [self.EMPTY, self.BLACK, self.EMPTY, self.BLACK, self.EMPTY, self.BLACK, self.EMPTY, self.BLACK],
            [self.EMPTY] * 8,
            [self.EMPTY] * 8,
            [self.WHITE, self.EMPTY, self.WHITE, self.EMPTY, self.WHITE, self.EMPTY, self.WHITE, self.EMPTY],
            [self.EMPTY, self.WHITE, self.EMPTY, self.WHITE, self.EMPTY, self.WHITE, self.EMPTY, self.WHITE],
            [self.WHITE, self.EMPTY, self.WHITE, self.EMPTY, self.WHITE, self.EMPTY, self.WHITE, self.EMPTY]
        ]






# Helper function to display the board
    def display_board(self):
        """
        Displays the board.
        :return: None
        """
        print("  0 1 2 3 4 5 6 7")
        for i in range(len(self.board)):
            row = ""
            for j in range(len(self.board[i])):
                row += self.board[i][j] + " "
            print(str(i) + " " + row)

    # Function to make a move (but check if it is valid first)
    def make_move(self, player, start_row, start_col, end_row, end_col):
        """
        Makes a move.
        :param player:
        :param start_row:
        :param start_col:
        :param end_row:
        :param end_col:
        :return:
        """
        #checks if the move is valid
        if self.is_valid_move(start_row, start_col, end_row, end_col, player):
            #calls the move function
            self.__make_move__(player, start_row, start_col, end_row, end_col)
            #returns true if the move is valid
            return True
        else:
            return False

    # Function to check if a move is valid
    def is_valid_move(self, start_row, start_col, end_row, end_col, player):
        """
        Checks if a move is valid.
        :param start_row:
        :param start_col:
        :param end_row:
        :param end_col:
        :param player:
        :return:
        """
        # Check if start and end coordinates are valid
        if self.board[start_row][start_col] != player:
            return False
        if end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
            return False
        if self.board[end_row][end_col] != self.EMPTY:
            return False

        # Check if move is diagonal
        if abs(end_row - start_row) != 1 or abs(end_col - start_col) != 1:
            # Check for jump move
            if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
                jumped_row = (end_row + start_row) // 2
                jumped_col = (end_col + start_col) // 2
                if self.board[jumped_row][jumped_col] in [player, player.upper()]:
                    return False
            else:
                return False

        # Check if player is moving in the right direction
        if player == self.BLACK and end_row < start_row:
            return False
        elif player == self.WHITE and end_row > start_row:
            return False

        # Valid move
        return True

    # Function to make a move
    def __make_move__(self, player, start_row,
                    start_col, end_row, end_col):
        """
        Makes a move.
        :param player:
        :param start_row:
        :param start_col:
        :param end_row:
        :param end_col:
        :return:
        """
        # Make move
        self.board[start_row][start_col] = self.EMPTY
        self.board[end_row][end_col] = player

        # Check if piece should be kinged
        if player == self.BLACK and end_row == 7:
            self.board[end_row][end_col] = self.KING_BLACK
        elif player == self.WHITE and end_row == 0:
            self.board[end_row][end_col] = self.KING_WHITE

        # Check for jump move
        if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
            jumped_row = (end_row + start_row) // 2
            jumped_col = (end_col + start_col) // 2
            self.board[jumped_row][jumped_col] = self.EMPTY


    # Function to check if a player has won
    def has_won(self, player):
        """
        Checks if a player has won.
        :param self:
        :param player:
        :return:
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] in [player, player.upper()]:
                    return False
        return True

    # Function to get all valid moves for a player
    def get_valid_moves(self, player):
        """
        Gets all valid moves for a player.
        :param self:
        :param player:
        :return:
        """
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == player:
                    # Check forward moves
                    if player == self.BLACK or self.board[row][col] == self.KING_BLACK:
                        if row < 7:
                            if col > 0 and self.board[row+1][col-1] == self.EMPTY:
                                moves.append((row, col, row+1, col-1))
                            if col < 7 and self.board[row+1][col+1] == self.EMPTY:
                                moves.append((row, col, row+1, col+1))
                    if player == self.WHITE or self.board[row][col] == self.KING_WHITE:
                        if row > 0:
                            if col > 0 and self.board[row-1][col-1] == self.EMPTY:
                                moves.append((row, col, row-1, col-1))
                            if col < 7 and self.board[row-1][col+1] == self.EMPTY:
                                moves.append((row, col, row-1, col+1))
                    # Check jump moves
                    if self.board[row][col] in [player.upper(), self.KING_BLACK, self.KING_WHITE]:
                        if row < 6 and col > 1 and self.board[row+1][col-1] in [self.WHITE, self.KING_WHITE] and self.board[row+2][col-2] == self.EMPTY:
                            moves.append((row, col, row+2, col-2))
                        if row < 6 and col < 6 and self.board[row+1][col+1] in [self.WHITE, self.KING_WHITE] and self.board[row+2][col+2] == self.EMPTY:
                            moves.append((row, col, row+2, col+2))
                        if row > 1 and col > 1 and self.board[row-1][col-1] in [self.BLACK, self.KING_BLACK] and self.board[row-2][col-2] == self.EMPTY:
                            moves.append((row, col, row-2, col-2))
                        if row > 1 and col < 6 and self.board[row-1][col+1] in [self.BLACK, self.KING_BLACK] and self.board[row-2][col+2] == self.EMPTY:
                            moves.append((row, col, row-2, col+2))
        return moves



###############################################################################################################
# AGENTS ######################################################################################################
###############################################################################################################



"""
Random agent
"""
def random_agent(board, player):
    """
    Returns a random move from the list of legal moves.
    :param board: The current board state.
    :param player: The player to move.
    :return: A random move from the list of legal moves.
    """
    return random.choice(board.get_valid_moves(player))



"""
Intelligent agents
"""



def intelligent_agent(board, game_settings, player):
    """
    Returns an intelligent agent's move.
    :param board:
    :param game_settings:
    :param player:
    :return:
    """

    #Evalutation functions

    def evaluate_greedy(board):
        """
        Evaluates the board for the greedy algorithm.
        :param board:
        :return:
        """
        # Get the number of pieces for each player
        black_pieces = 0
        white_pieces = 0
        for row in board:
            for piece in row:
                if piece == 'b' or piece == 'B':
                    black_pieces += 1
                elif piece == 'w' or piece == 'W':
                    white_pieces += 1
        # Return the difference between the number of pieces
        return black_pieces - white_pieces  # Positive is good for black, negative is good for white


    def greedy(board, player):
        """
        Greedy algorithm
        """
        # Get a list of all legal moves
        legal_moves = board.get_valid_moves(player)
        # Get the best move
        best_move = None
        best_move_score = float('-inf')
        for move in legal_moves:
            # Make the move
            board.make_move(move, player)
            # Get the score of the move
            move_score = evaluate_greedy(board)
            # Undo the move
            board.undo_move()
            # Check if the move is better than the current best move
            if move_score > best_move_score:
                # If it is, update the best move
                best_move = move
                best_move_score = move_score
        # Return the best move
        return best_move

    def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing_player):
        if is_maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.make_move(move, player)
                eval = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval


    # Logic of the function
    if game_settings[player] == "1":
        return greedy(board, player)
    elif game_settings[player] == "2":
        return alpha_beta_pruning(board, 3, float('-inf'), float('inf'), True)
    elif game_settings[player] == "3":
        return alpha_beta_pruning(board, 5, float('-inf'), float('inf'), True)
    elif game_settings[player] == "4":
        return alpha_beta_pruning(board, 10, float('-inf'), float('inf'), True)


"""
Human agent (hopefully intelligent)
"""
def human_agent(board, player):
    """
    Gets a move from the user.
    :param board: The current board state.
    :param player: The player to move.
    :return: A move from the user.
    """
    while True:
        try:
            # Prompt the user to enter the row and column of the piece they want to move
            start_row, start_col = map(int, input(
                f"Player {player}'s turn. Enter the row and column of the piece you want to move (e.g. 1 2): ").split())
            # Prompt the user to enter the row and column of the destination cell
            end_row, end_col = map(int, input("Enter the row and column of the destination cell: ").split())
            # Check if the move is valid
            if board.is_valid_move(start_row, start_col, end_row, end_col, player):
                # If the move is valid, return it as a tuple
                return (start_row, start_col, end_row, end_col)
            else:
                # If the move is not valid, print an error message and prompt the user to enter a valid move
                print("Invalid move. Please enter a valid move.")
        except ValueError:
            # If the user enters invalid input, print an error message and prompt them to enter valid input
            print("Invalid input. Please enter valid input.")




###############################################################################################################
# GAME ########################################################################################################
###############################################################################################################




# Main function
def main():
    """
    Main function.
    :return: None
    """
    # Asks whether the user wants an AI to play against another AI
    game_settings = {"ai_vs_ai": {"b": "1", "w": "1", "ag": False}, "bot": True, "difficulty": 1, "debug": False}

    if not game_settings["debug"]:
        #Ask if the user wants to play against a human or a computer
        print("Would you like to play against a human or a computer?")
        print("1. Human")
        print("2. Computer")
        choice = input("Enter your choice: ")
        while choice not in ["1", "2"]:
            choice = input("Invalid input. Please enter 1 or 2: ")
        if choice == "1":
            game_settings["bot"] = False

        # Get the difficulty of the bot
        if game_settings["bot"]:
            print("Please select a difficulty for the bot:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            choice = input("Enter your choice: ")
            while choice not in ["1", "2", "3"]:
                choice = input("Invalid input. Please enter 1, 2 or 3: ")
            if choice == "1":
                game_settings["difficulty"] = 1
            elif choice == "2":
                game_settings["difficulty"] = 2
            else:
                game_settings["difficulty"] = 3

    else:
        game_settings["ai_vs_ai"]["ag"] = True
        #get the level of the first agent
        print("Please select a difficulty for the first agent:")
        print("r. Random")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter your choice: ")
        while choice not in ["r", "1", "2", "3"]:
            choice = input("Invalid input. Please enter r, 1, 2 or 3: ")
        if choice == "r":
            game_settings["ai_vs_ai"]["b"] = "r"
        elif choice == "1":
            game_settings["ai_vs_ai"]["b"] = "1"
        elif choice == "2":
            game_settings["ai_vs_ai"]["b"] = "2"
        else:
            game_settings["ai_vs_ai"]["b"] = "3"
        #get the level of the second agent
        print("Please select a difficulty for the second agent:")
        print("r. Random")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter your choice: ")
        while choice not in ["r", "1", "2", "3"]:
            choice = input("Invalid input. Please enter r, 1, 2 or 3: ")
        if choice == "r":
            game_settings["ai_vs_ai"]["w"] = "r"
        elif choice == "1":
            game_settings["ai_vs_ai"]["w"] = "1"
        elif choice == "2":
            game_settings["ai_vs_ai"]["w"] = "2"
        else:
            game_settings["ai_vs_ai"]["w"] = "3"

    #the same as below but with the board object
    board = Board()

    #initialise variables
    player = board.BLACK

    #main game loop
    while not board.game_over:
        #display board
        board.display_board()

        #get move from player
        valid_moves = board.get_valid_moves(player)
        if len(valid_moves) == 0:
            print("No valid moves left. " + player + " loses!")
            board.game_over = True
            continue
        print("Valid moves: " + str(valid_moves))
        start_row, start_col, end_row, end_col = board.get_move(player)
        while not board.is_valid_move(start_row, start_col, end_row, end_col, player):
            print("Invalid move, please try again.")
            start_row, start_col, end_row, end_col = board.get_move(player)

        #make move
        board.make_move(player, start_row, start_col, end_row, end_col)

        #check if the game is over
        if board.has_won(player):
            board.game_over = True
            continue

        #switch player
        if player == board.BLACK:
            player = board.WHITE
        else:
            player = board.BLACK

    #display the final board
    board.display_board()

# Run the game
if __name__ == "__main__":
    main()