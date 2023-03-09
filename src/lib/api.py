'''
This file contains the API classes for using Ant as a backend with a GUI shell.

Usage:
    from lib.api import ANT_API

    ant = ANT_API() # This will load the config file and preloaded actions.
    
    ant.parser('ls') # This will execute the command.

    ant.script_parser('path/to/script.ant') # This will execute the script.

'''

from lib.core import Shell
from config import profile


class ANT_API:
    '''The main API class for Ant.'''

    def __init__(self) -> None:
        self.profile = profile
        self.shell = Shell(alias=self.profile['aliases'])

        for i in self.profile['preloaded_actions']:
            self.parser(i)

    def parser(self, command: str) -> None:
        '''This function parses a command and executes it.'''
        self.shell.execute(command)

    def script_parser(self, script: str) -> None:
        '''This function parses a script and executes it. It needs full path of the script file.'''
        self.shell.script_executer(script)

    def get_version(self) -> str:
        '''This function returns the version of Ant.'''
        return self.parser('version')
