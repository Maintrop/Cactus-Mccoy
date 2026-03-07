# Модулі
from email.mime import image
import pygame, sys, mixer
pygame.init()
pygame.mixer.init()

from config import WIDTH, HEIGHT, FPS, BLACK, YELLOW, BROWN
from button import Button
from game import game
import save_data

# Функція
def game_intro(window):
    clock = pygame.time.Clock()
    pygame.mixer.init()

    # Зображення
    images = []
    for i in range(7):
        img = pygame.image.load(f"assets/images/cutscenes/start/start{i+1}.png").convert_alpha()
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        images.append(img)

    current = 0
    alpha = 0

    # Кнопки
    font_start_btn = pygame.font.SysFont(None, 50)
    start_btn_next = Button(WIDTH-170, HEIGHT-80, 150, 60, YELLOW, font_start_btn, "NEXT", BROWN, 16)
    start_btn_skip = Button(WIDTH-340, HEIGHT-80, 150, 60, YELLOW, font_start_btn, "SKIP", BROWN, 16)

    # Музика
    pygame.mixer.music.load("assets/audios/music/Cactus_McCoy_Intro.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1 if save_data.music else 0)

    running = True
    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                sys.exit()

        window.fill(BLACK)

        img = images[current]
        img.set_alpha(alpha)
        window.blit(img, (0, 0))

        if alpha < 255:
            alpha += 1

        if start_btn_next.is_clicked(events):
            if current < len(images)-1:
                alpha = 0
                current += 1
            else:
                game(window)

        if start_btn_skip.is_clicked(events):
            game(window)
            break

        start_btn_next.show(window)
        start_btn_skip.show(window)

        pygame.display.flip()
        clock.tick(FPS)
