import numpy as np
from src.kalaha.board import KalahBoard
from src.kalaha.player import KalahaPlayer


class KalahaGameNormal:
    def __init__(self, player1, player2, num_cups=6, num_stones=4):
        self.board = KalahBoard(num_cups=num_cups, num_stones=num_stones)
        self.players = {0:player1, 1:player2}
        self.current_player = np.random.randint(2)
        self.winner = None

    def play(self):
        total_states_explored = 0
        print("Starting game of Kalaha!")
        while not self.board.is_game_over():
            print("-" * 50)
            print(self.board)
            self.board.player_turn = self.current_player
            player = self.players[self.current_player]
            print(f"It's {player.name}'s turn.")
            cup, states_explored = player.select_move(self.board)
            total_states_explored += states_explored
            if self.current_player == 1:
                print_cup = 6 - cup
            else:
                print_cup = cup + 1
            print(f"{player.name} selects cup {print_cup}.")
            self.current_player = self.board.make_move(player.player_num, cup)
            print("-" * 50)
        print(self.board)
        self.print_winner()
        print(f"Total states explored: {total_states_explored}.")

    def print_winner(self):
        p1_score = self.board.board[0][-1]
        p2_score = self.board.board[1][-1]
        if p1_score > p2_score:
            self.winner = self.players[0].player_num
            print(f"{self.players[0].name} wins with a score of {p1_score}-{p2_score}!")
        elif p2_score > p1_score:
            self.winner = self.players[1].player_num
            print(f"{self.players[1].name} wins with a score of {p2_score}-{p1_score}!")
        else:
            print(f"The game is a tie with a score of {p1_score}-{p2_score}!")
