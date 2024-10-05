# opponent.py

import pygame
import random
from settings import *

class Opponent(pygame.sprite.Sprite):
    def __init__(self, groups, target, speed):
        super().__init__(groups)
        self.position = pygame.math.Vector2(
            random.choice([0, WINDOW_WIDTH]),
            random.randint(0, WINDOW_HEIGHT)
        )
        self.speed = speed
        self.target = target
        self.radius = 15  # Ensure radius is set
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

    def update(self):
        direction = self.target.position - self.position
        if direction.length() > 0:
            direction = direction.normalize()
            self.position += direction * self.speed
            self.rect.center = self.position

    def draw(self, surface):
        pygame.draw.circle(surface, OPPONENT_COLOR, (int(self.position.x), int(self.position.y)), self.radius)
