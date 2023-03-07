from lib.userlib import UserLib
import glob


class Exclusive(UserLib):

    def __short_help__(self) -> None:
        short_help = 'where: \tTo get the where of a command lives'
        print(short_help)

    def __help__(self) -> None:
        usage = '''Usage: where
    Get the where of a command lives

where <command> - To get the where of a command lives
where -v        - To print the version of the command
where help      - To get this help screen
'''
        print(usage)

    def __version__(self) -> None:
        ver = 'version 1.0'
        print(ver)

    def path_display(self, path: list) -> None:
        '''
        This function is used to display the path of the file in a better way than the default one.
        '''
        if len(path) == 1:
            return f'\'{path[0]}\''
        else:
            return f'\'{path[0]}\',\n' + self.path_display(path[1:])

    def is_in_ant_command(self, command: str, path: list) -> bool:
        _file: list = []

        for i in path:
            files = glob.glob(f'{i}/{command}.*')
            if files != []:
                _file.extend(files)
            else:
                continue
        else:
            if _file != []:
                return self.path_display(_file)
            else:
                return False

    def is_in_system_command(self, command: str, path: list) -> bool:
        _file: list = []

        for i in path:
            files = glob.glob(f'{i}/{command}')
            if files != []:
                _file.extend(files)
            else:
                continue
        else:
            if _file != []:
                return self.path_display(_file)
            else:
                return False

    def is_in_current_dir(self, command: str) -> bool:
        _file: list = []

        files = glob.glob(f'{command}')
        if files != []:
            _file.extend(files)
        else:
            return False

        if _file != []:
            return self.path_display(_file)
        else:
            return False

    def run(self, args: list = None, *arg, **kwargs) -> None:

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            try:

                if args[0] == '':  # if the command is empty
                    print('Syntax error !')

                elif args[0][0] == '$':  # if the command is a variable
                    print('Variable')

                # if the command is a alias
                elif args[0] in kwargs.get('profile').get('aliases').keys():
                    print(f'Aliases: \'{args[0]}\' -> \'' + kwargs.get('profile').get('aliases').get(args[0]) + '\'')

                # if the command is a ant command
                elif self.is_in_ant_command(args[0], kwargs.get('profile').get('ANT_PATH')) != False:
                    print(self.is_in_ant_command(
                        args[0], kwargs.get('profile').get('ANT_PATH')))

                # if the command is a system command
                elif self.is_in_system_command(args[0], kwargs.get('profile').get('SYSTEM_PATH')) != False:
                    print(self.is_in_system_command(
                        args[0], kwargs.get('profile').get('SYSTEM_PATH')))

                # if the command is a command in the current directory
                elif self.is_in_current_dir(args[0]) != False:
                    print(self.is_in_current_dir(args[0]))

                else:
                    print('unidentified command')
            except Exception as e:
                print(e)
