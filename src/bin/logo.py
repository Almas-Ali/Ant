from userlib import UserLib
import rong


class Exclusive(UserLib):

    def __short_help__(self):
        short_help = 'logo: \tPrint the logo of the shell'
        print(short_help)

    def __help__(self):
        usage = '''Usage: logo
    Print the logo of the shell

logo        - To print the logo of the shell
logo -v     - To get the version of the program
logo help   - To get this help screen
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

        elif args[0] == '':
            # ANT ascii art
            logo = f"""
                 _   
     /\         | |  
    /  \   _ __ | |_ 
   / /\ \ | '_ \| __|
  / ____ \| | | | |_ 
 /_/    \_\_| |_|\__|
"""
            logo = rong.Text(logo, fg="green", styles=['bold', 'blink'])
            logo.print()

        else:
            pass
