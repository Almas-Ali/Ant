import os
import platform
from importlib import import_module


class color:
    '''Related colors.'''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Shell:
    '''Main shell class.'''

    def __init__(self) -> None:
        self.vars = {}

    def __repr__(self):
        return '<Ant Object>'

    def start(self):
        self._GO: bool = True
        path = os.getcwd()
        user = platform.uname().node

        while self._GO:
            try:
                input_ = input(
                    f'{color.OKGREEN + user} @ {path + color.ENDC} \n>>> ')

                self.execute(input_)

            except KeyboardInterrupt:
                print('\nKeyboard interupt ! Type exit to exit.')

    def get_input(self):
        pass

    def execute(self, input_):
        input_ = input_.split(' ')

        if input_[0] == 'exit':
            print('exiting...')
            self._GO = False

        else:
            if input_[0] == 'set':
                try:
                    data = ' '.join(input_)
                    data = data.replace('set', '').strip().split('=')
                    data = [j.strip() for j in data]
                    print(data)
                    self.vars[data[0]] = data[1]
                except:
                    print('[!] Invalid Syntax')
            elif input_[0][0] == '$':
                print(self.vars)
                try:
                    print(self.vars[input_[0][1:]])
                except:
                    print(f'\"{input_[0][1:]}\" undefined !')
            else:
                try:
                    file = import_module(f'bin.{input_[0]}')
                    if file.__name__ == 'bin.cmd':
                        if input_[1] == 'help':
                            file.__help__()
                        elif len(input_) > 1:
                            file.main(' '.join(input_[1:]))
                        else:
                            file.main('cmd')
                    elif len(input_) > 1:
                        if input_[1] == 'help':
                            file.__help__()
                    else:
                        file.main()

                except ImportError:
                    print(f'\"{input_[0]}\" command not exist !')
