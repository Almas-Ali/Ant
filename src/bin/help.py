from userlib import UserLib
from core import Shell
import glob
from importlib import import_module
from core import profile
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

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '':
            lists_ = glob.glob1(os.path.join(profile['root'], 'bin'), '*.py')
            print(lists_)
            lists_ = [i.replace('.py', '') for i in lists_]
            # lists_.remove('__init__')

            print(
                f'Welcome to Ant Interpreter (version {import_module("core").__version__})')
            print('Available commands are: ')
            for i in lists_:
                import_module(f'bin.{i}').Exclusive().__short_help__()

            print('''
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
                print('Error: Command not found')

        # else:
        #     self.__help__()
