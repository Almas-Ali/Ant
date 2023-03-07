
class Errors:
    '''Ant errors class.'''

    def __init__(self) -> None:
        pass

    def command_not_found(self, command: str) -> None:
        print(f'Ant: {command}: command not found')

    def command_not_found_help(self, command: str) -> None:
        print(
            f'Ant: {command}: command not found. Try "help" for more information.'
        )

    def error(self, error: str) -> None:
        print(f'Ant: {error}')

    def error_help(self, error: str) -> None:
        print(f'Ant: {error}. Try "help" for more information.')

    def syntax_error(self, command: str) -> None:
        print(f'Ant: Syntax error')

