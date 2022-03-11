import os


def __help__():
    usage = '''Usage: cls
This helps to clear the terminal screen.
'''


def main():
    if os.name == 'nt':
        try:
            os.system('cls')
        except:
            pass
    else:
        os.system('clear')

