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