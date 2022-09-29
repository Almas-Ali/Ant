from userlib import UserLib


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: history
    To get all previously used commands.
history       - To get all ant history
history clear - To clear history file
history help  - To get this help screen
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == 'clear':
            with open('.history.ant', 'w') as history:
                history.write('')

        else:
            with open('.history.ant', 'r') as history:
                i = 0
                f2 = [i.rstrip('\n') for i in history.readlines()]
                for line in f2:
                    i += 1
                    print(f'{i}: {line}')
