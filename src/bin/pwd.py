from lib.userlib import UserLib
from lib.backtrack import Errors
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'pwd: \tPrint working directory'
        print(short_help)

    def __help__(self):
        usage = '''Usage: pwd
    Print working directory

pwd      - To print the current working directory
pwd -v   - To print the version of the command
pwd help - To get this help screen
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None, *arg, **kwargs):
        self.ERRORS = Errors()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        elif args[0] == '':
            print(os.getcwd())

        else:
            self.ERRORS.command_not_found_help(args[0])
