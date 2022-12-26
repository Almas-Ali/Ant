'''
For permission error use this is linux os:
sudo setcap cap_net_raw+ep $(readlink -f $(which python))
'''

from userlib import UserLib
from pythonping import ping


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'ping: \tPing a host'
        print(short_help)

    def __help__(self):
        usage = '''Usage: ping
    To ping a host

ping <host> - To ping a host
ping -v     - To print the version of the command
ping help   - To get this help screen
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

        else:
            ping(args[0], verbose=True, timeout=2, interval=1, count=5)
