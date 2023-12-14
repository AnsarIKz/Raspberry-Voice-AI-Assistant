import os
import sys
import speech_recognition as sr
import vosk
import numpy as np

def recognize_audio(model_path):
    recognizer = sr.Recognizer()

    # Load Vosk model
    model = vosk.Model(model_path)

    # Create Vosk recognizer with a sample rate of 16000 (adjust as needed)
    vosk_recognizer = vosk.KaldiRecognizer(model, 16000)

    with sr.Microphone() as source:
        print("Say something:")
        audio_data = recognizer.listen(source)

    try:
        # Perform Vosk recognition
        audio_data_np = np.frombuffer(audio_data.frame_data, dtype=np.int16)
        vosk_recognizer.AcceptWaveform(audio_data_np)

        # Get the final result
        result = vosk_recognizer.Result()
        result_text = result["text"]

        print("You said:", result_text)
        return result_text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error during Vosk recognition; {e}")
        return None

if __name__ == "__main__":
    model_path = r'C:\Users\nansa\Desktop\AIY-Voice-Assistant\src\voice_models\vosk0.15'

    if not os.path.exists(model_path):
        print(f"Vosk model path {model_path} not found.")
        sys.exit(1)

    while True:
        command = recognize_audio(model_path)
        if command:
            if "hello" in command.lower():
                print("Hello! How can I help you?")
            elif "goodbye" in command.lower():
                print("Goodbye!")
                break
            else:
                print("Command not recognized. Try again.")
