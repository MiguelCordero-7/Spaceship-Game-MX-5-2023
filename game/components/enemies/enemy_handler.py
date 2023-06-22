
from game.components.enemies.ship import Ship
from game.components.enemies.speedship import Speedship
from game.components.enemies.alien import Alien
from game.components.enemies.boss_enemy import BossEnemy
from game.utils.constants import ENEMY_1, ENEMY_2

class EnemyHandler:

    ENEMIES = ["ship", "speedship", "alien", "boss_enemy"]
    ENEMY_SCORE_INTERVAL = {
        "ship": 0,
        "speedship": 5,
        "alien": 10,
        "boss_enemy": 15
    }

    def __init__(self):
        self.enemies = []
        self.number_enemies_destroyed = 0
        self.score_interval = 0
        self.current_interval_score = 0

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if enemy.is_destroyed:
                self.number_enemies_destroyed += 1
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) <= 4:
            for enemy_type, score_interval in self.ENEMY_SCORE_INTERVAL.items():
                if enemy_type == "boss_enemy":
                    if self.number_enemies_destroyed >= score_interval and enemy_type not in self.enemies:
                        self.enemies.append(BossEnemy())
                        break
                else:
                    if self.number_enemies_destroyed >= score_interval and enemy_type not in self.enemies:
                        if enemy_type == "ship":
                            self.enemies.append(Ship())
                        elif enemy_type == "speedship":
                            self.enemies.append(Speedship())
                        elif enemy_type == "alien":
                            self.enemies.append(Alien())   
                    

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        if isinstance(enemy, BossEnemy):
            self.ENEMY_SCORE_INTERVAL["boss_enemy"] = float("inf")

    def reset(self):
        self.enemies = []
        self.number_enemies_destroyed = 0