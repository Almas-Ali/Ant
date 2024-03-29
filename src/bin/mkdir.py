from lib.userlib import UserLib
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'mkdir: \tMake Directory command'
        print(short_help)

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

    def run(self, args: list = None, *arg, **kwargs):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            if args[0] == '':
                print('mkdir: error: file name required!')
            else:
                try:
                    os.mkdir(args[0])
                except:
                    print(f'mkdir: error: {args[0]}: File exists')
