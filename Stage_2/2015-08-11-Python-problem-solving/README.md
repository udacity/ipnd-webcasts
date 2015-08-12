# Webcast: Problem Solving with Dictionaries and Classes


## Webcast Recording

Here is the link to the [video][recording]
Here are links to [Jonah's Code][code1] and [Mark's Code][code2]

## Challenge 1:
Given a string, return the frequency of each character that occurs within that string disregarding the word "PARAGRAPH:" within the string.


We used the following framework to help us think through any problem:

###Understand the Problem
  - What are the input(s)?
  - What do we need to do to the input(s)?
  - What are the output(s)?

###Plan a solution
  - You can do this on paper!
  - Or with "pretend" code (otherwise known as pseudocode)

###Fill out your solution!
  - Test along the way!

Jonah thought through what sort of functions he would use to work through this problem. He used some pseudocode to outline in plain English what he wants the computer to do. This can either be used directly to translate into proper Python code, or just provide structure for writing out the code independently later on.


###Breaking It Down

Jonah approached the problem by first just making sure that he could work through each character individually. The input was a string and he needed to break it down into characters before analyzing it and returning an array of the frequencies of each character.

 He did this by using a `for` loop that would iterate through each character of input string `article` and then printing for each iteration of the loop. This gave a printout of every character in the article, including the newlines and spaces. Mark gave a further stipulation that newlines and whitespace should be ignored, which Jonah dealt with by including the conditional `if char != '\n' and char != ' ':` to the loop. The code so far would look like:
```
for char in article:
	if char != '\n' and char != ' ':
		print char

```
Everything looks good so far. Jonah realizes that he will need to use dictionaries, which are a Python data structure. Dictionaries contain keys that are paired with values. In this case the key would be the character and its value would be the frequency that it appears in the string.

He defines a dictionary with `distribution = {}` and then adds values to it by writing:
```
for char in article:
	if char != '\n' and char != ' ':
		if char in distribution:
			distribution[char] += 1
		else:
			distribution[char] = 1
	print distribution
```
The print function is at the end is to make sure the whole function worked. When the program runs, there is way too much data displayed and Jonah realizes that the print function is inside the for loop. After he moves it out, the function works, except it is still counting the characters within "PARAGRAPH:" 

He pulls those out by calling `article = article.replace('PARAGRAPH:', '')` and printing that to make sure everything works.
The final code looks like:

```
distribution = {}
article = article.replace('PARAGRAPH:', '')

for char in article:
	if char != '\n' and char != ' ':
		if char in distribution:
			distribution[char] += 1
		else:
			distribution[char] = 1

print distribution
```
## Challenge 2:
Suppose there is a database of dogs. Given a dog's name, write a function to return its age, color, and energy level.

###Breaking It Down

After asking some questions to better understand the problem, Mark breaks it down in the following way: 

What are my Inputs?
	The input is a name. name is a string
	I can assume that all the names given will be unique

I need to search a database. The database can be a simple list or dictionary
	What does this database look like and how does it get stored?
	I will use dictionary to store objects or dogs in my look up dictionary

What are my Outputs?:
	The Function will print out
	colors = ['brown','white','red']
	name = 'Fido'
	age = 2
	energy = 'medium'

So Mark then defines the following class for the dog

```
class Dog(object):
    def __init__(self,name,colors,age,energy):
        """name is string, colors is list, age is integer, energy is string
        """
        self.name = name
        self.colors = list(colors)
        self.age = age
        self.energy = energy
```
He then creates a dictionary called dogs and a sample entry of that dictionary by writing:
```
dogs = {}

dog = Dog('Fido',['white','brown'],2,'medium')
dogs[dog.name] = dog
```
The last line is adding an entry to the dictionary with the key being the dog.name and the value being the object dog (Fido.)

The actual function to be called is defined in the following way:
```
def find_dog(name):
    if name in dogs:
        print name
        print dogs[name].colors
        print dogs[name].age
        print dogs[name].energy
    else:
        print "There are no dogs named: " + name + "!"
```
The function is then called on Fido by using `find_dog('Fido')`

##Summary
When presented with a problem either in the course of working through a project or even in a coding interview, the best way to attack it is to formulate a plan by asking:

What are the inputs?
How do I need to manipulate the inputs?
How do I present the data in the output?

These questions allow us to break the problem into more manageable parts and think about the tools needed to address those parts. Having a plan of attack makes coding much less daunting when you see the blinking cursor on a blank screen.

Jonah takes the approach of getting roughly close to the answer and then coding the last few tweaks to get to the actual answer. Mark takes the approach of understanding the whole problem before gradually getting to the answer. They both use copious print statements along the way to make sure that they are on the right track. Printing allows the coder to validate his/her assumptions so that they don't code themselves into a corner. 

No matter what the situation it's always best to ask yourself (or your interviewer) as many qualifying questions as you need to understand the problem.

[recording]: https://plus.google.com/u/2/hangouts/onair/watch?hid=hoaevent%2Fcm7gab7fo4n4ngkuhkguitarmj0&ytl=Y-9ScYi-BWo&hl=en&t=2.34
[code1]: String_manipulation.py
[code2]: dogs_class.py
