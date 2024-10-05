# player.py

import pygame
from settings import *
from flail import Flail

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.base_speed = PLAYER_BASE_SPEED
        self.speed = self.base_speed
        self.score = 0
        self.health = PLAYER_MAX_HEALTH
        self.radius = PLAYER_MIN_RADIUS
        self.max_radius = PLAYER_MAX_RADIUS
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

        self.flail = Flail(self, groups)

        # Power-up effects
        self.shield = False
        self.double_score = False
        self.powerup_timer = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        self.velocity.y = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.velocity.y = -self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.velocity.y = self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
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
                self.shield = False
                self.double_score = False

    def grow(self, amount):
        self.radius += amount * PLAYER_GROWTH_RATE
        if self.radius > self.max_radius:
            self.radius = self.max_radius
        self.update_rect()

    def shrink(self):
        self.radius -= PLAYER_SHRINK_RATE
        if self.radius < PLAYER_MIN_RADIUS:
            self.radius = PLAYER_MIN_RADIUS
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(0, 0, int(self.radius * 2), int(self.radius * 2))
        self.rect.center = self.position

    def draw(self, surface):
        pygame.draw.circle(surface, PLAYER_COLOR,
                           (int(self.position.x), int(self.position.y)),
                           int(self.radius))
