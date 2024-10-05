# player.py

import pygame
from settings import *
from flail import Flail

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.base_speed = PLAYER_SPEED
        self.score = 0
        self.level = 1
        self.health = PLAYER_MAX_HEALTH
        self.radius = 15
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

        self.flail = Flail(self, groups)

        # Power-up effects
        self.invincible = False
        self.powerup_timer = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        self.velocity.y = 0
        if keys[pygame.K_w]:
            self.velocity.y = -self.speed
        if keys[pygame.K_s]:
            self.velocity.y = self.speed
        if keys[pygame.K_a]:
            self.velocity.x = -self.speed
        if keys[pygame.K_d]:
            self.velocity.x = self.speed

        # Flail controls
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            self.flail.throw()
        else:
            self.flail.retract()

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position
        self.flail.update()

        # Power-up duration handling
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
            if self.powerup_timer == 0:
                self.speed = self.base_speed
                self.invincible = False

    def draw(self, surface):
        pygame.draw.circle(surface, PLAYER_COLOR, (int(self.position.x), int(self.position.y)), self.radius)
