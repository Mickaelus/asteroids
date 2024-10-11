import pygame
from asteroidfield import *
from constants import *
from player import Player
BLACK = (0, 0, 0)

def main():
    pygame.init()
    clock = pygame.time.Clock()  # Create a new Clock object
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Asteroid.containers = (asteroids, updatable, drawable)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = clock.tick(60) / 1000
        for sprite in updatable:
            sprite.update(dt)
        for sprite in asteroids:
            if sprite.check_collision(player) is True:
                print("Game over!")
                pygame.quit()
                return
        screen.fill(BLACK)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
if __name__ == "__main__":
    main()