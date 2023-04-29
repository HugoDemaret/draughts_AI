import random

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
    :param depth:
    :param player:
    :return:
    """

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
            move_score = evaluate(board)
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
        if depth == 0 or board.is_game_over():
            return evaluate(board)

        if is_maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
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