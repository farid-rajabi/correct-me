from os import get_terminal_size
import gtts


def attention_banner():
    t = 'Attention:\n\tRun the program from its own folder, otherwise, the audio files will be dislocated.'
    print(t)


def help_banner():
    t = 'Help:\n\tFirst, enter the absolute path of the file, and then specify the language using its corresponding tag (en, it, fr, etc.).\n\t\
Enter -RPT to replay the audio file.'
    print(t)


def supported_langs():
    langs = gtts.lang.tts_langs()
    print('Supported languages:')
    print('\t' + 37 * '-')
    print('\t| {:5} | {:25} |'.format('Tag', 'Language'))
    print('\t' + 37 * '-')
    for item in langs:
        print('\t| {:5} | {:25} |'.format(item, langs.get(item)))
    print('\t' + 37 * '-')


def splitter():
    print(get_terminal_size().columns * '-')


def splitter2():
    print(get_terminal_size().columns * '=')
