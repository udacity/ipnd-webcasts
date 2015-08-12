# What are my Inputs?

# The input is a name. name is a string
# I can assume that all the names given will be unique
#
# I need to search a database. The database can be a simple list or dictionary
#
#   What does this database look like and how does it get stored?
#     Will use dictionary to store objects or dogs in my look up dictionary

# What are my Outputs?
# function will print out
# colors = ['brown','white','red']
# name = 'Fido'
# age = 2
# energy = 'medium'


# define class Dog first
class Dog(object):
    def __init__(self,name,colors,age,energy):
        """name is string, colors is list, age is integer, energy is string
        """
        self.name = name
        self.colors = list(colors)
        self.age = age
        self.energy = energy

# populate dictionary of dog objects
dogs = {}

dog = Dog('Fido',['white','brown'],2,'medium')
dogs[dog.name] = dog


# write function to look up dog objects by name and print out attributes
def find_dog(name):
    if name in dogs:
        print name
        print dogs[name].colors
        print dogs[name].age
        print dogs[name].energy
    else:
        print "There are no dogs named: " + name + "!"


find_dog('Fido')