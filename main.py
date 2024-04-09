import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, FPS
from player import Player
from obstacle import Obstacle
from game_functions import check_collisions, display_score
from random import choice

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()
    
    player = pygame.sprite.GroupSingle(Player())
    obstacles = pygame.sprite.Group()
    
    #main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.sprite.jump()
        
        #update
        player.update()
        obstacles.update()
        
        #if Collision
        game_active = check_collisions(player.sprite, obstacles)
        
        #draw
        screen.fill((0, 0, 0))  #clear screen
        player.draw(screen)
        obstacles.draw(screen)
        
        #refresh display
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
