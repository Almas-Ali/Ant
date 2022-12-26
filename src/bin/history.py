from userlib import UserLib
from config import path_dir
import os

class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'history: Get all previously used commands'
        print(short_help)

    def __help__(self):
        usage = '''Usage: history
    To get all previously used commands.
history       - To get all ant history
history clear - To clear history file
history -v    - To print the version of the command
history help  - To get this help screen
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()
        
        elif args[0] == '-v':
            self.__version__()

        elif args[0] == 'clear':
            with open(os.path.join(path_dir, '.ant_history'), 'w') as history:
                history.write('')

        else:
            with open(os.path.join(path_dir, '.ant_history'), 'r') as history:
                i = 0
                f2 = [i.rstrip('\n') for i in history.readlines()]
                for line in f2:
                    i += 1
                    print(f'{i}: {line}')
