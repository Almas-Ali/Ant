from lib.userlib import UserLib, SystemConfig
import os


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'shutdown: Shutdown the system'
        print(short_help)

    def __help__(self):
        usage = '''Usage: shutdown
    Shutdown the system

shutdown             - To shutdown the system. Default delay 60sec
shutdown now         - To shutdown the system immediately
shutdown -r          - To restart the system
shutdown -s -t <sec> - To shutdown the system after <sec> seconds
shutdown -r -t <sec> - To restart the system after <sec> seconds
shutdown -a          - To abort the shutdown
shutdown -v          - To get the version of the program
shutdown help        - To get this help screen
'''
        print(usage)

    def __version__(self):
        ver = 'version 1.0'
        print(ver)

    def run(self, args: list = None, *arg, **kwargs):
        _sys = SystemConfig()

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-v':
            self.__version__()

        elif args[0] == '':
            os_ = _sys.os_based_command(
                windows='shutdown -s -t 60',
                linux='shutdown -h 60',
                mac='shutdown -h 60'
            )
            os.system(os_)

        elif args[0] == 'now': # shutdown now
            os_ = _sys.os_based_command(
                windows='shutdown -s -t 0',
                linux='shutdown -h 0',
                mac='shutdown -h 0'
            )
            os.system(os_)

        elif args[0] == '-r': # shutdown -r
            os_ = _sys.os_based_command(
                windows='shutdown -r -t 60',
                linux='shutdown -r 60',
                mac='shutdown -r 60'
            )
            os.system(os_)

        elif args[0] == '-s' and args[1] == '-t': # shutdown -s -t <sec>
            os_ = _sys.os_based_command(
                windows=f'shutdown -s -t {args[2]}',
                linux=f'shutdown -h {args[2]}',
                mac=f'shutdown -h {args[2]}'
            )
            os.system(os_)

        elif args[0] == '-r' and args[1] == '-t': # shutdown -r -t <sec>
            os_ = _sys.os_based_command(
                windows=f'shutdown -r -t {args[2]}',
                linux=f'shutdown -r {args[2]}',
                mac=f'shutdown -r {args[2]}'
            )
            os.system(os_)

        elif args[0] == '-a': # shutdown -a
            os_ = _sys.os_based_command(
                windows='shutdown -a',
                linux='shutdown -c',
                mac='shutdown -c'
            )
            os.system(os_)

        else:
            print('shutdown: error: check \'shutdown help\' for usage.')
