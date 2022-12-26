import readline
import rlcompleter
import atexit
import os
from importlib import import_module, reload
import config
import glob

__version__ = '0.1.2'
profile = config.profile


class HistoryManager:
    '''History and autocomplete manager'''

    def __init__(self, commands) -> None:
        self.commands = commands

    @staticmethod
    def save(prev_h_len, histfile):
        '''History object saver'''
        new_h_len = readline.get_current_history_length()
        readline.set_history_length(2147483647)
        readline.append_history_file(new_h_len - prev_h_len, histfile)

    def completer1(self, text, state):
        '''Commands completer'''
        return [x for x in self.commands if x.startswith(text)][state]

    def completer2(self, text, state):
        '''Path and files completer'''
        return (glob.glob(text+'*')+[None])[state]


class Shell:
    '''Main shell class.'''

    def __init__(self, alias: dict = {}) -> None:
        self.vars: dict = {}
        self.alias = alias
        self.profile = profile

        # If history exists in path directory, Else create one.
        isHistoryExists = glob.glob(
            os.path.join(profile['path'], profile['history']))
        if isHistoryExists == []:
            with open(os.path.join(profile['path'], profile['history']), 'a') as history:
                history.write('')

    def __repr__(self):
        return '<Ant Object>'

    def start(self):
        self._GO: bool = True

        for i in self.profile['preloaded_actions']:
            self.execute(i)

        while self._GO:
            try:
                config = import_module('config')
                reload(config)
                profile = config.profile

                input_ = input(profile['prompt'])
                self.execute(input_)
                self.store_history(input_)

            except KeyboardInterrupt:
                # print('\nKeyboard interupt ! Type exit to exit.')
                print()

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

        # atexit.register(HistoryManager.save, h_len, histfile)
        # HistoryManager.store_history(histfile)

    def store_history(self, command: str):
        with open(os.path.join(profile['path'], profile['history']), 'a') as history:
            history.write(f'{command}\n')

    def execute(self, input_):
        input_ = input_.split(' ')

        if input_[0] == '':
            pass

        elif input_[0] == 'exit':
            print('exiting...')
            self._GO = False

        elif input_[0][0] == '$':
            try:
                data = ' '.join(input_)
                data = data.replace('$', '').strip().split('=')
                data = [j.strip() for j in data]

                if len(data[0].split(' ')) > 1:
                    print('Syntax error !')
                    return
                
                elif len(data) == 1:
                    print('Syntax error !')
                    return
                
                elif data[0] == '':
                    print('Syntax error !')
                    return

                # if len(data[1]) == 0:
                #     print('Syntax error !')
                #     return

                self.vars[data[0]] = data[1]

            except Exception as e:
                try:
                    print(self.vars[input_[0][1:]])
                except Exception as e:
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
                reload(import_module(f'bin.{input_[0]}'))
                file = getattr(import_module(
                    f'bin.{input_[0]}'), 'Exclusive')
                file = file()

                arg = input_[1:]
                # Manage empty args
                if arg == []:
                    arg.append('')

                file.run(args=arg, vars=self.vars,)

            except ImportError:
                try:
                    val = self.alias[input_[0]]
                    val = f"{val} {' '.join(input_[1:])}"
                    self.execute(val)
                except:
                    print(f'ant: \"{input_[0]}\" not found!')
