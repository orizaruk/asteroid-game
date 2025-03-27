import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)

    player_obj = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    running = True
     
    while running:
        # CLOSE GAME IF USER CLOSED THE SCREEN
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.Surface.fill(screen, (0, 0, 0))

        updateables.update(delta_time)
        # check if asteroids are colliding with player 
        for asteroid in asteroids:
            if asteroid.check_collision(player_obj):
                print("Game over!")
                sys.exit()


        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        delta_time = game_clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()
