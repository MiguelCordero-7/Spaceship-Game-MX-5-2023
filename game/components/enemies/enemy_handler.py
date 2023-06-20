from game.components.enemies.ship import Ship
from game.components.enemies.speedship import Speedship

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.spawn_speedships = False

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if not self.spawn_speedships:
            if len(self.enemies) < 5:
                self.enemies.append(Ship())
            elif len(self.enemies) == 5:
                self.enemies.extend([Speedship() for _ in range(4)])
                self.spawn_speedships = True

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        if isinstance(enemy, Ship):
            self.enemies = [e for e in self.enemies if not isinstance(e, Ship)]  
        elif isinstance(enemy, Speedship):
            self.spawn_speedships = False 