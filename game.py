# Модулі
from pygame import *
import sys
init()

from config import WIDTH, HEIGHT, FPS, BLACK, LIGHT_GREEN, LIGHT_ORANGE
from player import Player
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
    intro_level_img = transform.smoothscale(intro_level_img, (500, 300))

    # Тексти
    cutscene_level_font = font.SysFont("arialblack", 35)
    cutscene_level = cutscene_level_font.render("Level 1", True, LIGHT_GREEN)
    cutscene_title_font = font.SysFont("arialblack", 40)
    cutscene_title = cutscene_title_font.render("Cactus Canyon", True, LIGHT_ORANGE)

    # Вступ
    def start_cutscene():
        # Час
        start_time = time.get_ticks()
        
        # Затемнення
        fade_alpha = 255

        fade_surface = Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)

        # Цикл заставки рівня
        running_game_intro = True
        while running_game_intro:
            for e in event.get():
                if e.type == QUIT:
                    sys.exit()

            now = time.get_ticks()

            window.fill(BLACK)
            window.blit(cutscene_level, (WIDTH // 2 - cutscene_level.get_width() // 2, 120))
            window.blit(intro_level_img, (350, 200))
            window.blit(cutscene_title, (WIDTH // 2 - cutscene_title_font.render("Cactus Canyon", True, LIGHT_ORANGE).get_width() // 2, 510))

            if now - start_time <= 3000:
                if fade_alpha > 0:
                    fade_alpha -= 15
                    fade_surface.set_alpha(fade_alpha)
                    window.blit(fade_surface, (0, 0))
            else:
                if fade_alpha < 255:
                    fade_alpha += 20
                    fade_surface.set_alpha(fade_alpha)
                    window.blit(fade_surface, (0, 0))
                else:
                    running_game_intro = False

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
