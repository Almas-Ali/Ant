from userlib import UserLib
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'chdir: \tChange the current directory'
        print(short_help)

    def __help__(self):
        usage = '''Usage: chdir
    Change the current directory

chdir <path>   - To change the current directory
chdir -v       - To get the version of the program
chdir help     - To get this help screen
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

        elif args[0] == '':
            print('chdir: error: check \'chdir help\' for usage.')

        elif args[0] == '..':
            os.chdir('..')

        else:
            try:
                os.chdir(args[0])
            except:
                print('chdir: error: check \'chdir help\' for usage.')
