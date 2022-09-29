from userlib import UserLib

class Exclusive(UserLib):
    def __help__(self):
        usage = '''Usage: echo strings
	This helps to print a data in terminal.
'''
        print(usage)


    def main(self, args:list=None):
        if args[0] == 'help':
    	    self.__help__()
        else:
    	    print(' '.join(args))
