from userlib import UserLib
import time
import datetime


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'uptime: Print the uptime of the system'
        print(short_help)

    def __help__(self):
        usage = '''Usage: uptime
    Print the uptime of the system

uptime      - To print the uptime of the system
uptime -v   - To print the version of the command
uptime help - To get this help screen
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
            t = time.monotonic()
            _uptime = datetime.timedelta(seconds=t)
            print(f'UPTIME : {_uptime}')
