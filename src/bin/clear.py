from userlib import UserLib
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'clear: \tClear the screen'
        print(short_help)

    def __help__(self):
        usage = '''Usage: clear
    Clear the screen

clear      - To clear the screen
clear -v   - To print the version of the command
clear help - To get this help screen
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

        elif os.name == 'nt':
            try:
                os.system('cls')
            except:
                pass

        else:
            os.system('clear')
