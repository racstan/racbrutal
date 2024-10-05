# flail.py

import pygame
import math
from settings import *

class Flail(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.player = player
        self.length = FLAIL_BASE_LENGTH
        self.angle = 0
        self.speed = FLAIL_SPEED
        self.thrown = False
        self.offset = pygame.math.Vector2(self.length, 0)
        self.radius = FLAIL_BASE_RADIUS
        self.max_radius = FLAIL_MAX_RADIUS
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.position = self.player.position + self.offset

    def throw(self):
        self.thrown = True

    def retract(self):
        self.thrown = False

    def update(self):
        self.position = self.player.position

        # Adjust flail radius based on player's score
        self.radius = FLAIL_BASE_RADIUS + self.player.score * FLAIL_GROWTH_RATE
        if self.radius > self.max_radius:
            self.radius = self.max_radius

        # Realistic swinging mechanics
        if self.thrown:
            self.angle += self.speed
        else:
            self.angle -= self.speed

        self.offset = pygame.math.Vector2(self.length, 0).rotate(-self.angle)

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
                           (int(flail_pos.x), int(flail_pos.y)), int(self.radius))
