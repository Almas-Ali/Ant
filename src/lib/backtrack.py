from .userlib import stdlib


class Errors:
    '''Ant errors class.'''

    def __init__(self) -> None:
        self.output = stdlib().error

    def command_not_found(self, command: str) -> None:
        self.output(f'Ant: {command}: command not found!')

    def command_not_found_help(self, command: str) -> None:
        self.output(
            f'Ant: {command}: command not found. Try "help" for more information.'
        )

    def error(self, error: str) -> None:
        self.output(f'Ant: {error} error!')

    def error_help(self, error: str) -> None:
        self.output(f'Ant: {error}. Try "help" for more information.')

    def syntax_error(self, command: str) -> None:
        self.output(f'Ant: {command}: syntax error!')

    def undefined_error(self, command: str) -> None:
        self.output(f'Ant: \'${command}\' undefined!')
    
    def file_not_found(self, command: str, filename: str) -> None:
        self.output(f'Ant: {command}: \"{filename}\": No such file or directory!')

    def custom_error(self, command: str, text: str) -> None:
        self.output(f'Ant: {command}: {text}')
