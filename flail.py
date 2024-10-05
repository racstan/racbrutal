# flail.py

import pygame
import math
from settings import *

class Flail(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.player = player
        self.base_length = FLAIL_BASE_LENGTH
        self.length = self.base_length
        self.max_length = FLAIL_MAX_LENGTH
        self.angle = 0
        self.speed = FLAIL_SPEED
        self.thrown = False
        self.offset = pygame.math.Vector2(self.length, 0)
        self.radius = 10
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.position = self.player.position + self.offset

    def throw(self):
        self.thrown = True

    def retract(self):
        self.thrown = False

    def update(self):
        self.position = self.player.position

        # Adjust flail length based on player's score
        self.length = self.base_length + self.player.score * FLAIL_GROWTH_RATE
        if self.length > self.max_length:
            self.length = self.max_length

        # Realistic swinging mechanics
        if self.thrown:
            if self.length < self.max_length:
                self.length += 2  # Extend flail when thrown
        else:
            if self.length > self.base_length:
                self.length -= 2  # Retract flail when not thrown

        self.offset = pygame.math.Vector2(self.length, 0).rotate(-self.angle)
        self.angle = (self.angle + self.speed) % 360

        flail_pos = self.position + self.offset
        self.rect.center = flail_pos

    def draw(self, surface):
        flail_pos = self.position + self.offset
        # Draw the chain
        pygame.draw.line(surface, CHAIN_COLOR,
                         (int(self.position.x), int(self.position.y)),
                         (int(flail_pos.x), int(flail_pos.y)), 2)
        # Draw the flail as a circle
        pygame.draw.circle(surface, FLAIL_COLOR,
                           (int(flail_pos.x), int(flail_pos.y)), self.radius)
