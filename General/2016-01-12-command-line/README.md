# Using the Command Line
You can find a link to the video [here](https://plus.google.com/events/c6vvueadinlenchmvd87taj55r4?authkey=CMPnoYv2u_unxQE)

Thanks to the miracles of modern operating systems, the ways in which we interact with computers has changed dramatically. Gone are the days of using punch cards and text-based interfaces. Now we interact with computers largely through GUIs or Graphical User Interfaces. You're taking advantage of your operating system's GUI anytime you create a folder, drag a file, or click an icon to open an application.

A command line interface is a text-based way of interacting with your computer through something called shell commands. Using the command line, you can do everything on your computer that we now visualize with a GUI. Knowing how to use the command line is especially useful for programmers as it is an ideal interface for running code and reading error messages.

# Navigating the File System

An important note: The type of commands you can use in your computer's command line interface is dictated by your computer's "shell" which is the technology that allows you to interact with your operating system (by either the command line or a GUI). Mac OS X and Linux systems default to using bash (the Bourne-again shell) while Windows uses MS-DOS. The specifics of how these technologies work is not that important for us here, just know that you'll type slightly different commands depending on your OS.

The first thing we should learn about using the command line is how to navigate the file system. Let's start by opening our command line interface (CLI). On a Mac, you should open the application Terminal found in the Utilities folder under Applications. If you're using a Linux system, look for a similarly titled application. On Windows, open the Start menu and search for "Command Prompt"

When we open the CLI, we always "start" at our home directory. That's just the main folder for your user account. When we interact with the CLI, we usually refer to folders as directories, and when we use GUIs we call them folders. Folders and directories are the same thing, you should get used to both names and the contexts in which either is used.

Let's see the contents of our home directory. On Mac and Linux we can do this by typing `ls` (short for list) and on Windows we type `dir` (short for directory). Hit Enter to execute the command.

Our home directory probably isn't all that interesting. It will likely just have a bunch of other directories like Documents, Photos, and Downloads. Let's "move" to another directory. This is one of the few commands that is common across operating systems. We can change our current directory with the command `cd directory-name` (`cd` is short for "change directory"). Here's a fun tip: You can press Tab to autocomplete some commands. For example, press Tab after typing `cd Doc` and the word "Documents" will be automaticall completed. Let's change to our Documents directory.

Now our current directory is `Your-Home/Documents`. We can go back one directory with the command `cd ..`. If we enter `cd ..` from `Documents` we'll return to the home directory. We can also move forward many directories. For example, if we are in the home and enter `cd Documents/ipnd` we'll move to the `ipnd` folder within `Documents`. Note that Windows uses forward slashes `\` instead of back slashes `/` in file paths.

# Creating Directories and Files

We can also make new directories and files from the command line. Let's make a directory called `hello` in Documents. Navigate to the Documents directory and then make a new directory with `mkdir hello` (`mkdir` is short for "make directory"). This is another command common between Mac, Linux, and Windows.

We now have a "hello" directory inside our "Documents". Let's make an empty file named "file.txt" inside our new directory. We'll start by moving into "hello" with `cd hello`. Now we can make an empty file with `touch file.txt` on Mac/Linux and `copy nul > file.txt`. If you then enter `open file.txt` your computer will open the empty file.

We can remove files too. `rm file.txt` will remove the file we just created on Mac/Linux. We can do the same thing on Windows with `del file.txt`. If we then move back to Documents with `cd ..` we can delete the "hello" directory too. On Mac/Linux you need to do `rmdir hello` to remove the directory. On Windows, you use the same command as before, `del hello`, but will need to then confirm the command by entering `Y`. Note that on Mac/Linux, you can only remove a directory if it's empty.

# Running Python Code

The command line is especially useful for running Python code. The output of your code will appear directly in your CLI. To run Python code on your computer, you should first navigate to the directory where your code is. Once you've done that, you can then run the code on Mac/Linux by entering `python name-of-python-file.py` or on Windows just `name-of-python-file.py`. You can also run `.pyc` files in the same way. If your code runs without error, you'll see any print statements that your program reaches appear on the command line. If your code runs into any errors, you'll see the Traceback appear there too.