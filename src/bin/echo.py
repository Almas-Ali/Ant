from lib.userlib import UserLib
from lib.backtrack import Errors
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
        self.ERRORS = Errors()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        else:
            # args: str = ' '.join(args)
            # Here we will always deal with args[0] as a string. We won't take any other arguments.
            # check the string have quotes or not
            # if args.startswith('"') and args.endswith('"'):
            #     ...

            # find all the variables
            variables = re.findall(r'\$[a-zA-Z0-9_]+', ' '.join(args))

            # replace the variables with their values
            for i in variables:
                if i[1:] in kwargs.get('vars'):
                    args = [j.replace(i, kwargs.get('vars')[i[1:]])
                            for j in args]
                else:
                    self.ERRORS.undefined_error(i[1:])

            # Replace the string quotes
            # args = [i.replace('"', '').replace("'", '') for i in args]

            # A line break \n in anywhere in this string will be replaced with a break line
            print(' '.join(args).replace('\\n', '\n'))
