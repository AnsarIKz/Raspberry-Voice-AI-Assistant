import os
import sys
import speech_recognition as sr
import vosk
from dotenv import load_dotenv

load_dotenv()

model_path = os.getenv("MODEL_PATH")
model = vosk.Model(model_path)
vosk_recognizer = vosk.KaldiRecognizer(model, 16000)

def init():
    return True

import os
import sys
import speech_recognition as sr
import vosk

def recognize_audio():
    recognizer = sr.Recognizer()

    model = vosk.Model(model_path)
    recognizer.recognize_vosk = lambda audio_data, language="en-US", show_all=False: model.decode(audio_data, model.get_sample_frequency())

    with sr.Microphone() as source:
        print("Say something:")
        audio_data = recognizer.listen(source)

    try:
        result = recognizer.recognize_vosk(audio_data)
        print("You said:", result)
        return result
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error during Vosk recognition; {e}")
        return None