from userlib import UserLib
import os


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: rmdir
    Remove Directory command

rmdir       - Remove directory command to remove a directory
rmdir help  - To get this help screen
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        else:
            os.rmdir(args[0])
