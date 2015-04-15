import random

class Concept(object):
  """Class that represents our Concept object.
  Each Concept object will have a title and a description property
  """
  def __init__(self,title,description):
    """Constructor to initialize our object"""
    self.title = title
    self.description = description

  def __repr__(self):
    """Represent function that pretty prints the concept when called
    from a terminal"""
    repr_str = 'Title: %s\nDescription: %s\n'
    return repr_str % (self.title, self.description)

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

# ------------------------- Define Global variables ------------------------
TITLE_KEY = 'TITLE:'
DESCRIPTION_KEY = 'DESCRIPTION:'

# ------------------------- Define Helper functions ------------------------

def get_title(concept):
  """Extracts the title from a concept text"""
  start_location = concept.find(TITLE_KEY)      # Find the location of the Start of the title
  end_location = concept.find(DESCRIPTION_KEY)  # Find the end of the title
  print start_location,end_location
  title = concept[start_location + len(TITLE_KEY): end_location-1]  # The title will be between them!
  return title

def get_description(concept):
  """Extracts the description from a concept text"""
  start_location = concept.find(DESCRIPTION_KEY)                 # Find the start of the description
  description = concept[start_location + len(DESCRIPTION_KEY):]  # The description will go to the end of the concpt
  return description

# Here's a function that would load our concepts from a text file alternatively
def load_concepts(file_name):
  """Opens a concept file and returns the text inside the text file"""
  with open(file_name,'r') as file_input:
    lines = file_input.readlines()

  # lines will be a list that contains all of our lines.
  # We use the String.join technique to join all of our elements in the list
  return ''.join(lines)

# ------------------------- Define Main functions ------------------------
def generate_concept_objects(text):
  """Takes the total concepts text, creates Concepts objects, and
  returns a list containing these Concept objects
  """
  concepts = []

  while text != '':
    next_concept_start = text.find(TITLE_KEY)
    next_concept_end = text.find(TITLE_KEY, next_concept_start + 1)

    if next_concept_end >= 0:
      concept_str = text[next_concept_start:next_concept_end]
    else:
      # Else we are at the last concept in the text
      concept_str = text[next_concept_start:]

      # Set next_concept_end to a valid integer so text == '' in order
      # to exit the while loop appropriately
      next_concept_end = len(concept_str)

    # Create new concept object and append to concepts list
    concept = Concept(get_title(concept_str),get_description(concept_str))
    concepts.append(concept)

    # Cut the text and move on to the next concept
    text = text[next_concept_end:]
  return concepts

def generate_concept_objects_reg(text):
  """Use regular expressions to generate the Concept objects
  Returns a list containing these Concept objects"""

  # Import the regular expressions library
  import re

  # To make regular expressions work, we need to add an additional token to signify the end of a concept
  # in our input text, therefore each concept should have '/end' at the end of the concept description
  # Here's where you can read up more on regular expressions and get practice: http://regexone.com/lesson/0
  # Here's a great resource for you to play around with regular expressions with this pattern here: https://regex101.com/r/sU4iY1/1
  pattern = re.compile('(' + TITLE_KEY + r'.+\n(.|\n)*?(?=/end))')
  concepts = pattern.findall(text)

  concept_objects = []
  for concept_tuple in concepts:
    concept_str = concept_tuple[0]
    concept = Concept(get_title(concept_str),get_description(concept_str))
    concept_objects.append(concept)

  return concept_objects

def generate_all_html(concept_list,shuffle=False):
  """Returns a string of all generated html from the concept objects in our
  concept_list. shuffle is a flag that tells us whether the list should be
  randomized.
  """
  all_html = ''

  if shuffle:
    random.shuffle(concept_list)

  for concept in concept_list:
    all_html += concept.generate_html()

  return all_html

def main():

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

# Loading the concepts from a file
# total_concepts = load_concepts('concepts.txt')

# For regular expressions method, we need to add in a token to signify the end of a concept.
  total_concepts_re = """
TITLE: Variables in Python
DESCRIPTION: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
/end
TITLE: Decision Statements
DESCRIPTION: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
/end
TITLE: Loops
DESCRIPTION: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
/end
"""
  # Uses loops to extract the information
  concepts = generate_concept_objects(total_concepts)

  # Uses regular expressions to extract the information
  # concepts_from_re = generate_concept_objects_reg(total_concepts_re)

  print generate_all_html(concepts)

# Call main function
main()
