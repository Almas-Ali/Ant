import os

def __help__():
    usage = '''Usage: cmd
You can execute commands of cmd with this keyword.
'''
    print(usage)


def main(cmd):
    os.system(cmd)
