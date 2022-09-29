from userlib import UserLib
import os


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: cmd
You can execute commands of cmd with this keyword.
'''
        print(usage)

    def run(self, args: list = None):
        if args[0] == 'help':
            self.__help__()
        else:
            os.system(' '.join(args))
