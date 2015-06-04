Installing Twilio With PIP
==========================================

Here is a link to the [Webcast][WB]

We're going to run through basic instructions on installing the Twilio package in a Windows computer. 

## Setup

We will start with a fresh install of Windows and will install the basic Python package taken from [http://www.python.org](http://www.python.org)

From there, we will use terminal commands to use the PIP Python Package manager to install Twilio and make sure that we can import the package correctly using the IDLE terminal in windows.

## Steps

* Install Python from the package downloaded from http://www.python.org
* Make sure that Python is added to the system PATH during installation. It's very important that Python is added to the PATH or else we would not be able to call our commands from any folder in our command line.

![](path.png)

* We then go through our command prompt and type in the command `pip install twilio` to install the Twilio package. Make sure that your system is connected to the Internet and there are no firewalls that could be blocking Python from downloading Twilio.

## Verify

We verify our installation by going to our IDLE terminal and enter the command `import twilio`

If there are no errors, then Twilio has just been installed!

## Macintosh Users

If you have a Macintosh computer, Python is already installed and we simply need to install PIP, the package manager.

Open up your Terminal application and type:

`sudo easy-install pip`

You may need to enter in your password and PIP will get downloaded and installed.

From there, in our terminal, we type:

`sudo pip install twilio` 

to install Twilio.

## Troubleshooting

Make sure you have:

* Administrative access to your machine
* An Internet connection that does not block Python
* A clean install of Python
* Added the python executable file to the system's PATH

For beginners, it's suggested that we start from a fresh install of Python. We recommend you uninstall all instances of Python on your machine, install Python, and make sure that Python is added to your system PATH.


[WB]: https://plus.google.com/events/ch42gnbnrmm7ugqtnbtb2533004?authkey=CPC3z6Oc5YynOA