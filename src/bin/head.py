from userlib import UserLib


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: head
	To get spacific lines from a text file.

head FILE  - To read a file in terminal
head help - To see this help screen
'''
        print(usage)

    def run(self, args: list = None):
        if args[0] == 'help':
            self.__help__()

        elif args[0] == '':
            print('head: error: file name required!')

        elif args[1] == '-n':
            try:
                with open(args[0], 'r') as f:
                    f2 = [i.rstrip('\n') for i in f.readlines()][0:int(args[2])]
                    for i in f2:
                        print(i)
            except Exception as e:
                print('head: error: \'-n\' has no line value')
        else:
            with open(args[0], 'r') as f:
                f2 = [i.rstrip('\n') for i in f.readlines()][0:5]
                for i in f2:
                    print(i)
