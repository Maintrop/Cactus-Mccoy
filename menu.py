# Модулі
from pygame import *
import sys

from button import Button
from config import FPS, HEIGHT, WIDTH, BLACK, GRAY, YELLOW, BROWN, DARK_RED, LIGHT_RED, LIGHT_GRAY
from fade import Fade
import save_data

init()
mixer.init()

def menu(window):
    # Годинник
    clock = time.Clock()

    # Зображення
    black_stripe1 = image.load("assets/images/black_stripe.png").convert_alpha()
    black_stripe1_size = (WIDTH, 150)
    black_stripe1 = transform.smoothscale(black_stripe1, black_stripe1_size)

    black_stripe2 = transform.rotate(black_stripe1, 180)

    menu_bg = image.load("assets/images/menu_bg.jpg")
    menu_bg_size = (WIDTH+40, HEIGHT//1.5)
    menu_bg = transform.smoothscale(menu_bg, menu_bg_size)

    slots = [
        image.load("assets/images/empty_slot.png").convert_alpha(),
        image.load("assets/images/empty_slot.png").convert_alpha(),
        image.load("assets/images/empty_slot.png").convert_alpha()
    ]

    # Тексти
    slots_title_font = font.SysFont(None, 85)
    slots_title = slots_title_font.render("CHOOSE A SLOT", True, LIGHT_GRAY)

    # Музика
    mixer.music.load("assets/audios/music/menu.ogg")
    mixer.music.play(-1)

    # Кнопки
    font_btn_play = font.SysFont(None, 50)
    font_btn_music = font.SysFont(None, 40)
    font_btn_back = font.SysFont(None, 40)

    btn_play = Button(WIDTH//2-150, 565, 300, 75, YELLOW, font_btn_play, "Start Game!", BROWN, 32)
    btn_music = Button(WIDTH-110, HEIGHT-100, 100, 90, GRAY, font_btn_music, "ON" if save_data.music else "OFF", BLACK, 32)

    btn_back = Button(20, 20, 150, 50, LIGHT_RED, font_btn_back, "Exit", DARK_RED, 16)

    buttons = [btn_play, btn_music]

    # Фон
    fade = Fade(window)

    # Гра
    running = True
    selecting_slots = False

    while running:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                quit()
                sys.exit()

        hover_btn = False

        window.blit(black_stripe1, (0, 0))
        window.blit(black_stripe2, (0, HEIGHT-black_stripe2.get_height()))

        if not selecting_slots:
            window.blit(menu_bg, (-30, 130))
            
            if btn_play.is_clicked(events):
                def after_black():
                    nonlocal selecting_slots, buttons
                    selecting_slots = True
                    buttons = [btn_back]

                fade.start(fade_in=False, on_black=after_black)
                if not fade.active:
                    btn_music.x = 10
                
            elif btn_music.is_clicked(events):
                save_data.music = not save_data.music
                save_data.reload_settings()
                btn_music.text = "ON" if save_data.music else "OFF"
        else:
            window.fill(BLACK)
            window.blit(slots_title, (WIDTH//3.3, 20))

            if btn_back.is_clicked(events):
                selecting_slots = False
                buttons = [btn_play, btn_music]

        for btn in buttons:
            btn.show(window)
            if btn.is_hovered():
                hover_btn = True

        fade.update()
        fade.draw()

        mixer.music.set_volume(1 if save_data.music else 0)

        mouse.set_cursor(SYSTEM_CURSOR_HAND if hover_btn else SYSTEM_CURSOR_ARROW)

        display.flip()
        clock.tick(FPS)
