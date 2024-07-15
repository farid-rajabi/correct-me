import requests
import xml.etree.ElementTree as ET
import utils


class VerCheck:

    def __init__(self) -> None:
        self.LATEST_URL = 'https://raw.githubusercontent.com/farid-rajabi/correct-me/main/info.xml'
        try:
            utils.adv_print('Retrieving the latest version info...', ['CYAN'])
            response = requests.get(self.LATEST_URL)
            self.LATEST_VER = ET.fromstring(
                response.text).find('app').findtext('ver')
        except:
            self.LATEST_VER = None
            utils.adv_print('Failed to retrieve the latest version info!',
                            ['RED'])
        try:
            tree = ET.parse('./info.xml')
            self.CURRENT_VER = tree.getroot().find('app').findtext('ver')
        except FileNotFoundError:
            self.CURRENT_VER = None
            utils.adv_print('File not found: info.xml', ['RED'])

    def version_banner(self):
        if self.CURRENT_VER == None or self.LATEST_VER == None:
            return
        if self.CURRENT_VER == self.LATEST_VER:
            utils.adv_print('This is the latest version!', ['GREEN'])
        else:
            utils.adv_print('A newer version is available!',
                            ['UNDERLINE', 'GREEN'])
            sec_1 = '{}[{}]{}'.format(utils.STYLES.get('RED'),
                                      self.CURRENT_VER,
                                      utils.STYLES.get('END'))
            sec_2 = '{}[{}]{}'.format(utils.STYLES.get('GREEN'),
                                      self.LATEST_VER,
                                      utils.STYLES.get('END'))
            print(sec_1 + ' -> ' + sec_2)
            utils.adv_print(
                'Download: https://github.com/farid-rajabi/correct-me/releases/tag/v{}'.format(
                    self.LATEST_VER
                ), ['BOLD']
            )
