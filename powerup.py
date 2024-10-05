# powerup.py

import pygame
import random
from settings import *

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, powerup_type, groups):
        super().__init__(groups)
        self.powerup_type = powerup_type
        self.position = pygame.math.Vector2(
            random.randint(50, WINDOW_WIDTH - 50),
            random.randint(50, WINDOW_HEIGHT - 50)
        )
        self.radius = 10
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, POWERUP_COLOR,
                           (int(self.position.x), int(self.position.y)),
                           self.radius)
