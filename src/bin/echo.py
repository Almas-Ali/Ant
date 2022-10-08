from userlib import UserLib


class Exclusive(UserLib):
    def __help__(self):
        usage = '''Usage: echo <text>
    Print text to the screen

echo <text> - To print text to the screen
echo -v     - To print the version of the command
echo help   - To get this help screen
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
            print(' '.join(args))
