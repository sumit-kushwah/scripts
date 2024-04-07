import os
import argparse
from helpers import get_remote_url, get_current_branch, check_pull_push_needed
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
remote_diff_dirs = []

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
        if check_if_remote_exists(root):
            try:
                # check if local and remote branch have same head
                remote_url = get_remote_url(root)
                os.chdir(root)
                os.system("git fetch")
                branch = get_current_branch(root)
                local_head = os.popen(f"git rev-parse {branch}").read().strip()
                remote_head = (
                    os.popen(f"git ls-remote {remote_url} {branch}").read().split()[0]
                )
                if local_head != remote_head:
                    remote_diff_dirs.append(root)
            except Exception as e:
                print(f"Error: {e}")

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

if remote_diff_dirs:
    print(
        "\nThe following directories have local and remote branch at different commits:"
    )
    for d in remote_diff_dirs:
        current_branch = get_current_branch(d)
        pull_push_status = check_pull_push_needed(d)
        message = "Run git pull" if pull_push_status == 1 else "Run git push"
        print(
            Fore.LIGHTCYAN_EX
            + d
            + Style.RESET_ALL
            + Fore.YELLOW
            + f" ({current_branch})"
            + f" - {message}"
            + Style.RESET_ALL
        )
