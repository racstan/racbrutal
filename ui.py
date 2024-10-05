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
        health_bar_width = 200
        health_bar_height = 20
        health_percentage = health / PLAYER_MAX_HEALTH
        health_bar_x = (window_width - health_bar_width) // 2
        health_bar_y = 10

        # Draw background bar
        pygame.draw.rect(surface, (100, 100, 100), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        # Draw health
        pygame.draw.rect(surface, HEALTH_COLOR, (health_bar_x, health_bar_y, health_bar_width * health_percentage, health_bar_height))
        # Health text
        health_text = self.font.render(f"{int(health)}%", True, TEXT_COLOR)
        health_text_rect = health_text.get_rect(center=(health_bar_x + health_bar_width // 2, health_bar_y + health_bar_height // 2))
        surface.blit(health_text, health_text_rect)

    def draw_main_menu(self, surface, window_width, window_height):
        large_font = pygame.font.Font(FONT_NAME, 72)
        title_text = large_font.render("Rac's Flail Game", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(window_width // 2, window_height // 2 - 150))
        surface.blit(title_text, title_rect)

        # Start button
        button_rect_start = pygame.Rect(0, 0, 200, 50)
        button_rect_start.center = (window_width // 2, window_height // 2)
        # Settings button
        button_rect_settings = pygame.Rect(0, 0, 200, 50)
        button_rect_settings.center = (window_width // 2, window_height // 2 + 70)

        mouse_pos = pygame.mouse.get_pos()
        # Start button
        if button_rect_start.collidepoint(mouse_pos):
            color_start = BUTTON_HOVER_COLOR
        else:
            color_start = BUTTON_COLOR
        pygame.draw.rect(surface, color_start, button_rect_start)
        button_text_start = self.font.render("Start Game", True, TEXT_COLOR)
        button_text_rect_start = button_text_start.get_rect(center=button_rect_start.center)
        surface.blit(button_text_start, button_text_rect_start)

        # Settings button
        if button_rect_settings.collidepoint(mouse_pos):
            color_settings = BUTTON_HOVER_COLOR
        else:
            color_settings = BUTTON_COLOR
        pygame.draw.rect(surface, color_settings, button_rect_settings)
        button_text_settings = self.font.render("Settings", True, TEXT_COLOR)
        button_text_rect_settings = button_text_settings.get_rect(center=button_rect_settings.center)
        surface.blit(button_text_settings, button_text_rect_settings)

        return button_rect_start, button_rect_settings

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
        button_rect_resume = pygame.Rect(0, 0, 200, 50)
        button_rect_resume.center = (window_width // 2, window_height // 2 + 50)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect_resume.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, button_rect_resume)
        button_text = self.font.render("Resume", True, TEXT_COLOR)
        button_text_rect = button_text.get_rect(center=button_rect_resume.center)
        surface.blit(button_text, button_text_rect)
        return button_rect_resume

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
        high_score_rect = high_score_text.get_rect(center=(window_width // 2, window_height // 2 + 30))
        surface.blit(high_score_text, high_score_rect)

        # Try Again button
        button_rect_try_again = pygame.Rect(0, 0, 200, 50)
        button_rect_try_again.center = (window_width // 2, window_height // 2 + 100)
        mouse_pos = pygame.mouse.get_pos()
        if button_rect_try_again.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, button_rect_try_again)
        button_text = self.font.render("Try Again", True, TEXT_COLOR)
        button_text_rect = button_text.get_rect(center=button_rect_try_again.center)
        surface.blit(button_text, button_text_rect)
        return button_rect_try_again

    def draw_settings_menu(self, surface, window_width, window_height, music_on, sounds_on):
        overlay = pygame.Surface((window_width, window_height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, (0, 0))

        large_font = pygame.font.Font(FONT_NAME, 72)
        settings_text = large_font.render("Settings", True, TEXT_COLOR)
        settings_rect = settings_text.get_rect(center=(window_width // 2, window_height // 2 - 150))
        surface.blit(settings_text, settings_rect)

        # Music toggle button
        button_rect_music = pygame.Rect(0, 0, 200, 50)
        button_rect_music.center = (window_width // 2, window_height // 2 - 50)
        # Sounds toggle button
        button_rect_sounds = pygame.Rect(0, 0, 200, 50)
        button_rect_sounds.center = (window_width // 2, window_height // 2 + 20)
        # Back button
        button_rect_back = pygame.Rect(0, 0, 200, 50)
        button_rect_back.center = (window_width // 2, window_height // 2 + 90)

        mouse_pos = pygame.mouse.get_pos()

        # Music button
        if button_rect_music.collidepoint(mouse_pos):
            color_music = BUTTON_HOVER_COLOR
        else:
            color_music = BUTTON_COLOR
        pygame.draw.rect(surface, color_music, button_rect_music)
        music_status = "On" if music_on else "Off"
        button_text_music = self.font.render(f"Music: {music_status}", True, TEXT_COLOR)
        button_text_rect_music = button_text_music.get_rect(center=button_rect_music.center)
        surface.blit(button_text_music, button_text_rect_music)

        # Sounds button
        if button_rect_sounds.collidepoint(mouse_pos):
            color_sounds = BUTTON_HOVER_COLOR
        else:
            color_sounds = BUTTON_COLOR
        pygame.draw.rect(surface, color_sounds, button_rect_sounds)
        sounds_status = "On" if sounds_on else "Off"
        button_text_sounds = self.font.render(f"Sounds: {sounds_status}", True, TEXT_COLOR)
        button_text_rect_sounds = button_text_sounds.get_rect(center=button_rect_sounds.center)
        surface.blit(button_text_sounds, button_text_rect_sounds)

        # Back button
        if button_rect_back.collidepoint(mouse_pos):
            color_back = BUTTON_HOVER_COLOR
        else:
            color_back = BUTTON_COLOR
        pygame.draw.rect(surface, color_back, button_rect_back)
        button_text_back = self.font.render("Back", True, TEXT_COLOR)
        button_text_rect_back = button_text_back.get_rect(center=button_rect_back.center)
        surface.blit(button_text_back, button_text_rect_back)

        return button_rect_music, button_rect_sounds, button_rect_back
