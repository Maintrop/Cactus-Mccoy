# Модулі
import json

music = True

current_slot = None
user = "EMPTY SLOT"
level = 1
gold = 0
score = 0

# Робота з даними
def load_settings():
    global music

    try:
        with open("settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            music = data.get("music", True)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        music = True

def save_settings():
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump({
            "music" : music
            }, f, ensure_ascii=False, indent=2)

def get_slot_user(slot_file):
    try:
        with open(slot_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("user", "EMPTY SLOT")
    except (FileNotFoundError, json.JSONDecodeError):
        return "EMPTY SLOT"

def load_slot(slot_n):
    global current_slot, user, level, gold, score
    file_path = f"saves_slots/{slot_n}.json"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            current_slot = slot_n
            user = data.get("user", "EMPTY SLOT")
            level = data.get("level", 1)
            gold = data.get("gold", 0)
            score = data.get("score", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        user = "EMPTY SLOT"
        level = 1
        gold = 0
        score = 0
        save_slot()

def save_slot():
    if current_slot is None:
        return
    file_path = f"saves_slots/{current_slot}.json"

    data = {
        "user" : user,
        "level" : level,
        "gold" : gold,
        "score" : score
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def clear_data(slot_name):
    data = {
        "user" : "EMPTY SLOT",
        "level" : 1,
        "gold" : 0,
        "score" : 0
    }

    with open(f"saves_slots/{slot_name}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_score(points: int):
    global score
    score += points
    save_slot()

load_settings()
