import platform
import os


class color:
    """Related colors."""
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

# User's home directory
path_dir = os.environ["HOME"]  # Production environment
# path_dir = "./" # Testing
root = os.path.dirname(os.path.abspath(__file__))

# Prompt settings
path = os.getcwd()
user = platform.uname().node
prompt = f"{ color.OKGREEN }{ user } @ { path }{ color.ENDC } \n>>> "

profile = {
    "prompt": prompt,
    "path": path_dir,
    "root": root,
    "history": ".ant_history",
    "alias": {
        "cls": "clear",
        "dir": "cmd ls",
        "cd": "cmd chdir",
        "md": "mkdir",
        "rd": "rmdir",
        "git": "cmd git",
        "sudo": "cmd sudo"
    },
    "preloaded_action": [
        ""
    ]
}
