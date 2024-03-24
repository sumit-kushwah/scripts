import os
import datetime
import argparse
from helpers import get_uncommitted_dirs, get_all_git_dirs

parser = argparse.ArgumentParser(
    description="Auto commit all git repositories which have uncommitted changes"
)

# parse custom commit message
parser.add_argument(
    "--message",
    "-m",
    type=str,
    help="Commit message to use",
    default="Auto commit at " + str(datetime.datetime.now()),
)
# if all flag set, then no need to ask for directory
parser.add_argument(
    "--dir",
    "-d",
    type=str,
    help="Directory to check",
    default="/home/sumit/Development/",
)

parser.add_argument(
    "--force",
    "-f",
    type=bool,
    help="force push to origin",
    default=False,
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
commit_message = args.message
directory = args.dir
branch = args.branch
force = args.force

if force:
    print("Force push enabled")

uncommitted_dirs = get_uncommitted_dirs(directory)
if len(uncommitted_dirs) == 0:
    print("No uncommitted changes found")
    if not force:
        exit(0)
else:
    print(f"Committing uncommited changes with message: {commit_message}")

for d in uncommitted_dirs:
    os.chdir(d)
    os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push origin " + branch)
    print(f"Pushed {d} to origin/{branch}")

print("Force push other git repositories")

gitrepos = get_all_git_dirs(directory)

for d in gitrepos:
    print("------------------------")
    os.chdir(d)
    os.system(f"git push origin {branch}")
    print(f"Force pushed {d} to origin/{branch}")
