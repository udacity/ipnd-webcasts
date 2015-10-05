List Comprehensions and Generators
===

# Introduction

This Webcast session will be about list comprehensions -- a faster, cleaner-looking way to generate iterable structures like lists, tuples, dictionaries, and generators.

List comprehensions are used in Stage 4 and Stage 5 to generate complex lists. You will find them all over the place in your career developing in python, so it is definitely a useful syntax to get accustomed to and try out on your own.

At the end of the Webcast session, we will understand:

* How list comprehensions can be used to quickly generate iterable structures
* How to use generators and the yield statement to create a "disposable", iterable data structure
* Why speed and memory efficiency are desirable to have in code, balanced with code readability

# What is a List Comprehension?

A list comprehension is best understood by demonstration. Imagine that you are trying to fill a list with the numbers 0 through 9. Using a for-loop, the most efficient way to do this would be:

```python
# for-loop demonstration
numbers = []
for i in range(10):
  numbers.append(i)
```
This syntax is the most efficient way that we currently know of to add things to a list in python. This same list can be built using a list comprehension:

```python 
# list comprehension demonstration

numbers = [i for i in range(10)]
```

Wow! We just turned a three-line chunk of code into one! You can test out the two different techniques in your python console and see that you get the same value for `numbers` in each case. Let's break down what's going on here:

* furthest to the left is the name of the variable we store the result of the list comprehension into: `numbers`

* the square brackets ([ ]) are the usual syntax we use to indicate an empty list. By have the for-loop inside it, we are basically telling python "whatever the result of this for-loop is, it should go into a list"

* the `i` furthest to the left within the square square brackets is the variable that we are telling python to store in the list we are building. We can manipulate the value of whatever `i` is to how we would like to add it to the list -- we can store `i-1`, `i**2`, even store `i` into a list like this `[i]`!

* We don't need to use `i` per se -- `i` is just the variable name we give for the element that we are looking at in the for-loop, which is exactly the same syntax as it always is. 

What we CAN'T do is try to execute a statement that does an I/O operation on the `i` furthest to the left -- for example, we can't have something like:

```python
# this will result in syntax error
numbers = [print(i) for i in range(10)]
```

But we CAN call a function that manipulates `i` and then sends it back to be stored in the list. For example, this is perfectly valid code:

```python
# this function prints the number, x, and returns it with 1 added to it
def print_and_add_one(x):
    print x
    return x+1

# this code will not result in a syntax error
numbers = [print_and_add_one(i) for i in range(10)]
```
We can also add conditionals to our list comprehensions. To add a conditional to our for-loop, we tack it on to the end. See this example that creates a list of even numbers using the modulus operator (%). If you have never seen the modulus operator before, just think of it as the "remainder operator", like the remainder resulting from when you divide some number by another.

```python

# store only even numbers
# numbers are even when there are divisible by 2, that is, when they have no remainder
even_numbers = [i for i in range(10) if i%2==0]
```

If we want to make a double for-loop, or triple and so on, you can do that too! For every nested loop you need, just put them one after the other (but you must be careful: list comprehensions can become difficult to read when you have too much code in them):

```python
multiple_nums = [j for i in range(3) for j in range(10)]
```
and if you would like a conditional, just take it onto the end of the for-loop that is associated with it. Moreover, you can make a list comprehension within a list comprehension: 

```python
multiple_num_lists = [[j*i for i in range(3)]for j in range(10)] 
```
Try these out in your favorite python console and see what you get!

Here is a more complicated example that uses the power of list comprehensions to generate a list of primes from 0 to 50:

```python
# a list of non-prime numbers:
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]

# list of primes
primes = [x for x in range(2, 50) if x not in noprimes]
```

## Dictionaries

- iterating over an existing dictionary
- creating a dictionary

##Tuples

# Generators and the `yield` statement

So far in your python education you have come across a variety of different data structures including lists, dictionaries, and tuples. Each of these data structures are known as iterable structures, meaning we can go through each element one-by-one.

Another type of data structure that list comprehensions allow us to introduce are generators. Generators are a type of iterable data structure that can only be traversed once (in other programming languages, generators are often called iterators).

```python
```
















The constructor tells us that whenever we create a new object, we will create a new object with the position x and y, width, height, color, and velocity. Velocity will be a 2-dimensional list that contains the magnitude and direction that will help us calculate the position of our object for any frame.

We now want to program some helpful functions that will help us get and set information in our Shape object:

```python
  # Getters and Setters
  def get_vel(self):
    return list(self.vel)

  def set_vel(self, vel):
    self.vel = list(vel)

  def get_position(self):
    return tuple([self.x,self.y])

  def set_position(self,x,y):
    self.x = x
    self.y = y
```

Next we want to create our animation methods to help us update the position of our object and help us detect whether our object collided with the edge of the canvas

```python
  # Animation methods-------------------------------------------------------------------------------
  def update(self, canvas):
    """Updates x and y position of shape based on the shape's current state."""
    self.x += self.vel[Shape.x_pos]/float(FPS)
    self.y += self.vel[Shape.y_pos]/float(FPS)
```

This small function is the work horse of our entire animation because upon the call to `update()`, the x and y position of our object changes due to the velocity vector. Notice how we are dividing x and y components of our velocity by the variable `FPS`. This is purely used as a convenience factor for us when we set the velocity. When we set the velocity, it helps us to think in pixels per second. This conversion will convert the rate from pixels per second to pixels per frame.

## The Circle Class

We can now dive into the specific functions that make up the Circle class.

```python

class Circle(Shape):
  """Inherits from Shape class that contains that creates circle objects on the canvas and handles
  collisions between Circle objects
  """

  def __init__(self, vel, width, height, color, canvas_width, canvas_height, x=None,y=None):
    assert width == height, 'Width and Height need to be the same!'
    Shape.__init__(self, vel, width, height, color, canvas_width, canvas_height,x,y)

    self.radius = width/2
    self.center = (self.x + self.radius, self.y + self.radius)
```

We can see that we are inheriting the Shape class from the first line `class Circle(Shape):`. We are also overriding the Constructor method that Shape has. Since our shape is now a circle, there are two properties that would be useful for us to know: radius and center point.

The center point is the point at the center of the circle. Knowing the center of the circle is useful to calculate collisions and perform other calculations on the circle, so we need to add in a center attribute for all of our circle objects.

We also override the update function as well:

```python
  def update(self, canvas):
    """Updates the circle's center position in addition to its x and y position."""
    Shape.update(self, canvas)
    self.center = (self.x + self.radius, self.y + self.radius)
```

We can now move on to two new functions that are specific to our Circle class:

```python
@classmethod
  def create_random_circle(cls):
    """Creates a circle with random size, velocity, and colors"""

    min_width = 20
    max_width = 80
    min_speed = -400
    max_speed = 400

    colors = ['orange','blue','red','purple','cyan','yellow','magenta']

    width = random.randint(min_width, max_width)
    height = width

    vel = [random.randint(min_speed, max_speed),
           random.randint(min_speed, max_speed)]

    color = colors[random.randint(0,len(colors) - 1)]

    return cls(vel,width,height,color,Application.canvas_width,Application.canvas_height)
```

`create_random_circle` is a class method that takes in a reference to the class itself and does not belong to any object of the Circle class. This means that this function is at the class level and we call this class method like this: `Circle.create_random_circle()`.

Class methods are useful because we do not need to create instances of the same function per object, improving our efficiency.

We calculate our random variables and then return a new Circle object by invoking the Circle's constructor function:

`return cls(vel,width,height,color,Application.canvas_width,Application.canvas_height)`

`cls` is a reference to the Circle class itself.

Our final function to program is the draw function:

```python
def draw(self, canvas):
    """Takes in a canvas object and will draw a circle on the canvas object."""
    canvas.create_oval(self.x, self.y,
                       self.x + self.width, self.y + self.height,
                       fill = self.color,
                       width = 0)
                       
```

We use the `create_oval` method to actually draw the circle and fill it with the object's color

# Edge Collision

In order to detect whether the object has hit the edge of our canvas, we create a bounding box that is an imaginary box that covers our circle:

![](images/bound_box1.png)

If we were to analyze this bounding box further, we can see that we have four points that we can use in order to see whether the edge of the canvas crosses the edge of one of our bounding boxes

![](images/bound_box2.png)

Therefore, we can say that for any edge on the canvas, if the object's edge is at or beyond the edge of the canvas, we can say that the object collides with the edge and therefore we should change our velocity to have the object bounce back towards the inside of the canvas.

For example, to check whether the bounding box collides with the top edge of the canvas, we do:

`if obj.y <=0:`

The canvas coordinate system starts with (`0,0`) on the upper left corner of the canvas and (`canvas_width, canvas_height`) will be the lower right hand corner of the canvas:

![](images/canvas.png)

Therefore if we want to check whether the object edge is at or beyond the top edge of the canvas, we check whether `obj.y` is less than or equal to 0

If we want to check whether the bottom of the bounding box collides with the bottom edge of the canvas, we do:

`if obj.y + obj.height >= canvas.height`

Therefore our edge collision function can be:

```python
def edge_collision_check(self, canvas, canvas_width, canvas_height):
    """Assumes bounding box is rectangular in shape. Checks whether the edges of the bounding
    box intersect the edges of the canvas. If the shape is at the edge of the canvas, function
    updates the velocity vectors to bounce the shape away from the edge.
    """

    # Check top and bottom edges
    if self.y <= 0 or self.y + self.height >= canvas_height:
      self.vel[Shape.y_pos] = -self.vel[Shape.y_pos]

    # Check left and right edges
    if self.x <= 0 or self.x + self.width >= canvas_width:
      self.vel[Shape.x_pos] = -self.vel[Shape.x_pos]

```

# Putting Everything Together

Once we've created our classes, we can simply instantiate our objects and call the update methods for each object. Here is the final code with updated object creation and object update methods.  
               
```python
# Object Oriented Programming Example with Bouncing Balls using Tkinter GUI library: Final Code
from Tkinter import *
import random

# Define Settings, Globals, and other helper variables

PROGRAM_NAME = 'Bouncy'
FPS = 60
MS_PER_FRAME = int(1.0/FPS * 1000)            # Will equal 16 milliseconds

# Define Classes------------------------------------------------------------------------------------

class Shape(object):

  # Private variables
  x_pos, y_pos = 0, 1

  def __init__(self, vel, width, height, color, canvas_width, canvas_height, x=None, y=None):
    """Constructor for Shape. Randomly assigns a position of the shape in the canvas and
       assigns the velocity list [x,y] as a velocity vector to the shape.
    """
    self.x = random.randint(0,canvas_width - width) if not x else x
    self.y = random.randint(0,canvas_height - height) if not y else y
    self.width = width
    self.height = height
    self.color = color
    self.vel = list(vel)                      # We need to make a copy of the                         list or else
                                              # there will be reference errors

  # Getters and Setters
  def get_vel(self):
    return list(self.vel)

  def set_vel(self, vel):
    self.vel = list(vel)

  def get_position(self):
    return tuple([self.x,self.y])

  def set_position(self,x,y):
    self.x = x
    self.y = y

  # Animation methods-------------------------------------------------------------------------------
  def update(self, canvas):
    """Updates x and y position of shape based on the shape's current state."""
    self.x += self.vel[Shape.x_pos]/float(FPS)
    self.y += self.vel[Shape.y_pos]/float(FPS)

  def edge_collision_check(self, canvas, canvas_width, canvas_height):
    """Assumes bounding box is rectangular in shape. Checks whether the edges of the bounding
    box intersect the edges of the canvas. If the shape is at the edge of the canvas, function
    updates the velocity vectors to bounce the shape away from the edge.
    """

    # Check top and bottom edges
    if self.y <= 0 or self.y + self.height >= canvas_height:
      self.vel[Shape.y_pos] = -self.vel[Shape.y_pos]

    # Check left and right edges
    if self.x <= 0 or self.x + self.width >= canvas_width:
      self.vel[Shape.x_pos] = -self.vel[Shape.x_pos]

class Circle(Shape):
  """Inherits from Shape class that contains that creates circle objects on the canvas and handles
  collisions between Circle objects
  """

  def __init__(self, vel, width, height, color, canvas_width, canvas_height, x=None,y=None):
    assert width == height, 'Width and Height need to be the same!'
    Shape.__init__(self, vel, width, height, color, canvas_width, canvas_height,x,y)

    self.radius = width/2
    self.center = (self.x + self.radius, self.y + self.radius)

  @classmethod
  def create_random_circle(cls):
    """Creates a circle with random size, velocity, and colors"""

    min_width = 20
    max_width = 80
    min_speed = -400
    max_speed = 400

    colors = ['orange','blue','red','purple','cyan','yellow','magenta']

    width = random.randint(min_width, max_width)
    height = width

    vel = [random.randint(min_speed, max_speed),
           random.randint(min_speed, max_speed)]

    color = colors[random.randint(0,len(colors) - 1)]

    return cls(vel,width,height,color,Application.canvas_width,Application.canvas_height)

  def update(self, canvas):
    """Updates the circle's center position in addition to its x and y position."""
    Shape.update(self, canvas)
    self.center = (self.x + self.radius, self.y + self.radius)

  def draw(self, canvas):
    """Takes in a canvas object and will draw a circle on the canvas object."""
    canvas.create_oval(self.x, self.y,
                       self.x + self.width, self.y + self.height,
                       fill = self.color,
                       width = 0)

  def circle_collision_check(self, objects):
    """Bonus: Add in our circle collision check to calculate collisions amongst circle objects.
       Reference article to read: http://simonpstevens.com/articles/vectorcollisionphysics
    """
    pass

# Define Main GUI Application-----------------------------------------------------------------------

class Application(Frame):

  canvas_width = 800
  canvas_height = 800

  def __init__(self):
    Frame.__init__(self, master=None)
    self.grid()
    self.__create_widgets()
    self.__create_canvas_objects()
    self.__animate()

  def __create_widgets(self):
    """Creates all widgets for the Application Frame."""
    canvas_options = {'width' : Application.canvas_width,
                      'height': Application.canvas_height,
                      'bg'    : 'white'
                     }

    self.__canvas = Canvas(self, canvas_options)
    self.__canvas.pack()

  def __create_canvas_objects(self):
    """Initialize all of our objects to draw on the canvas."""
    self.__objects = []

    # Create 10 random circles to bounce around
    for num in range(10):
      self.__objects.append(Circle.create_random_circle())

  def __animate(self):
    """The animation function that updates all positions, redraws all objects and calls itself
    again.
    """
    # Update all object positions based on their current state: collisions for example
    self.__updateAll()

    # Clear canvas and redraw all objects with their new positions
    self.__redrawAll()

    # This is the key to our animation. We wait MS_PER_FRAME and call our animate function again
    self.__canvas.after(MS_PER_FRAME, self.__animate)

  def __updateAll(self):
    """Updates all object positions and vectors depending on where they are at any point of the
    canvas.
    """
    for obj in self.__objects:
      obj.edge_collision_check(self.__canvas, Application.canvas_width, Application.canvas_height)
      obj.circle_collision_check(self.__objects)
      obj.update(self.__canvas)

  def __redrawAll(self):
    """Deletes all existing objects from canvas and redraws everything"""
    self.__canvas.delete(ALL)

    for obj in self.__objects:
      obj.draw(self.__canvas)
      
def main():
  # Setup application
  app = Application()
  app.winfo_toplevel().title(PROGRAM_NAME)

  # Start application
  app.mainloop()

if __name__ == '__main__':
  main()
```