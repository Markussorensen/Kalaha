import copy
import numpy as np
from src.kalaha.heuristic import MaxStonesInPit, StonesInHouse, MovesEndInKalaha

class RandomAlgorithm:
    def select_move(self, board):
        # Select a move at random.
        valid_moves = board.get_valid_moves(board.player_turn)
        return np.random.choice(valid_moves), 1

class MinimaxKalaha:
    def __init__(self, depth, alpha=float("-inf"), beta=float("inf"), heuristic="None"):
        #Initialize the search algorithm.
        self.depth = depth
        self.alpha = alpha
        self.beta = beta
        if heuristic == "MaxStonesInPit":
            self.heuristic = MaxStonesInPit
        elif heuristic == "StonesInHouse":
            self.heuristic = StonesInHouse
        elif heuristic == "MovesEndInKalaha":
            self.heuristic = MovesEndInKalaha
        else:
            self.heuristic = None

    def get_score(self, board, player):
        # Get the score for the given player. 
        # This is the difference between the number of stones in the Kalaha for the given player and the number of stones in the Kalaha for the opponent.
        return board.get_kalaha(player) - board.get_kalaha(1 - player)

    def minimax(self, board, depth, player, alpha, beta, player_depth_turn, parent_idx, total_states_looked_at=[0]):
        #Perform the minimax algorithm.
        if depth == 0 or board.is_game_over():
            return self.get_score(board, player), None
        
        # Get the valid moves for the given player
        valid_moves = board.get_valid_moves(player)

        # Check if there are any valid moves
        if len(valid_moves) == 0:
            # If there are no valid moves, the game is over
            return self.get_score(board, player), None
        
        # If a heuristic is specified, use it to sort the valid moves
        if self.heuristic is not None:
            valid_moves = self.heuristic(board, player, valid_moves)
        
        # Check if we are maximizing or minimizing the score
        if player == board.player_turn:
            # We are maximizing the score
            best_score = float("-inf")
            best_move = None
            all_prints = []
            for idx, move in enumerate(valid_moves):
                #Adds 1 to total states looked at
                total_states_looked_at[0] += 1

                # Make a copy of the board
                new_board = copy.deepcopy(board)

                # Make the move
                new_board.make_move(player_depth_turn, move)

                # Get the score for the move
                score, _ = self.minimax(new_board, depth-1, player, alpha, beta, new_board.player_turn, idx, total_states_looked_at)
                all_prints.append(f"Depth: {depth}, Parent idx: {parent_idx}, Player: {player_depth_turn}, Move: {move}, Score: {score}")

                # Check if the score is better than the best score
                if score > best_score:
                    best_score = score
                    best_move = move

                # Check if the score is better than the current alpha
                if score > alpha:
                    alpha = score

                # Check if we can prune the search
                if alpha >= beta:
                    break
            
            # print(board)
            # for p in all_prints:
            #     print(p)
            # print(f"Depth: {depth}, Parent idx: {parent_idx}, Player: {player_depth_turn}, Best Move: {best_move}, Best Score: {best_score}")

            return best_score, best_move
        
        else:
            # We are minimizing the score
            best_score = float("inf")
            best_move = None
            all_prints = []
            for idx, move in enumerate(valid_moves):
                #Adds 1 to total states looked at
                total_states_looked_at[0] += 1
                
                # Make a copy of the board
                new_board = copy.deepcopy(board)

                # Make the move
                new_board.make_move(player_depth_turn, move)

                # Get the score for the move
                score, _ = self.minimax(new_board, depth-1, player, alpha, beta, new_board.player_turn, idx, total_states_looked_at)
                all_prints.append(f"Depth: {depth}, Parent idx: {parent_idx}, Player: {player_depth_turn}, Move: {move}, Score: {score}")

                # Check if the score is better than the best score
                if score < best_score:
                    best_score = score
                    best_move = move

                # Check if the score is better than the current beta
                if score < beta:
                    beta = score

                # Check if we can prune the search
                if alpha >= beta:
                    break
            
            # print(board)
            # for p in all_prints:
            #     print(p)
            # print(f"Depth: {depth}, Parent idx: {parent_idx}, Player: {player_depth_turn}, Best Move: {best_move}, Best Score: {best_score}")

            return best_score, best_move
    
    def select_move(self, board):
        # Select a move using the minimax algorithm.
        # Get the best move
        total_states_looked_at = [0]
        _, best_move = self.minimax(board, self.depth, board.player_turn, self.alpha, self.beta, board.player_turn, 0, total_states_looked_at)
        return best_move, total_states_looked_at[0]

