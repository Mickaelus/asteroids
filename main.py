import pygame
from constants import *
from player import Player
BLACK = (0, 0, 0)

def main():
    pygame.init()
    clock = pygame.time.Clock()  # Create a new Clock object
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = clock.tick(60) / 1000
        player.update(dt)
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()
        
if __name__ == "__main__":
    main()