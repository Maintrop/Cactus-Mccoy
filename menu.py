# Модулі
from pygame import *
import sys

from button import Button
from config import FPS, HEIGHT, WIDTH, BLACK, GRAY, LIGHT_GRAY, YELLOW, BROWN, DARK_RED, LIGHT_RED, WHITE, DARK_GRAY, BEIGE
from fade import Fade
from game_intro import game_intro
from game_menu import game_menu
import save_data
import json

init()
mixer.init()

def menu(window):
    # Годинник
    clock = time.Clock()

    # Чорні смуги
    black_stripe1 = image.load("assets/images/menu/black_stripe.png").convert_alpha()
    black_stripe1 = transform.smoothscale(black_stripe1, (WIDTH, 150))
    black_stripe2 = transform.rotate(black_stripe1, 180)

    # Фон меню
    menu_bg = image.load("assets/images/menu/menu_bg.jpg")
    menu_bg = transform.smoothscale(menu_bg, (WIDTH + 40, HEIGHT // 1.5))

    # Шрифти
    slots_title_font = font.SysFont(None, 85)
    slot_title_font = font.SysFont(None, 40)
    menu_input_title_font = font.SysFont(None, 40)
    font_btn_play = font.SysFont(None, 50)
    font_btn_music = font.SysFont(None, 40)
    font_btn_menu_exit = font.SysFont(None, 40)
    font_btn_slot = font.SysFont(None, 30)
    font_btn_clear_data = font.SysFont(None, 40)
    font_btn_menu_input = font.SysFont(None, 30)

    # Тексти
    slots_title = slots_title_font.render("CHOOSE A SLOT", True, LIGHT_GRAY)
    menu_input_title = menu_input_title_font.render("Enter your username:", True, WHITE)

    # Музика
    mixer.music.load("assets/audios/music/menu.ogg")
    mixer.music.play(-1)
    mixer.music.set_volume(1 if save_data.music else 0)

    # Прямокутник меню
    menu_input_box = Rect(WIDTH//3.4, HEIGHT//3, 500, 230)

    # Поле введення
    username = ""
    username_box = Rect(menu_input_box.x + 50, menu_input_box.y + 90, 400, 45)
    username_max_length = 16

    # Користувачі
    slot_titles = [
        save_data.get_slot_user(f"saves_slots/slot{i+1}.json") for i in range(3)
    ]

    # Кнопки
    btn_play = Button(WIDTH // 2 - 150, 565, 300, 75, YELLOW, font_btn_play, "START", BROWN, 32)
    btn_music = Button(WIDTH - 110, HEIGHT - 110, 100, 100, GRAY, font_btn_music, "ON" if save_data.music else "OFF", BLACK, 32)
    btn_menu_exit = Button(20, 20, 150, 50, LIGHT_RED, font_btn_menu_exit, "EXIT", DARK_RED, 16)
    btn_menu_input_back = Button(menu_input_box.x+10, menu_input_box.y+170, 150, 50, YELLOW, font_btn_menu_input, "BACK", BROWN, 32)
    btn_menu_input_next = Button(menu_input_box.x+340, menu_input_box.y+170, 150, 50, YELLOW, font_btn_menu_input, "NEXT", BROWN, 32)

    save_slot_buttons = [Button(0, 0, 200, 50, YELLOW, font_btn_slot, "New Save Slot" if slot_titles[i] == "EMPTY SLOT" else "SELECT", BROWN, 32) for i in range(3)]
    clear_data_slot_buttons = [Button(0, 0, 150, 38, BEIGE, font_btn_slot, "Clear Data", tuple(min(255, i+40) for i in BROWN), 16, border_width=4) for _ in range(3)]
    buttons = [btn_play, btn_music]

    slot_positions = [(200, 175), (500, 175), (800, 175)]
    slots = [transform.scale(image.load("assets/images/menu/slot.png").convert_alpha(), (250, 350)) for _ in range(3)]

    fade = Fade(window)

    # Прапорці
    running = True
    selecting_slots = False
    show_slots = False
    inputing_username = False
    username_active = False
    show_slot = 0

    # Гра
    while running:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                quit()
                sys.exit()

            if inputing_username:
                if e.type == MOUSEBUTTONDOWN:
                    if username_box.collidepoint(e.pos):
                        username_active = True
                    else:
                        username_active = False

                if e.type == KEYDOWN and username_active:
                    if e.key == K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if len(username) < username_max_length:
                            username += e.unicode

        if not selecting_slots:
            window.blit(menu_bg, (-30, 130))
            window.blit(black_stripe1, (0, 0))
            window.blit(black_stripe2, (0, HEIGHT - black_stripe2.get_height()))

            if btn_play.is_clicked(events):
                def after_black():
                    nonlocal selecting_slots, show_slots, buttons
                    selecting_slots = True
                    show_slots = True
                    buttons = [btn_menu_exit, btn_music]

                fade.start(fade_in=False, on_black=after_black)

            elif btn_music.is_clicked(events):
                save_data.music = not save_data.music
                save_data.save_settings()

        else:
            window.fill(BLACK)
            window.blit(black_stripe1, (0, 0))
            window.blit(black_stripe2, (0, HEIGHT - black_stripe2.get_height()))
            window.blit(slots_title, (WIDTH//3.3, 50))

            if show_slots:
                for i, pos in enumerate(slot_positions):
                    window.blit(slots[i], pos)

                    slot_title_surf = slot_title_font.render(slot_titles[i], True, WHITE)
                    slot_title_rect = slot_title_surf.get_rect(center=(pos[0] + slots[i].get_width()//2, pos[1]+35))
                    window.blit(slot_title_surf, slot_title_rect)

                    save_slot_buttons[i].rect.topleft = (pos[0] + 25, pos[1] + slots[i].get_height()-70)
                    save_slot_buttons[i].show(window)

                    clear_data_slot_buttons[i].rect.topleft = (pos[0] + 50, pos[1] + slots[i].get_height()-270)
                    if slot_titles[i] != "EMPTY SLOT":
                        clear_data_slot_buttons[i].show(window)
                        if clear_data_slot_buttons[i].is_clicked(events):
                            slot_name = f"slot{i+1}"
                            save_data.clear_data(slot_name)
                            slot_titles[i] = "EMPTY SLOT"
                            save_slot_buttons[i].text = "New Save Slot"

                    if save_slot_buttons[i].is_clicked(events):
                        slot_name = f"slot{i+1}"
                        if slot_titles[i] == "EMPTY SLOT":
                            show_slots = False
                            inputing_username = True
                            show_slot = i+1
                            buttons = [btn_menu_exit, btn_music, btn_menu_input_back, btn_menu_input_next]
                        else:
                            save_data.load_slot(slot_name)
                            game_menu(window)
                        
                    # if save_slot_buttons[0].is_clicked(events):
                    #     show_slot = 1
                    # elif save_slot_buttons[1].is_clicked(events):
                    #     show_slot = 2
                    # elif save_slot_buttons[2].is_clicked(events):
                    #     show_slot = 3

            else:
                if inputing_username:
                    draw.rect(window, DARK_GRAY, menu_input_box, border_radius=8)
                    window.blit(menu_input_title, (menu_input_box.x+70, menu_input_box.y+25))

                    draw.rect(window, GRAY, username_box, border_radius=8)
                    draw.rect(window, LIGHT_GRAY if username_active else BLACK, username_box, 2, border_radius=8)

                    username_surface = font_btn_menu_input.render(username, True, BLACK)
                    window.blit(username_surface, (username_box.x + 10, username_box.y + 10))

                    if btn_menu_input_back.is_clicked(events):
                        show_slots = True
                        inputing_username = False
                        buttons = [btn_menu_exit, btn_music]
                        username = ""
                    if btn_menu_exit.is_clicked(events):
                        show_slots = False
                        inputing_username = False
                        username = ""

                    if btn_menu_input_next.is_clicked(events):
                        if username.strip() != "":
                            slot_name = f"slot{show_slot}"
                            with open(f"saves_slots/{slot_name}.json", "w", encoding="utf-8") as f:
                                json.dump({
                                    "user" : username.strip(),
                                    "level" : 1,
                                    "gold" : 0,
                                    "score" : 0
                                }, f, ensure_ascii=False, indent=2)

                            save_data.load_slot(slot_name)
                            slot_titles[show_slot-1] = username.strip()

                            game_intro(window)
            
            if btn_menu_exit.is_clicked(events):
                selecting_slots = False
                buttons = [btn_play, btn_music]

            elif btn_music.is_clicked(events):
                save_data.music = not save_data.music
                save_data.save_settings()

        for btn in buttons:
            btn.show(window)

        fade.update()
        fade.draw()

        btn_music.text = "ON" if save_data.music else "OFF"
        mixer.music.set_volume(1 if save_data.music else 0)

        display.flip()
        clock.tick(FPS)
