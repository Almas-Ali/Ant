from lib.userlib import UserLib


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
        if args[0] == 'help':
            self.__help__()

        elif args[0] == '':
            print('cat: error: file name required!')

        else:
            try:
                with open(args[0], 'r') as f:
                    f2 = [i.rstrip('\n') for i in f.readlines()]
                    for i in f2:
                        print(i)
            except:
                print(f'cat: error: {args[0]}: No such file or directory')
