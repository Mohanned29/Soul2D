from random import choice, randint
from sys import exit

import pygame
import pygame.mixer


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk_1 = pygame.image.load('graphics/player/knight_Run1.png').convert_alpha()
        original_size = player_walk_1.get_size()
        new_size = (original_size[0] * 2, original_size[1] * 2)
        player_walk_1 = pygame.transform.scale(player_walk_1, new_size)

        player_walk_2 = pygame.image.load('graphics/player/knight_Run2.png').convert_alpha()
        original_size1 = player_walk_2.get_size()
        new_size1 = (original_size1[0] * 2, original_size1[1] * 2)
        player_walk_2 = pygame.transform.scale(player_walk_2, new_size1)

        player_walk_3 = pygame.image.load('graphics/player/knight_Run3.png').convert_alpha()
        original_size2 = player_walk_3.get_size()
        new_size2 = (original_size2[0] * 2, original_size2[1] * 2)
        player_walk_3 = pygame.transform.scale(player_walk_3, new_size2)

        player_walk_4 = pygame.image.load('graphics/player/knight_Run4.png').convert_alpha()
        original_size3 = player_walk_4.get_size()
        new_size3 = (original_size3[0] * 2, original_size3[1] * 2)
        player_walk_4 = pygame.transform.scale(player_walk_4, new_size3)

        player_walk_5 = pygame.image.load('graphics/player/knight_Run5.png').convert_alpha()
        original_size4 = player_walk_5.get_size()
        new_size4 = (original_size4[0] * 2, original_size4[1] * 2)
        player_walk_5 = pygame.transform.scale(player_walk_5, new_size4)

        player_walk_6 = pygame.image.load('graphics/player/knight_Run6.png').convert_alpha()
        original_size5 = player_walk_6.get_size()
        new_size5 = (original_size5[0] * 2, original_size5[1] * 2)
        player_walk_6 = pygame.transform.scale(player_walk_6, new_size5)

        player_walk_7 = pygame.image.load('graphics/player/knight_Run7.png').convert_alpha()
        original_size6 = player_walk_7.get_size()
        new_size6 = (original_size6[0] * 2, original_size6[1] * 2)
        player_walk_7 = pygame.transform.scale(player_walk_7, new_size6)

        self.player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6, player_walk_7]
        self.player_index = 0

        self.player_saut1 = pygame.image.load('graphics/player/knight_Jump1.png').convert_alpha()
        self.player_saut1 = pygame.transform.scale(self.player_saut1, new_size2)

        self.player_saut2 = pygame.image.load('graphics/player/knight_Jump2.png').convert_alpha()
        self.player_saut2 = pygame.transform.scale(self.player_saut2, new_size2)

        self.player_saut3 = pygame.image.load('graphics/player/knight_Jump3.png').convert_alpha()
        self.player_saut3 = pygame.transform.scale(self.player_saut3, new_size2)

        self.player_saut4 = pygame.image.load('graphics/player/knight_Jump4.png').convert_alpha()
        self.player_saut4 = pygame.transform.scale(self.player_saut4, new_size2)

        self.player_saut5 = pygame.image.load('graphics/player/knight_Jump5.png').convert_alpha()
        self.player_saut5 = pygame.transform.scale(self.player_saut5, new_size2)

        self.player_saut6 = pygame.image.load('graphics/player/knight_Jump1.png').convert_alpha()
        self.player_saut6 = pygame.transform.scale(self.player_saut6, new_size2)

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravité = 0

        self.player_saut = [self.player_saut1,self.player_saut2,self.player_saut3,self.player_saut4,self.player_saut5,self.player_saut6]
        self.player_index1 = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravité = -20

    def apply_gravité(self):
        self.gravité += 1
        self.rect.y += self.gravité
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def anime(self):
        if self.rect.bottom < 300:
            self.player_index1 += 0.2
            if self.player_index >= len(self.player_saut):
                self.player_index1 = 0
        else:
            self.player_index += 0.15
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravité()
        self.anime()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'enemy2':
            enemy2_1 = pygame.image.load('graphics/enemy2/Flight2.png').convert_alpha()
            enemy2_2 = pygame.image.load('graphics/enemy2/Flight3.png').convert_alpha()
            self.frames = [enemy2_1, enemy2_2]
            y_pos = 160

        else:
            enemy1_1 = pygame.image.load('graphics/enemy/Run1.png').convert_alpha()
            original_size = enemy1_1.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_1 = pygame.transform.scale(enemy1_1, new_size)

            enemy1_2 = pygame.image.load('graphics/enemy/Run2.png').convert_alpha()
            original_size = enemy1_2.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_2 = pygame.transform.scale(enemy1_2, new_size)

            enemy1_3 = pygame.image.load('graphics/enemy/Run3.png').convert_alpha()
            original_size = enemy1_3.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_3 = pygame.transform.scale(enemy1_3, new_size)

            enemy1_4 = pygame.image.load('graphics/enemy/Run4.png').convert_alpha()
            original_size = enemy1_4.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_4 = pygame.transform.scale(enemy1_4, new_size)

            enemy1_5 = pygame.image.load('graphics/enemy/Run5.png').convert_alpha()
            original_size = enemy1_5.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_5 = pygame.transform.scale(enemy1_5, new_size)

            enemy1_6 = pygame.image.load('graphics/enemy/Run6.png').convert_alpha()
            original_size = enemy1_6.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_6 = pygame.transform.scale(enemy1_6, new_size)

            enemy1_7 = pygame.image.load('graphics/enemy/Run7.png').convert_alpha()
            original_size = enemy1_7.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_7 = pygame.transform.scale(enemy1_7, new_size)

            enemy1_8 = pygame.image.load('graphics/enemy/Run8.png').convert_alpha()
            original_size = enemy1_8.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_8 = pygame.transform.scale(enemy1_8, new_size)

            enemy1_9 = pygame.image.load('graphics/enemy/Run9.png').convert_alpha()
            original_size = enemy1_9.get_size()
            new_size = (original_size[0] // 2*1.5, original_size[1] // 2*1.5)
            enemy1_9 = pygame.transform.scale(enemy1_9, new_size)

            self.frames = [enemy1_1, enemy1_2,enemy1_3,enemy1_4,enemy1_5,enemy1_6,enemy1_7,enemy1_8,enemy1_9]
            y_pos = 305

        self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def anime(self):
        self.animation_index += 0.3
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.anime()
        self.rect.x -= 6
        self.killer()

    def killer(self):
        if self.rect.x <= -100:
            self.kill()

def score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(enemy1_surface, obstacle_rect)
            else:
                screen.blit(enemy2_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.rect.colliderect(obstacle_rect.rect):  # Use rect attribute for collision detection
                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_saut
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

# Initialize variables:
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("SOULS")
horloge = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_on = False
start_time = 0
score1 = 0
dragon_x = 0

# groups:
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

# intro screen:
player_stand = pygame.image.load('graphics/player/idle.png').convert_alpha()
original_size = player_stand.get_size()
new_size = (original_size[0] * 2, original_size[1] * 2)
player_stand = pygame.transform.scale(player_stand, new_size)

player_stand_rect = player_stand.get_rect(center=(400, 180))

game_name = test_font.render('SOULS', False, (255, 255, 255))
game_name_rect = game_name.get_rect(center=(400, 80))
game_message = test_font.render("Press  space  to  start  the  game", False, (255, 255, 255))
game_message_rect = game_message.get_rect(center=(400, 340))

# surface:
sky_surface = pygame.image.load('graphics/bg.png').convert_alpha()

ground_surface = pygame.image.load('graphics/floor.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (800,400))

wall_surface = pygame.image.load('graphics/wall.png').convert_alpha()
wall_surface = pygame.transform.scale(wall_surface,(800,400))

flag_surface = pygame.image.load('graphics/columns&falgs.png').convert_alpha()
flag_surface = pygame.transform.scale(flag_surface,(800,400))

candle_surface = pygame.image.load('graphics/candeliar.png').convert_alpha()
candle_surface = pygame.transform.scale(candle_surface,(800,400))

dragon_surface = pygame.image.load('graphics/dragon.png').convert_alpha()
dragon_surface = pygame.transform.scale(dragon_surface,(800,400))


# multiple lives system
heart_interface1 = pygame.image.load('graphics/heart.png').convert_alpha()
original_size1 = heart_interface1.get_size()
new_size1 = (original_size1[0] //16 , original_size1[1] // 16)
heart_interface1 = pygame.transform.scale(heart_interface1, new_size1)

heart_interface2 = pygame.image.load('graphics/heart.png').convert_alpha()
heart_interface2 = pygame.transform.scale(heart_interface2, new_size1)

heart_interface3 = pygame.image.load('graphics/heart.png').convert_alpha()
heart_interface3 = pygame.transform.scale(heart_interface3, new_size1)

heart_list = [heart_interface1,heart_interface2,heart_interface3]
heart_rect = heart_interface1.get_rect(topleft=(0, 0))

# enemy1
enemy1_frame_1 = pygame.image.load('graphics/enemy/Run1.png').convert_alpha()

enemy1_frame_2 = pygame.image.load('graphics/enemy/Run2.png').convert_alpha()
enemy1_frame_3 = pygame.image.load('graphics/enemy/Run3.png').convert_alpha()
enemy1_frame_4 = pygame.image.load('graphics/enemy/Run4.png').convert_alpha()
enemy1_frame_5 = pygame.image.load('graphics/enemy/Run5.png').convert_alpha()
enemy1_frame_6 = pygame.image.load('graphics/enemy/Run6.png').convert_alpha()
enemy1_frame_7 = pygame.image.load('graphics/enemy/Run7.png').convert_alpha()
enemy1_frame_8 = pygame.image.load('graphics/enemy/Run8.png').convert_alpha()
enemy1_frame_9 = pygame.image.load('graphics/enemy/Run9.png').convert_alpha()

enemy1_frames = [enemy1_frame_1, enemy1_frame_2, enemy1_frame_3, enemy1_frame_4,enemy1_frame_5,enemy1_frame_6,enemy1_frame_7,enemy1_frame_8,enemy1_frame_9]
enemy1_index = 0
enemy1_surface = enemy1_frames[enemy1_index]

# enemy2
enemy2_frame_1 = pygame.image.load('graphics/enemy2/Flight2.png').convert_alpha()
enemy2_frame_2 = pygame.image.load('graphics/enemy2/Flight3.png').convert_alpha()
enemy2_frames = [enemy2_frame_1, enemy2_frame_2]
enemy2_index = 0
enemy2_surface = enemy2_frames[enemy2_index]

#player
player_walk_1 = pygame.image.load('graphics/player/character_maleAdventurer_run0.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/character_maleAdventurer_run1.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_saut = pygame.image.load('graphics/player/character_maleAdventurer_jump.png').convert_alpha()
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(80, 300))
gravité = 0

#rectangles
enemy1_rect = enemy1_surface.get_rect(midbottom=(600, 300))

# obstacles
obstacle_rect_list = []

# timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1450)

enemy1_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy1_animation_timer, 500)

enemy2_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(enemy2_animation_timer, 200)

# THE GAME:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_on:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    gravité = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    gravité = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_on = True
                start_time = int(pygame.time.get_ticks() / 1000)  # search

        if game_on:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['enemy2', 'enemy1', 'enemy1'])))  # search

            if event.type == enemy1_animation_timer:
                if enemy1_index == 0:
                    enemy1_index = 1
                else:
                    enemy1_index = 0
                enemy1_surface = enemy1_frames[enemy1_index]

            if event.type == enemy2_animation_timer:
                if enemy2_index == 0:
                    enemy2_index = 1
                else:
                    enemy2_index = 0
                enemy2_surface = enemy2_frames[enemy2_index]

    if game_on:
        # screen blit:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,0))
        screen.blit(wall_surface ,(0,0))
        screen.blit(flag_surface,(0,0))
        screen.blit(dragon_surface,(dragon_x,0))

        

        dragon_x -=5
        
        if dragon_x <= -1000:
            dragon_x = 800

        score1 = score()

        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        

        #collision:
        if not collision_sprite():
                heart_list.pop()
        if len(heart_list)== 0:
            game_on = False
            heart_list = [heart_interface1, heart_interface2, heart_interface3]


        for i in range(len(heart_list)):
            screen.blit(heart_list[i], (heart_rect.width * i, 10))

    else:
        screen.fill((169, 21, 26))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        gravité = 0

        score_message = test_font.render(f'Your Score: {score1}', False, (255, 255, 255))
        score_message_rect = score_message.get_rect(center=(400, 340))
        screen.blit(game_name, game_name_rect)

        if score1 == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # display update:
    pygame.display.update()
    horloge.tick(60)