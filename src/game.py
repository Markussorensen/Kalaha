import pygame
import numpy as np
from src.board import KalahBoard
from src.player import KalahaPlayer

class KalahaGameNormal:
    def __init__(self, player1, player2, num_cups=6, num_stones=4):
        self.board = KalahBoard(num_cups=num_cups, num_stones=num_stones)
        self.players = {0:player1, 1:player2}
        self.current_player = np.random.randint(2)

    def play(self):
        print("Starting game of Kalaha!")
        while not self.board.is_game_over():
            print("-"*50)
            print(self.board)
            self.board.player_turn = self.current_player
            player = self.players[self.current_player]
            print(f"It's {player.name}'s turn.")
            cup = player.select_move(self.board)
            if self.current_player == 1:
                print_cup = 6 - cup
            else:
                print_cup = cup + 1
            print(f"{player.name} selects cup {print_cup}.")
            self.current_player = self.board.make_move(player.player_num, cup)
            print("-"*50)
        print(self.board)
        self.print_winner()

    def print_winner(self):
        p1_score = self.board.board[0][-1]
        p2_score = self.board.board[1][-1]
        if p1_score > p2_score:
            print(f"{self.players[0].name} wins with a score of {p1_score}-{p2_score}!")
        elif p2_score > p1_score:
            print(f"{self.players[1].name} wins with a score of {p2_score}-{p1_score}!")
        else:
            print(f"The game is a tie with a score of {p1_score}-{p2_score}!")
