# ui.py

import pygame
from settings import *

class UI:
    def __init__(self):
        self.font = pygame.font.Font(FONT_NAME, 36)
        self.small_font = pygame.font.Font(FONT_NAME, 24)

    def draw_hud(self, surface, score, health, window_width):
        # Score
        score_text = self.font.render(f"Score: {int(score)}", True, TEXT_COLOR)
        surface.blit(score_text, (10, 10))

        # Health bar
        health_bar_width = 200
        health_bar_height = 20
        health_bar_x = window_width - health_bar_width - 20
        health_bar_y = 10

        # Background
        pygame.draw.rect(surface, (100, 100, 100), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        # Health amount
        health_width = (health / PLAYER_MAX_HEALTH) * health_bar_width
        pygame.draw.rect(surface, HEALTH_COLOR, (health_bar_x, health_bar_y, health_width, health_bar_height))
        # Border
        pygame.draw.rect(surface, (255, 255, 255), (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 2)

        # Health percentage text
        health_text = self.small_font.render(f"{int(health)}%", True, TEXT_COLOR)
        health_text_rect = health_text.get_rect(center=(health_bar_x + health_bar_width / 2, health_bar_y + health_bar_height / 2))
        surface.blit(health_text, health_text_rect)

    def draw_main_menu(self, surface, window_width, window_height):
        large_font = pygame.font.Font(FONT_NAME, 72)
        title_text = large_font.render("Rac's Flail Game", True, TEXT_COLOR)
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

        # Settings button
        settings_button_rect = pygame.Rect(0, 0, 200, 50)
        settings_button_rect.center = (window_width // 2, window_height // 2 + 70)
        if settings_button_rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, settings_button_rect)
        settings_text = self.font.render("Settings", True, TEXT_COLOR)
        settings_text_rect = settings_text.get_rect(center=settings_button_rect.center)
        surface.blit(settings_text, settings_text_rect)

        return button_rect, settings_button_rect

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

    def draw_game_over(self, surface, score, high_score, window_width, window_height):
        overlay = pygame.Surface((window_width, window_height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, (0, 0))

        large_font = pygame.font.Font(FONT_NAME, 72)
        text = large_font.render("Game Over", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2 - 100))
        surface.blit(text, text_rect)

        score_text = self.font.render(f"Your Score: {int(score)}", True, TEXT_COLOR)
        score_rect = score_text.get_rect(center=(window_width // 2, window_height // 2 - 30))
        surface.blit(score_text, score_rect)

        high_score_text = self.font.render(f"High Score: {int(high_score)}", True, TEXT_COLOR)
        high_score_rect = high_score_text.get_rect(center=(window_width // 2, window_height // 2 + 10))
        surface.blit(high_score_text, high_score_rect)

        # Try Again button
        button_rect = pygame.Rect(0, 0, 200, 50)
        button_rect.center = (window_width // 2, window_height // 2 + 100)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, button_rect)
        button_text = self.font.render("Main Menu", True, TEXT_COLOR)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        surface.blit(button_text, button_text_rect)
        return button_rect

    def draw_settings_menu(self, surface, music_volume, sfx_volume, window_width, window_height):
        overlay = pygame.Surface((window_width, window_height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, (0, 0))

        large_font = pygame.font.Font(FONT_NAME, 72)
        settings_text = large_font.render("Settings", True, TEXT_COLOR)
        settings_rect = settings_text.get_rect(center=(window_width // 2, window_height // 2 - 150))
        surface.blit(settings_text, settings_rect)

        # Music Volume Slider
        music_text = self.font.render("Music Volume", True, TEXT_COLOR)
        music_rect = music_text.get_rect(center=(window_width // 2, window_height // 2 - 50))
        surface.blit(music_text, music_rect)

        music_slider_rect = pygame.Rect(window_width // 2 - 100, window_height // 2 - 20, 200, 10)
        pygame.draw.rect(surface, (100, 100, 100), music_slider_rect)
        pygame.draw.rect(surface, (255, 255, 255), (music_slider_rect.x, music_slider_rect.y, music_volume * 200, 10))

        # SFX Volume Slider
        sfx_text = self.font.render("SFX Volume", True, TEXT_COLOR)
        sfx_rect = sfx_text.get_rect(center=(window_width // 2, window_height // 2 + 30))
        surface.blit(sfx_text, sfx_rect)

        sfx_slider_rect = pygame.Rect(window_width // 2 - 100, window_height // 2 + 60, 200, 10)
        pygame.draw.rect(surface, (100, 100, 100), sfx_slider_rect)
        pygame.draw.rect(surface, (255, 255, 255), (sfx_slider_rect.x, sfx_slider_rect.y, sfx_volume * 200, 10))

        # Back button
        back_button_rect = pygame.Rect(0, 0, 200, 50)
        back_button_rect.center = (window_width // 2, window_height // 2 + 150)
        mouse_pos = pygame.mouse.get_pos()
        if back_button_rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, back_button_rect)
        back_text = self.font.render("Back", True, TEXT_COLOR)
        back_text_rect = back_text.get_rect(center=back_button_rect.center)
        surface.blit(back_text, back_text_rect)

        return music_slider_rect, sfx_slider_rect, back_button_rect
