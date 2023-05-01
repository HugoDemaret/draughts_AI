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

    # constructor
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


    # Function to get the number of pieces of a player
    def get_num_pieces(self, player):
        """
        Gets the number of pieces of a player.
        :param player: The player to get the number of pieces for.
        :return: The number of pieces of a player.
        """
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player or self.board[i][j] == player.upper():
                    count += 1
        return count

    # Function to get the number of kings of a player
    def get_num_kings(self, player):
        """
        Gets the number of kings of a player.
        :param player: The player to get the number of kings for.
        :return: The number of kings of a player.
        """
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player.upper():
                    count += 1
        return count

    # Function to get the number of pieces in the center of the player
    def get_num_center_pieces(self, player):
        """
        Gets the number of pieces in the center of the player.
        :param player: The player to get the number of pieces in the center for.
        :return: The number of pieces in the center of a player.
        """
        count = 0
        for i in range(3, 5):
            for j in range(3, 5):
                if self.board[i][j] == player or self.board[i][j] == player.upper():
                    count += 1
        return count


    # Function to get the number of pieces at danger of being taken of a player
    def get_num_pieces_at_risk(self, player):
        """
        Gets the number of pieces at danger of being taken by the opponent of the player.
        :param player: The player to get the number of pieces at risk for.
        :return: The number of pieces at danger of being taken of a player.
        """
        count = 0
        opponent = self.BLACK if player == self.WHITE else self.WHITE
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player or self.board[i][j] == player.upper():
                    if self.is_piece_at_risk(i, j, opponent):
                        count += 1

        return count


    def is_pawn_at_risk(self, row, col, opponent):
        """
        Checks if a pawn is at risk of being taken by the opponent.
        :param row: The row of the pawn.
        :param col: The column of the pawn.
        :param opponent: The opponent of the player.
        :return: True if the pawn is at risk of being taken by the opponent, False otherwise.
        """
        # checks if the pawn is a white pawn
        if self.board[row][col] == self.WHITE:
            # checks if the pawn is at risk of being taken by the opponent
            return self.board[row + 1][col - 1] == opponent or self.board[row + 1][col + 1] == opponent
        # checks if the pawn is a black pawn
        elif self.board[row][col] == self.BLACK:
            # checks if the pawn is at risk of being taken by the opponent
            return self.board[row - 1][col - 1] == opponent or self.board[row - 1][col + 1] == opponent
        # returns false if the pawn is a king
        else:
            return False





    def get_king_safety(self, player):
        """
        Gets the king safety of a player.
        :param player: The player to get the king safety for.
        :return: The king safety of a player.
        """
        # Count the number of kings of player that can be taken by the opponent
        count = 0
        opponent = self.BLACK if player == self.WHITE else self.WHITE
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player.upper():
                    if self.is_king_at_risk(i, j, opponent):
                        count += 1
        return count


    def is_king_at_risk(self, row, col, opponent):
        """
        Checks if a king is at risk of being taken by the opponent.
        :param row: The row of the king.
        :param col: The column of the king.
        :param opponent: The opponent of the player.
        :return: True if the king is at risk of being taken by the opponent, False otherwise.
        """
        # if in the edges
        if row == 0 or row == 7 or col == 0 or col == 7:
            return False
        # checks if the king is a white king
        if self.board[row][col] == self.KING_WHITE:
            # checks if the king is at risk of being taken by the opponent
            return self.board[row + 1][col - 1] == opponent or self.board[row + 1][col + 1] == opponent or \
                   self.board[row - 1][col - 1] == opponent or self.board[row - 1][col + 1] == opponent
        # checks if the king is a black king
        elif self.board[row][col] == self.KING_BLACK:
            # checks if the king is at risk of being taken by the opponent
            return self.board[row + 1][col - 1] == opponent or self.board[row + 1][col + 1] == opponent or \
                   self.board[row - 1][col - 1] == opponent or self.board[row - 1][col + 1] == opponent
        # returns false if the king is a pawn
        else:
            return False

    def is_piece_at_risk(self, row, col, opponent):
        """
        Checks if a piece is at risk of being taken by the opponent.
        :param row: The row of the piece.
        :param col: The column of the piece.
        :param opponent: The opponent of the player.
        :return: True if the piece is at risk of being taken by the opponent, False otherwise.
        """
        # checks if the piece is a king
        if self.board[row][col] == self.KING_BLACK or self.board[row][col] == self.KING_WHITE:
            # checks if the piece is at risk of being taken by the opponent
            return self.is_king_at_risk(row, col, opponent)
        # checks if the piece is a normal piece
        elif self.board[row][col] == self.BLACK or self.board[row][col] == self.WHITE:
            # checks if the piece is at risk of being taken by the opponent
            return self.is_pawn_at_risk(row, col, opponent)
        # returns false if the piece is empty
        else:
            return False


    def can_pawn_become_king(self, row, col):
        """
        Checks if a pawn can become a king.
        :param row: The row of the pawn.
        :param col: The column of the pawn.
        :return: True if the pawn can become a king, False otherwise.
        """
        # checks if the pawn is a white pawn
        if self.board[row][col] == self.WHITE:
            # checks if the pawn can become a king
            return row == 0
        # checks if the pawn is a black pawn
        elif self.board[row][col] == self.BLACK:
            # checks if the pawn can become a king
            return row == 7
        # returns false if the pawn is a king
        else:
            return False


    def get_num_possible_kings(self, player):
        """
        Gets the number of possible kings for a player.
        :param player: The player to get the number of possible kings for.
        :return: The number of possible kings for a player.
        """
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player:
                    if self.can_pawn_become_king(i, j):
                        count += 1

        return count


    # Function to make a move (but check if it is valid first)
    def make_move(self,start_row, start_col, end_row, end_col, player):
        """
        Makes a move.
        :param player:
        :param start_row:
        :param start_col:
        :param end_row:
        :param end_col:
        :return:
        """
        self.__make_move__(start_row, start_col, end_row, end_col, player)



    # Function to make a move
    def __make_move__(self, start_row,
                      start_col, end_row, end_col, player):
        """
        Makes a move.
        :param player:
        :param start_row:
        :param start_col:
        :param end_row:
        :param end_col:
        :return:
        """
        # move the piece
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = "-"
        self.board[end_row][end_col] = piece

        # Make king if possible
        if self.can_pawn_become_king(end_row, end_col):
            #print("Pawn became king!")
            self.board[end_row][end_col] = piece.upper()

        # remove the captured piece if any
        if abs(start_row - end_row) == 2:
            captured_row = (start_row + end_row) // 2
            captured_col = (start_col + end_col) // 2
            self.board[captured_row][captured_col] = "-"

        # Force a capture if possible
        if abs(start_row - end_row) == 2:
            moves = self.get_capture_moves(end_row, end_col)
            if moves:
                self.__make_move__(end_row, end_col, moves[0][0], moves[0][1], player)


    def get_capture_moves(self, row, col):
        """
        Gets all the capture moves for a piece.
        :param row: The row of the piece.
        :param col: The column of the piece.
        :return: A list of all the capture moves for a piece.
        """
        moves = []
        if self.board[row][col] == self.WHITE or self.board[row][col] == self.BLACK:
            moves.extend(self.get_capture_moves_for_pawn(row, col))
        elif self.board[row][col] == self.KING_WHITE or self.board[row][col] == self.KING_BLACK:
            moves.extend(self.get_capture_moves_for_king(row, col))
        return moves

    def get_capture_moves_for_pawn(self, row, col):
        """
        Gets all the capture moves for a pawn.
        :param row: The row of the pawn.
        :param col: The column of the pawn.
        :return: A list of all the capture moves for a pawn.
        """
        moves = []
        if self.board[row][col] == self.WHITE:
            if row >= 2 and col >= 2:
                if self.board[row - 1][col - 1] == self.BLACK or self.board[row - 1][col - 1] == self.KING_BLACK:
                    if self.board[row - 2][col - 2] == "-":
                        moves.append([row - 2, col - 2])
            if row >= 2 and col <= 5:
                if self.board[row - 1][col + 1] == self.BLACK or self.board[row - 1][col + 1] == self.KING_BLACK:
                    if self.board[row - 2][col + 2] == "-":
                        moves.append([row - 2, col + 2])
        elif self.board[row][col] == self.BLACK:
            if row <= 5 and col >= 2:
                if self.board[row + 1][col - 1] == self.WHITE or self.board[row + 1][col - 1] == self.KING_WHITE:
                    if self.board[row + 2][col - 2] == "-":
                        moves.append([row + 2, col - 2])
            if row <= 5 and col <= 5:
                if self.board[row + 1][col + 1] == self.WHITE or self.board[row + 1][col + 1] == self.KING_WHITE:
                    if self.board[row + 2][col + 2] == "-":
                        moves.append([row + 2, col + 2])
        return moves

    def get_capture_moves_for_king(self, row, col):
        """
        Gets all the capture moves for a king.
        :param row: The row of the king.
        :param col: The column of the king.
        :return: A list of all the capture moves for a king.
        """
        moves = []
        if self.board[row][col] == self.KING_WHITE:
            if row >= 2 and col >= 2:
                if self.board[row - 1][col - 1] == self.BLACK or self.board[row - 1][col - 1] == self.KING_BLACK:
                    if self.board[row - 2][col - 2] == "-":
                        moves.append([row - 2, col - 2])
            if row >= 2 and col <= 5:
                if self.board[row - 1][col + 1] == self.BLACK or self.board[row - 1][col + 1] == self.KING_BLACK:
                    if self.board[row - 2][col + 2] == "-":
                        moves.append([row - 2, col + 2])
            if row <= 5 and col >= 2:
                if self.board[row + 1][col - 1] == self.BLACK or self.board[row + 1][col - 1] == self.KING_BLACK:
                    if self.board[row + 2][col - 2] == "-":
                        moves.append([row + 2, col - 2])
            if row <= 5 and col <= 5:
                if self.board[row + 1][col + 1] == self.BLACK or self.board[row + 1][col + 1] == self.KING_BLACK:
                    if self.board[row + 2][col + 2] == "-":
                        moves.append([row + 2, col + 2])
        elif self.board[row][col] == self.KING_BLACK:
            if row >= 2 and col >= 2:
                if self.board[row - 1][col - 1] == self.WHITE or self.board[row - 1][col - 1] == self.KING_WHITE:
                    if self.board[row - 2][col - 2] == "-":
                        moves.append([row - 2, col - 2])
            if row >= 2 and col <= 5:
                if self.board[row - 1][col + 1] == self.WHITE or self.board[row - 1][col + 1] == self.KING_WHITE:
                    if self.board[row - 2][col + 2] == "-":
                        moves.append([row - 2, col + 2])
            if row <= 5 and col >= 2:
                if self.board[row + 1][col - 1] == self.WHITE or self.board[row + 1][col - 1] == self.KING_WHITE:
                    if self.board[row + 2][col - 2] == "-":
                        moves.append([row + 2, col - 2])
            if row <= 5 and col <= 5:
                if self.board[row + 1][col + 1] == self.WHITE or self.board[row + 1][col + 1] == self.KING_WHITE:
                    if self.board[row + 2][col + 2] == "-":
                        moves.append([row + 2, col + 2])
        return moves


    # Function to check if a player has won
    def has_won(self, player):
        """
        Checks if a player has won.
        :param self:
        :param player:
        :return:
        """
        opponnent = "b" if player == "w" else "w"
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] in [opponnent, opponnent.upper()]:
                    return False
        return True

    # Get all possible moves for a player
    def get_all_moves(self, player):
        all_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.lower() == player.lower():
                    moves = self.get_valid_moves(row, col)
                    if moves:
                        all_moves.extend(moves)
        return all_moves

    def get_valid_moves(self, row, col):
        """
        Gets all the valid moves for a piece.
        :param row:
        :param col:
        :return:
        """
        piece = self.board[row][col]
        color = piece.lower()
        is_king = piece.isupper()
        valid_moves = []
        if color == "b" or is_king:
            # down left jump
            if row < 6 and col > 1 and self.board[row + 1][col - 1] not in [self.EMPTY, color] and \
                    self.board[row + 2][col - 2].lower() != color and self.board[row + 2][col - 2] == self.EMPTY:
                valid_moves.append((row, col, row + 2, col - 2))
            # down right jump
            if row < 6 and col < 6 and self.board[row + 1][col + 1] not in [self.EMPTY, color] and \
                    self.board[row + 2][col + 2].lower() != color and self.board[row + 2][col + 2] == self.EMPTY:
                valid_moves.append((row, col, row + 2, col + 2))

            # down left move
            if row < 7 and col > 0 and self.board[row + 1][col - 1] == self.EMPTY:
                valid_moves.append((row, col, row + 1, col - 1))
            # down right move
            if row < 7 and col < 7 and self.board[row + 1][col + 1] == self.EMPTY:
                valid_moves.append((row, col, row + 1, col + 1))





        if color == "w" or is_king:
            # up left jump
            if row > 1 and col > 1 and self.board[row - 1][col - 1] not in [self.EMPTY, color] and \
                    self.board[row - 2][col - 2].lower() != color and self.board[row - 2][col - 2] == self.EMPTY:
                valid_moves.append((row, col, row - 2, col - 2))
            # up right jump
            if row > 1 and col < 6 and self.board[row - 1][col + 1] not in [self.EMPTY, color] and \
                    self.board[row - 2][col + 2].lower() != color and self.board[row - 2][col + 2] == self.EMPTY:
                valid_moves.append((row, col, row - 2, col + 2))

            # up left move
            if row > 0 and col > 0 and self.board[row - 1][col - 1] == self.EMPTY:
                valid_moves.append((row, col, row - 1, col - 1))
            # up right move
            if row > 0 and col < 7 and self.board[row - 1][col + 1] == self.EMPTY:
                valid_moves.append((row, col, row - 1, col + 1))


        return valid_moves

    # Function to know if the game is over
    def is_game_over(self):
        """
        Checks if the game is over.
        :param self:
        :return:
        """
        return self.has_won(self.BLACK) or self.has_won(self.WHITE)
