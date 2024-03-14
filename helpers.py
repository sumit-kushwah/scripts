import os


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


def get_uncommitted_dirs(directory: str) -> list:
    uncommitted_dirs = []
    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            if check_commit_needed(root):
                uncommitted_dirs.append(root)
    return uncommitted_dirs


def get_unremote_dirs(directory: str) -> list:
    unremote_dirs = []
    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            if not check_if_remote_exists(root):
                unremote_dirs.append(root)
    return unremote_dirs
