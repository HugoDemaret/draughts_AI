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