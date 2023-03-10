"""
KALAHA RULES:

1:  At the beginning of the game, four seeds are placed in each house. This is the traditional method.
2:  Each player controls the six houses and their seeds on the player's side of the board. 
    The player's score is the number of seeds in the store to their right.
3:  Players take turns sowing their seeds. 
    On a turn, the player removes all seeds from one of the houses under their control. 
    Moving counter-clockwise, the player drops one seed in each house in turn, including the player's own store but not their opponent's.
4:  If the last sown seed lands in an empty house owned by the player, and the opposite house contains seeds, 
    both the last seed and the opposite seeds are captured and placed into the player's store.
5:  If the last sown seed lands in the player's store, the player gets an additional move. 
    There is no limit on the number of moves a player can make in their turn.
6:  When one player no longer has any seeds in any of their houses, the game ends. 
    The other player moves all remaining seeds to their store, and the player with the most seeds in their store wins.
"""


class KalahBoard:
    def __init__(self, num_cups=6, num_stones=4):
        # Initialize the board with the given number of cups and stones per cup
        self.num_cups = num_cups
        self.num_stones = num_stones
        self.board = [[num_stones for _ in range(num_cups)] for _ in range(2)]
        self.player_turn = -1
        self.board[0].append(0) # Player 1 Kalaha
        self.board[1].append(0) # Player 2 Kalaha

    def __str__(self):
        # Generate a string representation of the board for debugging purposes
        s = ""
        h = "Cup no:     " + " ".join(str(x) for x in range(1, self.num_cups + 1))
        p2 = "P2 Cups     "
        p2 += " ".join(str(x) for x in reversed(self.board[1][:-1]))
        m = (
            f"P2 Kalaha {self.board[1][-1]}"
            + " " * (len(p2) - 10)
            + f"{self.board[0][-1]} P1 Kalaha"
        )
        p1 = "P1 Cups     "
        p1 += " ".join(str(x) for x in self.board[0][:-1])
        s += h + "\n" + p2 + "\n" + m + "\n" + p1 + "\n"
        return s

    def get_num_stones(self, player, cup):
        # Get the number of stones in the given cup for the given player
        return self.board[player][cup]

    def remove_stones(self, player_side, cup):
        # Remove all the stones from the given cup for the given player
        num_stones = self.board[player_side][cup]
        self.board[player_side][cup] = 0
        return num_stones

    def add_stones(self, player_side, cup, num_stones):
        # Add the given number of stones to the given cup for the given player
        self.board[player_side][cup] += num_stones

    def get_kalaha(self, player):
        # Get the number of stones in the Kalaha for the given player
        return self.board[player][-1]

    def add_to_kalaha(self, player, num_stones):
        # Add the given number of stones to the Kalaha for the given player
        self.board[player][-1] += num_stones

    def get_opposite_cup(self, cup):
        # Get the index of the cup opposite to the given cup for the given player
        return self.num_cups - cup - 1

    def is_valid_move(self, player, cup):
        # Check if the given move is valid for the given player
        if self.get_num_stones(player, cup) == 0:
            return False
        return True

    def get_valid_moves(self, player):
        # Get a list of valid moves for the given player
        return [i for i in range(self.num_cups) if self.is_valid_move(player, i)]

    def make_move(self, player, cup):
        # Make the given move for the given player and return the next player's turn
        player_side = player
        next_cup = cup
        num_stones = self.remove_stones(player_side, cup)
        # Distribute the stones
        while num_stones > 0:
            # Distribute all the stones collected
            for i in range(num_stones):
                # Check if we switch sides
                if next_cup + 1 == self.num_cups + 1:
                    player_side = 1 - player_side

                # Check which number the next cup is
                next_cup = (next_cup + 1) % (self.num_cups + 1)
                # Skip the opponent's Kalaha
                if next_cup == self.num_cups and player_side != player:
                    if next_cup + 1 == self.num_cups + 1:
                        player_side = 1 - player_side
                    next_cup = (next_cup + 1) % (self.num_cups + 1)
                self.add_stones(player_side, next_cup, 1)

            # All current stones have been distributed
            num_stones = 0

            # Check if we landed in our Kalaha then the same player take another turn
            if next_cup == self.num_cups and player_side == player:
                return player

            # Check if we did not land in an empty cup, and pick up stones
            if self.get_num_stones(player_side, next_cup) > 1:
                num_stones = self.remove_stones(player_side, next_cup)

        # Now we know we landed in an empty cup and that it is not our Kalaha
        # Now check if we landed in cup on our side
        if player_side == player:
            opposite_cup = self.get_opposite_cup(next_cup)
            if not self.get_num_stones(1 - player_side, opposite_cup) == 0:
                # Pick up the stones in the opposite cup and the cup we landed in and put them in our Kalaha
                num_opposite_stones = self.remove_stones(1 - player_side, opposite_cup)
                num_stones = self.remove_stones(player_side, next_cup)
                self.add_to_kalaha(player, num_stones + num_opposite_stones)

        # Now give the other player a turn
        self.player_turn = 1 - player
        return 1 - player

    def is_game_over(self):
        # Check if either player's cups are empty
        if sum(self.board[0][:-1]) == 0 or sum(self.board[1][:-1]) == 0:
            # Move all remaining stones to the respective player's Kalaha
            self.add_to_kalaha(0, sum(self.board[0][:-1]))
            self.add_to_kalaha(1, sum(self.board[1][:-1]))
            # Clear the cups
            for i in range(self.num_cups):
                self.board[0][i] = 0
                self.board[1][i] = 0
            return True

        return False
