import core
from config import profile
import argparse

'''Ant - An Interpreter'''


def main():
    shell = core.Shell(alias=profile['aliases'])
    shell.shell_history()
    shell.start()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version',
                        version=f'{core.__version__}')
    parser.add_argument('-c', '--command', help='Run a command')
    parser.add_argument('-s', '--script', help='Run a script')

    args = parser.parse_args()

    if args.command:
        try:
            _shell = core.Shell()
            _shell.execute(args.command)
        except Exception as e:
            print(e)

    elif args.script:
        _shell = core.Shell()
        with open(args.script, 'r') as _script:
            for line in _script.readlines():
                _shell.execute(line.strip())

    else:
        main()
