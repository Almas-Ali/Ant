from lib.userlib import UserLib
from lib.core import Shell, profile
from lib.backtrack import Errors
import glob
from importlib import import_module
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'help: \tTo get help for a command'
        print(short_help)

    def __help__(self):
        usage = '''Usage: help
    Help command

help            - To get this help screen
help <command>  - To get help for a specific command
help -v         - To print the version of the command
help help       - To get this help screen
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None, *arg, **kwargs):
        self.ERRORS = Errors()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '':
            # Listing all the commands in the bin directory and getting their short help
            # Getting all the files in the bin directory
            lists_ = glob.glob1(os.path.join(
                profile['BASE_DIR'], 'bin'), '*.py')
            lists_ = [i.replace('.py', '')
                      for i in lists_]  # Removing the .py extension
            lists_.remove('__init__')  # Removing the __init__.py file

            print(
                f'Welcome to Ant Interpreter (version {import_module("lib.core").__version__})\n')
            print('Available commands are: ')

            for i in lists_:
                import_module(f'bin.{i}').Exclusive().__short_help__()

            print('''
Type $<variable> = <value> to set a variable and $<variable> to get the value of a variable
Type \'help <command>\' to get help for a specific command
Type \'exit\' to exit the interpreter
''')

        elif args[0] == '-v':
            self.__version__()

        else:
            try:
                s = Shell()
                s.execute(args[0] + ' help')
            except:
                self.ERRORS.command_not_found_help(args[0])

        # else:
        #     self.__help__()
