# Модуль Pygame
import pygame

# Функція
class Fade:
    def __init__(self, window, speed=10, pause=2000):
        self.window = window
        self.speed = speed
        self.pause = pause  # пауза у мс на чорному
        self.overlay = pygame.Surface(window.get_size()).convert_alpha()
        self.overlay.fill((0, 0, 0))

        self.alpha = 0
        self.active = False
        self.fade_in = True

        # Стан паузи
        self.waiting = False
        self.wait_start = 0

        # Додатковий callback після чорного
        self.on_black = None

    def start(self, fade_in=True, on_black=None):
        self.fade_in = fade_in
        self.active = True
        self.alpha = 255 if fade_in else 0
        self.on_black = on_black
        self.waiting = False

    def fade_in_update(self):
        self.alpha -= self.speed
        if self.alpha <= 0:
            self.alpha = 0
            self.active = False

    def fade_out_update(self):
        self.alpha += self.speed
        if self.alpha >= 255:
            self.alpha = 255
            self.active = False
            self.waiting = True
            self.wait_start = pygame.time.get_ticks()
            if self.on_black:
                self.on_black()

    def update(self):
        if not self.active and not self.waiting:
            return

        if self.active:
            if self.fade_in:
                self.fade_in_update()
            else:
                self.fade_out_update()

        # Обробка паузи
        if self.waiting:
            if pygame.time.get_ticks() - self.wait_start >= self.pause:
                self.waiting = False
                self.start(fade_in=True)  # автоматичний fade in після паузи

    def draw(self):
        if self.active or self.waiting:
            self.overlay.set_alpha(self.alpha)
            self.window.blit(self.overlay, (0, 0))
