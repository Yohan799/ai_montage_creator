
import random

MOOD_TO_MUSIC = {
    "relaxed": ["static/music/relaxed1.mp3", "static/music/relaxed2.mp3"],
    "happy": ["static/music/happy1.mp3", "static/music/happy2.mp3"],
    "nostalgic": ["static/music/nostalgic1.mp3"],
    "romantic": ["static/music/romantic1.mp3"],
    "adventure": ["static/music/adventure1.mp3"]
}

def detect_mood(prompt):
    prompt = prompt.lower()
    for mood in MOOD_TO_MUSIC:
        if mood in prompt:
            return mood
    return "relaxed"

def select_music_by_mood(prompt):
    mood = detect_mood(prompt)
    return random.choice(MOOD_TO_MUSIC.get(mood, MOOD_TO_MUSIC["relaxed"]))
