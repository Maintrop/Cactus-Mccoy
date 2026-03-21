# Модулі
from pygame import *

class Platform:
    def __init__(self, x, y, image_path, width=None, height=None, is_ground=False):
        self.image = image.load(image_path).convert_alpha()
        if width and height:
            self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def shift(self, shift_x, shift_y=0):
        self.rect.x += shift_x
        self.rect.y += shift_y

    def show(self, window):
        window.blit(self.image, self.rect)
