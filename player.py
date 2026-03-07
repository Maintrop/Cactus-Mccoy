# Модулі
from pygame import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.speed = 5

        self.image = image.load("assets/images/player.png").convert_alpha()
        self.image = transform.smoothscale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, window):
        window.blit(self.image, self.rect)
