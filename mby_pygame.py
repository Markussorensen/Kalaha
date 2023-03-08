"""
This is not used, but just saved in case we wanted to use the pygame library for the game.
"""
import pygame

def main():
    use_pygame = False
    player1_human = False
    player2_human = False

    if use_pygame:
        # Initialize Pygame
        pygame.init()
        screen_width, screen_height = 800, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Kalaha")
        clock = pygame.time.Clock()

        # Initialize the game
        game = KalahaGamePygame(screen, clock)

        # Show the main menu
        game.show_menu()

        # Quit Pygame when the menu is closed
        pygame.quit()


class KalahaGamePygame:
    def __init__(self, num_cups=6, num_stones=4):
        # Initialize Pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        
        # Set up the display
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Kalaha")
        
        # Load images
        self.board_image = pygame.image.load("board.png").convert()
        self.stone_image = pygame.image.load("stone.png").convert_alpha()
        self.font = pygame.font.SysFont("Arial", 20)
        
        # Initialize the game
        self.board = KalahBoard(num_cups=num_cups, num_stones=num_stones)
        self.players = [KalahaPlayer("Player 1", True), KalahaPlayer("Player 2", False)]
        self.current_player = 0

    def play(self):
        # Start the game loop
        while not self.board.game_over():
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.current_player == 0:
                        if event.pos[1] < 300:
                            cup = event.pos[0] // 100
                        else:
                            cup = (event.pos[0] - 700) // 100
                        self.current_player = self.board.make_move(self.players[0].name, cup)
            
            # Draw the board
            self.screen.blit(self.board_image, (0, 0))
            
            # Draw the stones
            for i in range(6):
                for j in range(2):
                    num_stones = self.board.get_num_stones(i, j)
                    for k in range(num_stones):
                        if j == 0:
                            x = i * 100 + 50
                            y = (k + 1) * (300 // (num_stones + 1))
                        else:
                            x = (6 - i) * 100 + 750
                            y = (k + 1) * (300 // (num_stones + 1)) + 300
                        self.screen.blit(self.stone_image, (x, y))
                        
            # Draw the scores
            p1_score = self.board.get_score(0)
            p2_score = self.board.get_score(1)
            p1_text = self.font.render(f"Player 1: {p1_score}", True, (255, 255, 255))
            p2_text = self.font.render(f"Player 2: {p2_score}", True, (255, 255, 255))
            self.screen.blit(p1_text, (10, 560))
            self.screen.blit(p2_text, (690, 560))
            
            # Update the display
            pygame.display.flip()
            self.clock.tick(60)
        
        # Print the winner
        self.print_winner()
        
        # Quit Pygame
        pygame.quit()

    def print_winner(self):
        p1_score = self.board.get_score(0)
        p2_score = self.board.get_score(1)
        if p1_score > p2_score:
            print(f"Player 1 wins with a score of {p1_score}-{p2_score}!")
        elif p2_score > p1_score:
            print(f"Player 2 wins with a score of {p2_score}-{p1_score}!")
        else:
            print("The game ended in a tie!")
    
    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
        
    def draw_button(self, x, y, w, h, inactive_color, active_color, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            pygame.draw.rect(self.screen, active_color, (x, y, w, h))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.screen, inactive_color, (x, y, w, h))
            
        self.draw_text(text, self.font, (255, 255, 255), x + w // 2, y + h // 2)
        
    def show_menu(self):
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
            # Draw the menu
            self.screen.fill((0, 0, 0))
            self.draw_text("Kalaha", pygame.font.SysFont("Arial", 40), (255, 255, 255), 400, 100)
            self.draw_button(300, 250, 200, 50, (255, 0, 0), (200, 0, 0), "Play Game", self.play)
            self.draw_button(300, 350, 200, 50, (0, 255, 0), (0, 200, 0), "Exit", pygame.quit)
            
            # Update the display
            pygame.display.flip()
            self.clock.tick(60)

