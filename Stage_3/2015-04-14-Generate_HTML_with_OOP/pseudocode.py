# Pseudocode



# Crucial questions we always need to ask:
# What is our input?
#    Block of text that contains concepts
# What is our output?
#    HTML code contains the concept title and descriptions
# How are we going to do this?
#    We want to extract the concepts from this block of text and generate
#    HTML from it. We want to use classes to create objects.


# In a nutshell:
#
# Get the input like:
#   concepts_object_list = generate_concept_objects(block_of_text)
# Output concept title and concept description as HTML
#   print generate_all_html(concepts_object_list)

# Define Class "Concept"

class Concept():

# Each object will contain:
#   title
#   description
#   A generate_html_function

# Once we have our class Concept, we now have a way to load our concepts into
# an object.


# What is our input again?

total_concepts = """
TITLE: Variables in Python
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
"""

# But we need to have a way to load the concepts into our objects,
# therefore let's define a function called:

def generate_concept_objects(concepts_text):

  # Let's plan to return a list of concept objects so we can manipulate in a list
  concept_objects = []

  # Process the string: concepts_text and do other stuff

  # Create class objects such as:
  concept = Concept('concept_title', 'concept_description')

  #Add concept object to my list
  concept_objects.append(concept)

  # Return our list of concept objects
  return concept_objects

# Okay we now have a list of objects, how do we put together all of the HTML?
# Let's create a function called generate_all_html() and take in a
# list of all concept objects

def generate_all_html(concept_object_list):

  # Loop through all concept objects

  # Build a string and add in the string that concept.generate_html() returns
  all_html = ''

    # Loop through my concepts and get the html code from each concept

  return all_html

# Okay we have all the necessary steps we need to take care of, let's
# run these functions

def main():
  # Input!
  concepts = generate_concept_objects(total_concepts)

  # Process and Give Output!
  print generate_all_html(concepts)

# Call our main function to execute the program
main()












