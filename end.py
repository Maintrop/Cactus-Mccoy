# Модулі
import pygame, sys, mixer
pygame.init()
pygame.mixer.init()

from config import WIDTH, HEIGHT, FPS, BLACK, YELLOW, BROWN
from button import Button
import save_data

# Функція
def game_intro(window):
    clock = pygame.time.Clock()
    pygame.mixer.init()

    # Зображення
    end1_img = pygame.image.load("assets/images/cutscenes/end/end1.png").convert_alpha()
    end2_img = pygame.image.load("assets/images/cutscenes/end/end2.png").convert_alpha()
    end3_img = pygame.image.load("assets/images/cutscenes/end/end3.png").convert_alpha()
    end4_img = pygame.image.load("assets/images/cutscenes/end/end4.png").convert_alpha()

    # Кнопки
    font_end_btn = pygame.font.SysFont(None, 50)
    end_btn_next = Button(WIDTH-170, HEIGHT-80, 150, 60, YELLOW, font_end_btn, "NEXT", BROWN, 16)
    end_btn_skip = Button(WIDTH-340, HEIGHT-80, 150, 60, YELLOW, font_end_btn, "SKIP", BROWN, 16)

    # Музика
    pygame.mixer.music.load("assets/audios/music/Cactus_McCoy_Intro.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1 if save_data.music else 0)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

        window.fill(BLACK)

        end_btn_next.show(window)
        end_btn_skip.show(window)

        pygame.display.flip()
        clock.tick(FPS)
