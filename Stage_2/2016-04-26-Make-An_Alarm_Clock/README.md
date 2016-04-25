## Intro
This webcast is intended to show you all the ways you can use programming to think out of the box to solve your everyday needs.
By the end of this webcast, you'll make your very own "alarm clock" that plays your favorite song at any time of the day. You'll learn
a little about cron jobs -- tasks that run in the background on your computer at certain times of the day. You'll also learn how to
open up files of different types on your computer using Python.

Here is the link to the [video][recording]

## A Story

So I didn't wake up one day and decide to make this alarm clock -- it was driven out of necessity. Recently, I went on vacation and, oops, I dropped my phone in the ocean.
I was out of a phone for the next week, argh. The real trouble came on the way back home. I had a 4am flight and really, really wanted to sleep -- but my alarm clock, like many things today, was on my now defunct phone. The airport I was at also did not have internet readily available for free, so I couldn't use online alarm clocks. How could I catch some z's while not missing my flight back home?

What I did have was my computer and my brain! So I thought about how I could simulate an alarm clock, and guess what? It worked! Let me show you how.

## The Python Program

### os module

Need to import the os module
Use the "system" function to execute a system command, like "open"

### linux command line
The way that we open a file in a Unix-based operating system is with the "open" command. So what I did was open up an .mp3 file, which, by default, opens in iTunes.
I set my computer to not go to sleep (thank goodness for power outlets!) and began to set up my cron job.

### choose a song
I chose _____. My default music player is iTunes, so when I open this file 

(test the program)

It works! So now we try to implement the timing part -- the cron job.

## What's a cron job?
A cron job is a scheduled task that repeats a command in terminal at certain times that you set during the day.

Why can't we just run the program until a certain time is met? Well, you could use something like the time module,
but you'd have to have it running all the time, whereas when the system runs it you will generally save RAM.

## Use a cron job to run our program

- Create a text file
- set MAILTO environment
- create timing interval: minutes of day, hour of day, day of month, month of year, what day of week to run

- use the * to show every day
- find absolute path using PWD
- set the command we want to run (python )

## run the cron job

`crontab alarm_cron.txt`

to see what cron jobs you have set, you can type in `crontab -l`
to remove all the cron jobs you have set, type in `crontab -r`

for more cool stuff and info about cron jobs, check out this page http://www.thesitewizard.com/general/set-cron-job.shtml

[recording]: 