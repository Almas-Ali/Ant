from userlib import UserLib
import os


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: mkdir
    Make Directory command

mkdir <dir> - To create a directory
mkdir -v    - To print the version of the command
mkdir help  - To get this help screen
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

        else:
            os.mkdir(args[0])
