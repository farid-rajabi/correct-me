import time
import xml.etree.ElementTree as ET
from teacher import Teacher
import utils


try:
    tree = ET.parse('./info.xml')
except FileNotFoundError:
    utils.adv_print('File not found: info.xml', ['RED'])
    exit(1)
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
    print(line)

print('{} ({})'.format(app_name, app_ver))
print('Open-source and free, available on {}GitHub: {}{}'.format(utils.STYLES.get('BOLD'),
                                                                 app_repo,
                                                                 utils.STYLES.get('END')))
print('Written by {}{} ({}){}.'.format(utils.STYLES.get('BOLD'),
                                       dev_name, dev_github,
                                       utils.STYLES.get('END')))
time.sleep(2)
utils.splitter2()
utils.attention_banner()
utils.splitter()
utils.help_banner()
utils.splitter2()

while True:
    teacher = Teacher()
    teacher.read_check()
