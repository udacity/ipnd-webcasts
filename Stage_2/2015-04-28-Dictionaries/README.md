Air Date: 4/28/2015
[Video](https://plus.google.com/events/c72ie1a5nt2s5ciea6d0cg3vn00?authkey=CNG0vpOezYH7SA)

Webcast: Using Dictionaries in Python
==========================================
##Review of Lists:
Here's a nested list (a series of lists inside another list):
```
coaches = [["Mark", "Intro to Computer Science"],
           ["Jeff", "Web Development"],
           ["Randa", "Intro to Data Science"]]
```
If we want to isolate the information about the first coach, we would use the following line (don't forget that indexes start with 0 in Python):
```
print coaches[0]
```
And we would see:
```
["Mark", "Intro to Computer Science"]
```
If we now want to isolate Mark's favorite class, we would use:
```
print coaches[0][1]
```
```
"Intro to Computer Science"
```
We can also add more information about each of our coaches in the list:
```
coaches = [["Mark", "Intro to Computer Science", "IPND", 13],
           ["Jeff", "Web Development", "FEND", 5],
           ["Randa", "Intro to Data Science", "IPND", 17]]
```
The problem with this type of data storage is that it is necessary to remember where each type of data is stored. Was the coach's favorite course stored in index 1 or 2?

List do however have their benefits, we don't want to ignore that. Lists are great for storing multiple pieces of information in a single variable.
##Using Dictionaries to Avoid the Pitfalls of Lists:
Lets create a dictionary to store Mark's information, we'll start by defining an empty dictionary:
```
mark = {}
```
To add information to the Mark's dictionary, we can do the following where the *key* is `'name'` and the *value* is `'Mark'`:
```
mark['name'] = 'Mark'
```
So now the variable `mark` contains the following:
```
{'name': 'Mark'}
```
Now let's add more information:
```
mark['course'] = 'Intro to Computer Science'
mark['number'] = 13
```
The updated dictionary now looks like this:
```
{'course': 'Intro to Computer Science', 'name': 'Mark', 'number': 13}
```
Unlike lists, the order in which the information is added to the dictionary is not necessarily the order the dictionary displays.

Accessing information from a dictionary is similar to accessing information from a list, but instead of using an index the *key* is used instead.
```
print mark['name']
```
Would print the following:
```
'Mark'
```
**Question:** What happens if you misspell the key?
If we tried to run the following line:
```
print mark['nam']
```
We can expect the following key error:
`KeyError: 'nam'`

**Question:** Can you use other types of values as keys in a dictionary?
Yes! You can use integers and [tuples](https://docs.python.org/2/library/functions.html#tuple).
```
mark[13] = 'favorite number'
mark[(1,2)] = 'San Jose'
```
**Question:** What happens if you use a list for the key value?
Say we did the following:
```
pets = ['Rover', 'Goldie']
mark[pets] = 'Mark's favorite pets'
```
We would get the following error: `TypeError: unhashable type:'list'`
Python doesn't like this beacuse it's fairly easy for use to change the list stored in `pets`:
```
pets.append('Spooky')
print pets
```
```
['Rover', 'Goldie', 'Spooky']
```
##Useful Things to Know:
 - `print mark.keys()` returns a list of all the keys unsed in the dictionary `mark'.

 - Way to define the contents of the dictionary all at once:
 
```
mark = {
    'name': 'Mark'
    'course': 'Intro to Computer Science'
}
```
 - Nested dictionaries
```
coaches_dictionary = {
    'mark': {
        'name': 'Mark'
        'course': 'Intro to Computer Science'
    }
    'jeff': {
        'name': 'Jeff'
        'course': 'Web Development'
    }
    'randa': {
        'name': 'Randa'
        'course': 'Intro to Data Science'
    }
}
```
  - Accessing information in a nested dictionary:
  ```
  print coaches_dictionary['mark']['name']
  ```

##Interested in More Python Practice? 
Checkout [Learn Python the Hard Way](http://learnpythonthehardway.org/book/ex39.html) and the course material from [Intro to Computer Science](https://www.udacity.com/course/intro-to-computer-science--cs101).