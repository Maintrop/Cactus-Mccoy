# Модулі
from pygame import *
import sys

from button import Button
from config import FPS, HEIGHT, WIDTH, BLACK, GRAY, LIGHT_GRAY, YELLOW, BROWN, DARK_RED, LIGHT_RED, WHITE
from fade import Fade
import save_data

init()
mixer.init()

def menu(window):
    # Годинник
    clock = time.Clock()

    # Чорні смуги
    black_stripe1 = image.load("assets/images/black_stripe.png").convert_alpha()
    black_stripe1 = transform.smoothscale(black_stripe1, (WIDTH, 150))
    black_stripe2 = transform.rotate(black_stripe1, 180)

    # Фон меню
    menu_bg = image.load("assets/images/menu_bg.jpg")
    menu_bg = transform.smoothscale(menu_bg, (WIDTH + 40, HEIGHT // 1.5))

    # Тексти
    slots_title_font = font.SysFont(None, 85)
    slots_title = slots_title_font.render("CHOOSE A SLOT", True, LIGHT_GRAY)

    slot_titles = ["EMPTY SLOT", "EMPTY SLOT", "EMPTY SLOT"]

    # Музика
    mixer.music.load("assets/audios/music/menu.ogg")
    mixer.music.play(-1)
    mixer.music.set_volume(1 if save_data.music else 0)

    # Кнопки
    slot_title_font = font.SysFont(None, 40)
    font_btn_play = font.SysFont(None, 50)
    font_btn_music = font.SysFont(None, 40)
    font_btn_back = font.SysFont(None, 40)
    font_btn_slot = font.SysFont(None, 30)

    btn_play = Button(WIDTH // 2 - 150, 565, 300, 75, YELLOW, font_btn_play, "Start Game!", BROWN, 32)
    btn_music = Button(WIDTH - 110, HEIGHT - 110, 100, 100, GRAY, font_btn_music, "ON" if save_data.music else "OFF", BLACK, 32)
    btn_back = Button(20, 20, 150, 50, LIGHT_RED, font_btn_back, "Exit", DARK_RED, 16)

    slot_buttons = [Button(0, 0, 200, 50, YELLOW, font_btn_slot, "New Save Slot", BROWN, 32) for _ in range(3)]
    buttons = [btn_play, btn_music]

    # Координати кнопок
    slot_positions = [(200, 200), (500, 200), (800, 200)]

    # Слоти
    slots = [transform.scale(image.load("assets/images/slot.png").convert_alpha(), (250, 350)) for _ in range(3)]

    # Fade
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

        window.blit(black_stripe1, (0, 0))
        window.blit(black_stripe2, (0, HEIGHT - black_stripe2.get_height()))

        if not selecting_slots:
            window.blit(menu_bg, (-30, 130))

            if btn_play.is_clicked(events):
                def after_black():
                    nonlocal selecting_slots, buttons
                    selecting_slots = True
                    buttons = [btn_back, btn_music]

                fade.start(fade_in=False, on_black=after_black)

            elif btn_music.is_clicked(events):
                save_data.music = not save_data.music
                save_data.reload_settings()
                btn_music.text = "ON" if save_data.music else "OFF"
                mixer.music.set_volume(1 if save_data.music else 0)

        else:
            window.fill(BLACK)
            window.blit(slots_title, (WIDTH//3.3, 20))

            if btn_back.is_clicked(events):
                selecting_slots = False
                buttons = [btn_play, btn_music]
            elif btn_music.is_clicked(events):
                save_data.music = not save_data.music
                save_data.reload_settings()
                btn_music.text = "ON" if save_data.music else "OFF"
                mixer.music.set_volume(1 if save_data.music else 0)

            for i, pos in enumerate(slot_positions):
                window.blit(slots[i], pos)

                slot_title_surf = slot_title_font.render(slot_titles[i], True, WHITE)
                slot_title_rect = slot_title_surf.get_rect(center=(pos[0] + slots[i].get_width()//2, pos[1]+35))
                window.blit(slot_title_surf, slot_title_rect)

                slot_buttons[i].rect.topleft = (pos[0] + 25, pos[1] + slots[i].get_height()-70)
                slot_buttons[i].show(window)

                if slot_buttons[i].is_clicked(events):
                    pass

        for btn in buttons:
            btn.show(window)

        fade.update()
        fade.draw()

        display.flip()
        clock.tick(FPS)
