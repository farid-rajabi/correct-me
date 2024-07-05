import time
from teacher import Teacher
import utils


print('CORRECT ME!\n\
Open-source and free, available on GitHub: https://github.com/farid-rajabi/correct-me\n\
Written by Farid Rajabi (https://github.com/farid-rajabi).')
time.sleep(2)
utils.splitter2()
utils.attention_banner()
utils.splitter()
utils.help_banner()
utils.splitter2()

while True:
    teacher = Teacher()
    teacher.read_check()
