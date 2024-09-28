from platform import system
import xml.etree.ElementTree as ET
from teacher import Teacher
import utils as utils
import vercheck as vercheck

OS = system()
SETTINGS = utils.load_settings()

try:
    if OS == 'Linux':
        tree = ET.parse('./info.xml')
    elif OS == 'Windows':
        tree = ET.parse('.\\info.xml')
except FileNotFoundError:
    utils.adv_print('File not found: info.xml', ['RED'])
    utils.exit(1)
root = tree.getroot()

app_name = root.find('app').findtext('name')
app_ver = root.find('app').findtext('ver')
app_repo = root.find('app').findtext('repo')
dev_name = root.find('dev')[0].get('name')
dev_github = root.find('dev')[0].get('github')

name_banner = ['   _____                         _     __  __      _ ',
               '  / ____|                       | |   |  \/  |    | |',
               ' | |     ___  _ __ _ __ ___  ___| |_  | \  / | ___| |',
               ' | |    / _ \| \'_ | \'__/ _ \/ __| __| | |\/| |/ _ \ |',
               ' | |___| (_) | |  | | |  __/ (__| |_  | |  | |  __/_|',
               '  \_____\___/|_|  |_|  \___|\___|\__| |_|  |_|\___(_)',
               '                                                     ']
for line in name_banner:
    utils.adv_print(line, ['BOLD'])

if OS == 'Linux':
    print('{}{}{} ({})'.format(utils.STYLES.get('BOLD'),
                               app_name,
                               utils.STYLES.get('END'),
                               app_ver))
    print('Open-source and free, available on {}GitHub: {}{}'.format(utils.STYLES.get('BOLD'),
                                                                     app_repo,
                                                                     utils.STYLES.get('END')))
    print('Written by {}{} ({}){}.'.format(utils.STYLES.get('BOLD'),
                                           dev_name, dev_github,
                                           utils.STYLES.get('END')))
elif OS == 'Windows':
    print('{} ({})'.format(app_name, app_ver))
    print('Open-source and free, available on GitHub: {}'.format(app_repo))
    print('Written by {} ({}).'.format(dev_name, dev_github))

if SETTINGS.get('check_update', 1):
    utils.splitter()
    ver_checker = vercheck.VerCheck()
    ver_checker.version_banner()
utils.splitter2()
utils.attention_banner()
utils.splitter()
utils.help_banner()
utils.splitter2()

while True:
    teacher = Teacher()
    teacher.read_check()
