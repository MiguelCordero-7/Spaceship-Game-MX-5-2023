import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_TYPE, SPACESHIP_SHIELD
from game.components.power_up.shild import Shield

class Spaceship:
    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    SHOOT_DELAY = 100

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.has_shield = False
        self.time_up = 0
        self.last_shot_time = 0

    def update(self, user_input, bullet_handler):
        if user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_w]:
            self.move_up()
        elif user_input[pygame.K_s]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot_time >= self.SHOOT_DELAY:
                self.shoot(current_time, bullet_handler)    
        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show < 0:
                self.desactivate_power_up()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_up(self):
        top_limit = SCREEN_HEIGHT // 2
        if self.rect.top > top_limit:
            self.rect.y -= 10
    
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y +=10

    def shoot(self, current_time, bullet_handler):
        self.last_shot_time = current_time
        bullet_handler.add_bullet(BULLET_TYPE, self.rect.center)

    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if type(power_up) == Shield:
            self.has_shield = True
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))

    def desactivate_power_up(self):
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))


    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True