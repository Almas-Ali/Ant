from lib.userlib import UserLib
from lib.backtrack import Errors


class Exclusive(UserLib):

    def __short_help__(self) -> None:
        short_help = 'var: \tTo manipulate the variables of the shell'
        print(short_help)

    def __help__(self) -> None:
        usage = '''Usage: var
    Get the var of a command

var list      - To list all the variables
var clear     - To clear all the variables
var remove    - To remove a variable
var -v        - To print the version of the command
var help      - To get this help screen
'''
        print(usage)

    def __version__(self) -> None:
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None, *arg, **kwargs) -> None:
        self.ERROR = Errors()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            if args[0] == 'list':
                print('Variables: ')
                print('-'*30)
                for key, value in kwargs['vars'].items():
                    print(f'\'{key}\' \b\b\b\t\t-> \'{value}\'')

            elif args[0] == 'clear':
                kwargs['vars'] = {}

            elif args[0] == 'remove':
                try:
                    del kwargs['vars'][args[1]]
                except:
                    print(f'Variable \'{args[1]}\' not found!')

            else:
                print('Invalid argument!')
