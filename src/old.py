# Function to get a move from the user
def get_move(self, player):
    """
    Gets a move from the user.
    :param player:
    :return:
    """
    while True:
        try:
            # Prompt the user to enter the row and column of the piece they want to move
            start_row, start_col = map(int, input(
                f"Player {player}'s turn. Enter the row and column of the piece you want to move (e.g. 1 2): ").split())
            # Prompt the user to enter the row and column of the destination cell
            end_row, end_col = map(int, input("Enter the row and column of the destination cell: ").split())
            # Check if the move is valid
            if self.is_valid_move(start_row, start_col, end_row, end_col, player):
                # If the move is valid, return it as a tuple
                return (start_row, start_col, end_row, end_col)
            else:
                # If the move is not valid, print an error message and prompt the user to enter a valid move
                print("Invalid move. Please enter a valid move.")
        except ValueError:
            # If the user enters invalid input, print an error message and prompt them to enter valid input
            print("Invalid input. Please enter valid input.")



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
        piece = self.board[row][col]
        color = piece.lower()
        is_king = piece.isupper()
        valid_moves = []
        if color == "b" or is_king:
            # down left jump
            if row < 6 and col > 1 and self.board[row + 1][col - 1] not in [self.EMPTY, color] and \
                    self.board[row + 2][col - 2].lower() != color:
                valid_moves.append((row, col, row + 2, col - 2))
            # down right jump
            if row < 6 and col < 6 and self.board[row + 1][col + 1] not in [self.EMPTY, color] and \
                    self.board[row + 2][col + 2].lower() != color:
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
                    self.board[row - 2][col - 2].lower() != color:
                valid_moves.append((row, col, row - 2, col - 2))
            # up right jump
            if row > 1 and col < 6 and self.board[row - 1][col + 1] not in [self.EMPTY, color] and \
                    self.board[row - 2][col + 2].lower() != color:
                valid_moves.append((row, col, row - 2, col + 2))

            # up left move
            if row > 0 and col > 0 and self.board[row - 1][col - 1] == self.EMPTY:
                valid_moves.append((row, col, row - 1, col - 1))
            # up right move
            if row > 0 and col < 7 and self.board[row - 1][col + 1] == self.EMPTY:
                valid_moves.append((row, col, row - 1, col + 1))


        return valid_moves



    def get_all_moves(self, player):
        """
        Gets all the moves for a player.
        :param player: The player to get all the moves for.
        :return: All the moves for a player.
        """
        moves = []
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == player or self.board[row][col] == player.upper():
                    if self.board[row][col] == player.upper():
                        moves += self.get_all_king_moves(row, col, player)
                    else:
                        moves += self.get_all_pawn_moves(row, col, player)
        return moves

    def get_all_pawn_moves(self, row, col, player):
        moves = []
        capture = []
        forward = 1 if player == self.BLACK else -1
        direction = [(forward, 1), (forward, -1)]
        for d in direction:
            r = row + d[0]
            c = col + d[1]
            if 0 <= r < 7 and 0 <= c < 8:
                if self.board[r][c] == "-":
                    moves.append((row, col, r, c))
                elif self.board[r][c] == player or self.board[r][c] == player.upper():
                    pass
                else:
                    r2 = r + d[0]
                    c2 = c + d[1]
                    if 0 <= r2 < 7 and 0 <= c2 < 8 and self.board[r2][c2] == "-":
                        capture.append((row, col, r2, c2))
        return capture if capture else moves

    def get_all_king_moves(self, row, col, player):
        moves = []
        capture = []
        direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d in direction:
            r = row + d[0]
            c = col + d[1]
            while 0 <= r < 7 and 0 <= c < 8:
                if self.board[r][c] == "-":
                    moves.append((row, col, r, c))
                elif self.board[r][c] == player or self.board[r][c] == player.upper():
                    break
                else:
                    r2 = r + d[0]
                    c2 = c + d[1]
                    if 0 <= r2 < 7 and 0 <= c2 < 8 and self.board[r2][c2] == "-":
                        capture.append((row, col, r2, c2))
                        break
                r += d[0]
                c += d[1]
        return capture if capture else moves