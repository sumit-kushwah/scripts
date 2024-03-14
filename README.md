# Project Title

This project provides a convenient way to add aliases for frequently used commands.

## Getting Started

These instructions will guide you on how to use the aliases provided by this project.

### Prerequisites

- You need to have `python3` installed and available in your system's PATH.
- The `requirements.txt` file lists the Python dependencies needed for the script to run.

### Installation

1. **Clone the repository**

   Use the following command to clone this repository:

   ```bash
   git clone https://github.com/sumit-kushwah/scripts

2. **Install dependencies**

    Navigate to the project directory and install the required Python dependencies using:

    ```bash
    pip install -r requirements.txt

3. **Run the installation script**

    Run the install.py script using Python 3. This script will add all the aliases available in the commands.json file to your shell's configuration file.

    ```bash
    python3 install.py
    ```
    
    Now, the setup is complete and you're ready to use the aliases.


### Usage

Here's an example of how to use one of the aliases:

```bash
gitreport -d ~/Development
```

This command will run the gitreport alias on all repositories in the ~/Development directory.

Note: Check `commands.json` for each alias.