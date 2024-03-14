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


def get_remote_dirs(directory: str) -> list:
    remote_dirs = []
    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            if check_if_remote_exists(root):
                remote_dirs.append(root)
    return remote_dirs


def get_remote_url(directory: str) -> str:
    os.chdir(directory)
    result = os.popen("git remote get-url origin").read().strip()
    return result


def check_if_https_url(url: str) -> bool:
    return "https://" in url


def ssh_to_https(ssh_url):
    if check_if_https_url(ssh_url):
        return ssh_url
    https_url = ssh_url.replace(":", "/")
    https_url = https_url.replace("git@", "https://")
    https_url = https_url[:-4] if https_url.endswith(".git") else https_url
    return https_url


def get_current_branch(directory: str) -> str:
    os.chdir(directory)
    result = os.popen("git branch --show-current").read().strip()
    return result


def get_all_git_dirs(directory: str) -> list:
    git_dirs = []
    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            git_dirs.append(root)
    return git_dirs
