import rlcompleter
import atexit
import os
from importlib import import_module, reload
import config
import glob
import sys
import subprocess
try:
    import readline
except:
    from pyreadline3 import Readline
    readline = Readline()

__version__ = '0.1.3'
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
        self.alias: dict = alias
        self.profile: dict = profile
        self.SYSTEM_PATH: list = []
        # sys.path = []

        # Is paths exists from path variables in config.py
        # sys.path = []
        for i in profile['ANT_PATH']:
            if not os.path.exists(i):
                print(f'Path {i} not found !')
            else:
                # self.ANT_PATH.append(i)
                sys.path.insert(0, i)
                # print(sys.path)

        for i in profile['SYSTEM_PATH']:
            if not os.path.exists(i):
                print(f'Path {i} not found !')
            else:
                self.SYSTEM_PATH.append(i)

        # Setting default variables
        self.vars['HOME'] = profile['HOME_PATH']
        self.vars['ANT_PATH'] = ', '.join(list(map(lambda x: f'\'{x}\'', profile['ANT_PATH'])))
        self.vars['SYSTEM_PATH'] = ', '.join(list(map(lambda x: f'\'{x}\'', profile['SYSTEM_PATH'])))
        self.vars['BASE_DIR'] = profile['BASE_DIR']
        self.vars['ANT_VERSION'] = __version__

        # If history exists in path directory, Else create one.
        isHistoryExists = glob.glob(
            os.path.join(profile['HOME_PATH'], profile['history']))
        if isHistoryExists == []:
            with open(os.path.join(profile['HOME_PATH'], profile['history']), 'a') as history:
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

                input_ = input(profile['PROMPT'])
                self.execute(input_)
                self.store_history(input_)
                print()
                
            except KeyboardInterrupt:
                # print('\nKeyboard interupt ! Type exit to exit.')
                print()

    def shell_history(self):

        commands = glob.glob(os.path.join(profile['BASE_DIR'], 'bin/*.py'))
        commands = [x.replace(os.path.join(
            profile['BASE_DIR'], 'bin/'), '').replace('.py', '') for x in commands]

        readline.set_completer(HistoryManager(commands).completer1)
        # readline.set_completer(completer2)
        readline.set_completer_delims(' \t\n;')

        if 'libedit' in readline.__doc__:
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")

        histfile = os.path.join(profile['HOME_PATH'], profile['history'])

        try:
            readline.read_history_file(histfile)
            h_len = readline.get_current_history_length()
        except FileNotFoundError:
            open(histfile, 'w').close()
            h_len = 0

        # atexit.register(HistoryManager.save, h_len, histfile)
        # HistoryManager.store_history(histfile)

    def store_history(self, command: str):
        with open(os.path.join(profile['HOME_PATH'], profile['history']), 'a') as history:
            history.write(f'{command}\n')

    def script_executer(self, script: str):
        self.lines = 0
        with open(script, 'r') as _script:
            for line in _script.readlines():
                self.lines += 1
                self.execute(line.strip())

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

                if data[0] == '':
                    print('Syntax error !')
                    return

                if data[1] == '':
                    print('Syntax error !')
                    return

                if len(data) == 1:
                    print('Syntax error !')
                    return

                try:
                    _out = self.execute(self.vars[data[1]])
                    self.vars[data[0]] = _out
                except Exception as e:
                    self.vars[data[0]] = data[1]

            except Exception as e:
                try:
                    print(self.vars[input_[0][1:]])
                except Exception as e:
                    print(f'\"{input_[0][1:]}\" undefined !')

        elif input_[0] == 'varlist':
            for i in self.vars:
                print(f'{i} = \t{self.vars[i]}')

        elif input_[0] == 'varclear':
            self.vars = {}

        elif input_[0] == 'read':
            input_ = [i for i in input_ if i != '']
            try:
                if input_[1] == '' or input_[2] == '':
                    print('Syntax error !')
                    return

                if len(input_[1:]) > 2:
                    print('Syntax error !')
                    return

                if input_[1][0] == '$':
                    try:
                        self.vars[input_[1][1:]] = input(input_[2])
                    except:
                        print('Syntax error !')
                        return
                else:
                    print('Syntax error !')
            except Exception as e:
                print(e)
                print('Syntax error !')

        elif input_[0] == 'version':
            print(__version__)

        elif input_[0][0:2] == '//' or input_[0][0] == '#':
            pass

        elif input_[0] == 'alias':
            try:
                data = ' '.join(input_)
                data = data.replace('alias', '').strip().split('=')
                data = [j.strip() for j in data]
                self.alias[data[0]] = data[1]
            except:
                print('Aliases: ')
                print('-'*30)
                for key, value in self.alias.items():
                    print(f'\'{key}\' \b\b\b\t\t-> \'{value}\'')

        else:
            # Try to call commands from self.ANT_PATH else from aliases else from system commands from self.SYSTEM_PATH else throw error !
            try:
                try:
                    try:
                        # get modules from python path and reload them to get the latest changes
                        file = import_module(f'{input_[0]}')
                        reload(file)
                        file = getattr(file, 'Exclusive')
                        file = file()

                        arg = input_[1:]
                        # Manage empty args
                        if arg == []:
                            arg.append('')

                        file.run(args=arg, vars=self.vars, profile=self.profile)

                    except:
                        val = self.alias[input_[0]]
                        val = f"{val} {' '.join(input_[1:])}"
                        self.execute(val)

                except:
                    # If not found in self.ANT_PATH, try to call system commands from self.SYSTEM_PATH
                    for h, i in enumerate(self.SYSTEM_PATH):
                        success, fail = subprocess.Popen(
                            f'{i}/{" ".join(input_)}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

                        if success.decode('utf-8') != '':
                            print(success.decode('utf-8'))
                            break

                        if len(self.SYSTEM_PATH) - 1 == h:
                            break

            except Exception as e:
                print(e)
                print(f'ant: \"{input_[0]}\" not found!')
