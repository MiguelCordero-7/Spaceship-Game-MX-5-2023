import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_TYPE

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

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True