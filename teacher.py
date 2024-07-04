from os.path import isfile, isdir
from os import getcwd, makedirs
from platform import system
from gtts import gTTS
from playsound import playsound
import utils


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
            print('The file is not found!')
            exit(1)
        if len(items) == 0:
            utils.splitter()
            print('The file is empty!')
            exit(0)
        utils.splitter()
        print('The file is loaded...')
        utils.splitter2()
        return items

    def read_check(self):
        for item in self.items_list:
            self.play_audio_file(item)
            while True:
                user_input = input()
                if user_input == item:
                    break
                elif user_input == '-RPT':
                    self.play_audio_file(item)
                else:
                    print('Correct:', item)
                    break
            utils.splitter()
        print('The file is over...')
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
            print('The current OS is not defined!')
            exit(1)
        if not isdir(audio_dir_loc):
            makedirs(audio_dir_loc)
        audio_file_name = item.replace(' ', '_') + '.mp3'
        audio_file_loc = audio_dir_loc + audio_file_name
        if not isfile(audio_file_loc):
            try:
                audio_file = gTTS(text=item, lang=self.file_lang, slow=False)
            except ValueError:
                print('Language code is not supported!')
                exit(1)
            audio_file.save(audio_file_loc)
        playsound(audio_file_loc)


class TeacherException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
