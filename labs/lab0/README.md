# Lab 0: Setup your development environment

In this lab, we will set up the development environment for Python programming.

## Shell basics

You will need to use a shell to run commands. This will be the primary way to interact with your computer during this course.

### File system

A Unix-like file system is organized as a hierarchical structure of directories and files. The root directory is denoted by `/`. Each directory is separated by `/`. For example, `/home/user/Documents` is a directory named `Documents` under the directory `user`, which is under the directory `home`. This string that represents the location of a file or directory is called a path.

#### Absolute path vs. relative path

-   An absolute path starts from the root directory. For example, `/home/user/Documents`.
-   A relative path starts from the current working directory. For example, `Documents`.

There are some special directories:

-   `.`: the current directory
-   `..`: the parent directory
-   `~`: the home directory

You can combine these special directories with other directories to form a path. For example, `~/Documents` is the `Documents` directory under the home directory.

#### Basic file system commands

You can navigate the file system using the following commands:

-   `ls`: list files and directories in the current directory
-   `cd`: change directory
    -   `cd <target directory>`: change to the target directory
    -   `cd ..`: change to the parent directory
    -   `cd ~` or `cd`: change to the home directory
-   `pwd`: print the current working directory
-   `mkdir <directory name>`: create a new directory
-   `rm <file name>`: remove a file
-   `rm -r <directory name>`: remove a directory and its contents
-   `mv <source> <destination>`: move or rename a file or directory
-   `cp <source> <destination>`: copy a file or directory
-   `cp -r <source> <destination>`: copy a directory and its contents

####

## Python setup

### Pyenv

We will use [pyenv](https://github.com/pyenv/pyenv) to manage Python versions. You don't have to understand how it works right now. But you will appreciate it when you have to switch between different Python versions for different projects.

Simple installation:

```bash
curl https://pyenv.run | bash
```

Then, append the following lines to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`):

```bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Restart your shell or run `source ~/.bashrc` (or `~/.zshrc`, `~/.bash_profile`) to apply the changes.

Now, you can install Python 3.12 with pyenv:

```bash
pyenv install 3.12
```

After the installation, set the global Python version to 3.12:

```bash
pyenv global 3.12
```

Check the Python version:

```bash
python --version
```

### Create a project directory

Create a directory for your project. You will need to `cd` into a desired directory and run the following command:

```bash
mkdir summer_project
cd summer_project
```

### Create a virtual environment

We will use [venv](https://docs.python.org/3/library/venv.html) to create a virtual environment for the project. A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

You will see the prompt changes to indicate the virtual environment is activated.

## Editor setup

If you don't have a preferred editor, I recommend using [Visual Studio Code](https://code.visualstudio.com/). It is a lightweight but powerful source code editor that runs on your desktop.

### Visual Studio Code

Download and install Visual Studio Code from the [official website](https://code.visualstudio.com/).
