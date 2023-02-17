# Ant - An Interpreter

**version - 0.1.3**

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Super Global Variables](#super-global-variables)
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

Internal libraries and short help:
<details>
<summary><strong>alias</strong></summary>

## alias - Alias Command

**Usage:** alias \<alias_name> = \<command>

**Example:** `alias dir = ls`

**Description:** alias command is used to create alias for any command. It is very usefull when you want to create alias for a long command. It is also usefull when you want to create alias for a command which is not in the internal library. To create alias for a command which is not in the internal library you have to use `cmd` command. For more information about `cmd` command see `help cmd` command. You can set aliases in the config.py file. 
</details>

<details>
<summary><strong>comments</strong></summary>

## comments - Comments

**Usage:** comments \<comment>

**Example:** `// This is a comment` or `# This is a comment`

**Description:** // is used to add comments in the script. It is very usefull when you want to add comments in the script. It is also usefull when you want to add comments in the interactive shell. You can also use `#` symbol to add comments in the script. It is also usefull when you want to add comments in the interactive shell. 
</details>

<details>
<summary><strong>cat</strong></summary>

## cat - Concatenate files and print on the standard output

**Usage:** cat \<file_name>

**Example:** `cat file.txt`

**Description:** cat command is used to concatenate files and print on the standard output. It is very usefull when you want to see the content of a file. You can also use `cat` command to see the content of a file in the interactive shell. For more help about `cat` command see `help cat` or `cat help` command.
</details>

<details>
<summary><strong>clear</strong></summary>

## clear - Clear the screen

**Usage:** clear

**Example:** `clear`

**Description:** clear command is used to clear the screen. It is very usefull when you want to clear the screen. You can also use `clear` command to clear the screen in the interactive shell. For more help about `clear` command see `help clear` or `clear help` command. There is a pre-defined alias for `clear` command. You can use `cls` command to clear the screen.
</details>

<details>
<summary><strong>chdir</strong></summary>

## chdir - Change the current working directory

**Usage:** chdir \<directory_name>

**Example:** `chdir /home`

**Description:** chdir command is used to change the current working directory. It is very usefull when you want to change the current working directory. You can also use `chdir` command to change the current working directory in the interactive shell. For more help about `chdir` command see `help chdir` or `chdir help` command. There is a pre-defined alias for `chdir` command. You can use `cd` command to change the current working directory.
</details>

<details>
<summary><strong>cmd</strong></summary>

## cmd - Run any external command

**Usage:** cmd \<any external command>

**Example:** `cmd ls`

**Description:** cmd command is used to run any external command. It is very usefull when you want to run any external command. You can also use `cmd` command to run any external command in the interactive shell. For more help about `cmd` command see `help cmd` or `cmd help` command.
</details>

<details>
<summary><strong>config (D)</strong></summary>

## config - Config Command

**Usage:** config \<config_name> = \<value>

**Example:** `config prompt = $`

**Description:** config command is used to set config values. It is very usefull when you want to set config values. You can also use `config` command to set config values in the interactive shell. For more help about `config` command see `help config` or `config help` command. You can set config values in the config.py file.
</details>

<details>
<summary><strong>copy (D)</strong></summary>

## copy - Copy files and directories

**Usage:** copy \<file_name> \<destination>

**Example:** `copy file.txt /home`

**Description:** copy command is used to copy files and directories. It is very usefull when you want to copy files and directories. You can also use `copy` command to copy files and directories in the interactive shell. For more help about `copy` command see `help copy` or `copy help` command.
</details>

<details>
<summary><strong>date (D)</strong></summary>

## date - Display the current date and time

**Usage:** date

**Example:** `date`

**Description:** date command is used to display the current date and time. It is very usefull when you want to display the current date and time. You can also use `date` command to display the current date and time in the interactive shell. For more help about `date` command see `help date` or `date help` command.
</details>

<details>
<summary><strong>echo</strong></summary>

## echo - Display a line of text or variables

**Usage:** echo \<text> or echo \<$var>

**Example:** `echo Hello World!` or `echo $var $var2`

**Description:** echo command is used to display a line of text or variables. It is very usefull when you want to display a line of text or variables. You can also use `echo` command to display a line of text or variables in the interactive shell. For more help about `echo` command see `help echo` or `echo help` command.
</details>

<details>
<summary><strong>exit</strong></summary>

## exit - Exit the interactive shell

**Usage:** exit

**Example:** `exit`

**Description:** exit command is used to exit the interactive shell. It is very usefull when you want to exit the interactive shell. You can also use `exit` command to exit the interactive shell. For more help about `exit` command see `help exit` or `exit help` command.
</details>

<details>
<summary><strong>file (D)</strong></summary>

## file - Display file type

**Usage:** file \<file_name>

**Example:** `file file.txt`

**Description:** file command is used to display file type. It is very usefull when you want to display file type. You can also use `file` command to display file type in the interactive shell. For more help about `file` command see `help file` or `file help` command.
</details>

<details>
<summary><strong>find (D)</strong></summary>

## find - Find files and directories

**Usage:** find \<file_name>

**Example:** `find file.txt`

**Description:** find command is used to find files and directories. It is very usefull when you want to find files and directories. You can also use `find` command to find files and directories in the interactive shell. For more help about `find` command see `help find` or `find help` command.
</details>

<details>
<summary><strong>get (D)</strong></summary>

## get - Download files from the internet

**Usage:** get \<url> \<destination>

**Example:** `get https://example.com/file.txt /home`

**Description:** get command is used to download files from the internet. It is very usefull when you want to download files from the internet. You can also use `get` command to download files from the internet in the interactive shell. For more help about `get` command see `help get` or `get help` command.
</details>

<details>
<summary><strong>head</strong></summary>

## head - Display the first 10 lines of a file

**Usage:** head \<file_name>

**Example:** `head file.txt`

**Description:** head command is used to display the first 10 lines of a file. It is very usefull when you want to display the first 10 lines of a file. You can also use `head` command to display the first 10 lines of a file in the interactive shell. For more help about `head` command see `help head` or `head help` command.
</details>

<details>
<summary><strong>help</strong></summary>

## help - Display help about commands

**Usage:** help \<command_name>

**Example:** `help echo`

**Description:** help command is used to display help about commands. It is very usefull when you want to display help about commands. You can also use `help` command to display help about commands in the interactive shell. For more help about `help` command see `help help` or `help help` command.
</details>

<details>
<summary><strong>history</strong></summary>

## history - Display the history of commands

**Usage:** history

**Example:** `history`

**Description:** history command is used to display the history of commands. It is very usefull when you want to display the history of commands. You can also use `history` command to display the history of commands in the interactive shell. For more help about `history` command see `help history` or `history help` command.
</details>

<details>
<summary><strong>logo</strong></summary>

## logo - Display the logo of ant

**Usage:** logo

**Example:** `logo`

**Description:** logo command is used to display the logo of ant. It is very usefull when you want to display the logo of ant. You can also use `logo` command to display the logo of ant in the interactive shell. For more help about `logo` command see `help logo` or `logo help` command.
</details>

<details>
<summary><strong>ls</strong></summary>

## ls - List files and directories

**Usage:** ls

**Example:** `ls`

**Description:** ls command is used to list files and directories. It is very usefull when you want to list files and directories. You can also use `ls` command to list files and directories in the interactive shell. For more help about `ls` command see `help ls` or `ls help` command.
</details>

<details>
<summary><strong>mkdir</strong></summary>

## mkdir - Make directories

**Usage:** mkdir \<directory_name>

**Example:** `mkdir test`

**Description:** mkdir command is used to make directories. It is very usefull when you want to make directories. You can also use `mkdir` command to make directories in the interactive shell. For more help about `mkdir` command see `help mkdir` or `mkdir help` command. There is also a pre-defined alias for `mkdir` command. You can use `md` command to make directories.
</details>

<details>
<summary><strong>mv (D)</strong></summary>

## mv - Move files and directories

**Usage:** mv \<file_name> \<destination>

**Example:** `mv file.txt /home`

**Description:** mv command is used to move files and directories. It is very usefull when you want to move files and directories. You can also use `mv` command to move files and directories in the interactive shell. For more help about `mv` command see `help mv` or `mv help` command.
</details>

<details>
<summary><strong>ping</strong></summary>

## ping - Ping a domain or ip address

**Usage:** ping -u \<domain/ip>

**Example:** `ping -u example.com`

**Description:** ping command is used to ping a domain or ip address. It is very usefull when you want to ping a domain or ip address. You can also use `ping` command to ping a domain or ip address in the interactive shell. For more help about `ping` command see `help ping` or `ping help` command.
</details>

<details>
<summary><strong>print</strong></summary>

## print - Print a string

**Usage:** print \<string>

**Example:** `print Hello World`

**Description:** print command is used to print a string. It is very usefull when you want to print a string. You can also use `print` command to print a string in the interactive shell. For more help about `print` command see `help print` or `print help` command.

**Note:** This command is not available in the interactive shell.

</details>

<details>
<summary><strong>pwd</strong></summary>

## pwd - Display the current working directory

**Usage:** pwd

**Example:** `pwd`

**Description:** pwd command is used to display the current working directory. It is very usefull when you want to display the current working directory. You can also use `pwd` command to display the current working directory in the interactive shell. For more help about `pwd` command see `help pwd` or `pwd help` command.
</details>

<details>
<summary><strong>read</strong></summary>

## read - Read a file

**Usage:** read <$var> \<string>

**Example:** `read $var >>>`

**Description:** read command is used to read a file. It is very usefull when you want to read a file. You can also use `read` command to read a file in the interactive shell. For more help about `read` command see `help read` or `read help` command.
</details>

<details>
<summary><strong>rmdir</strong></summary>

## rmdir - Remove directories

**Usage:** rmdir \<directory_name>

**Example:** `rmdir test`

**Description:** rmdir command is used to remove directories. It is very usefull when you want to remove directories. You can also use `rmdir` command to remove directories in the interactive shell. For more help about `rmdir` command see `help rmdir` or `rmdir help` command. There is also a pre-defined alias for `rmdir` command. You can use `rd` command to remove directories.
</details>

<details>
<summary><strong>sysinfo</strong></summary>

## sysinfo - Display the system information

**Usage:** sysinfo

**Example:** `sysinfo`

**Description:** sysinfo command is used to display the system information. It is very usefull when you want to display the system information. You can also use `sysinfo` command to display the system information in the interactive shell. For more help about `sysinfo` command see `help sysinfo` or `sysinfo help` command.

</details>

<details>
<summary><strong>type</strong></summary>

## type - Display the type of a command

**Usage:** type \<command_name>

**Example:** `type echo`

**Description:** type command is used to display the type of a command. It is very usefull when you want to display the type of a command. You can also use `type` command to display the type of a command in the interactive shell. For more help about `type` command see `help type` or `type help` command.

</details>

<details>
<summary><strong>uptime</strong></summary>

## uptime - Display the uptime of the system

**Usage:** uptime

**Example:** `uptime`

**Description:** uptime command is used to display the uptime of the system. It is very usefull when you want to display the uptime of the system. You can also use `uptime` command to display the uptime of the system in the interactive shell. For more help about `uptime` command see `help uptime` or `uptime help` command.
</details>

<details>
<summary><strong>varclear</strong></summary>

## varclear - Clear all variables

**Usage:** varclear

**Example:** `varclear`

**Description:** varclear command is used to clear all variables. It is very usefull when you want to clear all variables. You can also use `varclear` command to clear all variables in the interactive shell. For more help about `varclear` command see `help varclear` or `varclear help` command.
</details>

<details>
<summary><strong>varlist</strong></summary>

## varlist - List all variables

**Usage:** varlist

**Example:** `varlist`

**Description:** varlist command is used to list all variables. It is very usefull when you want to list all variables. You can also use `varlist` command to list all variables in the interactive shell. For more help about `varlist` command see `help varlist` or `varlist help` command.
</details>

<details>
<summary><strong>version</strong></summary>

## version - Display the version of Ant CLI

**Usage:** version

**Example:** `version`

**Description:** version command is used to display the version of Ant CLI. It is very usefull when you want to display the version of Ant CLI. You can also use `version` command to display the version of Ant CLI in the interactive shell. For more help about `version` command see `help version` or `version help` command.
</details>

<details>
<summary><strong>webis</strong></summary>

## webis - Check if a website is up or down

**Usage:** webis -u \<domain>

**Example:** `webis -u example.com`

**Description:** webis command is used to check if a website is up or down. It is very usefull when you want to check if a website is up or down. You can also use `webis` command to check if a website is up or down in the interactive shell. For more help about `webis` command see `help webis` or `webis help` command.
</details>

<details>
<summary><strong>where</strong></summary>

## where - Display the path of a command

**Usage:** where \<command>

**Example:** `where ls`

**Description:** where command is used to display the path of a command. It is very usefull when you want to display the path of a command. You can also use `where` command to display the path of a command in the interactive shell. For more help about `where` command see `help where` or `where help` command.
</details>

<details>
<summary><strong>whoami</strong></summary>

## whoami - Display the current user

**Usage:** whoami

**Example:** `whoami`

**Description:** whoami command is used to display the current user. It is very usefull when you want to display the current user. You can also use `whoami` command to display the current user in the interactive shell. For more help about `whoami` command see `help whoami` or `whoami help` command.
</details>

<details>
<summary><strong>$</strong></summary>

## $ - Set a variable

**Usage:** $ \<$var = value>

**Example:** `$ $var = "Hello World"`

**Description:** $ command is used to set a variable. It is very usefull when you want to set a variable. You can also use `$` command to set a variable in the interactive shell. For more help about `$` command see `help $` or `$ help` command.
</details>

[+] and much more...
<br/>
type `help` in the interactive shell to see all updated commands. 
<br/>
**There is some more powerfull features like: Tab completion command, up/down arrow key history etc.**
<br/>
***Also some ester eggs are hidden in it. Try to find them.*** 😀 


## Super Global Variables

Ant CLI has some super global variables. You can use them in your custom commands. Here is the list of super global variables:

| Variable | Description |
| --- | --- |
| `$ANT_PATH` | Paths of Ant CLI internal commands |
| `$ANT_VERSION` | Version of Ant CLI |
| `$BASE_DIR` | Home directory of Ant CLI |
| `$HOME` | Home directory of current user |
| `$SYSTEM_PATH` | Paths of system commands |



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