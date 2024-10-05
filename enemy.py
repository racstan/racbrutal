# enemy.py

import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type, groups, target, window_width, window_height):
        super().__init__(groups)
        self.enemy_type = enemy_type
        self.window_width = window_width
        self.window_height = window_height
        self.position = pygame.math.Vector2(
            random.choice([0, self.window_width]),
            random.randint(0, self.window_height)
        )
        self.speed = ENEMY_BASE_SPEED * ENEMY_SPEED_MULTIPLIER[enemy_type]
        self.target = target
        self.health = ENEMY_HEALTH[enemy_type]
        self.damage = ENEMY_DAMAGE[enemy_type]
        self.radius = 15
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

    def update(self):
        self.move_towards_player()
        self.rect.center = self.position

    def move_towards_player(self):
        direction = self.target.position - self.position
        if direction.length() > 0:
            direction = direction.normalize()
            self.position += direction * self.speed

    def resize(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

    def draw(self, surface):
        color = ENEMY_COLORS[self.enemy_type]
        pygame.draw.circle(surface, color,
                           (int(self.position.x), int(self.position.y)),
                           self.radius)
