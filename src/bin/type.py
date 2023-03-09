from lib.userlib import UserLib
from lib.backtrack import Errors
from importlib import import_module
import subprocess


class Exclusive(UserLib):

    def __short_help__(self) -> None:
        short_help = 'type: \tTo get the type of a command'
        print(short_help)

    def __help__(self) -> None:
        usage = '''Usage: type
    Get the type of a command

type <command> - To get the type of a command
type -v        - To print the version of the command
type help      - To get this help screen
'''
        print(usage)

    def __version__(self) -> None:
        ver = 'version 1.0'
        print(ver)

    def is_ant_command(self, command: str) -> bool:
        try:
            import_module(command)
            return True
        except:
            return False

    def is_system_command(self, command: str) -> bool:
        try:
            success, error = subprocess.Popen(
                command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            if error == b'':
                return True
            else:
                return False
        except:
            return False

    def run(self, args: list = None, *arg, **kwargs) -> None:
        self.ERRORS = Errors()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            # Get the type of command is it a system command or a ant command or a alias or a variable or a script or a file or a directory or a unidentified command

            if args[0] == '':  # if the command is empty
                self.ERRORS.command_not_found_help('type')

            elif args[0][0] == '$':  # if the command is a variable
                print('Variable')

            # if the command is a alias
            elif args[0] in kwargs.get('profile').get('aliases').keys():
                print('Aliases')

            # if the command is a ant command
            elif self.is_ant_command(args[0]):
                print('Ant command')

            # if the command is a system command
            elif self.is_system_command(args[0]):
                print('System command')

            else:
                print('Unidentified command')
