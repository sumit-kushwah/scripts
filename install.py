import os
import json

# read json file
with open("commands.json", "r") as myfile:
    data = myfile.read()

# parse file
commands = json.loads(data)
cwd = os.getcwd()

# clean all the aliases from .bashrc and .zshrc
for command in commands:
    reg_exp = f"^alias.*{command['alias']}=.*"
    os.system(f"sed -i '/{reg_exp}/d' ~/.bashrc")
    os.system(f"sed -i '/{reg_exp}/d' ~/.zshrc")

# writing to .zshrc
# check .zshrc exist or not
for file in [os.path.expanduser("~/.zshrc"), os.path.expanduser("~/.bashrc")]:
    filename = os.path.basename(file)
    if os.path.isfile(file):
        cwd_with_backslashes = cwd.replace("/", "\/")
        sedcommand = f"sed -i '/# Added by {cwd_with_backslashes}\/install.py/d' {file}"
        os.system(sedcommand)
        with open(file, "a") as myfile:
            myfile.write(f"# Added by {cwd}/install.py\n")
            alias_commands = []
            for command in commands:
                full_path = os.path.join(cwd, command["file"])
                alias_command = (
                    f"alias {command['alias']}=\"{command['program']} {full_path}\""
                )
                alias_commands.append(alias_command)
                print(f"Added {alias_command} to {filename}")
            myfile.write("\n".join(alias_commands))
    else:
        print(f"No {filename} file found")
