import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Speedship(Enemy):
    WIDTH = 50
    HEIGHT = 60
    SPEED_X = 10
    SPEED_Y = 4
    X_POS_LIST = [50, 1000]

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)