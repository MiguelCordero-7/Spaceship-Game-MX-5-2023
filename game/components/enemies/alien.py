import random
import pygame
from game.components.enemies.enemy import Enemy,SCREEN_WIDTH, SCREEN_HEIGHT
from game.utils.constants import ENEMY_3

import random

class Alien(Enemy):
    WIDTH = 60
    HEIGHT = 60
    SPEED_X = 10
    SPEED_Y = 10
    INTERVAL = [50, 100, 200, 300, 400, 500, 650, 700, 800, 900]
    WAIT_TIME = 30

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.start_y = self.rect.y
        self.target_x = random.choice(self.X_POS_LIST)
        self.move_to_target = False
        self.going_down = False

    def move(self):
        if not self.move_to_target:
            if self.rect.y < self.start_y + (SCREEN_HEIGHT // 2):
                self.rect.y += self.SPEED_Y
            else:
                self.move_to_target = True
        else:
            if self.rect.x < self.target_x:
                self.rect.x += self.SPEED_X
                if self.rect.x > self.target_x:
                    self.rect.x = self.target_x
            elif self.rect.x > self.target_x:
                self.rect.x -= self.SPEED_X
                if self.rect.x < self.target_x:
                    self.rect.x = self.target_x
            else:
                if self.WAIT_TIME > 0:
                    self.WAIT_TIME -= 1
                else:
                    if self.rect.y < self.start_y:
                        self.rect.y += self.SPEED_Y
                    elif self.rect.y > self.start_y:
                        self.rect.y -= self.SPEED_Y
                    else:
                        self.is_alive = False
        self.index += 1
