import platform
import os
import rong


# User's home directory
HOME_PATH = os.environ["HOME"]  # Production environment
# HOME_PATH = "./" # Testing
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# PROMPT settings
path = os.getcwd()
user = platform.uname().node
PROMPT = f"{ rong.Mark.GREEN }{ user } @ { path }{ rong.Mark.END } \n>>> "

# Operating System settings
OPERATING_SYSTEM = os.name
match OPERATING_SYSTEM:
    case "nt":
        OPERATING_SYSTEM = "windows"
    case "posix":
        OPERATING_SYSTEM = "linux"
    case "mac":
        OPERATING_SYSTEM = "macos"
    case _:
        OPERATING_SYSTEM = "unknown"
        
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
    "history": ".ant_history",
    "aliases": {
        "cls": "clear",
        "dir": "ls",
        "cd": "chdir",
        "md": "mkdir",
        "rd": "rmdir",
        "print": "echo",
        "sysinfo": "whoami -a",
    },
    "preloaded_actions": [
        'logo',
        'version',
    ]
}
