## Модулі
import pygame
import sys
import mixer
from intro import play_intro
from button import Button

## Ініцілізування
pygame.init()
pygame.mixer.init()

## Кольори
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
DARK_GREY = (80, 80, 80)
LIGHT_GREY = (200, 200, 200)
YELLOW = (255, 214, 32)
DARK_BROWN = (101, 67, 33)
LIGHT_YELLOW = (255, 235, 93)
LIGHT_RED = (255, 167, 165)
RED = (255, 0, 0)
DARK_RED = (177, 0, 0)

## Розміри вікна
WIDTH = 1200
HEIGHT = 750

## Кількість кадрів за секунду
FPS = 60

## Створення вікна
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cactus McСoy")
clock = pygame.time.Clock()

## Запуск заставки
play_intro(window)

## Курсор
hand_cursor = pygame.SYSTEM_CURSOR_HAND
arrow_cursor = pygame.SYSTEM_CURSOR_ARROW

# Мишка
mouse = pygame.mouse.get_pos()

## Функції
# Малювання елементів меню
def draw_menu_elements(window):
    window.fill(BLACK)
    window.blit(bg_menu, (-15, 140))
    window.blit(black_stripe, (0, 25))
    window.blit(rotated_black_stripe, (0, HEIGHT-black_stripe.get_height()-20))
    window.blit(img_dev, (35, 45))
    window.blit(text_dev, (35, 12))
    window.blit(text_important_info, (WIDTH-550, 25))
    btn_menu_music.show(window)
    btn_menu_play.show(window)

# Малювання елементів у виборі слотів
def draw_elements_selecting_slots(window):
    global empty_slot1_y, empty_slot2_y, empty_slot3_y

    if empty_slot1_y <= 150:
        empty_slot1_y += 15

    if empty_slot1_y >= 50 and empty_slot2_y <= 150:
            empty_slot2_y += 15

    if empty_slot2_y >= 50 and empty_slot3_y <= 150:
        empty_slot3_y += 15
    
    window.fill(BLACK)
    window.blit(empty_slot1, (100, empty_slot1_y))
    window.blit(empty_slot2, (450, empty_slot2_y))
    window.blit(empty_slot3, (800, empty_slot3_y))
    btn_menu_back.show(window)

# Затемнення
def fade_out(window, speed=10, delay=10, pause_delay=2000):
    global menu, selecting_slots, play_clicked, timer_to_rest_mus

    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)

    for alpha in range(0, 255, speed):
        draw_menu_elements(window)
        pygame.mouse.set_cursor(arrow_cursor)
        fade.set_alpha(alpha)
        window.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(delay)
        timer_to_rest_mus += 1

    menu = False
    selecting_slots = True

    # Пауза
    pygame.time.delay(pause_delay)

# Повернення прозорості
def fade_in(window, speed=10, delay=10):
    global play_clicked, timer_to_rest_mus
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill(BLACK)

    for alpha in range(255, 0, -speed):
        draw_elements_selecting_slots(window)
        pygame.mouse.set_cursor(arrow_cursor)
        fade.set_alpha(alpha)
        window.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(delay)
        timer_to_rest_mus += 1
    
    play_clicked = False

### Шрифти
## Меню
menu_btn_font = pygame.font.SysFont(None, 30)
font_dev = pygame.font.SysFont(None, 35)
font_important_info = pygame.font.SysFont(None, 30)

### Тексти
## Меню
# Розробник
text_dev = font_dev.render("Developed by", True, DARK_GREY)

# Важлива інформація
text_important_info = font_important_info.render("""WARNING: It isn't original game. It's ONLY REMAKE!""", True, DARK_GREY)

### Зображення
## Логотип
img_dev = pygame.image.load("images/Flipline_logo.png").convert_alpha()
img_dev_size = (220, 90)
img_dev = pygame.transform.smoothscale(img_dev, img_dev_size)

## Фон меню
bg_menu = pygame.image.load("images/menu_bg.jpg").convert_alpha()
bg_menu_size = (WIDTH+30, HEIGHT//1.55)
bg_menu = pygame.transform.smoothscale(bg_menu, bg_menu_size)

## Чорна смуга
black_stripe = pygame.image.load("images/black_stripe.png").convert_alpha()
black_stripe_size = (WIDTH, HEIGHT//6)
black_stripe = pygame.transform.smoothscale(black_stripe, black_stripe_size)

rotated_black_stripe = pygame.transform.rotate(black_stripe, 180)

## Слоти
empty_slot = pygame.image.load("images/empty_slot.png").convert_alpha()
empty_slot_size = (300, 400)
empty_slot = pygame.transform.smoothscale(empty_slot, empty_slot_size)

empty_slot1, empty_slot2, empty_slot3 = empty_slot, empty_slot, empty_slot

### Музика
music_menu = pygame.mixer.Sound("audios/Cactus_McCoy_Menu.ogg")
timer_to_rest_mus = 0
music_menu.play()

### Слоти
## Координати
empty_slot1_y, empty_slot2_y, empty_slot3_y = -empty_slot1.get_height(), -empty_slot2.get_height(), -empty_slot3.get_height()

### Кнопки
## Меню
# Play
font_btn_menu_play = pygame.font.SysFont(None, 50)
btn_menu_play = Button(WIDTH//2.65, 620, 300, 70, font_btn_menu_play, YELLOW, "PLAY", DARK_BROWN, LIGHT_YELLOW, 20)

# Музика
font_btn_menu_music = pygame.font.SysFont(None, 50)
btn_menu_music = Button(WIDTH-120, HEIGHT-120, 100, 100, font_btn_menu_music, LIGHT_GREY, "ON", BLACK, GREY, 40)

## Вибір слота
font_btn_back = pygame.font.SysFont(None, 40)
btn_menu_back = Button(20, 20, 150, 50, font_btn_back, LIGHT_RED, "BACK", DARK_RED, RED, 20)

### Фінальна підготовка до гри
play_clicked = False
clicked_to_menu = False
music_on = True

game = True

menu = True
selecting_slots = False

### Гра
while game:
    while menu:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                menu = False
                game = False

        draw_menu_elements(window)

        if btn_menu_play.is_clicked(events):
            play_clicked = True

        if play_clicked == True:
            fade_out(window)

        if clicked_to_menu == True and music_on:
            timer_to_rest_mus = 0
            music_menu.stop()
            music_menu = pygame.mixer.Sound("audios/Cactus_McCoy_Menu.ogg")
            music_menu.play()
            
            clicked_to_menu = False

        if btn_menu_music.is_clicked(events):
            if music_on == True:
                btn_menu_music = Button(WIDTH-120, HEIGHT-120, 100, 100, font_btn_menu_music, LIGHT_GREY, "OFF", BLACK, GREY, 40)
                music_menu.set_volume(0)
                music_on = False
            
            else:
                btn_menu_music = Button(WIDTH-120, HEIGHT-120, 100, 100, font_btn_menu_music, LIGHT_GREY, "ON", BLACK, GREY, 40)
                music_menu.set_volume(1)
                music_on = True

        timer_to_rest_mus += 1
        if timer_to_rest_mus >= 1900:
            timer_to_rest_mus = 0
            music_menu.play()

        pygame.display.flip()
        clock.tick(FPS)

    while selecting_slots:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                selecting_slots = False
                game = False
        
        draw_elements_selecting_slots(window)

        if empty_slot1_y <= 150:
            empty_slot1_y += 15

        if empty_slot1_y >= 50 and empty_slot2_y <= 150:
            empty_slot2_y += 15

        if empty_slot2_y >= 50 and empty_slot3_y <= 150:
            empty_slot3_y += 15

        if play_clicked == True:
            fade_in(window)
        
        if btn_menu_back.is_clicked(events):
            selecting_slots = False
            clicked_to_menu = True
            menu = True
            empty_slot1_y, empty_slot2_y, empty_slot3_y = -empty_slot1.get_height(), -empty_slot2.get_height(), -empty_slot3.get_height()

        timer_to_rest_mus += 1
        if timer_to_rest_mus >= 2000:
            timer_to_rest_mus = 0
            music_menu.play()

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
sys.exit()
