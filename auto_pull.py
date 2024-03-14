import os
import datetime
import argparse
from helpers import get_all_git_dirs, check_if_remote_exists
from colorama import Fore, Style

parser = argparse.ArgumentParser(description="Auto pull all git repositories")

# if all flag set, then no need to ask for directory
parser.add_argument(
    "--dir",
    "-d",
    type=str,
    help="Directory to check",
    default="/home/sumit/Development/",
)

# get branch
parser.add_argument(
    "--branch",
    "-b",
    type=str,
    help="Branch to push",
    default="master",
)

args = parser.parse_args()
directory = args.dir
branch = args.branch

git_dirs = get_all_git_dirs(directory)
for d in git_dirs:
    if check_if_remote_exists(d):
        print(Fore.YELLOW + f"Checking {d}............." + Style.RESET_ALL)
        os.chdir(d)
        os.system("git pull origin " + branch)
        print()
