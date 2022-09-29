from userlib import UserLib
import glob


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: ls
To get all directors and file of current location.

ls       - Everything in current folder
ls -f    - All files in current folder
ls help  - To get this help screen
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-f':
            l = glob.glob('*.*')
            print(' '.join(l))

        else:
            l = glob.glob('*')
            print(' '.join(l))
