from userlib import UserLib
import platform


class Exclusive(UserLib):

    def __help__(self):
        usage = '''usage: whoami
    A system checker utility
whoami      - To see user name
whoami -a   - To see full system information
whoami -v   - To see utility version number
whoami help - To see this help screen
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

        elif args[0] == '-a':
            sys_info = platform.uname()
            print(f'''\
            Username  : {sys_info.node}
            System    : {sys_info.system}
            Release   : {sys_info.release}
            Version   : {sys_info.version}
            Machine   : {sys_info.machine}
            Processor : {sys_info.processor}\
            ''')

        else:
            sys_info = platform.uname()
            print(sys_info.node)
