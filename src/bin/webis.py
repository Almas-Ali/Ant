
from userlib import UserLib
import whois


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: webis
    A website whois information collector utility.
webis -u URL  - To see whois information of particular website.
webis help - To see this help screen
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        elif args[0] == '-u':
            try:
                web = whois.query(args[1])
                for key, value in web.__dict__.items():
                    print(f'{key} : {value}')
            except Exception as e:
                # print('[!] Connection Error !')
                print(e)
        else:
            print('whois: error: check \'whois help\' for usage.')
