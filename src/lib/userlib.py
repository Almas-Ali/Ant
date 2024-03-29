import os
import sys


class UserLib:
    '''Ant library maker class.'''

    def __init__(self):
        pass

    def __short_help__(self):
        short_help = 'help: \tTo get help for a command'
        print(short_help)

    def __help__(self):
        usage = '''Ant user library
version 1.0
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None, *arg, **kwargs):
        use = '''Congratulations!
Your library works!
'''
        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            print(use)

    def __repr__(self):
        return '<Ant Library Object>'


class SystemConfig:
    '''To get informations about current system.'''

    def __init__(self):
        pass

    def check_os(self):
        '''To check current os.'''

        if os.name == 'nt':
            return 'windows'
        elif os.name == 'posix':
            return 'linux'
        elif os.name == 'mac':
            return 'mac'
        else:
            return False

    def os_based_command(self, windows: str = None, linux: str = None, mac: str = None) -> str:
        '''To get command based on os.'''

        if self.check_os() == 'windows':
            return windows
        elif self.check_os() == 'linux':
            return linux
        elif self.check_os() == 'mac':
            return mac
        else:
            return False


class stdlib:
    '''Ant standard library class for input, output and error.'''

    def __init__(self):
        pass

    def write(self, text: str = None):
        '''To print text.'''
        sys.stdout.write(f'{text}\n')

    def read(self, text: str = None):
        '''To take input.'''
        sys.stdout.write(text)
        return sys.stdin.readline()

    def error(self, text: str = None):
        '''To print error.'''
        sys.stderr.write(f'{text}\n')
        # sys.exit(1)

    def __repr__(self):
        return '<Ant Operations Object>'

    def __str__(self):
        return '<Ant Operations Object>'

    def __len__(self):
        return 1
