from lib.userlib import UserLib
import re

class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'echo: \tPrint text to the screen'
        print(short_help)

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

    def run(self, args: list = None, *arg, **kwargs):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            try:
                # find all the variables
                variables = re.findall(r'\$[a-zA-Z0-9_]+', ' '.join(args))
                # replace the variables with their values
                for i in variables:
                    args = [j.replace(i, kwargs.get('vars')[i[1:]]) for j in args]
                print(' '.join(args))

            except Exception as e:
                print(' '.join(args))
