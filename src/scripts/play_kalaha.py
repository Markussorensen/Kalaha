from src.game import KalahaGameNormal
from src.player import KalahaPlayer

def main():
    # Initialize the game
    player1 = KalahaPlayer(player_num=0, name="Player 1", is_human=False, ai_method="minimax", minimax_depth=10)
    player2 = KalahaPlayer(player_num=1, name="Player 2", is_human=False, ai_method="minimax", minimax_depth=10)
    game = KalahaGameNormal(player1=player1, player2=player2)

    # Start the game
    game.play()


# Initialize Pygame
if __name__ == "__main__":
    main()
