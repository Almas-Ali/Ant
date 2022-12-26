# Ant - An Interpreter

**version - 0.1.2**

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Create a command](#create-a-command)
- [Ant CLI](#ant-cli)
- [Ant Script](#ant-script)
- [Ant Interpreter](#ant-interpreter)
- [Contribute](#contribute)



## Introduction
It is developed in Python for any platform. The main perpose for making it is getting same user interface experience in multiple platforms.
<br/>

## Features

There is a huge internal library and external command access. You can also create your own command and use it in Ant. It is very easy to create a command. Just follow the instruction below. [Create Your Own Command](#create-a-command)

Internal librarys and short help:
- alias 
- // comments 
- cat 
- clear 
- echo 
- chdir 
- cmd \<any external command> 
- exit 
- head 
- help 
- history 
- logo 
- ls 
- mkdir 
- ping \<domain/ip> 
- pwd 
- rmdir 
- $ \<$var = value> 
- uptime 
- version 
- webis 
- whoami 

[+] and much more...
<br/>
type `help` in the interactive shell to see all updated commands. 
<br/>
**There is some more powerfull features like: Tab completion command, up/down arrow key history etc.**
<br/>
***Also some ester eggs are hidden in it. Try to find them.*** 😀 


## Installation

Installation is not ready yet! But you can clone this repo and run it from source code. Follow the instructions below:


```bash
# Clone this repo
git clone

# Go to ant source folder
cd ant/src

# Run ant.py
python3 ant.py

# Use ant -h to get help about Ant CLI
python3 ant.py -h
```


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

    def __short_help__(self):
        short_help = 'help: \tTo get help for a command'
        print(short_help)

    def __help__(self):
        usage = '''Ant user library
version 1.0
'''
        print(usage)

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


## Ant Interpreter
Ant Interpreter is a python script. You can run it from your terminal by typing `python3 ant.py` or `python ant.py`
<br><br>
Use `ant.py -h` to get help for Ant Interpreter.


## Ant CLI
Ant CLI is here. Now you can use Ant from your native terminal. Just type `ant -c <command>` to run any Ant command from your terminal. Use `ant -s <script>` to run any Ant script from your terminal.
<br><br>
Use `ant -h` to get help for Ant cli.


## Ant Script
Ant script is a file with `.ant` extension. It is a simple text file with Ant commands. You can run Ant script from Ant CLI or Ant Interpreter.


## Contribute
<!-- If you want to contribute then follow instructions in [Contributions](./CONTRIBUTIONS.md) -->
Help us to add more usefull commands by letting know in issue or add by pull request.


*Developed by - [Md. Almas Ali][1]* 

[1]: <https://github.com/Almas-Ali> "Md. Almas Ali" 