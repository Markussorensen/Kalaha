import numpy as np


class KalahaPlayer:
    def __init__(self, player_num, name, is_human, ai_method="random"):
        self.name = name
        self.is_human = is_human
        self.ai_method = ai_method
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
                    cup = board.num_cups - int(cup)
                    if cup not in valid_cups:
                        raise ValueError
                    return cup
                except ValueError:
                    print("Invalid input, please enter a valid cup number.")
        else:
            valid_cups = board.get_valid_moves(self.player_num)
            # Select a random valid move for the AI player
            if self.ai_method == "random":
                cup = np.random.choice(valid_cups)

            return cup
