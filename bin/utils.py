import sys
from os import get_terminal_size
from platform import system
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
ATTENTION_BANNER = '\tRun the program from its own folder, otherwise, the audio files will be dislocated.'
HELP_BANNER = '\tFirst, enter the absolute path of the file, and then specify the language using its corresponding tag (en, it, fr, etc.).\n\t\
Enter -RPT to replay the audio file.'
OS = system()


def attention_banner():
    if OS == 'Linux':
        utils.adv_print('Attention:', ['BOLD', 'YELLOW'])
        utils.adv_print(ATTENTION_BANNER, ['YELLOW'])
    elif OS == 'Windows':
        print('Attention:')
        print(ATTENTION_BANNER)


def help_banner():
    if OS == 'Linux':
        utils.adv_print('Help:', ['BOLD', 'CYAN'])
        utils.adv_print(HELP_BANNER, ['CYAN'])
    elif OS == 'Windows':
        print('Help:')
        print(HELP_BANNER)


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
    if OS == 'Linux':
        for st in style:
            text = STYLES.get(st, '') + text
        print(text + STYLES.get('END'))
    elif OS == 'Windows':
        print(text)


def exit(code: int):
    input('Press Enter to exit...')
    # exit() method results in RecursionError that cannot handle closing all
    # the subprocesses.
    sys.exit(code)


def load_settings() -> dict:
    with open('./CorrectMeSettings.ini', mode='r', ) as file:
        lines = file.readlines()
        settings = dict()
        for line in lines:
            if line[0] != '#':
                settings[line[:line.index('=')]] = int(
                    line[line.index('=') + 1])
    return settings
