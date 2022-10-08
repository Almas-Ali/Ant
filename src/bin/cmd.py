from userlib import UserLib
import os


class Exclusive(UserLib):

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

    def run(self, args: list = None):
        if args[0] == 'help':
            self.__help__()
        
        elif args[0] == '-v':
            self.__version__()

        else:
            os.system(' '.join(args))
