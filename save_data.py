# Модуль json
import json

# Відкриваємо налаштування та збережені дані
with open("settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

with open("saves_slots/slot1.json", "r", encoding="utf-8") as f:
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

def load_new_data(slot_file, username):
    try:
        with open(slot_file, "r", encoding="utf-8") as f:
            data = json.load(f)

    except FileNotFoundError:
        data = {}

    data["user"] = username
    data["level"] = 1
    data["gold"] = 0

    with open(slot_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
