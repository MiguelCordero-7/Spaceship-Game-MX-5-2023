import random

class Enemy:
    Y_POS = 0
    X_POS_LIST = [50,150, 250, 350, 450, 550, 650, 750, 850, 950]

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

    def update(self):
        pass

    def draw (self, screen):
        screen.blit(self.image, self.rect)