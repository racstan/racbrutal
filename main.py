# main.py

import pygame
import random
from settings import *
from player import Player
from energy_particle import EnergyParticle
from enemy import Opponent
from ui import UI
from game_state import GameState

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Racbrutal")
    clock = pygame.time.Clock()

    # Game variables
    game_state = GameState.PLAYING

    while True:
        if game_state == GameState.PLAYING:
            # Initialize game objects
            all_sprites = pygame.sprite.Group()
            particles = pygame.sprite.Group()
            opponents = pygame.sprite.Group()
            flails = pygame.sprite.Group()

            player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, all_sprites)
            ui = UI()

            player.flail.add(all_sprites, flails)

            for _ in range(PARTICLE_COUNT):
                EnergyParticle([all_sprites, particles])

            # Events
            opponent_spawn_event = pygame.USEREVENT + 1
            pygame.time.set_timer(opponent_spawn_event, OPPONENT_SPAWN_INTERVAL)

            level_up_event = pygame.USEREVENT + 2
            pygame.time.set_timer(level_up_event, LEVEL_UP_TIME)

            running = True
            while running:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                    elif event.type == opponent_spawn_event:
                        for _ in range(LEVEL_OPPONENT_INCREMENT):
                            Opponent([all_sprites, opponents], player, speed=2 + player.level * 0.5)

                    elif event.type == level_up_event:
                        player.level += 1

                # Update game objects
                player.handle_input()
                all_sprites.update()

                # Collision detection
                collected_particles = pygame.sprite.spritecollide(
                    player, particles, True, pygame.sprite.collide_circle
                )
                for particle in collected_particles:
                    player.score += 10
                    player.flail.length += FLAIL_GROWTH

                hit_opponents = pygame.sprite.spritecollide(
                    player.flail, opponents, True, pygame.sprite.collide_circle
                )
                for opponent in hit_opponents:
                    player.score += 50
                    print("Opponent hit by flail!")  # Debugging print

                colliding_opponents = pygame.sprite.spritecollide(
                    player, opponents, True, pygame.sprite.collide_circle
                )
                for opponent in colliding_opponents:
                    player.health -= 1
                    if player.health <= 0:
                        game_state = GameState.GAME_OVER
                        running = False

                # Drawing
                window.fill(BACKGROUND_COLOR)
                for sprite in all_sprites:
                    sprite.draw(window)
                ui.draw_score(window, player.score, player.level)
                ui.draw_health(window, player.health)
                pygame.display.flip()

        elif game_state == GameState.GAME_OVER:
            # Game over screen
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        button_rect = ui.draw_game_over(window, player.score)
                        if button_rect.collidepoint(mouse_pos):
                            # Restart the game
                            game_state = GameState.PLAYING
                            break
                else:
                    # Draw game over screen
                    window.fill(BACKGROUND_COLOR)
                    ui.draw_game_over(window, player.score)
                    pygame.display.flip()
                    continue
                break

if __name__ == "__main__":
    main()
