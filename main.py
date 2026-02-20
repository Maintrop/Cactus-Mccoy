# Модулі
from pygame import *
import sys

from intro import intro
from menu import menu
from config import WIDTH, HEIGHT, FPS

# Вікно
window = display.set_mode((WIDTH, HEIGHT))

# Заголовок
display.set_caption("Cactus McCoy")

# Логотип
logo = image.load("assets/images/logo.png")
logo = transform.smoothscale(logo, (64, 64))

display.set_icon(logo)

# Годинник
clock = time.Clock()

# Заставка
# intro(window)

# Підготова до запуску гри
game = True

while game:
    menu(window)

    display.flip()
    clock.tick(FPS)

quit()
sys.exit()
