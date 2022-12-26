from userlib import UserLib
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'ls: \tList directory contents'
        print(short_help)

    def __help__(self):
        usage = '''Usage: ls
To get all directors and file of current location.

ls       - Everything in current folder
ls -v    - To print the version of the command
ls help  - To get this help screen
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None, *arg, **kwargs):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            l = os.listdir()
            print(' '.join(l))
