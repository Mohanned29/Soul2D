# player.py
import pygame
from settings import PLAYER_GRAVITY, JUMP_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.load_images()
        self.image = self.player_walk[0]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = PLAYER_GRAVITY
        self.player_index = 0

    def load_images(self):
        self.player_walk = [pygame.image.load(f'graphics/player/knight_Run{i}.png').convert_alpha() for i in range(1, 8)]
        self.player_jump = [pygame.image.load(f'graphics/player/knight_Jump{i}.png').convert_alpha() for i in range(1, 7)]

    def update(self):
        self.gravity += PLAYER_GRAVITY
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
        self.animate()

    def jump(self):
        if self.rect.bottom == 300:
            self.gravity = JUMP_HEIGHT

    def animate(self):
        #update animation; example for walking
        self.player_index += 0.1
        if self.player_index >= len(self.player_walk):
            self.player_index = 0
        self.image = self.player_walk[int(self.player_index)]
