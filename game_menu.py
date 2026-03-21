# Модулі
from pygame import *
import sys
init()

from config import LIGHT_ORANGE, WIDTH, HEIGHT, FPS, BLACK, LIGHT_GRAY, GRAY, LIGHT_RED, DARK_RED, YELLOW, BROWN
from button import Button
import save_data

# Функція
def game_menu(window):
    clock = time.Clock()
    mixer.init()

    # Зображення
    black_stripe1 = image.load("assets/images/menu/black_stripe.png").convert_alpha()
    black_stripe1 = transform.smoothscale(black_stripe1, (WIDTH, 100))
    black_stripe2 = transform.rotate(black_stripe1, 180)

    locked_level_img = image.load("assets/images/menu/locked_level.png").convert_alpha()
    locked_level_img = transform.smoothscale(locked_level_img, (220, 135))

    # Шрифти
    font_game_menu_title = font.SysFont(None, 85)
    font_btn_music = font.SysFont(None, 40)
    font_btn_menu_exit = font.SysFont(None, 40)
    font_game_menu_btns = font.SysFont(None, 30)
    font_menu_map_total_score = font.SysFont("arialblack", 30)

    # Тексти
    game_menu_title = font_game_menu_title.render("MAP", True, LIGHT_GRAY)
    menu_total_score_text = font_menu_map_total_score.render(f"TOTAL SCORE: {save_data.score}", True, LIGHT_ORANGE)

    # Кнопки
    btn_music = Button(WIDTH - 90, HEIGHT - 90, 80, 80, GRAY, font_btn_music, "ON" if save_data.music else "OFF", BLACK, 24)
    btn_menu_exit = Button(20, 20, 150, 50, LIGHT_RED, font_btn_menu_exit, "EXIT", DARK_RED, 16)

    btn_menu_btn_map = Button(350, HEIGHT-85, 80, 45, YELLOW, font_game_menu_btns, "MAP", BROWN, 14)
    btn_menu_btn_upgrades = Button(445, HEIGHT-85, 150, 45, YELLOW, font_game_menu_btns, "UPGRADES", BROWN, 14)
    btn_menu_btn_badges = Button(610, HEIGHT-85, 130, 45, YELLOW, font_game_menu_btns, "BADGES", BROWN, 14)
    btn_menu_btn_help = Button(755, HEIGHT-85, 90, 45, YELLOW, font_game_menu_btns, "HELP", BROWN, 14)

    buttons = [btn_music, btn_menu_exit, btn_menu_btn_map, btn_menu_btn_upgrades, btn_menu_btn_badges, btn_menu_btn_help]
    
    menu_tab = "map"
        
    running = True
    while running:
        events = event.get()
        for e in events:
            if e.type == QUIT:
                sys.exit()
        
        window.fill(BLACK)

        window.blit(black_stripe1, (0, 0))
        window.blit(black_stripe2, (0, HEIGHT - black_stripe2.get_height()))

        if menu_tab == "map":
            window.blit(game_menu_title, (530, 30))
            window.blit(menu_total_score_text, (450, 550))

            for row in range(3):
                for col in range(4):
                    locked_level_img_x = 140 + col * 230
                    locked_level_img_y = 115 + row * 145
                    window.blit(locked_level_img, (locked_level_img_x, locked_level_img_y))

        elif menu_tab == "upgrades":
            window.blit(game_menu_title, (435, 30))

        elif menu_tab == "badges":
            window.blit(game_menu_title, (480, 30))

        elif menu_tab == "help":
            window.blit(game_menu_title, (520, 30))
        
        if btn_menu_exit.is_clicked(events):
            break

        elif btn_music.is_clicked(events):
            save_data.music = not save_data.music
            save_data.save_settings()

        elif btn_menu_btn_map.is_clicked(events):
            menu_tab = "map"
            game_menu_title = font_game_menu_title.render("MAP", True, LIGHT_GRAY)
        
        elif btn_menu_btn_upgrades.is_clicked(events):
            menu_tab = "upgrades"
            game_menu_title = font_game_menu_title.render("UPGRADES", True, LIGHT_GRAY)
        
        elif btn_menu_btn_badges.is_clicked(events):
            menu_tab = "badges"
            game_menu_title = font_game_menu_title.render("BADGES", True, LIGHT_GRAY)

        elif btn_menu_btn_help.is_clicked(events):
            menu_tab = "help"
            game_menu_title = font_game_menu_title.render("HELP", True, LIGHT_GRAY)

        for btn in buttons:
            btn.show(window)

        btn_music.text = "ON" if save_data.music else "OFF"
        mixer.music.set_volume(1 if save_data.music else 0)

        display.flip()
        clock.tick(FPS)
