# player.py

import pygame
from settings import *
from flail import Flail

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_BASE_SPEED
        self.score = 0
        self.health = PLAYER_MAX_HEALTH
        self.radius = PLAYER_RADIUS
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
        self.check_bounds()
        self.rect.center = self.position
        self.flail.update()

        # Power-up duration handling
        if self.powerup_timer > 0:
            self.powerup_timer -= 1
            if self.powerup_timer == 0:
                self.shield = False
                self.double_score = False

    def check_bounds(self):
        # Ensure the player stays within the window boundaries
        if self.position.x - self.radius < 0:
            self.position.x = self.radius
        if self.position.x + self.radius > WINDOW_WIDTH:
            self.position.x = WINDOW_WIDTH - self.radius
        if self.position.y - self.radius < 0:
            self.position.y = self.radius
        if self.position.y + self.radius > WINDOW_HEIGHT:
            self.position.y = WINDOW_HEIGHT - self.radius

    def draw(self, surface):
        pygame.draw.circle(surface, PLAYER_COLOR,
                           (int(self.position.x), int(self.position.y)),
                           self.radius)
