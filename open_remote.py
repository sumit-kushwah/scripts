import os
import argparse
from helpers import ssh_to_https, check_if_remote_exists, get_remote_url

parser = argparse.ArgumentParser(description="Open remote repository in browser")

parser.add_argument(
    "--dir",
    "-d",
    type=str,
    help="Directory to check",
    required=True,
)
args = parser.parse_args()

direcotry = args.dir

if not os.path.isdir(direcotry):
    print(f"{direcotry} is not a directory")
    exit(1)

if not check_if_remote_exists(direcotry):
    print(f"No remote found in {direcotry}")
    exit(1)

# get the remote url
remote_url = get_remote_url(direcotry)
print("Remote: " + remote_url)
https_url = ssh_to_https(remote_url)
print("HTTPS URL: " + https_url)
print("Opening in browser...")
success = os.system(f"xdg-open {https_url}")
if success != 0:
    print("Could not open in browser")
    exit(1)
