import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  # You can experiment with different indices
engine.setProperty('rate', 130)

def say_text(text):
    engine.say(text)
    engine.runAndWait()
