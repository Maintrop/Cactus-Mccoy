# Модулі
from pygame import *
import sys
init()

from config import WIDTH, HEIGHT, FPS, BLACK, LIGHT_GREEN, LIGHT_ORANGE, BEIGE, BROWN, WHITE, DARK_BEIGE, DARK_GREEN
from button import Button
from player import Player
from enemy import Enemy
from platform import Platform
import save_data

# Функція
def game(window):
    clock = time.Clock()
    mixer.init()

    # Блоки
    game_HUD = Rect(0, HEIGHT-70, WIDTH, 70)

    # Фон
    bg = image.load("assets/images/levels/bg/bg_level1.png").convert_alpha()
    bg = transform.scale(bg, (WIDTH, HEIGHT-70))
    
    # Зображення
    intro_level_img = image.load("assets/images/levels/intro/intro_level1.png").convert_alpha()
    intro_level_img = transform.smoothscale(intro_level_img, (500, 300))
    money_icon_img = image.load("assets/images/levels/money_icon.png").convert_alpha()

    # Шрифти
    cutscene_level_font = font.SysFont("arialblack", 35)
    cutscene_title_font = font.SysFont("arialblack", 40)
    font_btns_game = font.SysFont(None, 30)
    font_pause_title = font.SysFont("arialblack", 50)
    font_pause_descr = font.SysFont("arialblack", 30)
    font_level_score_text = font.SysFont("arialblack", 18)
    font_level_counter = font.SysFont(None, 25)

    # Тексти
    level_titles = {
        "level1" : "Cactus Canyon",
        "level2" : "Prospector Mines",
        "level3" : "Rustler Railroad",
        "level4" : "Shady Springs",
        "level5" : "Powderkeg Pass",
        "level6" : "Midnight Express",
        "level7" : "Rattler Ravine",
        "level8" : "Brimstone Mine",
        "level9" : "Deadridge Railway",
        "level10" : "Sunset Gulch",
        "level11" : "Emerald Temple",
        "level12" : "Emerald Shrine",
    }

    title = level_titles[f"level{save_data.level}"]

    cutscene_level = cutscene_level_font.render(f"Level {save_data.level}", True, LIGHT_GREEN)
    cutscene_title = cutscene_title_font.render(f"{title}", True, LIGHT_ORANGE)
    pause_title = font_pause_title.render("GAME PAUSED", True, WHITE)
    pause_descr = font_pause_descr.render("CLICK THE PAUSE AGAIN TO CONTINUE", True, WHITE)
    level_score_text = font_level_score_text.render("Pts.", True, DARK_GREEN)
    level_counter_score = font_level_counter.render(f"{save_data.score}", True, BROWN)
    level_counter_gold = font_level_counter.render(f"{save_data.gold}", True, BROWN)

    # Кнопки
    btn_music = Button(WIDTH-70, HEIGHT-50, 60, 40, BEIGE, font_btns_game, "ON" if save_data.music else "OFF", tuple(min(255, i+40) for i in BROWN), 16, border_width=4)
    btn_pause = Button(WIDTH-140, HEIGHT-50, 60, 40, BEIGE, font_btns_game, "| |", tuple(min(255, i+40) for i in BROWN), 16, border_width=4)
    btn_menu = Button(WIDTH-250, HEIGHT-50, 100, 40, BEIGE, font_btns_game, "Menu", tuple(min(255, i+40) for i in BROWN), 16, border_width=4)
    btn_rest = Button(10, HEIGHT-50, 100, 40, BEIGE, font_btns_game, "Restart", tuple(min(255, i+40) for i in BROWN), 16, border_width=4)
    
    buttons = [btn_music, btn_pause, btn_menu, btn_rest]

    # Гравець
    player = Player(0, 0)
    player.rect.center = (WIDTH//2, HEIGHT//2)
    
    if save_data.level == 1:
        # Платформи
        ground1 = Platform(-600, 100, "assets/images/levels/platforms/level1/ground1.png", 700, HEIGHT-100, is_ground=True)
        ground2 = Platform(0, HEIGHT-300, "assets/images/levels/platforms/level1/ground1.png", WIDTH-250, 400)
        ground3 = Platform(WIDTH-250, HEIGHT-150, "assets/images/levels/platforms/level1/ground1.png", WIDTH-250, 300)
        ground4 = Platform(WIDTH+600, 0, "assets/images/levels/platforms/level1/ground1.png", WIDTH, 700)
        platform1 = Platform(WIDTH+300, HEIGHT-400, "assets/images/levels/platforms/level1/platform1.png", 200, 40)
        tutorial_sign1 = Platform(500, HEIGHT-230, "assets/images/levels/tutorial_signs/sign1.png", 350, 140)

        GROUND_LEVEL = HEIGHT - 150 
    
        platforms = [
            ground2,
            ground1,
            ground3,
            ground4,
            platform1,
            tutorial_sign1
        ]

        # Вороги
        # enemy1 = Enemy(300, HEIGHT-300, 50, "assets/images/levels/enemy/enemy.png")

        # enemies = [
        #     enemy1
        # ]

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
                if fade_alpha >= 0:
                    fade_alpha -= 15
                    fade_surface.set_alpha(fade_alpha)
                    window.blit(fade_surface, (0, 0))
            else:
                if fade_alpha < 240:
                    fade_alpha += 20
                    fade_surface.set_alpha(fade_alpha)
                    window.blit(fade_surface, (0, 0))
                else:
                    running_game_intro = False
                    mixer.music.load("assets/audios/music/Cactus_McCoy_Main.ogg")
                    mixer.music.play(-1)
                    mixer.music.set_volume(1 if save_data.music else 0)

            display.flip()
            clock.tick(FPS)

    # Перезапуск рівня
    def init_game():
        # Музика
        mixer.music.load("assets/audios/music/Cactus_McCoy_startLevel.mp3")
        mixer.music.play()
        mixer.music.set_volume(1 if save_data.music else 0)

        start_cutscene()

    init_game()

    running_game = True
    running = "level"
    restart = False
    pause = False

    while running_game:
        while running == "level":
            events = event.get()
            for e in events:
                if e.type == QUIT:
                    sys.exit()

            window.blit(bg, (0, 0))

            shift_x, shift_y = player.move([p.rect for p in platforms])

            for platform in platforms:
                platform.shift(-shift_x, 0)

            for platform in platforms:
                if ground1.is_ground:
                    platform.shift(0, -shift_y)

            for platform in platforms:
                platform.shift(0, -shift_y)

            print(shift_y)
                
            for platform in platforms:
                platform.show(window)

            # for enemy in enemies:
            #     enemy.show(window)
            player.show(window)

            draw.rect(window, DARK_BEIGE, game_HUD)

            window.blit(money_icon_img, (130, HEIGHT-60))
            window.blit(level_counter_gold, (170, HEIGHT-55))
            window.blit(level_score_text, (125, HEIGHT-30))
            window.blit(level_counter_score, (170, HEIGHT-25))

            if btn_menu.is_clicked(events):
                pass

            elif btn_music.is_clicked(events):
                save_data.music = not save_data.music
                save_data.save_settings()
                btn_music.text = "ON" if save_data.music else "OFF"
                mixer.music.set_volume(1 if save_data.music else 0)

            elif btn_pause.is_clicked(events):
                pause = True

                while pause:
                    events = event.get()
                    for e in events:
                        if e.type == QUIT:
                            sys.exit()

                    window.blit(bg, (0, 0))

                    for platform in platforms:
                        platform.show(window)
                    
                    player.show(window)

                    draw.rect(window, DARK_BEIGE, game_HUD)

                    window.blit(money_icon_img, (130, HEIGHT-60))
                    window.blit(level_counter_gold, (170, HEIGHT-55))
                    window.blit(level_score_text, (125, HEIGHT-30))
                    window.blit(level_counter_score, (170, HEIGHT-25))

                    window.blit(pause_title, (WIDTH//2-pause_title.get_width()//2, HEIGHT//2 - 150))
                    window.blit(pause_descr, (WIDTH//2-pause_descr.get_width()//2, HEIGHT//2 - 60))

                    if btn_menu.is_clicked(events):
                        pass

                    elif btn_music.is_clicked(events):
                        save_data.music = not save_data.music
                        save_data.save_settings()
                        btn_music.text = "ON" if save_data.music else "OFF"

                    elif btn_pause.is_clicked(events):
                        pause = False

                    elif btn_rest.is_clicked(events):
                        restart = True
                        pause = False
                        running = ""

                    for btn in buttons:
                        btn.show(window)

                    mixer.music.set_volume(0)

                    display.flip()
                    clock.tick(FPS)
                mixer.music.set_volume(1 if save_data.music else 0)

            elif btn_rest.is_clicked(events):
                restart = True
                running = ""

            for btn in buttons:
                btn.show(window)

            display.flip()
            clock.tick(FPS)

        if not restart:
            break
        else:
            init_game()
            restart = False
            running = "level"

        display.flip()
        clock.tick(FPS)
