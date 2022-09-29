from userlib import UserLib
import os


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: cls
    This helps to clear the terminal screen.
'''
        print(usage)

    def run(self, args: list = None):
        
        if args[0] == 'help':
            self.__help__()

        elif os.name == 'nt':
            try:
                os.system('cls')
            except:
                pass

        else:
            os.system('clear')
