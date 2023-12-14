import os
import sys
import queue
import threading
import struct
import speech_recognition as sr
import vosk
from dotenv import load_dotenv

load_dotenv()

model_path = os.getenv("MODEL_PATH")
model = vosk.Model(model_path)
vosk_recognizer = vosk.KaldiRecognizer(model, 16000)

# Create a queue for audio frames
audio_queue = queue.Queue()

def init():
    return True

def audio_capture():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            try:
                audio_data = recognizer.listen(source)
                audio_queue.put(audio_data)
            except Exception as e:
                print(f"Error capturing audio: {e}")


def recognize_audio():
    try:
        audio_data_frames = []
        while not audio_queue.empty():
            audio_data = audio_queue.get()
            audio_data_frames.extend(audio_data.frame_data)

        audio_data_bytes = struct.pack('<' + 'h' * len(audio_data_frames), *audio_data_frames)
        vosk_recognizer.AcceptWaveform(audio_data_bytes)
        result = vosk_recognizer.Result()
        result_text = result["text"]

        return result_text
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

    # Start the audio capture thread
    audio_thread = threading.Thread(target=audio_capture, daemon=True)
    audio_thread.start()

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


# import os
# import sys
# import struct
# import speech_recognition as sr
# import vosk
# from dotenv import load_dotenv

# load_dotenv()

# model_path = os.getenv("MODEL_PATH")
# model = vosk.Model(model_path)
# vosk_recognizer = vosk.KaldiRecognizer(model, 16000)

# def init():
#     return True

# def recognize_audio():
#     recognizer = sr.Recognizer()


#     with sr.Microphone() as source:
#         print("Say something:")
#         audio_data = recognizer.listen(source)

#     try:
#         audio_data_bytes = struct.pack('<' + 'h' * len(audio_data.frame_data), *audio_data.frame_data)
#         vosk_recognizer.AcceptWaveform(audio_data_bytes)
#         result = vosk_recognizer.Result()
#         result_text = result["text"]

#         return result_text
#     except sr.UnknownValueError:
#         print("Sorry, could not understand audio.")
#         return None
#     except sr.RequestError as e:
#         print(f"Error during Vosk recognition; {e}")
#         return None
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return None

# if __name__ == "__main__":
#     if not os.path.exists(model_path):
#         print(f"Vosk model path {model_path} not found.")
#         sys.exit(1)

#     while True:
#         command = recognize_audio()
#         if command:
#             if "hello" in command.lower():
#                 print("Hello! How can I help you?")
#             elif "goodbye" in command.lower():
#                 print("Goodbye!")
#                 break
#             else:
#                 print("Command not recognized. Try again.")
