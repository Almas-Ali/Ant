import platform
import os
import sys
import rong


# User home directory
HOME_PATH = os.path.expanduser('~')
# Base directory of Ant Interpreter
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)

from lib.userlib import SystemConfig

# PROMPT settings
path = os.getcwd()
user = platform.uname().node
PROMPT = f"{ rong.Mark.GREEN }{ user } @ { path }{ rong.Mark.END } \n>>> "

# Operating System settings
OPERATING_SYSTEM = SystemConfig().check_os()

# PATH settings
# Ant paths
# Add all absolute paths of your custom commands here.
ANT_PATH = [
    os.path.join(BASE_DIR, "bin"),
    os.path.abspath(BASE_DIR),
]


# System paths
# Add all absolute paths of your custom commands here.
SYSTEM_PATH = os.environ["PATH"].split(":")
SYSTEM_PATH.extend([
    # Add your custom system path here
])

profile = {
    "PROMPT": PROMPT,
    "HOME_PATH": HOME_PATH,
    "BASE_DIR": BASE_DIR,
    "ANT_PATH": ANT_PATH,
    "SYSTEM_PATH": SYSTEM_PATH,
    "OPERATING_SYSTEM": OPERATING_SYSTEM,
    "history": ".ant_history", # history file name
    "aliases": {
        "cls": "clear",  # cls is a windows command
        "dir": "ls",  # dir is a windows command
        "cd": "chdir",
        "md": "mkdir",
        "rd": "rmdir",
        "print": "echo",
        "sysinfo": "whoami -a",
        "reboot": "shutdown -r -t 0",
        "doskey": "alias",  # doskey is a windows command
    },
    "preloaded_actions": [
        # "logo",
        # "version",
    ]
}
