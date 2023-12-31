import os
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from dotenv import load_dotenv

load_dotenv()

model_path = os.getenv("MODEL_PATH")
model = Model(model_path)

def init():
    return True

class VoskRecognizer(sr.Recognizer):
    def recognize_vosk(self, audio_data, show_all=False):
        sample_frequency = audio_data.sample_rate
        vosk_recognizer = KaldiRecognizer(model, sample_frequency)
        result = vosk_recognizer.AcceptWaveform(audio_data)

        if show_all:
            return result
        else:
            return result

def recognize_audio():
    recognizer = VoskRecognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio_data = recognizer.listen(source)
        print(audio_data)

    try:
        result = recognizer.recognize_vosk(audio_data)
        print("Vosk Result:", result)
        return result
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error during Vosk recognition; {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    if not os.path.exists(model_path):
        print(f"Vosk model path {model_path} not found.")
        sys.exit(1)

    while True:
        command = recognize_audio()
        if command:
            if "hello" in command.lower():
                print("Hello! How can I help you?")
            elif "goodbye" in command.lower():
                print("Goodbye!")
                break
            else:
                print("Command not recognized. Try again.")
