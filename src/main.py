import locale
import argparse
import text_to_speech

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language


def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Assistant Akif.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Init language %s...', args.language)
    text_to_speech.say_text("Hi, i Am Akif assistaint. Do you have problems?")



