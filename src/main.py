import locale
import argparse
import text_to_speech

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language


def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Ассистент Акиф.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Инициализация языка %s...', args.language)
    text_to_speech.say_text("Добро пожаловать я ассистент Акиф. Я могу ответить на твои вопросы")



