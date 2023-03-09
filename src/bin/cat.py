from lib.userlib import UserLib, stdlib
from lib.backtrack import Errors
import os

print = stdlib().write  # Standard output


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'cat: \tConcatenate files and print on the standard output'
        print(short_help)

    def __help__(self):
        usage = '''Usage: cat
	Concatenate files and print on the standard output

cat <file> - To print the contents of a file
cat -v     - To print the version of the command
cat help   - To get this help screen
'''
        print(usage)

    def run(self, args: list = None, *arg, **kwargs):
        self.ERRORS = Errors()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '':
            # print('cat: error: file name required!')
            self.ERRORS.syntax_error('cat')

        else:
            if os.path.exists(args[0]):
                with open(args[0], 'r') as f:
                    f2 = [i.rstrip('\n') for i in f.readlines()]
                    for i in f2:
                        print(i)
            else:
                self.ERRORS.file_not_found('cat', args[0])
