from userlib import UserLib
from core import Shell


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: help
    Make Directory command

help            - To get this help screen
help <command>  - To get help for a specific command
help -v         - To print the version of the command
help help       - To get this help screen
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            try:
                s = Shell()
                s.execute(args[0] + ' help')
            except:
                print('Error: Command not found')

        # else:
        #     self.__help__()
