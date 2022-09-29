# Ant - An Interpreter

**version - 0.1.1**

## Introduction
It is developed in Python for any platform. The main perpose for making it is getting same user interface experience in multiple platforms.
<br/>

## Features

There is a huge internal library and external command access.

Internal librarys and short help:
- // comments
- cat 
- clear 
- echo 
- cmd \<any external command> 
- exit 
- head
- help 
- history
- ls
- mkdir
- ping \<domain/ip>
- pwd 
- rmdir
- set \<var = value> 
- version 

[+] and much more...
<br/>
type `help` to see all updated commands.
<br/>
**There is some more powerfull features like: Tab completion command, up/down arrow key history etc.**


## Installation

<br/>

    Windows:
        - Comming soon


<br/>

    Linux:
        - Comming soon

<br/>

    Mac:
        - Comming soon



## Create a command
If you want to create a custom command the use this template as reference:<br/>

```python
from userlib import UserLib


class Exclusive(UserLib):

    def __help__(self):
        usage = '''Usage: custom_command
    custom_command slogan

custom_command       - custom_command description
custom_command help  - To get this help screen
custom_command version
'''
        print(usage)

    def run(self, args: list = None):

        if args[0] == 'help':
            self.__help__()

        else:
            do_something_here

```
Now, save it as `<command_name>.py` into `bin/` folder.
<br/>
**Congratulations!** You have successfully created your very first ant command.


## Contribute
<!-- If you want to contribute then follow instructions in [Contributions](./CONTRIBUTIONS.md) -->
Help us to add more usefull commands by letting know in issue or add by pull request.


*Developed by - [Md. Almas Ali][1]* 

[1]: <https://github.com/Almas-Ali> "Md. Almas Ali" 