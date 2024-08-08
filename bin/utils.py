from os import get_terminal_size
import gtts
import utils as utils


STYLES = {
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'DARKCYAN': '\033[36m',
    'BLUE': '\033[94m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'END': '\033[0m'
}


def attention_banner():
    utils.adv_print('Attention:',
                    ['BOLD', 'YELLOW'])
    utils.adv_print('\tRun the program from its own folder, otherwise, the audio files will be dislocated.',
                    ['YELLOW'])


def help_banner():
    utils.adv_print('Help:',
                    ['BOLD', 'CYAN'])
    utils.adv_print('\tFirst, enter the absolute path of the file, and then specify the language using its corresponding tag (en, it, fr, etc.).\n\t\
Enter -RPT to replay the audio file.',
                    ['CYAN'])


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


def adv_print(
    text: str,
    style: list[str]
):
    for st in style:
        text = STYLES.get(st, '') + text
    print(text + STYLES.get('END'))
