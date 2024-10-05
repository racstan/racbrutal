# main.py

import pygame
import random
from settings import *
from player import Player
from energy_particle import EnergyParticle
from enemy import Enemy
from powerup import PowerUp
from ui import UI
from game_state import GameState

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Flail Game")
    clock = pygame.time.Clock()

    game_state = GameState.MENU

    # Initialize UI
    ui = UI()

    running = True
    while running:
        if game_state == GameState.MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect = ui.draw_main_menu(window)
                    if button_rect.collidepoint(mouse_pos):
                        # Start the game
                        game_state = GameState.PLAYING
                        # Initialize game variables
                        all_sprites = pygame.sprite.Group()
                        particles = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        powerups = pygame.sprite.Group()
                        flails = pygame.sprite.Group()

                        player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, all_sprites)
                        player.flail.add(all_sprites, flails)

                        for _ in range(PARTICLE_COUNT):
                            EnergyParticle([all_sprites, particles])

                        # Events
                        enemy_spawn_event = pygame.USEREVENT + 1
                        pygame.time.set_timer(enemy_spawn_event, ENEMY_SPAWN_INTERVAL)

                        powerup_spawn_event = pygame.USEREVENT + 2
                        pygame.time.set_timer(powerup_spawn_event, POWERUP_SPAWN_INTERVAL)

                        level_up_event = pygame.USEREVENT + 3
                        pygame.time.set_timer(level_up_event, LEVEL_UP_TIME)

                        level = 1

            # Draw main menu
            window.fill(BACKGROUND_COLOR)
            ui.draw_main_menu(window)
            pygame.display.flip()

        elif game_state == GameState.PLAYING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == enemy_spawn_event:
                    enemy_type = random.choice(ENEMY_TYPES[:level])
                    Enemy(enemy_type, [all_sprites, enemies], player, speed_increment=level * ENEMY_SPEED_INCREMENT)
                elif event.type == powerup_spawn_event:
                    powerup_type = random.choice(POWERUP_TYPES)
                    PowerUp(powerup_type, [all_sprites, powerups])
                elif event.type == level_up_event:
                    if level < MAX_LEVEL:
                        level += 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = GameState.PAUSED

            # Update game objects
            player.handle_input()
            all_sprites.update()

            # Collision detection
            # Player collects energy particles
            collected_particles = pygame.sprite.spritecollide(player, particles, True, pygame.sprite.collide_circle)
            for particle in collected_particles:
                player.score += 10
                player.flail.length += FLAIL_GROWTH

            # Flail hits enemies
            hit_enemies = pygame.sprite.spritecollide(player.flail, enemies, False, pygame.sprite.collide_circle)
            for enemy in hit_enemies:
                enemy.health -= 1
                if enemy.health <= 0:
                    enemy.kill()
                    player.score += 50

            # Enemies collide with player
            colliding_enemies = pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_circle)
            for enemy in colliding_enemies:
                if not player.invincible:
                    player.health -= 1
                    if player.health <= 0:
                        game_state = GameState.GAME_OVER
                # Knockback effect (optional)
                knockback = (player.position - enemy.position).normalize() * 20
                player.position += knockback

            # Player collects power-ups
            collected_powerups = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_circle)
            for powerup in collected_powerups:
                if powerup.powerup_type == 'speed':
                    player.speed += 2
                    player.powerup_timer = POWERUP_DURATION
                elif powerup.powerup_type == 'invincibility':
                    player.invincible = True
                    player.powerup_timer = POWERUP_DURATION
                elif powerup.powerup_type == 'health':
                    if player.health < PLAYER_MAX_HEALTH:
                        player.health += 1

            # Drawing
            window.fill(BACKGROUND_COLOR)
            for sprite in all_sprites:
                sprite.draw(window)
            ui.draw_hud(window, player.score, level, player.health)
            pygame.display.flip()

            clock.tick(FPS)

        elif game_state == GameState.PAUSED:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = GameState.PLAYING
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect = ui.draw_pause_menu(window)
                    if button_rect.collidepoint(mouse_pos):
                        game_state = GameState.PLAYING

            # Draw pause menu
            ui.draw_pause_menu(window)
            pygame.display.flip()
            clock.tick(FPS)

        elif game_state == GameState.GAME_OVER:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button_rect = ui.draw_game_over(window, player.score)
                    if button_rect.collidepoint(mouse_pos):
                        game_state = GameState.MENU

            # Draw game over screen
            ui.draw_game_over(window, player.score)
            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
