import numpy as np
from src.kalaha.algorithms import MinimaxKalaha, RandomAlgorithm

class KalahaPlayer:
    def __init__(self, player_num, name, is_human, ai_method="random", minimax_depth=3, heuristic=None):
        self.name = name
        self.is_human = is_human
        if ai_method == "random":
            self.ai_method = RandomAlgorithm()
        elif ai_method == "minimax":
            self.ai_method = MinimaxKalaha(minimax_depth, heuristic=heuristic)
        else:
            raise ValueError("Invalid AI method.")
        self.player_num = player_num

    def select_move(self, board):
        if self.is_human:
            # Ask the human player for input
            valid_cups = board.get_valid_moves(self.player_num)
            if self.player_num == 1:
                print_cups = [board.num_cups - cup - 1 for cup in valid_cups]
                print_cups = sorted(print_cups)
                print_cups = [str(cup + 1) for cup in print_cups]
            else:
                print_cups = [str(cup + 1) for cup in valid_cups]
            while True:
                cup = input(
                    f"{self.name}, select a cup to move (valid cups: {print_cups}): "
                )
                try:
                    if self.player_num == 1:
                        cup = board.num_cups - int(cup)
                    else:
                        cup = int(cup) - 1
                    if cup not in valid_cups:
                        raise ValueError
                    return cup, 1
                except ValueError:
                    print("Invalid input, please enter a valid cup number.")
        else:
            # Use the AI method to select a move
            move, total_states_looked_at = self.ai_method.select_move(board)
            return move, total_states_looked_at
