from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemies):
        for bullet in self.bullets:
            if type(bullet) is BulletEnemy:
                bullet.update(player)
            elif type(bullet) is BulletPlayer:
                for enemy in enemies:
                    bullet.update(enemy)
            if not bullet.is_alive:
                self.remove_bullet(bullet)


    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        if type == BULLET_TYPE:
            self.bullets.append(BulletPlayer(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)

    def reset (self):
        self.bullets = []