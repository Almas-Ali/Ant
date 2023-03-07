class Sanitizer:
    '''Sanitizer class for sanitizing user input and checking for errors in the input.'''

    def __init__(self) -> None:
        pass

    def __getitem__(self, index: int) -> str:
        '''Get the input from the shell.'''

        return self.sanitized_list[index]

    def __repr__(self) -> str:
        return '<Sanitizer Object>'

    def __str__(self) -> str:
        return '<Sanitizer Object>'

    def sanitize(self, input_: str) -> object:
        '''Sanitize the input from the shell.'''

        input_ = input_.strip()
        input_ = input_.replace('  ', ' ')
        input_ = input_.split(' ') 

        input_ = [i for i in input_ if i != ''] # Remove empty strings
        self.sanitized_list: list = input_

        return self

    def get_input(self) -> str:
        '''Get the input from the shell.'''

        return self.sanitized_list

    def get_command(self) -> str:
        '''Get the command from the input.'''

        try:
            command = self.sanitized_list[0]
            return command
        except:
            return ''

    def get_args(self) -> list:
        '''Get the arguments from the input.'''

        try:
            args = self.sanitized_list[1:]
            return args
        except:
            return []

    def get_args_by_index(self, exact: int = None, starting: int = None, end: int = None) -> list:
        '''Get the arguments from the input by index.'''

        if exact:
            try:
                self.sanitized_list[exact]
            except:
                return []

        elif starting and end:
            try:
                self.sanitized_list[starting:end]
            except:
                return []

        elif starting:
            try:
                self.sanitized_list[starting:]
            except:
                return []

        else:
            return []
