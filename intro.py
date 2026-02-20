# Модулі
import pygame, sys, mixer
pygame.init()
pygame.mixer.init()

from config import WIDTH, HEIGHT, FPS, BLACK

# Функція
def intro(window):
    clock = pygame.time.Clock()
    pygame.mixer.init()

    logo_FS = pygame.image.load("assets/images/flipline_logo.png").convert_alpha() # convert_alpha - оптимізація зображення

    # Чорна смуга
    black_stripe = pygame.image.load("assets/images/black_stripe.png")
    black_stripe_size = (WIDTH, HEIGHT//5)
    black_stripe = pygame.transform.smoothscale(black_stripe, black_stripe_size)

    rotated_black_stripe = pygame.transform.rotate(black_stripe, 180)

    height = 0.1
    state = "grow"
    timer = 0

    sound_FS = pygame.mixer.Sound("assets/audios/sounds/Flipline_Studios_intro.mp3")

    x = WIDTH//2
    y = HEIGHT//2

    sound_FS.play()

    running_FS = True
    while running_FS:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

        window.fill(BLACK)

        window.blit(black_stripe, (0, HEIGHT//3.20))
        window.blit(rotated_black_stripe, (0, HEIGHT//1.40-black_stripe.get_height()-20))

        if state == "grow":
            height += 0.05

            if height >= 1.0:
                height = 1.0
                state = "hold"

        elif state == "hold":
            timer += 1

            if 0 <= timer <= 5:
                height -= 0.01

            if 5 <= timer <= 10:
                height += 0.01

            if timer > 150:
                state = "move_right"

        elif state == "move_right":
            x += 20
            if x >= WIDTH + int(logo_FS.get_width()):
                running_FS = False

        new_size = (int(logo_FS.get_width()), int(logo_FS.get_height() * height))
        scaled_logo = pygame.transform.smoothscale(logo_FS, new_size)
        rect_FS = scaled_logo.get_rect(center=(x, y))
        window.blit(scaled_logo, rect_FS)

        pygame.display.flip()
        clock.tick(FPS)
