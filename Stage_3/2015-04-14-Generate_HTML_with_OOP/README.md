# Office Hours: Generate HTML In Python With Object-Oriented Programming

## Office Hours Recording

Here is the link to the [Office Hour Recording][recording]

## What We Will Learn

  - Apply Object Oriented Programming to our Python HTML Generator
  - Define a Concept class and create instance method for the Concept class
  - Learn a key framework that all programmers use when they code
  
###Review
  From Stage 2, we programmed a HTML generator. We hope you remember that we programmed a couple of functions that goes through our block of text:
  
> TITLE: Variables in Python
DESCRIPTION: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
TITLE: Decision Statements
DESCRIPTION: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
TITLE: Loops
DESCRIPTION: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  
Our Stage 2 functions are able to extract a particular concept from this block of text and is able to use the title and the description strings to produce our HTML code like this example:

```
<div class="concept">
      <div class="concept-title">
         Loops
    </div>
    <div class="concept-description"><p>
         Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>
    </div>
</div>
```
##Using Object Oriented Programming

There is another method that we use to organize our code using Object Oriented Programming. We will be defining a Class called Concept and we will create objects that represent a Concept. Each instance of the class will contain a title and description variable and a function called generate_html that will produce the HTML that we saw in Stage 2.

Therefore let's refactor our code (reorganize and rewrite) our code so we can use objects instead of a group of strings to represent our Concept object. We'll see that organizing the concepts as objects will make it easier for us to manipulate and organize our concepts.

###What to Keep and What to Refactor

From Stage 2, here is a list of functions that were used:

```
get_title()
get_description()
generate_concept_HTML()
get_concept_by_number()
generate_all_html()
```

If you remember the code from Stage 2, `get_title()` and `get_description()` are small helper functions to help us process our input. These functions are small and efficient and we will decide to keep those functions and not change them. 

The other three functions `generate_concept_HTML()`, `get_concept_by_number()`, `generate_all_html()` will be refactored because we're now going to represent our concepts as objects.

##Pseudocode

We always should start off with an outline or some pseudocode and ask ourselves these three big questions:

1. What is the input?
2. What is our output?
3. How are we going to get from input to output?

The pseudocode found [here][pseudocode] serves as an outline to our thought process of how we are going to refactor the code.

Please take a moment to study the logic and flow of this outline.

As we can see, we have clearly defined our inputs and our outputs at the top of pseudocode.py. These lines:

```
# Crucial questions we always need to ask:
# What is our input?
#    Block of text that contains concepts
# What is out output?
#    HTML code contains the concept title and descriptions
# How are we going to do this?
#    We want to extract the concepts from this block of text and generate
#    HTML from it. We want to use classes to create objects.
```
Help drive the overall flow and organization of our code. This process mirrors a process to writing a paper: we always start off with an outline to understand the bigger picture of what's going on.

Therefore in a nutshell, our program will be doing this:

```
# Get the input like:
concepts_object_list = generate_concept_objects(block_of_text)

# Output concept title and concept description as HTML
print generate_all_html(concepts_object_list)
```

This outline will drive the rest of our code implementation.

##Defining The Concept Class

The rest of the notes will focus on how to implement a class to create our Concept objects.

Remember from the course that we define a class by typing in the code:

`class Concept(object)`

We are being very explicit in inheriting the object class in Python. It's good practice to be very explicit in our class definitions.

We then proceed to define a Constructor function called __init__ that will help us set the title and description:

`def __init__(self,title,description)`

This tells us that whenever we create a new object from this class, we now have a way to pass in the title and description such as:

`concept = Concept('concept title','concept description goes here')`

We then proceed to create our instance function, generate_html():

```
  def generate_html(self):
    """Generates html for our concept"""
    html_text_1 = '''
    <div class="concept">
      <div class="concept-title">
        ''' + self.title
    html_text_2 = '''
    </div>
      <div class="concept-description"><p>
        ''' + self.description + '</p>'
    html_text_3 = '''
      </div>
    </div>'''
    
    return html_text_1 + html_text_2 + html_text_3
```

We refactored this HTML generator function and put this function inside our Class. Now whenever we call this function from our object such as `concept.generate_html()`, the function will be able to pull the title and description data from its object instance using `self.title` and `self.description` in order to generate the HTML code. We no longer need to pass in strings of concept titles and descriptions to a function anymore.

Using objects with functions such as `generate_html()` makes the code shorter and easily scalable.

###Playing With The Concept Objects

Once we're able to represent the concepts as objects, we can easily shuffle our objects and have the ability to organize our objects in a list, similar to picking balls in a bucket.

From the file [Generate HTML OOP.py][full_code], in the `generate_all_html()` function on line 115, we have an option to randomly shuffle the order of the concepts that gets displayed in our HTML. If we pass in `True` to the shuffle keyword, the function will randomly shuffle our concept objects and then proceed to access each concept object's `generate_html()` function.

##Bonus

To further your knowledge in Python, we've included an alternative method to load our total_concepts string from a text file. The function is called `load_concepts`.

In addition, we've included another method to extract our concepts from a block of text using regular expressions. Regular expressions is a method to extract and manipulate substrings in a text. The code is much shorter because we give the regular expressions function a string pattern to search. The regular expressions function will return a list of all matches allowing us to simply manipulate the extracted data from the returned list.

##Summary

Whenever we code a new project, we always need to ask ourselves these three crucial questions:

1. What is the input?
2. What is our output?
3. How are we going to get from input to output?

These key questions will help us outline a plan to code any project. It's important to realize how important research and preparation is in order to successfully program a project.

Object-Oriented Programming is a useful way to organize information in a conceptual way. In this case, we created a Concept class that contains our concept title and concept description with a generate html function. This new way to create a data structure allows us to represent our concept in an object giving us the freedom to manipulate our objects in a concise and efficient way.

[recording]: https://plus.google.com/events/chqthg658so240mlfkuq7jmg03c?authkey=CLiQoMLiw5XUdw
[pseudocode]: pseudocode.py
[full_code]: Generate_HTML_OOP.py
