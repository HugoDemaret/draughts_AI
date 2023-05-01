import copy
import random
from Board import Board

###############################################################################################################
# AGENTS ######################################################################################################
###############################################################################################################


"""
Random agent
"""


def random_agent(board: Board, player):
    """
    Returns a random move from the list of legal moves.
    :param board: The current board state.
    :param player: The player to move.
    :return: A random move from the list of legal moves.
    """
    return random.choice(board.get_all_moves(player)) if board.get_all_moves(player) else None


"""
Intelligent agents
"""


def intelligent_agent(board: Board, player, game_settings):
    """
    Returns an intelligent agent's move.
    :param board:
    :param game_settings:
    :param player:
    :return:
    """

    # Evalutation functions

    def evaluate_greedy(game_board: Board, game_player):
        """
        Evaluates the board for the greedy algorithm.
        :param game_player:
        :param game_board:
        :return:
        """
        match game_player:
            case "b":
                return game_board.get_num_pieces(game_player) - game_board.get_num_pieces("w")
            case "w":
                return game_board.get_num_pieces(game_player) - game_board.get_num_pieces("b")

    def evaluate_minimax(game_board: Board, game_player):
        """
        Evaluates the board for the minimax algorithm.
        :param game_board:
        :param game_player:
        :return:
        """
        opponent = "b" if game_player == "w" else "w"

        # Difference between the number of pieces
        difference_pieces = evaluate_greedy(game_board, game_player)

        # Difference between the number of kings
        difference_kings = game_board.get_num_kings(game_player) - game_board.get_num_kings(opponent)

        # Difference between the number of pieces in the center
        difference_center = game_board.get_num_center_pieces(game_player) - game_board.get_num_center_pieces(opponent)

        # Difference of pieces at risk
        # difference_risk = game_board.get_num_pieces_at_risk(game_player) - game_board.get_num_pieces_at_risk(opponent)

        # Creation of kings
        creation_kings = game_board.get_num_possible_kings(game_player) - game_board.get_num_possible_kings(opponent)

        # King safety
        king_at_risk = -1 * game_board.get_king_safety(game_player)

        #formula = 2 * difference_pieces + 1 * difference_kings + 0.5 * difference_center + 1 * creation_kings + 0.5 * king_at_risk

        # formula = 5 * board.get_num_pieces(player) + 7.75 * board.get_num_kings(player) + 2.5 * board.get_num_center_pieces(player) + 0.5 * king_safety + 2 * creation_kings

        #formula = board.get_num_pieces(player) + board.get_num_kings(player) + board.get_num_center_pieces(player) + king_at_risk

        formula = 7 * difference_pieces + 1 * difference_kings + 0.5 * difference_center + 1 * creation_kings + 0.5 * king_at_risk

        return formula

    def greedy(game_board, game_player):
        """
        Greedy algorithm
        :param game_board:
        :param game_player:
        :return: The best move according to the greedy algorithm.
        """

        # Get a list of all legal moves
        legal_moves = game_board.get_all_moves(game_player)
        # Get the best move
        best_move = None
        best_move_score = float('-inf')
        for move in legal_moves:
            # Make the move
            copy_board = copy.deepcopy(game_board)
            copy_board.make_move(move[0], move[1], move[2], move[3], game_player)
            # Get the score of the move
            move_score = evaluate_greedy(copy_board, "b")
            # Check if the move is better than the current best move
            if move_score > best_move_score:
                # If it is, update the best move
                best_move = move
                best_move_score = move_score
        # Return the best move
        return best_move

    def alpha_beta_pruning_dummy(game_board, depth, alpha, beta, maximizing_player, game_player):
        """
        Alpha-beta pruning algorithm with dummy evaluation function.
        :param game_board:
        :param depth:
        :param alpha:
        :param beta:
        :param maximizing_player:
        :param game_player:
        :return: the best move according to the alpha-beta pruning algorithm.
        """
        if depth == 0 or game_board.is_game_over():
            return (), evaluate_greedy(game_board, game_player)

        if maximizing_player:
            best_value = float('-inf')
            best_move = None
            for move in game_board.get_all_moves(game_player):
                new_board = copy.deepcopy(game_board)
                new_board.make_move(move[0], move[1], move[2], move[3], game_player)
                dummy, value = alpha_beta_pruning_dummy(new_board, depth - 1, alpha, beta, False, game_player)
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_move, best_value

        else:
            best_value = float('inf')
            best_move = None
            for move in game_board.get_all_moves(game_player):
                new_board = copy.deepcopy(game_board)
                new_board.make_move(move[0], move[1], move[2], move[3], player)
                dummy, value = alpha_beta_pruning_dummy(new_board, depth - 1, alpha, beta, True, game_player)
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_move, best_value

    def alpha_beta_pruning_higher(game_board, depth, alpha, beta, maximizing_player, game_player):
        """
        Alpha-beta pruning algorithm with a higher evaluation function.
        :param game_player:
        :param game_board:
        :param depth:
        :param alpha:
        :param beta:
        :param maximizing_player:
        :return:
        """
        if depth == 0 or game_board.is_game_over():
            return (), evaluate_minimax(game_board, game_player)

        if maximizing_player:
            best_value = float('-inf')
            best_move = None
            for move in game_board.get_all_moves(player):
                new_board = copy.deepcopy(game_board)
                new_board.make_move(move[0], move[1], move[2], move[3], player)
                dummy, value = alpha_beta_pruning_higher(new_board, depth - 1, alpha, beta, False, game_player)
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_move, best_value

        else:
            best_value = float('inf')
            best_move = None
            for move in game_board.get_all_moves(player):
                new_board = copy.deepcopy(game_board)
                new_board.make_move(move[0], move[1], move[2], move[3], player)
                dummy, value = alpha_beta_pruning_higher(new_board, depth - 1, alpha, beta, True, game_player)
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_move, best_value

    next_move = None

    # Logic of the function
    if game_settings["ai_vs_ai"][player] == "1":
        next_move = greedy(board, player)
    elif game_settings["ai_vs_ai"][player] == "2":
        next_move, dummy = alpha_beta_pruning_dummy(board, 3, float('-inf'), float('inf'), True, player)
    elif game_settings["ai_vs_ai"][player] == "3":
        next_move, dummy = alpha_beta_pruning_higher(board, 5, float('-inf'), float('inf'), True, player)

    return next_move


"""
Human agent (hopefully intelligent)
"""


def human_agent(board, player, valid_moves):
    """
    Gets a move from the user.
    :param board: The current board state.
    :param player: The player to move.
    :return: A move from the user.
    """
    while True:
        try:
            # Prompt the user to enter the row and column of the piece they want to move
            print("Choose a piece to move from the valid moves below:")
            for i in range(len(valid_moves)):
                print(str(i) + ": " + str(valid_moves[i]))
            print("Enter the index of the move you want to make.")
            move_index = int(input())
            while not move_index in range(len(valid_moves)):
                print("Invalid move. Please enter a valid move.")
                move_index = int(input())
            move = valid_moves[move_index]
            return move
        except:
            print("Invalid entry, it must be an integer.")


###############################################################################################################
# GAME ########################################################################################################
###############################################################################################################

def match_making_loop(game_settings):
    """
        The main game loop for AI vs AI.
        :param game_settings: The settings of the game.
        :return: None
        """
    # Initialize the board
    board = Board()
    # Initialize the players
    players = ["b", "w"]
    # Initialize the current player
    current_player = players[0]
    # Initialize the number of moves
    num_moves = 0

    finish_game = False
    # Main game loop
    while not finish_game:
        # Check if the game is over
        if board.is_game_over():
            # If the game is over, print the winner and exit the game
            if board.has_won(current_player):
                return current_player
            elif board.has_won(players[(num_moves + 1) % 2]):
                opponent = players[(num_moves + 1) % 2]
                return opponent
            else:
                return "draw"

        if num_moves >= 500:
            return "draw"

        if game_settings["ai_vs_ai"][current_player] == "r":
            next_move = random_agent(board, current_player)
        else:
            next_move = intelligent_agent(board, current_player, game_settings)

        if next_move is None or len(next_move) == 0:
            opponent = players[(num_moves + 1) % 2]
            return opponent
        # Make the move
        board.make_move(next_move[0], next_move[1], next_move[2], next_move[3], current_player)

        # Increment the number of moves
        num_moves += 1

        # Switch the current player
        current_player = players[num_moves % 2]

def n_matches(game_settings, n):
    results = {"b": 0, "w": 0, "draw": 0}
    for i in range(n):
        print("Match " + str(i))
        res = match_making_loop(game_settings)
        results[res] += 1
    return results

def match_making():
    """
    Comparison between AI agents.
    :return:
    """
    n = 100
    debug = True
    # Random vs Random 1000 games
    game_settings_random_vs_random = {"ai_vs_ai": {"b": "r", "w": "r", "ag": True}, "bot": True, "debug": debug}
    results_random_vs_random = n_matches(game_settings_random_vs_random, n)
    print("Finished random vs random")
    game_settings_random_vs_a1 = {"ai_vs_ai": {"b": "r", "w": "1", "ag": True}, "bot": True, "debug": debug}
    results_random_vs_a1 = n_matches(game_settings_random_vs_a1, n)
    print("Finished random vs a1")
    game_settings_random_vs_a2 = {"ai_vs_ai": {"b": "r", "w": "2", "ag": True}, "bot": True, "debug": debug}
    results_random_vs_a2 = n_matches(game_settings_random_vs_a2, n)
    print("Finished random vs a2")
    game_settings_random_vs_a3 = {"ai_vs_ai": {"b": "r", "w": "3", "ag": True}, "bot": True, "debug": debug}
    results_random_vs_a3 = n_matches(game_settings_random_vs_a3, 10)
    print("Finished random vs a3")
    game_settings_a1_vs_random = {"ai_vs_ai": {"b": "1", "w": "r", "ag": True}, "bot": True, "debug": debug}
    results_a1_vs_random = n_matches(game_settings_a1_vs_random, n)
    print("Finished a1 vs random")
    game_settings_a2_vs_random = {"ai_vs_ai": {"b": "2", "w": "r", "ag": True}, "bot": True, "debug": debug}
    results_a2_vs_random = n_matches(game_settings_a2_vs_random, n)
    print("Finished a2 vs random")
    game_settings_a3_vs_random = {"ai_vs_ai": {"b": "3", "w": "r", "ag": True}, "bot": True, "debug": debug}
    results_a3_vs_random = n_matches(game_settings_a3_vs_random, 10)
    print("Finished a3 vs random")

    results = {}
    results["random_vs_random"] = results_random_vs_random
    results["random_vs_a1"] = results_random_vs_a1
    results["random_vs_a2"] = results_random_vs_a2
    results["random_vs_a3"] = results_random_vs_a3
    results["a1_vs_random"] = results_a1_vs_random
    results["a2_vs_random"] = results_a2_vs_random
    results["a3_vs_random"] = results_a3_vs_random

    return results



def ai_vs_ai_game_loop(game_settings):
    """
    The main game loop for AI vs AI.
    :param game_settings: The settings of the game.
    :return: None
    """
    # Initialize the board
    board = Board()
    # Initialize the players
    players = ["b", "w"]
    # Initialize the current player
    current_player = players[0]
    # Initialize the number of moves
    num_moves = 0

    finish_game = False
    # Main game loop
    while not finish_game:
        # Check if the game is over
        if board.is_game_over():
            # If the game is over, print the winner and exit the game
            if board.has_won(current_player):
                print(f"Player {current_player} has won!")
            elif board.has_won(players[(num_moves + 1) % 2]):
                print(f"Player {players[(num_moves + 1) % 2]} has won!")
            else:
                print("It's a tie!")
            break

        # Print the board
        board.display_board()

        if game_settings["ai_vs_ai"][current_player] == "r":
            next_move = random_agent(board, current_player)
        else:
            next_move = intelligent_agent(board, current_player, game_settings)

        if next_move is None or len(next_move) == 0:
            opponent = players[(num_moves + 1) % 2]
            print("No valid moves. Game over. The winner is: " + opponent)
            break

        # Make the move
        board.make_move(next_move[0], next_move[1], next_move[2], next_move[3], current_player)

        # Increment the number of moves
        num_moves += 1

        # Switch the current player
        current_player = players[num_moves % 2]


def game_loop(game_settings):
    """
    The main game loop.
    :param game_settings: The settings of the game.
    :return: None
    """
    # Initialize the board
    board = Board()
    # Initialize the players
    players = ["b", "w"]
    # Initialize the current player
    current_player = players[0]
    # Initialize the number of moves
    num_moves = 0
    finish = False
    # Main game loop
    while not finish:

        # Print the board
        board.display_board()
        valid_moves = board.get_all_moves(current_player)
        if len(valid_moves) == 0:
            print(f"Player {current_player} has no valid moves.")
            finish = True
            break
        # Get the next move
        next_move = None
        if game_settings["bot"] and current_player == "w":
            if game_settings["ai_vs_ai"][current_player] == "r":
                next_move = random_agent(board, current_player)
            else:
                next_move = intelligent_agent(board, current_player, game_settings)
        else:
            next_move = human_agent(board, current_player, valid_moves)
            print("Human move: ", next_move)

        # Make the move
        board.make_move(next_move[0], next_move[1], next_move[2], next_move[3], current_player)

        # Check if the game is over
        if board.is_game_over():
            # If the game is over, print the winner and exit the game
            if board.has_won(current_player):
                print(f"Player {current_player} has won!")
            else:
                print("It's a draw!")
            break

        # Increment the number of moves
        num_moves += 1

        # Switch the current player
        current_player = players[num_moves % 2]


# Main function
def main():
    """
    Main function.
    :return: None
    """
    # Asks whether the user wants an AI to play against another AI
    print("Would you like to watch an AI play against another AI?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    debug = False
    while choice not in ["1", "2"]:
        choice = input("Invalid input. Please enter 1 or 2: ")
    if choice == "1":
        debug = True
    game_settings = {"ai_vs_ai": {"b": "1", "w": "1", "ag": False}, "bot": True, "debug": debug}
    benchmark = False
    if not game_settings["debug"]:
        # Ask if the user wants to play against a human or a computer
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
            print("r. Random")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            choice = input("Enter your choice: ")
            while choice not in ["1", "2", "3", "r"]:
                choice = input("Invalid input. Please enter 1, 2 or 3: ")
            game_settings["ai_vs_ai"]["w"] = choice
            game_settings["ai_vs_ai"]["b"] = choice

        game_loop(game_settings)
    elif benchmark:
        print("Benchmarking...")
        results = match_making()
        for elem in results:
            print(elem, results[elem])
    else:
        game_settings["ai_vs_ai"]["ag"] = True
        # get the level of the first agent
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
        # get the level of the second agent
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

        ai_vs_ai_game_loop(game_settings)


# Run the game
if __name__ == "__main__":
    main()
