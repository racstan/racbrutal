# energy_particle.py

import pygame
import random
from settings import *

class EnergyParticle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.position = pygame.math.Vector2(
            random.randint(0, WINDOW_WIDTH),
            random.randint(0, WINDOW_HEIGHT)
        )
        self.radius = 5
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, PARTICLE_COLOR, (int(self.position.x), int(self.position.y)), self.radius)
