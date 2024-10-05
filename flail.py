# flail.py

import pygame
import math
from settings import *

class Flail(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.player = player
        self.length = FLAIL_LENGTH
        self.angle = 0
        self.speed = FLAIL_SPEED
        self.thrown = False
        self.offset = pygame.math.Vector2(self.length, 0)
        self.original_offset = self.offset.copy()
        self.radius = 10
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)

    def throw(self):
        self.thrown = True

    def retract(self):
        self.thrown = False

    def update(self):
        self.position = self.player.position
        # Adjust flail length based on player size
        self.length = FLAIL_LENGTH + (self.player.radius - PLAYER_MIN_RADIUS)
        self.offset = self.original_offset.rotate(-self.angle)
        self.offset.scale_to_length(self.length)
        self.angle = (self.angle + self.speed) % 360

        flail_pos = self.position + self.offset
        self.rect.center = flail_pos

    def draw(self, surface):
        flail_pos = self.position + self.offset
        pygame.draw.line(surface, CHAIN_COLOR,
                         (int(self.position.x), int(self.position.y)),
                         (int(flail_pos.x), int(flail_pos.y)), 2)
        pygame.draw.circle(surface, FLAIL_COLOR,
                           (int(flail_pos.x), int(flail_pos.y)), self.radius)
