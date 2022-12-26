import platform
import os
import rong


# User's home directory
path_dir = os.environ["HOME"]  # Production environment
# path_dir = "./" # Testing
root = os.path.dirname(os.path.abspath(__file__))

# Prompt settings
path = os.getcwd()
user = platform.uname().node
prompt = f"{ rong.Mark.GREEN }{ user } @ { path }{ rong.Mark.END } \n>>> "


profile = {
    "prompt": prompt,
    "path": path_dir,
    "root": root,
    "history": ".ant_history",
    "aliases": {
        "cls": "clear",
        "dir": "cmd ls",
        "cd": "chdir",
        "md": "mkdir",
        "rd": "rmdir",
        "git": "cmd git",
        "sudo": "cmd sudo"
    },
    "preloaded_actions": [
        'logo',
        'version',
    ]
}
