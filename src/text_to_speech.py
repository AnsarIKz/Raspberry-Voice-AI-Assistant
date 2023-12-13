from aiy.voice.tts import say

def say_text(text, language_code):
    say(text, lang=language_code, voice_id='en-US-Wavenet-D', volume=60, pitch=130, speed=100, device='default')
    return text