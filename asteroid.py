import pygame
from circleshape import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self)
        
        # Automatically add to specified groups
        if hasattr(self.__class__, 'containers'):
            for group in self.__class__.containers:
                group.add(self)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
