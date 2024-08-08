from os.path import isfile, isdir, getsize
from os import getcwd, makedirs
from platform import system
from gtts import gTTS
from playsound import playsound
import utils as utils


class Teacher:

    def __init__(
        self
    ) -> None:
        self.os = system()
        self.items_list = self.load_file()

    def load_file(self) -> list[str]:
        items = []
        self.file_loc = input('Enter the path: ')
        utils.splitter()
        utils.supported_langs()
        self.file_lang = input('Enter the language tag: ')
        try:
            with open(file=self.file_loc, mode='r') as file:
                items = [item.rstrip() for item in file]
        except FileNotFoundError:
            utils.splitter()
            utils.adv_print('File not found!', ['RED'])
            exit(1)
        if len(items) == 0:
            utils.splitter()
            utils.adv_print('The file is empty!', ['CYAN'])
            exit(0)
        utils.splitter()
        utils.adv_print('The file is loaded...', ['CYAN'])
        utils.splitter2()
        return items

    def read_check(self):
        self.err_list = []
        for item in self.items_list:
            self.play_audio_file(item)
            while True:
                user_input = input()
                if user_input == item:
                    break
                elif user_input == '-RPT':
                    self.play_audio_file(item)
                else:
                    print('Correct: {}{}{}{}'.format(
                        utils.STYLES.get('UNDERLINE'),
                        utils.STYLES.get('GREEN'),
                        item,
                        utils.STYLES.get('END')
                    ))
                    self.err_list.append(item)
                    break
            utils.splitter()
        utils.adv_print('The file is over...', ['CYAN'])
        utils.splitter2()
        if len(self.err_list) > 0:
            utils.adv_print('Errors:', ['BOLD', 'RED'])
            print('\t' + ' - '.join(self.err_list))
            utils.splitter()
            save_bool = True if input(
                'Do you want to save the errors? [Y / n]: ').lower() == 'y' else False
            if save_bool:
                self.save_errors()
            utils.splitter2()

    def play_audio_file(
        self,
        item: str
    ):
        if self.os == 'Linux':
            audio_dir_loc = getcwd() + '/Audio/'
        elif self.os == 'Windows':
            audio_dir_loc = getcwd() + '\\Audio\\'
        else:
            utils.adv_print('The current OS is not defined!', ['RED'])
            exit(1)
        if not isdir(audio_dir_loc):
            makedirs(audio_dir_loc)
        audio_file_name = self.file_lang + \
            '_' + item.replace(' ', '_') + '.mp3'
        audio_file_loc = audio_dir_loc + audio_file_name
        if not isfile(audio_file_loc):
            try:
                audio_file = gTTS(text=item, lang=self.file_lang, slow=False)
            except ValueError:
                utils.adv_print('The entered language code is not defined!',
                                ['RED'])
                exit(1)
            audio_file.save(audio_file_loc)
        if getsize(audio_file_loc) == 0:
            utils.adv_print('The audio file is empty: {}'.format(
                audio_file_loc), ['RED'])
            utils.adv_print('Remove the file before running the app again!',
                            ['RED'])
            exit(1)
        playsound(audio_file_loc)

    def save_errors(self):
        while True:
            err_file_loc = input('Enter the path to save the file: ')
            try:
                with open(file=err_file_loc, mode='x') as file:
                    file.writelines('\n'.join(self.err_list))
                utils.adv_print('The file is saved!',
                                ['CYAN'])
                break
            except FileExistsError:
                utils.adv_print('The file exists! Try another name...',
                                ['RED'])
                continue
            except FileNotFoundError:
                utils.adv_print('The created file not found!',
                                ['RED'])
                continue
