import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import BOSS_ENEMY, SCREEN_HEIGHT, SCREEN_WIDTH


class BossEnemy(Enemy):
    WIDTH = 250
    HEIGHT = 200
    SPEED_X = 5

    def __init__(self):
        self.image = BOSS_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.rect.x = (SCREEN_WIDTH - self.WIDTH) // 2  
        self.direction = 1  

    def move(self):
        self.rect.x += self.SPEED_X * self.direction

        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1  
    
    def update(self, bullet_handler):
        super().update(bullet_handler)
        if len(bullet_handler.bullets) >= 50:
            self.is_alive = False


    def draw(self, screen):
        screen.blit(self.image, self.rect)

