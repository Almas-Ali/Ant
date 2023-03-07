from lib.userlib import UserLib
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'rmdir: \tRemove Directory command'
        print(short_help)

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

    def run(self, args: list = None, *arg, **kwargs):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        elif args[0] == '--sub':
            if args[1] == '':
                print('rmdir: error: file name required!')
                return
            if args[2] == '-f':
                inp = 'y'
            else:
                inp = input(
                    f'Are you sure you want to delete {args[1]} [y/n]: ')
                
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
            if args[0] == '':
                print('rmdir: error: file name required!')
            else:
                if args[1] == '-f':
                    inp = 'y'
                else:
                    inp = input(
                        f'Are you sure you want to delete {args[0]} [y/n]: ')

                if inp == 'y':
                    try:
                        os.rmdir(args[0])
                    except:
                        print('Error: Directory not found')
                else:
                    print('Execution terminated')
