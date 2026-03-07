# Модулі
from pygame import *
import sys
init()

from config import WIDTH, HEIGHT, FPS, BLACK
import save_data

# Функція
def game(window):
    clock = time.Clock()
    mixer.init()
    
    # Музика
    mixer.music.load("assets/audios/music/Cactus_McCoy_startLevel.mp3")
    mixer.music.play()
    mixer.music.set_volume(1 if save_data.music else 0)
    
    # Зображення
    intro_level_img = image.load("assets/images/levels/intro/intro_level1.png").convert_alpha()

    # Вступ
    def start_cutscene():
        running_game_intro = True
        while running_game_intro:
            for e in event.get():
                if e.type == QUIT:
                    sys.exit()

            window.fill(BLACK)
            window.blit(intro_level_img, (WIDTH//5, HEIGHT//5))

            display.flip()
            clock.tick(FPS)

    start_cutscene()

    running_game = True
    while running_game:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                sys.exit()

        window.fill(BLACK)

        display.flip()
        clock.tick(FPS)
