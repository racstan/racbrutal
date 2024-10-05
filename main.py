# main.py

import pygame
import random
from settings import *
from player import Player
from enemy import Enemy
from powerup import PowerUp
from health_ball import HealthBall
from ui import UI
from game_state import GameState
from high_score import load_high_score, save_high_score

def main():
    pygame.init()

    # Allow window to be resizable
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Rac's Flail Game")
    clock = pygame.time.Clock()

    ui = UI()
    game_state = GameState.MENU

    window_width, window_height = WINDOW_WIDTH, WINDOW_HEIGHT

    # Load high score
    high_score = load_high_score(HIGH_SCORE_FILE)

    # Settings
    music_on = True  # Placeholder, as we have no music
    sounds_on = True  # Placeholder, as we have no sounds

    running = True
    while running:
        if game_state == GameState.MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    window_width, window_height = event.w, event.h
                    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        # Toggle fullscreen
                        pygame.display.toggle_fullscreen()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect_start, button_rect_settings = ui.draw_main_menu(window, window_width, window_height)
                    if button_rect_start.collidepoint(mouse_pos):
                        # Start the game
                        game_state = GameState.PLAYING
                        # Initialize game variables
                        all_sprites = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        powerups = pygame.sprite.Group()
                        health_balls = pygame.sprite.Group()
                        flails = pygame.sprite.Group()

                        player = Player(window_width // 2, window_height // 2, all_sprites, window_width, window_height)
                        player.flail.add(all_sprites, flails)

                        # Events
                        enemy_spawn_event = pygame.USEREVENT + 1
                        pygame.time.set_timer(enemy_spawn_event, 1000)

                        powerup_spawn_event = pygame.USEREVENT + 2
                        pygame.time.set_timer(powerup_spawn_event, 10000)

                        health_ball_spawn_event = pygame.USEREVENT + 3
                        pygame.time.set_timer(health_ball_spawn_event, HEALTH_BALL_SPAWN_INTERVAL)

                    elif button_rect_settings.collidepoint(mouse_pos):
                        game_state = GameState.SETTINGS

            # Draw main menu
            window.fill(BACKGROUND_COLOR)
            ui.draw_main_menu(window, window_width, window_height)
            pygame.display.flip()
            clock.tick(FPS)

        elif game_state == GameState.SETTINGS:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    window_width, window_height = event.w, event.h
                    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        pygame.display.toggle_fullscreen()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect_music, button_rect_sounds, button_rect_back = ui.draw_settings_menu(
                        window, window_width, window_height, music_on, sounds_on)
                    if button_rect_music.collidepoint(mouse_pos):
                        music_on = not music_on
                    elif button_rect_sounds.collidepoint(mouse_pos):
                        sounds_on = not sounds_on
                    elif button_rect_back.collidepoint(mouse_pos):
                        game_state = GameState.MENU

            # Draw settings menu
            window.fill(BACKGROUND_COLOR)
            ui.draw_settings_menu(window, window_width, window_height, music_on, sounds_on)
            pygame.display.flip()
            clock.tick(FPS)

        elif game_state == GameState.PLAYING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    window_width, window_height = event.w, event.h
                    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                    player.resize(window_width, window_height)
                    for enemy in enemies:
                        enemy.resize(window_width, window_height)
                    for powerup in powerups:
                        powerup.resize(window_width, window_height)
                    for health_ball in health_balls:
                        health_ball.resize(window_width, window_height)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = GameState.PAUSED
                    elif event.key == pygame.K_F11:
                        # Toggle fullscreen
                        pygame.display.toggle_fullscreen()
                elif event.type == enemy_spawn_event:
                    enemy_type = random.choice(ENEMY_TYPES)
                    Enemy(enemy_type, [all_sprites, enemies], player, window_width, window_height)
                elif event.type == powerup_spawn_event:
                    powerup_type = random.choice(POWERUP_TYPES)
                    PowerUp(powerup_type, [all_sprites, powerups], window_width, window_height)
                elif event.type == health_ball_spawn_event:
                    # Spawn health energy ball
                    HealthBall([all_sprites, health_balls], window_width, window_height)

            # Update game objects
            player.handle_input()
            all_sprites.update()

            # Health regeneration
            player.health += HEALTH_REGEN_RATE
            if player.health > PLAYER_MAX_HEALTH:
                player.health = PLAYER_MAX_HEALTH

            # Collision detection
            # Flail hits enemies
            hit_enemies = pygame.sprite.spritecollide(
                player.flail, enemies, False, pygame.sprite.collide_circle)
            for enemy in hit_enemies:
                enemy.health -= 1
                if enemy.health <= 0:
                    enemy.kill()
                    score_increment = 50
                    if player.double_score:
                        score_increment *= 2
                    player.score += score_increment

            # Enemies collide with player
            colliding_enemies = pygame.sprite.spritecollide(
                player, enemies, False, pygame.sprite.collide_circle)
            for enemy in colliding_enemies:
                if not player.shield:
                    player.health -= enemy.damage
                    if player.health <= 0:
                        game_state = GameState.GAME_OVER
                        # Update high score
                        if player.score > high_score:
                            high_score = player.score
                            save_high_score(HIGH_SCORE_FILE, high_score)
                        break
                enemy.kill()

            # Player collects power-ups
            collected_powerups = pygame.sprite.spritecollide(
                player, powerups, True, pygame.sprite.collide_circle)
            for powerup in collected_powerups:
                if powerup.powerup_type == 'shield':
                    player.shield = True
                    player.powerup_timer = POWERUP_DURATION // (1000 // FPS)
                elif powerup.powerup_type == 'double_score':
                    player.double_score = True
                    player.powerup_timer = POWERUP_DURATION // (1000 // FPS)

            # Player collects health balls
            collected_health_balls = pygame.sprite.spritecollide(
                player, health_balls, True, pygame.sprite.collide_circle)
            for health_ball in collected_health_balls:
                player.health += HEALTH_BALL_RECHARGE
                if player.health > PLAYER_MAX_HEALTH:
                    player.health = PLAYER_MAX_HEALTH

            # Drawing
            window.fill(BACKGROUND_COLOR)
            for sprite in all_sprites:
                sprite.draw(window)
            ui.draw_hud(window, player.score, player.health, window_width)
            pygame.display.flip()

            clock.tick(FPS)

        elif game_state == GameState.PAUSED:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    window_width, window_height = event.w, event.h
                    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                    player.resize(window_width, window_height)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = GameState.PLAYING
                    elif event.key == pygame.K_F11:
                        # Toggle fullscreen
                        pygame.display.toggle_fullscreen()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect_resume = ui.draw_pause_menu(window, window_width, window_height)
                    if button_rect_resume.collidepoint(mouse_pos):
                        game_state = GameState.PLAYING

            # Draw pause menu
            ui.draw_pause_menu(window, window_width, window_height)
            pygame.display.flip()
            clock.tick(FPS)

        elif game_state == GameState.GAME_OVER:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    window_width, window_height = event.w, event.h
                    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        # Toggle fullscreen
                        pygame.display.toggle_fullscreen()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect_try_again = ui.draw_game_over(window, player.score, high_score, window_width, window_height)
                    if button_rect_try_again.collidepoint(mouse_pos):
                        game_state = GameState.MENU

            # Draw game over screen
            ui.draw_game_over(window, player.score, high_score, window_width, window_height)
            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
