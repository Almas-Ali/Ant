'''
This file contains the API classes for using Ant as a backend with a GUI shell.

Usage:
    from lib.api import ANT_API

    ant = ANT_API() # This will load the config file and preloaded actions.
    
    ant.parser('ls') # This will execute the command.

    ant.script_parser('path/to/script.ant') # This will execute the script.

'''

from lib.core import Shell, __version__
from config import profile
import sys
import os
from pathlib import Path


# base ant directory path (Ant/src)
sys.path.append(
    os.path.dirname(Path(__file__).resolve().parent)
)


class ANT_API:
    '''The main API class for Ant.'''

    def __init__(self) -> None:
        self.profile = profile
        self.shell = Shell(alias=self.profile['aliases'])
        self.history = []

        for i in self.profile['preloaded_actions']:
            self.parser(i)

    def parser(self, command: str) -> None:
        '''This function parses a command and executes it.'''
        return self.shell.execute(command)

    def script_parser(self, script: str) -> None:
        '''This function parses a script and executes it. It needs full path of the script file.'''
        return self.shell.script_executer(script)

    def get_version(self) -> str:
        '''This function returns the version of Ant.'''
        return __version__

    def get_config(self) -> dict:
        '''This function returns the config of Ant.'''
        return self.profile

    def get_aliases(self) -> dict:
        '''This function returns the aliases of Ant.'''
        return self.profile['aliases']

    def start_shell(self) -> None:
        '''This function starts the interactive shell CLI.'''
        self.shell.start()

    def set_history(self, command: str) -> None:
        '''This function sets the history.'''
        self.shell.shell_history(command)

    def get_history(self) -> list:
        '''This function returns the histories.'''
        return self.parser('history')
