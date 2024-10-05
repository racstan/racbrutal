# ui.py

import pygame
from settings import *

class UI:
    def __init__(self):
        self.font = pygame.font.Font(FONT_NAME, 36)

    def draw_hud(self, surface, score, health, window_width):
        # Score
        score_text = self.font.render(f"Score: {int(score)}", True, TEXT_COLOR)
        surface.blit(score_text, (10, 10))

        # Health bar
        for i in range(health):
            pygame.draw.rect(surface, HEALTH_COLOR, (window_width - 30 * (i + 1), 10, 20, 20))

    def draw_main_menu(self, surface, window_width, window_height):
        large_font = pygame.font.Font(FONT_NAME, 72)
        title_text = large_font.render("Flail Game", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(window_width // 2, window_height // 2 - 100))
        surface.blit(title_text, title_rect)

        # Start button
        button_rect = pygame.Rect(0, 0, 200, 50)
        button_rect.center = (window_width // 2, window_height // 2)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, button_rect)
        button_text = self.font.render("Start Game", True, TEXT_COLOR)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        surface.blit(button_text, button_text_rect)
        return button_rect

    def draw_pause_menu(self, surface, window_width, window_height):
        overlay = pygame.Surface((window_width, window_height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, (0, 0))

        large_font = pygame.font.Font(FONT_NAME, 72)
        pause_text = large_font.render("Paused", True, TEXT_COLOR)
        pause_rect = pause_text.get_rect(center=(window_width // 2, window_height // 2 - 50))
        surface.blit(pause_text, pause_rect)

        # Resume button
        button_rect = pygame.Rect(0, 0, 200, 50)
        button_rect.center = (window_width // 2, window_height // 2 + 50)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, button_rect)
        button_text = self.font.render("Resume", True, TEXT_COLOR)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        surface.blit(button_text, button_text_rect)
        return button_rect

    def draw_game_over(self, surface, score, window_width, window_height):
        overlay = pygame.Surface((window_width, window_height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, (0, 0))

        large_font = pygame.font.Font(FONT_NAME, 72)
        text = large_font.render("Game Over", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 50))
        surface.blit(text, text_rect)

        score_text = self.font.render(f"Your Score: {int(score)}", True, TEXT_COLOR)
        score_rect = score_text.get_rect(center=(window_width // 2, window_height // 2))
        surface.blit(score_text, score_rect)

        # Try Again button
        button_rect = pygame.Rect(0, 0, 200, 50)
        button_rect.center = (window_width // 2, window_height // 2 + 100)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, button_rect)
        button_text = self.font.render("Try Again", True, TEXT_COLOR)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        surface.blit(button_text, button_text_rect)
        return button_rect
