from lib.userlib import UserLib
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'cmd: \tExecute a command in the shell'
        print(short_help)

    def __help__(self):
        usage = '''Usage: cmd
    Execute a command in the shell

cmd <command> - To execute a command
cmd -v        - To print the version of the command
cmd help      - To get this help screen
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
            try:
                os.system(' '.join(args))
            except:
                print('cmd: error: command not found')
