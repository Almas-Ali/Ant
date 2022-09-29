from userlib import UserLib
import os


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: mkdir
    Make Directory command

mkdir       - Make directory command to create a directory
mkdir help  - To get this help screen
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        else:
            os.mkdir(args[0])
