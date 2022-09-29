from userlib import UserLib
import time
import datetime


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: uptime
    A uptime monitor of your system
uptime      - To see current uptime
uptime help - To see this help screen
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        else:
            t = time.monotonic()
            _uptime = datetime.timedelta(seconds=t)
            print(f'UPTIME : {_uptime}')
