import os
import sys
import speech_recognition as sr
import vosk

def recognize_audio(model_path):
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

if __name__ == "__main__":
    model_path = r'C:\\Users\\nansa\\Desktop\\AIY-Voice-Assistant\\src\\voice_models\\vosk0.15'

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
