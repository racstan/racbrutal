# health_ball.py

import pygame
import random
from settings import *

class HealthBall(pygame.sprite.Sprite):
    def __init__(self, groups, window_width, window_height):
        super().__init__(groups)
        self.window_width = window_width
        self.window_height = window_height
        self.radius = HEALTH_BALL_RADIUS
        self.position = pygame.math.Vector2(
            random.randint(self.radius, self.window_width - self.radius),
            random.randint(self.radius, self.window_height - self.radius)
        )
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

    def resize(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, ENERGY_BALL_COLOR,
                           (int(self.position.x), int(self.position.y)),
                           self.radius)
