import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    WIDTH = 40
    HEIGTH = 60
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        if user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_w]:
            self.move_up()
        elif user_input[pygame.K_s]:
            self.move_down()


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