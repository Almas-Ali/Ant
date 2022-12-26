class UserLib:
    '''Ant library maker class.'''

    def __init__(self):
        pass

    def __short_help__(self):
        short_help = 'help: \tTo get help for a command'
        print(short_help)

    def __help__(self):
        usage = '''Ant user library
version 1.0
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None, *arg, **kwargs):
        use = '''Congratulations!
Your library works!
'''
        if args[0] == 'help':
            self.__help__()
		
        elif args[0] == '-v':
            self.__version__()

        else:
            print(use)

    def __repr__(self):
        return '<Ant Library Object>'
