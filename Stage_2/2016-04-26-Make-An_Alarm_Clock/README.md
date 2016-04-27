## Intro
This webcast is intended to show you ways you can use programming to think out of the box to solve your everyday needs. By the end of this webcast, you'll make your very own "alarm clock" that plays your favorite song at any time of the day. You'll learn a little about cron jobs -- tasks that run in the background on your computer at certain times of the day. You'll also learn how to
open up files of different types on your computer using Python.

Here is the link to the [video][recording]

## A Story

So I didn't wake up one day and decide to make this alarm clock -- it was driven out of necessity. Recently, I went on vacation and, oops, I dropped my phone in the ocean. I was out of a phone for the next week, argh. The real trouble came on the way back home. I had a 4am flight and really, really wanted to sleep -- but my alarm clock, like many things today, was on my now defunct phone. The airport I was at also did not have internet readily available for free, so I couldn't use online alarm clocks. How could I catch some z's while not missing my flight back home?

So I began to think: How I could simulate an alarm clock using my computer and programming knowledge? Let me show you how.

## The Python Program
Let's start by making the python program that opens up a sound file in our default music player. For me, I chose a song file, and my default player for this is iTunes.

### The `os` Module
The first line in our program is this:

```python
import os
```

The `os` module is a library of different system function written in python for our use. Using this module, we can delete files, run programs, open files, and more.

Remember that modules are just programs that only contain functions that you can use and don't need to re-implement. Some do a lot of complex work -- low level hardware access. For this reason we leave it to the os module to take care of hardware access for us, abstracting away the hard parts that we don't need to know for our purposes.

Use the "system" function to execute a system command, like "open"

### Opening the File

Using the `os` module's `system` command, we can execute the Unix command that opens the music file. The Unix command to open a file is the "open" command:

```python
os.system("open /Users/rahul/Desktop/to_u.mp3")
```

Also in the string containing the `open` command is the absolute PATH to location of my sound file in my file system, called "to_u.mp3".

## What's a cron job?
A cron job is a scheduled task that repeats a command at certain times that you set during the day.

Why can't we just run the program until a certain time is met? Well, you could use something like the time module,but you'd have to have it running all the time, whereas when the system runs it you will generally save RAM.

This demonstration is for Unix-based machines -- that is, if you have a Linux or Mac Computer. If you have a windows computer, don't worry! There's a cron job like scheduler that you can use that's built-in: Take a look at <a href="http://windows.microsoft.com/en-US/windows/schedule-task#1TC=windows-7">this tutorial</a>. 

## Use a cron job to run our program
To generate a cron job, we create a configuration file -- it's just a text file, with a ".txt" extension. This is my cron text file, `alarm_cron.txt` (you can call it anything you want):

```bash
MAILTO=support@udacity.com
30 7 * * * python /Users/rahul/Work/ipnd-webcasts/Stage_2/2016-04-26-Make-An_Alarm_Clock/alarm.py
```
The `MAILTO` variable you see is what as known as an environmental variable -- you can think of this as a variable that your operating system keeps over the course of its operations. (Remember that an operating system is an environment that is the result of a program executing, known as a kernel.) The email address  that I set the `MAILTO` variable to will be sent errors if the cron job fails to operate.

The second line creates timing interval for the job. The first five space-delimited values are the minutes of the day, hour of day, day of month, month of year, and what day of week to run the cron job, in that order. The `*` that you see means "all" in programmer-speak, so what we're saying here is "repeat this task every day of every week of every month at 7:30 AM.

The last two pieces on this line is the command that we want to be executed when the cron job starts. The command we run is just the python program that we want to execute, `alarm.py`, which will run everyday at 7:30 AM. We use the absolute PATH, which, we can find by opening up terminal, `cd`ing into the folder containing our python file, and typing `pwd`, which stands for `Print Working Directory`. This gives us the absolute PATH, which we copy and paste into here.

## Running the Cron Job
To tell the operating system to set up a cron job, we run the following command:

`crontab alarm_cron.txt`

And that's it! To see what cron jobs you have set, you can type in `crontab -l` and to remove all the cron jobs you have set, type in `crontab -r`. You can change the time of the cron job, but you first need to remove the cron job you just set using `crontab -r` because the operating system doesn't know changes that you make right away without being updated.

For more cool stuff and info about cron jobs, check out this page http://www.thesitewizard.com/general/set-cron-job.shtml

[recording]: https://plus.google.com/u/0/110965457514018530372/posts/Kb5S1PYifZe?cfem=1