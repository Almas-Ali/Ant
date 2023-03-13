import rlcompleter
import atexit
import os
from importlib import import_module, reload
from .. import config
import glob
import sys
import subprocess
from .backtrack import Errors
from .sanitizer import Sanitizer

try:
    import readline
except:
    from pyreadline3 import Readline
    readline = Readline()

__version__ = '0.2.0'
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
        self.ERRORS = Errors()
        self.SANITIZER = Sanitizer()
        # sys.path = []

        self.define_default_vars()  # Setting default variables
        self.shell_history()  # Setting shell history

        # If history exists in path directory, Else create one.
        isHistoryExists = glob.glob(
            os.path.join(profile['HOME_PATH'], profile['history']))
        if isHistoryExists == []:
            with open(os.path.join(profile['HOME_PATH'], profile['history']), 'a') as history:
                history.write('')

    def __repr__(self):
        return '<Ant Object>'

    def define_default_vars(self):
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
        self.vars['ANT_PATH'] = ', '.join(
            list(map(lambda x: f'\'{x}\'', profile['ANT_PATH'])))
        self.vars['SYSTEM_PATH'] = ', '.join(
            list(map(lambda x: f'\'{x}\'', profile['SYSTEM_PATH'])))
        self.vars['BASE_DIR'] = profile['BASE_DIR']
        self.vars['ANT_VERSION'] = __version__

        return self

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

            except KeyboardInterrupt:
                # print('\nKeyboard interupt ! Type exit to exit.')
                print()

    def shell_history(self):

        commands = glob.glob(os.path.join(profile['BASE_DIR'], 'bin/*.py'))
        commands = [x.replace(os.path.join(
            profile['BASE_DIR'], 'bin/'), '').replace('.py', '') for x in commands]
        commands.extend(self.alias.keys())
        commands.remove('__init__')

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
        '''Main execution function'''

        input_ = self.SANITIZER.sanitize(input_)

        if input_.get_command() == '':
            pass

        elif input_.get_command() == 'exit':
            self._GO = False
            print('exiting...')

        elif input_.get_command()[0] == '$':
            try:
                data = ' '.join(input_)
                data = data.replace('$', '').strip().split('=')
                data = [j.strip() for j in data]

                if data[0] == '':
                    self.ERRORS.syntax_error(input_[1:])
                    return

                if data[1] == '':
                    self.ERRORS.syntax_error(input_[1:])
                    return

                # if len(data) == 1:
                #     self.ERRORS.syntax_error(input_[1:])
                #     return

                try:
                    _out = self.execute(self.vars[data[1]])
                    self.vars[data[0]] = _out
                except Exception as e:
                    self.vars[data[0]] = data[1]

            except Exception as e:
                try:
                    print(self.vars[input_.get_command()[1:]])
                except Exception as e:
                    # print(f'\"{input_.get_command()[1:]}\" undefined !')
                    self.ERRORS.undefined_error(input_.get_command()[1:])

        # elif input_.get_command() == 'varlist':
        #     for i in self.vars:
        #         print(f'{i} = \t{self.vars[i]}')

        # elif input_.get_command() == 'varclear':
        #     self.vars = {}

        elif input_.get_command() == 'read':
            # input_ = [i for i in input_ if i != '']
            try:
                if input_[1] == '' or input_[2] == '':
                    self.ERRORS.syntax_error(input_.get_args())
                    return

                if len(input_.get_args()) > 2:
                    self.ERRORS.syntax_error(input_.get_args())
                    return

                if input_[1][0] == '$':
                    try:
                        self.vars[input_[1][1:]] = input(input_[2])
                    except:
                        self.ERRORS.syntax_error(input_.get_args())
                        return
                else:
                    self.ERRORS.syntax_error(input_.get_args())

            except Exception as e:
                # print(e)
                self.ERRORS.syntax_error(input_.get_args())

        elif input_.get_command() == 'version':
            if input_.get_args() == ['']:
                print(__version__)
            else:
                self.ERRORS.syntax_error(input_.get_args())

        elif input_.get_command()[0:2] == '//' or input_.get_command()[0] == '#':
            pass

        elif input_.get_command() == 'alias':
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
                        file = import_module(f'bin.{input_.get_command()}')
                        reload(file)
                        file = getattr(file, 'Exclusive')
                        file = file()

                        arg = input_.get_args()

                        file.run(
                            args=arg,
                            vars=self.vars,
                            profile=self.profile
                        )

                    except Exception as e:
                        print(e)
                        val = self.alias[input_.get_command()]
                        val = f"{val} {' '.join(input_.get_args())}"
                        self.execute(val)

                except Exception as e:
                    # print(e)
                    if self.vars.get('only_internals', False):
                        self.ERRORS.command_not_found(input_.get_command())
                        return

                    # If not found in self.ANT_PATH, try to call system commands from self.SYSTEM_PATH
                    for __index, __path in enumerate(self.SYSTEM_PATH):
                        success, fail = subprocess.Popen(
                            f'{__path}/{" ".join(input_)}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

                        if success.decode('utf-8') != '':
                            print(success.decode('utf-8'))
                            break

                        if len(self.SYSTEM_PATH) - 1 == __index:
                            if fail.decode('utf-8') != '':
                                raise # Exception(fail.decode('utf-8'))

            except Exception as e:
                # print(e)
                self.ERRORS.command_not_found(input_.get_command())
