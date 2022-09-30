import readline
import rlcompleter
import atexit
import os
from importlib import import_module
from config import profile
import glob

__version__ = '0.1.1'


class HistoryManager:
    '''History and autocomplete manager'''

    def __init__(self, commands) -> None:
        self.commands = commands

    def save(prev_h_len, histfile):
        '''History object saver'''
        new_h_len = readline.get_current_history_length()
        readline.set_history_length(1000)
        readline.append_history_file(new_h_len - prev_h_len, histfile)

    def completer1(self, text, state):
        '''Commands completer'''
        return [x for x in self.commands if x.startswith(text)][state]

    def completer2(text, state):
        '''Path and files completer'''
        return (glob.glob(text+'*')+[None])[state]


class Shell:
    '''Main shell class.'''

    def __init__(self, alias: dict = {}) -> None:
        self.vars: dict = {}
        self.alias = alias

        # If history exists in path directory
        isHistoryExists = glob.glob(
            os.path.join(profile['path'], profile['history']))
        if isHistoryExists == []:
            with open(profile['history'], 'a') as history:
                history.write('')

    def __repr__(self):
        return '<Ant Object>'

    def start(self):
        self._GO: bool = True

        while self._GO:
            try:
                input_ = input(profile['prompt'])
                self.execute(input_)

            except KeyboardInterrupt:
                # print('\nKeyboard interupt ! Type exit to exit.')
                pass

    def shell_history(self):

        commands = glob.glob(os.path.join(profile['root'], 'bin/*.py'))
        commands = [x.replace(os.path.join(
            profile['root'], 'bin/'), '').replace('.py', '') for x in commands]

        readline.set_completer(HistoryManager(commands).completer1)
        # readline.set_completer(completer2)
        readline.set_completer_delims(' \t\n;')

        if 'libedit' in readline.__doc__:
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")

        histfile = os.path.join(profile['path'], profile['history'])

        try:
            readline.read_history_file(histfile)
            h_len = readline.get_current_history_length()
        except FileNotFoundError:
            open(histfile, 'w').close()
            h_len = 0

        atexit.register(HistoryManager.save, h_len, histfile)

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

        elif input_[0] == 'alias':
            try:
                data = ' '.join(input_)
                data = data.replace('alias', '').strip().split('=')
                data = [j.strip() for j in data]
                self.alias[data[0]] = data[1]
            except:
                for key, value in self.alias.items():
                    print(f'{key} = {value}')

        else:
            try:
                file = getattr(import_module(
                    f'bin.{input_[0]}'), 'Exclusive')
                file = file()

                arg = input_[1:]
                if arg == []:
                    arg.append('')
                file.run(args=arg)

            except ImportError:
                try:
                    val = self.alias[input_[0]]
                    val = f"{val} {' '.join(input_[1:])}"
                    self.execute(val)
                except:
                    print(f'ant: \"{input_[0]}\" not found!')
