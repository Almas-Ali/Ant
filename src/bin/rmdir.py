from userlib import UserLib
import os


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: rmdir
    Remove Directory command

rmdir       - Remove directory command to remove a directory
rmdir --sub - Remove directory with all sub directory included
      -f    - Force remove directory without asking for confirmation
rmdir -v    - To get the version of the command
rmdir help  - To get this help screen
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

        elif args[0] == '--sub':
            inp = input(f'Are you sure you want to delete {args[1]} [y/n]: ')
            if inp == 'y':
                try:
                    os.removedirs(args[1])
                except:
                    print('Error: Directory not found')
            else:
                print('Execution terminated')

        elif args[0] == '--sub' and args[1] == '-f':
            try:
                os.removedirs(args[2])
            except:
                print('Error: Directory not found')

        else:
            os.rmdir(args[0])
