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
        self.OS = system()
        self.items_list = self.load_file()

    def load_file(self) -> list[str]:
        # A list to store each line as its elements
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
            utils.exit(1)
        # If the file is empty
        if len(items) == 0:
            utils.splitter()
            utils.adv_print('The file is empty!', ['CYAN'])
            utils.exit(0)
        utils.splitter()
        utils.adv_print('The file is loaded...', ['CYAN'])
        utils.splitter2()
        return items

    def read_check(self):
        # A list to store the user errors
        self.err_list = []
        # Iterate each line of the file
        for item in self.items_list:
            self.play_audio_file(item)
            while True:
                user_input = input()
                # If the inout is correct
                if user_input == item:
                    break
                # If the repetition command is entered
                elif user_input == '-RPT':
                    self.play_audio_file(item)
                # If the input is incorrect
                else:
                    if self.OS == 'Linux':
                        print('Correct: {}{}{}{}'.format(
                            utils.STYLES.get('UNDERLINE'),
                            utils.STYLES.get('GREEN'),
                            item,
                            utils.STYLES.get('END')
                        ))
                    elif self.OS == 'Windows':
                        print('Correct: {}'.format(item))
                    self.err_list.append(item)
                    break
            utils.splitter()
        # The iteration is over
        utils.adv_print('The file is over...', ['CYAN'])
        utils.splitter2()
        # If the list of user errors is not empty
        if len(self.err_list) > 0:
            utils.adv_print('Errors:', ['BOLD', 'RED'])
            # Print the user errors separated by a dash
            print('\t' + ' - '.join(self.err_list))
            utils.splitter()
            # Ask whether to save the user errors or not
            save_bool = True if input(
                'Do you want to save the errors? [Y / n]: ').lower() == 'y' else False
            if save_bool:
                self.save_errors()
            utils.splitter2()

    def play_audio_file(
        self,
        item: str
    ):
        # Define the Audio directory path
        # If the working directory is not changed to the app root dir in the
        # .bat and .sh files, the Audio dir will be created somewhere else.
        if self.OS == 'Linux':
            audio_dir_loc = getcwd() + '/Audio/'
        elif self.OS == 'Windows':
            audio_dir_loc = getcwd() + '\\Audio\\'
        else:
            utils.adv_print('The current OS is not defined!', ['RED'])
            utils.exit(1)
        # If the Audio dir does not exist
        if not isdir(audio_dir_loc):
            makedirs(audio_dir_loc)
        # Define the audio file name
        # The spaces in the possible phrase are replaced with underlines to
        # avoid every potential errors.
        audio_file_name = self.file_lang + \
            '_' + item.replace(' ', '_') + '.mp3'
        # Define the audio file path
        # By adding the Audio dir path to the audio file name, the absolute
        # path is created.
        audio_file_loc = audio_dir_loc + audio_file_name
        # If the audio file does not exist
        if not isfile(audio_file_loc):
            try:
                audio_file = gTTS(text=item, lang=self.file_lang, slow=False)
            except ValueError:
                utils.adv_print('The entered language code is not defined!',
                                ['RED'])
                utils.exit(1)
            audio_file.save(audio_file_loc)
        # If the file is created but the data stored is 0
        # This can occur when the internet connection is lost
        if getsize(audio_file_loc) == 0:
            utils.adv_print('The audio file is empty: {}'.format(
                audio_file_loc), ['RED'])
            utils.adv_print('Remove the file before running the app again!',
                            ['RED'])
            utils.exit(1)
        # Play the audio file
        playsound(audio_file_loc)

    def save_errors(self):
        while True:
            # The given path can be relative to the app root directory.
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
