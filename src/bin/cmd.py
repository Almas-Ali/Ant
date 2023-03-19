from lib.userlib import UserLib
from lib.backtrack import Errors
import subprocess


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
        self.ERRORS = Errors()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            if args == ['']:
                self.__help__()
                return
            
            process = subprocess.Popen(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )

            for line in process.stdout:
                print(line, end='')
            for line in process.stderr:
                self.ERRORS.os_command_not_found(process.stderr)

            # args = ' '.join(args)
            # stdout, stderr = subprocess.Popen(
            #     args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
            # ).communicate()

            # if stdout.decode('utf-8') != '':
            #     print(stdout.decode('utf-8'))
                
            # else:
            #     self.ERRORS.command_not_found(stderr.decode('utf-8'))
