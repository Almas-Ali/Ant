import core
from config import profile

'''Ant - An Interpreter'''


def main():
    shell = core.Shell(alias=profile['aliases'])
    shell.shell_history()
    shell.start()


if __name__ == '__main__':
    main()
