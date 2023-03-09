from src.kalaha.game import KalahaGameNormal


def main():
    # Set up the game
    p1_is_human = False
    p2_is_human = True

    # Initialize the game
    game = KalahaGameNormal(p1_is_human=p1_is_human, p2_is_human=p2_is_human)

    # Start the game
    game.play()


# Initialize Pygame
if __name__ == "__main__":
    main()
