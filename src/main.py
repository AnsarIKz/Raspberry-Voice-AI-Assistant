import locale
import argparse
import voice_to_text
import generate_ai_response
from text_to_speech

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    language = locale_language()
    text_to_speech.say_text("Hi, i Am Akif assistaint.")
    text_to_speech.say_text("What can i do for you.")
    # logging.basicConfig(filename='telebot.log', level=logging.INFO,
    #                 format='%(asctime)s - %(levelname)s - %(message)s')

    while True:
        # Voice to Text
        command = voice_to_text.recognize_audio()

        if command:
            # Text Handler (AI Response)
            ai_response = generate_ai_response.get_resp(command)
            # logging.info(f"User said {command}")

            if ai_response:
                print("AI Response:", ai_response)
                text_to_voice.say_text(ai_response)
            else:
                print("No AI Response. Try again.")

if __name__ == "__main__":
    main()
