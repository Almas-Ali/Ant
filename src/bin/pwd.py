from userlib import UserLib
import os


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: pwd
    This use to get the current working directory.
'''
        print(usage)

    def run(self, args: list = None):
        
        if args[0] == 'help':
            self.__help__()

        else:
            print(os.getcwd())
