# Before you start

## Why using English?

We will be using English as the primary language in all course materials, including lab documents like this one, code, and comments. This is because English is the standard language for programming and computer science. Almost all public projects like the libraries and their documentation are written in English. This helps you to practice reading documentation and code written in English, which is essential for your future career.

## How to use this document

Follow the instructions in this document to complete the lab. You will be asked to run commands in the terminal, write code, and answer questions. You can simply share a screenshot of the terminal to show your answers to the questions.

## Using the terminal

You will need to use a terminal emulator to run commands.

-   For Mac, you can use the built-in "Terminal" app.
-   For Windows, you can use "Terminals" app. Remember to select "Ubuntu" as the shell.

# Shell basics

You will need to use a shell to run commands. This will be the primary way to interact with your computer during this course.

You've already used a shell to run commands in the terminal. You've pulled this repository using `git` commands. You've also run Python using the `python` command. In this lab, we will learn more useful shell commands.

## Why using the shell rather than a GUI (Graphical User Interface)?

You may be more familiar with GUIs. You've been using them since you started using computers. For example, you can use a file explorer to navigate the file system, click on files to open them, and drag and drop files to move them. You can also use a text editor to write code and run it.

However, the shell is more powerful and efficient for the following reasons:

-   **Direct access to the file system**: You can navigate the file system and manipulate files and directories more efficiently.
-   **Access to a wide range of command-line tools**: There are many command-line tools that can help you perform various tasks, such as text processing, file management, and system administration.
-   **Automation**: You can write shell scripts to automate repetitive tasks.
-   **Easier to build and run programs**: You can easily build your own programs and run them from the shell.

## Navigating the file system

You are already familiar with the file explorer, which allows you to navigate the file system using a graphical interface. In the shell, you can navigate the file system using commands.

**Terminalogy**:

-   **Directory**: A directory is a container for files and other directories. It is similar to a folder in a file explorer.
-   **File**: A file is a collection of data stored on a computer. It can contain text, images, videos, or any other type of data.
-   **Path**: A path is a string that specifies the location of a file or directory in the file system.
-   **Current working directory**: The current working directory is the directory you are currently in. When you open a shell, you are in a directory. This directory is called the current working directory.

### Who am I?

When you open a shell, you are logged in as a user. You can find out which user you are logged in as using the `whoami` command:

```bash
whoami
```

If your username is `student`, the output will be `student`.

> **Note: in the following examples, we will use `student` as the username. Replace `student` with your actual username.**

### Where am I?

When you open a shell, you are in a directory. This directory is called the **current working directory**. You can find out which directory you are in using the `pwd` command:

```bash
pwd
```

This command will print the full path of the current working directory. For example, if your username is `student` and you are in the home directory, the output may be `/home/student`.

### Listing files and directories

You can list the files and directories in the current working directory using the `ls` command:

```bash
ls
```

This command will print the names of the files and directories in the current working directory. For example, if the current working directory contains the files `file1.txt` and `file2.txt`, the output will be:

```
file1.txt file2.txt
```

### Creating a directory

You can create a new directory using the `mkdir` command. To use the `mkdir` command, you need to provide the name of the directory you want to create. For example, to create a directory named `mydir`, you can use the following command:

```bash
mkdir ~/Projects
```

This command will create a new directory named `Projects` in the current working directory under the home directory (`~`). We will learn more about paths later in future labs.

### Changing directories

Now that you've created a `Projects` directory, you can change to that directory using the `cd` command. To use the `cd` command, you need to provide the path of the directory you want to change to.

There are multiple ways to specify the path of the directory you want to change to. You may try the following commands:

```bash
cd ~/Projects
pwd
```

In the example above, the `cd` command changes the current working directory to the `Projects` directory under the home directory (`~`). The `pwd` command prints the full path of the current working directory, which should be `/home/student/Projects`.

```bash
cd /home/student/Projects
pwd
```

In this example, the `cd` command changes the current working directory to the `Projects` directory under the directory `/home/student`. Note that the path `/home/student` is equivalent to `~`, because `~` is a shorthand for the home directory of the current user. The output of the `pwd` command still should be `/home/student/Projects`.

```bash
cd
cd Projects
pwd
```

In this example, we did the following:

1. The first `cd` command changes the current working directory to the home directory (`~`).
2. The second `cd` command changes the current working directory to the `Projects` directory under the home directory.
3. The `pwd` command prints the full path of the current working directory, which should be `/home/student/Projects`.

### Creating a file

Now, let's create a Python script called `hello.py` in the `Projects` directory. You can create a new file using the `touch` command. To use the `touch` command, you need to provide the name of the file you want to create.

First, make sure you are in the `Projects` directory. You can use the `pwd` command to confirm that you are in the `Projects` directory. The output of the `pwd` command should be `/home/student/Projects`.

After you've confirmed that you are in the `Projects` directory, you can create a new directory named `hello` and `cd` into it:

```bash
mkdir hello
cd hello
```

Now, create a new file named `hello.py` using the following command:

```bash
touch hello.py
```

This command will create a new file named `hello.py` in the current working directory.

### Editing a file

You can edit the `hello.py` file using a text editor. You can use any text editor you like. But for now, if you don't know what to use, we've set up Visual Studio Code for you. You can open the `hello.py` file using Visual Studio Code by running the following command:

```bash
code hello.py
```

This will open the `hello.py` file in Visual Studio Code. You can write Python code in this file.

You are free to write any Python code you like in this file, but for now, let's write a simple Python script that prints "Hello, world!":

```python
print("Hello, world!")
```

After writing the Python code, save the file and close the text editor.

### Printing the content of a file

You can print the content of the `hello.py` file using the `cat` command. To use the `cat` command, you need to provide the name of the file you want to print the content of. For example, to print the content of the `hello.py` file, you can use the following command:

```bash
cat hello.py
```

The output of this command should be the content of the `hello.py` file you just created.

### Running a Python script

You can run the `hello.py` Python script using the `python` command. To use the `python` command, you need to provide the name of the Python script you want to run. For example, to run the `hello.py` script, you can use the following command:

```bash
python hello.py
```

This command will run the `hello.py` script using the Python interpreter. The output of this command should be `Hello, world!`.

**Take a screenshot** of the terminal showing the output of the `python hello.py` command and share it in the group chat.

# Conclusion

Today, you've learned:

-   How to find out which user you are logged in as
-   How to find out which directory you are in
-   How to create directories and files
-   How to list files and directories
-   How to change directories
-   How to print the content of a file
-   How to run a Python script

These are the basic shell commands you will need to use throughout this course. You will learn more advanced shell commands in the upcoming labs.
