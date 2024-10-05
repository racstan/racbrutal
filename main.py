# main.py

import pygame
import random
from settings import *
from player import Player
from enemy import Enemy
from powerup import PowerUp
from energy_ball import EnergyBall
from ui import UI
from game_state import GameState
from high_score import save_high_score, load_high_score

def main():
    pygame.init()

    # Allow window to be resizable
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Rac's Flail Game")
    clock = pygame.time.Clock()

    # Load sounds and music
    pygame.mixer.music.load('assets/music/background_music.mp3')
    pygame.mixer.music.set_volume(MUSIC_VOLUME)
    pygame.mixer.music.play(-1)

    hit_sound = pygame.mixer.Sound('assets/sounds/hit.wav')
    powerup_sound = pygame.mixer.Sound('assets/sounds/powerup.wav')
    energy_ball_sound = pygame.mixer.Sound('assets/sounds/energy_ball.wav')

    hit_sound.set_volume(SFX_VOLUME)
    powerup_sound.set_volume(SFX_VOLUME)
    energy_ball_sound.set_volume(SFX_VOLUME)

    ui = UI()
    game_state = GameState.MENU

    window_width, window_height = WINDOW_WIDTH, WINDOW_HEIGHT

    # Load high score
    high_score = load_high_score()

    # Settings variables
    music_volume = MUSIC_VOLUME
    sfx_volume = SFX_VOLUME

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
                    start_button_rect, settings_button_rect = ui.draw_main_menu(window, window_width, window_height)
                    if start_button_rect.collidepoint(mouse_pos):
                        # Start the game
                        game_state = GameState.PLAYING
                        # Initialize game variables
                        all_sprites = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        powerups = pygame.sprite.Group()
                        energy_balls = pygame.sprite.Group()
                        flails = pygame.sprite.Group()

                        player = Player(window_width // 2, window_height // 2, all_sprites, window_width, window_height)
                        player.flail.add(all_sprites, flails)

                        # Events
                        enemy_spawn_event = pygame.USEREVENT + 1
                        pygame.time.set_timer(enemy_spawn_event, 1000)

                        powerup_spawn_event = pygame.USEREVENT + 2
                        pygame.time.set_timer(powerup_spawn_event, 10000)

                        energy_ball_spawn_event = pygame.USEREVENT + 3
                        pygame.time.set_timer(energy_ball_spawn_event, ENERGY_BALL_SPAWN_INTERVAL)

                    elif settings_button_rect.collidepoint(mouse_pos):
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
                    music_slider_rect, sfx_slider_rect, back_button_rect = ui.draw_settings_menu(window, music_volume, sfx_volume, window_width, window_height)
                    if back_button_rect.collidepoint(mouse_pos):
                        game_state = GameState.MENU
                elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    music_slider_rect, sfx_slider_rect, back_button_rect = ui.draw_settings_menu(window, music_volume, sfx_volume, window_width, window_height)
                    if music_slider_rect.collidepoint(mouse_pos):
                        music_volume = (mouse_pos[0] - music_slider_rect.x) / 200
                        if music_volume < 0:
                            music_volume = 0
                        if music_volume > 1:
                            music_volume = 1
                        pygame.mixer.music.set_volume(music_volume)
                    elif sfx_slider_rect.collidepoint(mouse_pos):
                        sfx_volume = (mouse_pos[0] - sfx_slider_rect.x) / 200
                        if sfx_volume < 0:
                            sfx_volume = 0
                        if sfx_volume > 1:
                            sfx_volume = 1
                        hit_sound.set_volume(sfx_volume)
                        powerup_sound.set_volume(sfx_volume)
                        energy_ball_sound.set_volume(sfx_volume)

            # Draw settings menu
            window.fill(BACKGROUND_COLOR)
            ui.draw_settings_menu(window, music_volume, sfx_volume, window_width, window_height)
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
                    for energy_ball in energy_balls:
                        energy_ball.resize(window_width, window_height)
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
                elif event.type == energy_ball_spawn_event:
                    EnergyBall([all_sprites, energy_balls], window_width, window_height)

            # Update game objects
            player.handle_input()
            all_sprites.update()

            # Collision detection
            # Flail hits enemies
            hit_enemies = pygame.sprite.spritecollide(
                player.flail, enemies, False, pygame.sprite.collide_circle)
            for enemy in hit_enemies:
                enemy.health -= 1
                if enemy.health <= 0:
                    enemy.kill()
                    hit_sound.play()
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
                        # Save high score
                        if player.score > high_score:
                            high_score = player.score
                            save_high_score(high_score)
                        break
                enemy.kill()

            # Player collects power-ups
            collected_powerups = pygame.sprite.spritecollide(
                player, powerups, True, pygame.sprite.collide_circle)
            for powerup in collected_powerups:
                powerup_sound.play()
                if powerup.powerup_type == 'shield':
                    player.shield = True
                    player.powerup_timer = POWERUP_DURATION // (1000 // FPS)
                elif powerup.powerup_type == 'double_score':
                    player.double_score = True
                    player.powerup_timer = POWERUP_DURATION // (1000 // FPS)

            # Player collects energy balls
            collected_energy_balls = pygame.sprite.spritecollide(
                player, energy_balls, True, pygame.sprite.collide_circle)
            for energy_ball in collected_energy_balls:
                energy_ball_sound.play()
                player.health += ENERGY_BALL_RECHARGE_AMOUNT
                if player.health > PLAYER_MAX_HEALTH:
                    player.health = PLAYER_MAX_HEALTH

            # Drawing
            window.fill(BACKGROUND_COLOR)
            for sprite in all_sprites:
                sprite.draw(window)
            ui.draw_hud(window, player.score, player.health, window_width)
            pygame.display.flip()

            clock.tick
