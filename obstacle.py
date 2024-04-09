import pygame
from settings import OBSTACLE_MIN_X, OBSTACLE_MAX_X, OBSTACLE_SPEED
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.load_images()
        self.image = self.frames[0]
        self.rect = self.image.get_rect(midbottom=(randint(OBSTACLE_MIN_X, OBSTACLE_MAX_X), 300))
        self.animation_index = 0

    def load_images(self):
        if self.type == 'enemy2':
            self.frames = [pygame.image.load(f'graphics/enemy2/Flight{i}.png').convert_alpha() for i in range(2, 4)]
        else:
            self.frames = [pygame.image.load(f'graphics/enemy/Run{i}.png').convert_alpha() for i in range(1, 10)]

    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()
        self.animate()

    def animate(self):
        self.animation_index += 0.3
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
