import os


def __help__():
    usage = '''Usage: pwd
This use to get the current working directory.
'''
    print(usage)


def main():
    print(os.getcwd())
