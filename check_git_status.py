import os
import argparse

parser = argparse.ArgumentParser(
    description="Check git status of all git repositories in a directory"
)
parser.add_argument("--dir", type=str, help="Directory to check", required=True)
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
        print(f"Checking {root}")
        if check_commit_needed(root):
            uncommitted_dirs.append(root)
        if not check_if_remote_exists(root):
            unremote_dirs.append(root)

if uncommitted_dirs:
    print("\nThe following directories have uncommitted changes:")
    for d in uncommitted_dirs:
        print(d)

if unremote_dirs:
    print("\nThe following directories do not have a remote:")
    for d in unremote_dirs:
        print(d)
