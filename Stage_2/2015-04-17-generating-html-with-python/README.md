OH: Generating HTML with Python
==========================================

Here is a link to the [Office Hours Video][OH]

###How to break down a problem:

First, look at what your objective is:
 - Generate your HTML with Python using functions

Now, we break down how we are going to attack the problem.

###Output:  What do we want our output and input to look like?

Our output should look like a finished HTML page, or, if it turns out that is beyond our capabilities, as close to a finished HTML page as we can imagine

###Input:  What do we want our input to look like?
        
This one is less clear, so we should consider what our objectives are:

Making our objective of taking notes as easy as possible.  One way to accomplish this would be to use a text file, or, barring that, putting our notes in as a single long string.

Ok, now we know what our program should do; it will turn our input of text notes into output of an html!

So, how do we start here?

We don't currently know how to take text from an input file, so lets start with how to parse a long input string (which we do know how to do).

Before we start, how can we break this into small steps?

We can:

- Make the body piece by piece
- Break pieces into individual concepts

Look at how we can do this for one concept before doing others

###Looking at a single concept

As we're taking notes, we can break things into what the concept name is called and descritions of the concept, we can do the same thing here.  One way to do this is to literally have our notes designate where the title and descriptions are:  
```python
"""
TITLE:  Some title
DESCRIPTION:  Some description

TITLE:  Some other title
DESCRIPTION:  Some other description
"""
```
The above would be two concepts.

Let's see if we can get the title and concept from a single couple of those, so a single concept would be:
```python
"""
TITLE:  Some title
DESCRIPTION:  Some description
"""
```
Finding a single title from a single concept:
```python
def get_title(concept):
    start_location = concept.find('TITLE:')  #Find the location of the Start of the title
    end_location = concept.find('DESCRIPTION:')  #Find the end of the title
    title = concept[start_location+len('TITLE:') : end_location-1]  #The title will be between them!
    return title
```

Now we can do the same thing with the description!
```python
def get_description(concept):
    start_location = concept.find('DESCRIPTION:')  #Find the start of the description
    description = concept[start_location+len('DESCRIPTION:'):]  #The description will go to the end of the concpt
    return description
```
Now that we have the title and description, we can write html for the concept:

```python
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text
```

Ok, so now we can get a single concept's html.  Let's work on combining them.

First, let's be able to get any particular concept:

```python
def get_concept_by_number(text, concept_number):
    counter = 0  
    while counter < concept_number:
        counter = counter + 1  #Which concept are we on?
        #Find the beginning of the next one
        next_concept_start = text.find('TITLE:')  
        #Find end of the next one, which will be the beginning of the one after that
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)  
        #if we got to the last concept, nex_concept_end will be -1, since there won't be another
        if next_concept_end >= 0:  
            concept = text[next_concept_start:next_concept_end]  
        else:
            concept = text[next_concept_start:]
        #Move through the text after we've completely found a concept
        text = text[next_concept_end:]  
    return concept
```

Next, we can use that to write the whole html from our notes:

```python
def generate_all_html(text):
    current_concept_number = 1  
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html
```
Now we can generate some basic html!

There are still some things to do, though.... 

We're going to have to make a desision on our notes; do we want to write some basic html in our notes, or do we want to escape our characters so we can write notes *about* escaped charectars faster?  (If we want to do both, we're going to have to invent our own markup language!)  Do we want to include html headers, designating css and such?  Do we want to get our text from a text file?  All of these are things you can explore if you chose...

[OH]: https://plus.google.com/u/0/events/ce4q4b7kbkk7vqdjlg82n9tsgrg?authkey=CMOi96bUucjhrAE
