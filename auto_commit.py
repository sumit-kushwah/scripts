import os
import datetime
import argparse
from helpers import get_uncommitted_dirs

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

uncommitted_dirs = get_uncommitted_dirs(directory)

print(f"Committing uncommited changes with message: {commit_message}")

for d in uncommitted_dirs:
    os.chdir(d)
    os.system("git add .")
    os.system(f'git commit -m "{commit_message}"')
    os.system("git push origin " + branch)
    print(f"Pushed {d} to origin/{branch}")
