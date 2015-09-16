Basic Visualization Workflow
===
# Webcast Recording
[Link to video](https://plus.google.com/events/ck3p4c8uqlml0m4s7elg3n62pac?authkey=CLqq7NvM4caJ0gE)

[Link to Anaconda download](http://continuum.io/downloads)

[Link to gold price data](https://www.quandl.com/api/v1/datasets/FRED/GOLDPMGBD228NLBM.csv)
# Introduction

This webcast discusses the importance of data visualization and how to analyze data using the Pandas library.
At the end of the Webcast session, we will understand:

* What data looks like in a digital context
* How to install Anaconda and use iPython Notebook
* How to plot simple time-domain data in iPython

# Data Visualization 

Whenever you collect data, it usually ends up in some kind of text-based format, like a CSV file for instance. You can perform operations on this data like finding average, median, quartiles, standard deviation and so on, but for certain kinds of data, there are important trends and findings that could be missed unless you actually plot out all of the data. For our purposes we'll be tracking the price of gold over time since 1965. This will be somewhat interesting since gold peaked significantly a few years ago and the graph will allow us to see when this happened and how significant it was. This is a fairly easy thing to plot since it will just be the value of gold at specific dates. More complex data needs to be 'cleaned and scrubbed' in order to be analyzed, but that is beyond the scope of what we'll be doing.

# Anaconda Installation

For doing scientific work and data analysis, the program Anaconda is incredibly useful as well as user-friendly. 

[Download Anaconda here](http://continuum.io/downloads)

Once that is installed, open it and launch iPython Notebook. Click **New** and then **Python 2**. This creates an iPython notebook where you can keep lines of code as well as their output. It's different from typical Python in that this output can be saved and persists even after the launcher is closed. It's useful for analyzing data and presenting the findings.
# Plotting the Data
Start by importing the necessary libraries
```
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```
In iPython you'll run each block by pressing the play button in the top menu.
Pandas is the library which allows us to process data like the CSV file we will be reading in. Matplotlib is the library which allows us to graphically plot the data. The last line is what's called a Magic Function. Essentially it is a special iPython function which allows us to graph the data inline within the notebook. 
Next write the following code and run:
```
pd.set_option('display.mpl_style', 'default') 
```
This sets the style of the graph, making it look a little prettier in general. Now that we've laid all of the groundwork, it's time to read in the csv data. You can download the [data from here.](https://www.quandl.com/api/v1/datasets/FRED/GOLDPMGBD228NLBM.csv) Once the data is downloaded, read it into the variable `data` by running the command:
```
data = pd.read_csv('/path-to-file/FRED-GOLDPMGBD228NLBM.csv')
```
**Be sure to replace 'path-to-file' with the path to where you downloaded your file**

A good methodology when working with data is to always check the table that you have imported to make sure that everything got read in properly. Run the following command to read the first 3 rows of the table.
```
data[:3]
```
![data table](http://i.imgur.com/TkPSQLy.png)

You'll notice that this is a very similar to how we read into lists. Pandas stores the rows of the table in a similar way to how list items are stored, which gives us this ability. The table looks pretty good, so let's try graphing it using 
```
data['Value'].plot()
```
Which plots the series 'Value' against the index, which is just the sequence of numbers on the left currently. We get a graph that looks like

![basic graph](http://i.imgur.com/LmmVYPV.png)

So that's not exactly what we're looking for. To begin with the x axis doesn't represent time, we need to clean this up a little bit so let's go back to the read_csv file and revise a bit.
```
data = pd.read_csv('/Users/jonah/Downloads/GOLD.csv', index_col = 'Date', parse_dates = 'Date')
```
The index\_col argument allows us to define which column will index the data. The parse_dates argument allows pandas to understand that we are passing date values and to process them accordingly. The resulting graph with the new arguments looks like
![improved graph](http://i.imgur.com/bA5Ww69.png)

This looks a lot better! We can see a huge spike around 2011 which far outweighs any other spike before it.
# Next Steps
The graph we created is good for gathering some information for making decisions perhaps, but if you ever want to present your data for scientific or business purposes, a lot more work needs to be done. Properly labeling axes, putting in a legend and qualifying the results, for example.
This is beyond the scope of what we do, but if you liked what you did here, we recommend signing up for the Data Analyst Nanodegree. Data is a very interesting and rapidly growing field. Part of the appeal is that data is accessible everywhere, so anybody can go in, analyze it, and find some very interesting results. Google is predicting flu outbreaks, Nate Silver is predicting presidents, and insurance companies are predicting claims. What will you discover?

Here are some good resources
* [Bureau of Labor Statistic](http://www.bls.gov/)
* [World Bank Data](http://data.worldbank.org/)
* [Google N-Gram Viewer](https://books.google.com/ngrams)
