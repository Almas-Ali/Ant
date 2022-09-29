import os
from importlib import import_module
from config import profile

__version__ = '0.0.1'


class Shell:
    '''Main shell class.'''

    def __init__(self) -> None:
        self.vars: dict = {}

    def __repr__(self):
        return '<Ant Object>'

    def start(self):
        self._GO: bool = True

        while self._GO:
            try:
                input_ = input(profile['prompt'])
                with open('.history', 'a') as history:
                    history.writelines(input_+'\n')
                self.execute(input_)

            except KeyboardInterrupt:
                print('\nKeyboard interupt ! Type exit to exit.')

    def get_input(self):
        pass

    def execute(self, input_):
        input_ = input_.split(' ')

        if input_[0] == '':
            pass

        elif input_[0] == 'exit':
            print('exiting...')
            self._GO = False

        elif input_[0] == 'set':
            try:
                data = ' '.join(input_)
                data = data.replace('set', '').strip().split('=')
                data = [j.strip() for j in data]
                self.vars[data[0]] = data[1]
            except:
                print('[!] Invalid Syntax')

        elif input_[0][0] == '$':
            try:
                print(self.vars[input_[0][1:]])
            except:
                print(f'\"{input_[0][1:]}\" undefined !')

        elif input_[0] == 'version':
            print(__version__)

        elif input_[0][0:2] == '//':
            pass

        else:
            try:
                file = getattr(import_module(
                    f'bin.{input_[0]}'), 'Exclusive')
                file = file()

                try:
                    arg = input_[1:]
                    if arg == []:
                        arg.append('')
                    file.run(args=arg)
                    
                except Exception as e:
                    print('error: import 1 line')
                    print(e)

            except ImportError:
                print(f'ant: \"{input_[0]}\" not found!')
