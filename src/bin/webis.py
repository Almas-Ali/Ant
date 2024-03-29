from lib.userlib import UserLib
import whois


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'webis: \tGet information about a website'
        print(short_help)

    def __help__(self):
        usage = '''Usage: webis
    Get information about a website

webis -u <url>  - To get information about a website
webis -v        - To get the version of the program
webis help      - To get this help screen
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

        elif args[0] == '-u':
            try:
                web = whois.query(args[1])
                for key, value in web.__dict__.items():
                    print(f'{key} : {value}')
            except Exception as e:
                # print(e)
                print('[!] Connection Error !')
        else:
            print('whois: error: check \'whois help\' for usage.')
