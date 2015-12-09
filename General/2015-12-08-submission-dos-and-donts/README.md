# Submission "Do's and Don'ts"

[Link to the webcast](https://join.onstreammedia.com/play/udacity/8480-common-reasons)

Today we're going to be talking about common reasons why submissions we receive from students don't always meet specifications. Many of you might feel like you're the only one experiencing issues with certain aspects of the projects -- but fear not! Soon enough you'll see that the problems you've been having are not as uncommon as you think. You'll also see that there are only a handful of problems that students are having, and that it's natural to struggle when it comes to programming and web development.

# Project 1

Let's talk about the first project in the nanodegree, "Create Your Own Webpage."

Probably the most common feature lacking from project 1 submissions are notes on the DOM, that is, the Document Object Model of HTML. The DOM is basically just the structure of HTML that allows us to access any "node" in our HTML code given a starting "root" node, because each node is a child of some other node in the HTML structure. And by "node," we mean an HTML tag like "body" or "head." The DOM gives HTML its tree-like structure.

Another common feature we see lacking in Project 1 is mention of a coding resource, like Stack Overflow, Quora, or even Udacity. The use of resources during times of struggle is a time-honored tradition of software development, and everyone -- from the most senior veteran developers to absolute beginners -- utilize coding resources in times of need. That's why it's important that you check one out when you run into road blocks developing, and we want to see that you did. So just remember to mention one in your notes on your webpage!

Finally, remember to pass your HTML through validator online to make sure that you aren't missing any tags -- a very common reason why projects fail. Here's a link to the validator I usually use: http://www.freeformatter.com/html-validator.html


# Projects 2 & 3

Now let's talk about Projects 2 & 3, which deal with coding in Python. While most students tend to struggle with the actual mad libs assignment, most of the failed submissions we receive result from commenting incorrectly and very lengthy functions -- that is, functions of 18 lines or more (and if any more, you should consider the use of helper functions). Let's quickly go over how one can comment code effectively and concisely.

It's generally expected that one comment at the beginning of functions and the beginning of classes as docstrings. In particular there are two things that need to be included when commenting functions:

- comment in a triple quote string right underneath the function declaration
- what the inputs to the function are (if any), and 
- what the function does/output

```python
def add_one(num):
	""" This function accepts a number, num, as input
		and returns that number, plus 1, as output
	"""
	return num + 1
```

And for classes we expect that you:

- comment in a triple quote string right underneath the class declaration
- what the class as a whole is modeling and
- what classes, if any, are being inherited

```python
	class Dog(Animal):
		"""This class models the actions and attributes of a dog.
			The class inherits from Animal because a dog is a type of animal.
		"""
		etc.
		etc.
```

Commenting your code in this way makes it easier for you to understand why you are writing the function you are writing, to help you organize your code, and to make it easier for others to quickly grasp what your code is designed to do. It is also standard to comment particularly complex lines of code using the single-line hash way of commenting (`#`).

For example, here is a particularly complex if-statement:

```python
    # remove periods only from ends of sentences, not from abbreviations
    if words[(i+1) % total_words].istitle() and words[i][-1] == '.':
        sentences.append(words[i].strip(".").lower())
```

# Project 4

## Server-side validation

Stage 4 is probably the most difficult stage in intro to programming because it's really where all concepts you learned about come together. For that reason, it's no wonder that it's in this stage that we see the most failing submissions. 

The most common reason for the failed submissions is not validating user input to *produce* errors. Remember that we're not talking about *producing* errors in the sense that input that will cause your website to crash, which are errors that you would normally see in the error stack trace or what you would see in the logs of Google App Engine. We mean errors that could occur on the user-side, and could cause unexpected behavior on the part of your website, like the user inputing HTML that renders on your page, or the user submitting blank inputs. To handle these errors, you need to *show* the user something on your webpage that indicates they have entered invalid input, or prevent them from entering such input altogether.

Another common reason for a failed submission is not including *why* the previous check is important! In your notes, you need to indicate why, for both the user who might be making a mistake AND for the server-side developer who is trying to maintain her codebase safely, it is important to check for blank inputs and to prevent others from posting code on your website directly and/or stop it from rendering on your page after the user tries to post it.

## Other things to do with Stage 4
Some other more minor reasons that Stage 4 projects don't pass include the following:

- Don't include "magic numbers" in your code; always use variable names, not stray numbers. For example when you write a while loop:

```python
while i < 10:
	# do something
```

is bad. 10 is the magic number here. Instead, you should be doing something like this:

```python
max_cycles = 10
while i < max_cycles:
	# do something
```

- Don't have unused code in your files. Make sure before submitting that every line of code that you have makes some progress towards achieving what your program is intending to do, and any extra code is deleted, not just commented out.

- You need to understand *and take notes on* how servers handle requests, specifically POST requests and GET requests. When are these requests used and what are they intended to do? You have to discuss what types of responses you can expect a web server to send back! For example, what type of response is 300? 404? Anything in the 500s?

# Summary

There are a few simple changes you can make to your code to pass your submissions! Don't be afraid to fail, and don't ever feel like you're the only one making mistakes!