import os
import argparse
from helpers import get_remote_url, get_current_branch
from colorama import Fore, Style

parser = argparse.ArgumentParser(
    description="Check git status of all git repositories in a directory"
)
parser.add_argument(
    "--dir",
    "-d",
    type=str,
    help="Directory to check",
    default="/home/sumit/Development/",
)
args = parser.parse_args()

directory = args.dir

if not os.path.isdir(directory):
    print(f"{directory} is not a directory")
    exit(1)


def check_commit_needed(path: str) -> bool:
    os.chdir(path)
    result = os.popen("git status").read()
    if "nothing to commit, working tree clean" in result:
        return False
    return True


def check_if_remote_exists(path: str) -> bool:
    os.chdir(path)
    result = os.popen("git remote -v").read()
    if "origin" in result:
        return True
    return False


uncommitted_dirs = []
unremote_dirs = []

for root, dirs, files in os.walk(directory):
    if ".git" in dirs:
        current_branch = get_current_branch(root)
        print(
            Fore.LIGHTGREEN_EX
            + f"Checking {root}"
            + Style.RESET_ALL
            + Fore.YELLOW
            + f" ({current_branch})"
            + Style.RESET_ALL
        )
        if check_commit_needed(root):
            uncommitted_dirs.append(root)
        if not check_if_remote_exists(root):
            unremote_dirs.append(root)

if uncommitted_dirs:
    print("\nThe following directories have uncommitted changes:")
    for d in uncommitted_dirs:
        current_branch = get_current_branch(d)
        print(
            Fore.RED
            + d
            + Style.RESET_ALL
            + Fore.YELLOW
            + f" ({current_branch})"
            + Style.RESET_ALL
        )

if unremote_dirs:
    print("\nThe following directories do not have a remote:")
    for d in unremote_dirs:
        print(Fore.LIGHTMAGENTA_EX + d + Style.RESET_ALL)
