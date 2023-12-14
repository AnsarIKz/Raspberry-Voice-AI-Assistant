import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  # You can experiment with different indices
engine.setProperty('rate', 120)

text = "Hello, this is a text-to-speech example."
engine.say(text)
engine.runAndWait()
