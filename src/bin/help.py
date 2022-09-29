from userlib import UserLib


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: help
    Make Directory command

help   - To get this help screen
'''
        print(usage)

    def run(self, args: list = None):

        self.__help__()

        
