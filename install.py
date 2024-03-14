import os
import json

# read json file
with open("commands.json", "r") as myfile:
    data = myfile.read()

# parse file
commands = json.loads(data)

for command in commands:
    cwd = os.getcwd()
    full_path = os.path.join(cwd, command["file"])
    alias_command = f"alias {command['alias']}=\"{command['program']} {full_path}\""
    # check .bashrc exist or not
    if os.path.isfile(os.path.expanduser("~/.bashrc")):
        with open(os.path.expanduser("~/.bashrc"), "a") as myfile:
            myfile.write(f"\n{alias_command}")
            print(f"Added {alias_command} to .bashrc")
    else:
        print("No .bashrc file found")

    # check .zshrc exist or not
    if os.path.isfile(os.path.expanduser("~/.zshrc")):
        with open(os.path.expanduser("~/.zshrc"), "a") as myfile:
            myfile.write(f"\n{alias_command}")
            print(f"Added {alias_command} to .zshrc")
    else:
        print("No .zshrc file found")
