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
          enemy2_1 = pygame.image.load('graphics/enemy2/Flight2.png').convert_alpha()
          enemy2_2 = pygame.image.load('graphics/enemy2/Flight3.png').convert_alpha()
          self.frames = [enemy2_1, enemy2_2]
      else:
          enemy1_1 = pygame.image.load('graphics/enemy/Run1.png').convert_alpha()
          enemy1_2 = pygame.image.load('graphics/enemy/Run2.png').convert_alpha()
          enemy1_3 = pygame.image.load('graphics/enemy/Run3.png').convert_alpha()
          enemy1_4 = pygame.image.load('graphics/enemy/Run4.png').convert_alpha()
          enemy1_5 = pygame.image.load('graphics/enemy/Run5.png').convert_alpha()
          enemy1_6 = pygame.image.load('graphics/enemy/Run6.png').convert_alpha()
          enemy1_7 = pygame.image.load('graphics/enemy/Run7.png').convert_alpha()
          enemy1_8 = pygame.image.load('graphics/enemy/Run8.png').convert_alpha()
          enemy1_9 = pygame.image.load('graphics/enemy/Run9.png').convert_alpha()
          self.frames = [enemy1_1, enemy1_2, enemy1_3, enemy1_4, enemy1_5, enemy1_6, enemy1_7, enemy1_8, enemy1_9]

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
