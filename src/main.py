import locale
import argparse
import voice_to_text
import generate_ai_response
import text_to_speech
import tg_bot
import logging

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80)) 
        ip_address = s.getsockname()[0]
        return ip_address
    except Exception as e:
        print(f"Ошибка при получении IP-адреса: {e}")
        return None
    finally:
        s.close()

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    ip = get_ip_address()
    if ip:
        tg_bot.send_message(f"Akif Assistant started on {ip}")

    #inititalization
    voice_to_text.init()
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
            tg_bot.send_message(command)

            # logging.info(f"User said {command}")

            if ai_response:
                print("AI Response:", ai_response)
                tg_bot.send_message(ai_response)
                text_to_voice.say_text(f'Answer {ai_response}')
            else:
                print("No AI Response. Try again.")

if __name__ == "__main__":
    main()
