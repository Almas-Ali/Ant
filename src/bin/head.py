from userlib import UserLib


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'head: \tPrint first 5 lines of a file'
        print(short_help)

    def __help__(self):
        usage = '''Usage: head
    Print first 5 lines of a file

head <file> - To print first 5 lines of a file
head <file> -n <number> - To print first <number> lines of a file
head -v     - To print the version of the command
head help   - To get this help screen
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None):
        if args[0] == 'help':
            self.__help__()

        elif args[0] == '':
            print('head: error: file name required!')

        elif args[0] == '-v':
            self.__version__()

        elif args[1] == '-n':
            try:
                with open(args[0], 'r') as f:
                    f2 = [i.rstrip('\n')
                          for i in f.readlines()][0:int(args[2])]
                    for i in f2:
                        print(i)
            except Exception as e:
                print('head: error: \'-n\' has no line value')
        else:
            with open(args[0], 'r') as f:
                f2 = [i.rstrip('\n') for i in f.readlines()][0:5]
                for i in f2:
                    print(i)
