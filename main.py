import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player_obj = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        # CLOSE GAME IF USER CLOSED THE SCREEN
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0, 0, 0))
        player_obj.draw(screen)
        pygame.display.flip()

        delta_time = game_clock.tick(60) / 1000





if __name__ == "__main__":
    main()
