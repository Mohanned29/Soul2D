import pygame
from settings import FONT_PATH, FONT_SIZE

#in case of collisions
def check_collisions(player, obstacles):
    if pygame.sprite.spritecollide(player, obstacles, False):
        return False
    return True

#score display
def display_score(screen, score):
    font = pygame.font.Font(FONT_PATH, FONT_SIZE)
    score_surf = font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
