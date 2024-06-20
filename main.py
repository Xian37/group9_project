import pygame
import sys
import time
import random
from pygame.locals import *
from constants import *
from Game_Objects.game_object import GameObject
from Game_Objects.player import Player
from Game_Objects.Player.Cucu import Cucu
from Game_Objects.Player.Fox import Fox
from Game_Objects.Player.Monkey import Monkey
from Game_Objects.enemy import Enemy
from Game_Objects.bomb import Bomb
from Game_Objects.flame import Flame
from Game_Objects.Items.Health_Item import HealthItem
from Game_Objects.Items.Invincible_Item import InvincibleItem
from Game_Objects.Items.Speed_Item import SpeedItem
from Game_Objects.Items.Landmine_Item import LandmineItem
from Game_Objects.game import Game
# Initialize Pygame
pygame.init()
pygame.time.set_timer(ADD_ITEM_EVENT, 5000)


def main():
    game_results = []

    def save_game_result(game):
        result = {
            'time': game.game_time,
            'winner': game.winner
        }
        game_results.append(result)
        with open('game_results.txt', 'a') as f:
            f.write(
                f"ROUND {round} RESULT --->    Time: {game.game_time:.2f} seconds, Bombs you have used: {bomb_times}, Winner: {game.winner}\n")

    def print_game_results():
        with open('game_results.txt', 'r') as f:
            for line in f:
                print(line)

    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 50)
    Role_chosen = False
    Map_chosen = False
    start = False
    bomb_times = 0
    global round
    round += 1
    try:
        while not start:
            screen.fill(LIGHTBLUE)
            screen.blit(start_image, (0, 150))
        # screen.blit(font.render('WELCOME TO BOMBERMAN!', True, BLACK), (50, 250))
            screen.blit(font.render('PRESS ENTER TO START',
                        True, DARKBLUE), (100, 650))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start = True
                        break
            pygame.display.flip()
        while not Role_chosen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        role_num = "1"
                        Role_chosen = True
                    elif event.key == pygame.K_2:
                        role_num = "2"
                        Role_chosen = True
                    elif event.key == pygame.K_3:
                        role_num = "3"
                        Role_chosen = True
            screen.fill(LIGHTBLUE)
            screen.blit(role1_image, (100, 300))
            screen.blit(role2_image, (400, 300))
            screen.blit(role3_image, (700, 300))
            screen.blit(font.render(' FOX', True, BLACK), (100, 600))
            screen.blit(font.render('MONKEY', True, BLACK), (400, 600))
            screen.blit(font.render('  GUGU', True, BLACK), (700, 600))
            screen.blit(font.render('---- 1 ----', True, BLACK), (100, 200))
            screen.blit(font.render('---- 2 ----', True, BLACK), (400, 200))
            screen.blit(font.render('---- 3 ----', True, BLACK), (700, 200))
            screen.blit(font2.render('HEALTH : 100', True, BLACK), (100, 50))
            screen.blit(font2.render('DAMAGE : 40', True, BLACK), (100, 100))
            screen.blit(font2.render('SPEED : 5', True, BLACK), (100, 150))
            screen.blit(font2.render('HEALTH : 125', True, BLACK), (400, 50))
            screen.blit(font2.render('DAMAGE : 30', True, BLACK), (400, 100))
            screen.blit(font2.render('SPEED : 5', True, BLACK), (400, 150))
            screen.blit(font2.render('HEALTH : 100', True, BLACK), (700, 50))
            screen.blit(font2.render('DAMAGE : 30', True, BLACK), (700, 100))
            screen.blit(font2.render('SPEED : 6.25', True, BLACK), (700, 150))
            pygame.display.flip()
        while not Map_chosen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        map_num = "1"
                        Map_chosen = True
                    elif event.key == pygame.K_2:
                        map_num = "2"
                        Map_chosen = True
                    elif event.key == pygame.K_3:
                        map_num = "3"
                        Map_chosen = True
            screen.fill(LIGHTBLUE)
            screen.blit(map1_image, (100, 300))
            screen.blit(map2_image, (400, 300))
            screen.blit(map3_image, (700, 300))
            screen.blit(font.render('FOREST', True, BLACK), (100, 600))
            screen.blit(font.render('OCEAN', True, BLACK), (400, 600))
            screen.blit(font.render('DESERT', True, BLACK), (700, 600))
            screen.blit(font.render('---- 1 ----', True, BLACK), (100, 200))
            screen.blit(font.render('---- 2 ----', True, BLACK), (400, 200))
            screen.blit(font.render('---- 3 ----', True, BLACK), (700, 200))
            pygame.display.flip()
        game = Game(map_num, role_num)
        clock = pygame.time.Clock()
        while True:
            if not game.enemies:
                game.game_over == True
            if game.game_over:
                game.draw()
                pygame.display.update()
                # Handle key events after game over or win
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                main()  # Restart the game
                                return  # Exit the current loop
                            elif event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()

                    # Redraw the game over/win screen
                    game.draw()

                    pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE and not game.game_over and game.player.can_place_bomb():
                        bomb_times += 1
                        bomb_x = (game.player.x - MARGIN_WIDTH) // TILE_SIZE * \
                            TILE_SIZE + MARGIN_WIDTH
                        bomb_y = (game.player.y - 10) // TILE_SIZE * \
                            TILE_SIZE + 10
                        if not any(bomb.x == bomb_x and bomb.y == bomb_y for bomb in game.bombs):
                            if role_num == '1':
                                game.bombs.append(
                                    Bomb(bomb_x, bomb_y, TILE_SIZE, RED, time.time(), 40, bomb_path))
                            else:
                                game.bombs.append(
                                    Bomb(bomb_x, bomb_y, TILE_SIZE, RED, time.time(), 30, bomb_path))
                            game.player.bombs -= 1  # Decrease bomb count
                if event.type == USEREVENT + 1:
                    if role_num == 3:
                        game.player.speed = 6.25  # Reset player speed
                    else:
                        game.player.speed = 5  # Reset player speed
                if event.type == USEREVENT + 2:
                    for enemy in game.enemies:
                        enemy.speed = 5  # Reset enemy speed
                if event.type == USEREVENT + 3:
                    game.player.invincible = False  # Reset player invincibility
                if event.type == USEREVENT + 4:
                    for enemy in game.enemies:
                        enemy.invincible = False  # Reset enemy invincibility
                if event.type == ADD_ITEM_EVENT:
                    game.generate_random_item()
            keys = pygame.key.get_pressed()
            if not game.game_over:
                if keys[K_LEFT]:
                    game.player.move(-game.player.speed, 0, game.map_data)
                if keys[K_RIGHT]:
                    game.player.move(game.player.speed, 0, game.map_data)
                if keys[K_UP]:
                    game.player.move(0, -game.player.speed, game.map_data)
                if keys[K_DOWN]:
                    game.player.move(0, game.player.speed, game.map_data)

            game.update()
            game.draw()
            pygame.display.update()
            clock.tick(30)
            if game.game_over:
                game.end_game()  # Ensure end_game is called
                save_game_result(game)  # Save game result

    finally:
        print_game_results()


if __name__ == "__main__":
    main()
