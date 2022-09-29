'''
For permission error use this is linux os:
sudo setcap cap_net_raw+ep $(readlink -f $(which python))
'''

from userlib import UserLib
from pythonping import ping


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: ping
    To ping any website or ip addresses.
It's only supports single ping at a time. Multi-threading is not supported yet.

ping DOMAIN - To get response from server
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        else:
            ping(args[0], verbose=True, timeout=2, interval=1, count=5)
