# Модуль json
import json

# Відкриваємо налаштування та збережені дані
with open("settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

with open("saves.json", "r", encoding="utf-8") as f:
    saves = json.load(f)

music = settings.get("music", True)
saves = saves.get("level", 1)

# Робота з даними
def set_music(mus):
    global music
    music = mus

def reload_settings():
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump({
            "music" : music
        }, f, ensure_ascii=False, indent=2)
