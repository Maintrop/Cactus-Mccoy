# Модулі
from pygame import *

class Enemy:
    def __init__(self, x, y, hp, image_path, speed=2, patrol_width=200):
        self.image = transform.smoothscale(image.load(image_path).convert_alpha(), (80, 140))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = speed
        self.direction = 1
        self.start_x = x
        self.patrol_width = patrol_width

        self.gravity = 0.8
        self.vilocity_y = 0
        self.on_ground = False

    def update(self, platforms):
        self.velocity_y += self.gravity
        if self.velocity_y > 10:
            self.velocity_y = 10
        self.rect.y += self.velocity_y

        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    self.rect.top = platform.bottom
                    self.velocity_y = 0

        if self.on_ground:
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.start_x) >= self.patrol_width:
                self.direction *= -1

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.direction > 0:
                    self.rect.right = platform.left
                    self.direction *= -1
                elif self.direction < 0:
                    self.rect.left = platform.right
                    self.direction = -1

    def show(self, window):
        window.blit(self.image, self.rect)
