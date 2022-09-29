import platform
import os
from sys import path_hooks


class color:
    '''Related colors.'''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


path = os.getcwd()
user = platform.uname().node
# path_dir = os.environ['HOME'] # Production environment
path_dir = './'

profile = {
    "prompt": f'{color.OKGREEN + user} @ {path + color.ENDC} \n>>> ',
    "path": path_dir,
    "history": '.ant_history'
}
