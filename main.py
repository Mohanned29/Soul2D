import pygame
import sys
from player import Player
from obstacle import Obstacle

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("SOULS")
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Start Screen Elements
player_stand = pygame.image.load('graphics/player/idle.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (player_stand.get_width() * 2, player_stand.get_height() * 2))
player_stand_rect = player_stand.get_rect(center=(400, 180))

game_name = font.render('SOULS', False, (255, 255, 255))
game_name_rect = game_name.get_rect(center=(400, 80))
game_message = font.render("Press space to start the game", False, (255, 255, 255))
game_message_rect = game_message.get_rect(center=(400, 340))

# Backgrounds
sky_surface = pygame.image.load('graphics/bg.png').convert_alpha()
ground_surface = pygame.image.load('graphics/floor.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (800, 400))
wall_surface = pygame.image.load('graphics/wall.png').convert_alpha()
wall_surface = pygame.transform.scale(wall_surface, (800, 400))
flag_surface = pygame.image.load('graphics/columns&falgs.png').convert_alpha()
flag_surface = pygame.transform.scale(flag_surface, (800, 400))
candle_surface = pygame.image.load('graphics/candeliar.png').convert_alpha()
candle_surface = pygame.transform.scale(candle_surface, (800, 400))
dragon_surface = pygame.image.load('graphics/dragon.png').convert_alpha()
dragon_surface = pygame.transform.scale(dragon_surface, (800, 400))

# Lives System
heart_interface1 = pygame.image.load('graphics/heart.png').convert_alpha()
heart_interface1 = pygame.transform.scale(heart_interface1, (heart_interface1.get_width() // 16, heart_interface1.get_height() // 16))
heart_list = [heart_interface1, heart_interface1, heart_interface1]  # Assuming 3 lives initially
heart_rect = heart_interface1.get_rect(topleft=(0, 0))

game_active = False
player = pygame.sprite.GroupSingle(Player())
obstacles = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(wall_surface, (0, 0))
        screen.blit(flag_surface, (0, 0))
        screen.blit(candle_surface, (0, 0))
        screen.blit(dragon_surface, (0, 0))
        
        player.update()
        obstacles.update()
        player.draw(screen)
        obstacles.draw(screen)
        
        # Display lives
        for i, heart in enumerate(heart_list):
            screen.blit(heart, (10 + i * 30, 10))  # Adjust position as necessary
    else:
        # Display start screen
        screen.fill((169, 21, 26))  # Or any color you prefer
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_message, game_message_rect)

    pygame.display.update()
    clock.tick(60)
