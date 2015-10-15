The Importance of Structure
===

Here's a link to the [Webcast][WB]

Anthony and Jonah discuss the importance of structuring code for readability.

# Why care about structure?

Structure refers to the way that your code is written and how it flows. Well structured code is easy to read, debug, and share with others. Poorly structured code, on the other hand, can be none of these things.

Many programmers refer to poorly structured code as "spaghetti." It is loose and tangled; difficult to see any order in its chaos. The term has broad modern usage. Before we had highly structured programming languages (like Python), the following would be common (note this is written in a language called BASIC; even though you don't know this language you can probably still read it):

```
10 i = 0
20 i = i + 1
30 PRINT i; " squared = "; i * i
40 IF i >= 10 THEN GOTO 60
50 GOTO 20
60 PRINT "Program completed."
70 END
```

Confusing huh? This program prints out the squares of all numbers from 1 to 10, but it's difficult to read. The `goto` command used to be very common in programming, and it's a very powerful way of managing control flow by instructing the computer to go to a specified line of code. However, it's much more difficult to read than the structured alternative in Python:

```
for i in range(1, 10):
    print i, "squared =", i * i
print "Program completed"
```

Much easier to understand! Under the hood, the Python interpreter converts this code into instructions for the machine, and those instructions do contain a `goto` statement in some form (that's how the flow returns to the beginning of the loop). But thanks to modern programming, we don't have to deal with that at the top level. `goto` can now only explicitly be used using the joke `goto` module which was released as an April Fools joke in 2004.

Using that module, the bad Python code would be:

```
from goto import goto, label
i = 0
label .start
i = i + 1
print i, "squared =", i * i
if i >= 10:
	goto .end
else:
	goto .start
label .end
print "Program completed."
```

Just. So. Ugly.

# Modern spaghetti

Nowadays, spaghetti code refers less to its original meaning, and more to poor use of Python's structure. Here's a more modern example of spaghetti. In this code, we want to determine the shipping costs of a product bought online. If the shipping address is in the continental US, the cost will be $5. If the shipping address is international or in Hawaii or Alaska, the cost will be $10. Here's two possible ways of solving this

```
def shipping_costs(country, state):
    if country == "USA" and \
        (state != "Hawaii" and state != "Alaska"):
            cost = 5
    else:
        cost = 10
    return cost

print shipping_costs('USA', 'California')
print shipping_costs('USA', 'Alaska')
print shipping_costs('Germany', None)
```

```
def shipping_costs(country, state):
    if country == "USA":
        if state != "Hawaii" and state != "Alaska":
            cost = 5
        else:
            cost = 10
    else:
        cost = 10
    return cost

print shipping_costs('USA', 'California')
print shipping_costs('USA', 'Alaska')
print shipping_costs('Germany', None)
```

The first solution is difficult to read because of the first if statement. It's very verbose and it takes time to figure out what it's actually checking for (it's checking if the location is in the US but not in Hawaii or Alaska).

The second solution is confusing for a different reason, namely its nested if statement. In particular, the repeated `else` statement is not clear since it is not immediately obvious which cases fall into that.

Let's try refactoring this:

```
def shipping_costs(country, state):
    if country != "USA":
        cost = 10
    elif state == "Hawaii" or state == "Alaska":
        cost = 10
    else:
        cost = 5
    return cost

print shipping_costs('USA', 'California')
print shipping_costs('USA', 'Alaska')
print shipping_costs('Germany', None)
```

That's better. Our "spaghetti noodles" are more nicely laid out and we can see the structure of this code much better. You may be thinking, "But wait, we assign the value 10 to `cost` twice. Why not just combine those two conditionals?" While we could do that, and thus cut out that `elif` statement, the context of our problem makes it more natural to separate the cases for ease of readability. Hawaii and Alaska are parts of the US after all!

# Object-oriented spaghetti

Object-oriented programming is a really powerful programming technique, and in many ways its relatively recent popularity has dramatically changed the world of computer programming! However, as with any tool, there are dangers of using it incorrectly. Object-oriented spaghetti is a specific type of spaghetti code. It doesn't look like the examples we've already seen, so we'll have to think a little more abstractly.

There are lots of ways that OOP can turn into a sloppy mess of spaghetti code, but the one we'll focus on now is circular dependency. Consider the following two classes for example:

```
class Car():
    def __init__(self, model, driver):
        self.model = model
        self.driver = driver
    def is_driven_by(self):
        return self.driver.name

class Driver():
    def __init__(self, name, car):
        self.name = name
        self.car = car
    def drives(self):
        return self.car.model

optima = Car('Optima', None)
anthony = Driver('Anthony', optima)
optima.driver = anthony

print "Anthony drives an", anthony.drives()
print "The Optima is driven by", optima.is_driven_by()
```

You might ask, "Why is this bad? Cars need drivers and drivers need cars, so this seems to make sense." The issue is that this type of code is really hard to maintain. With this structure, the two classes essentially become one object. Furthermore, you can't run tests on the Car class without the Driver class. Modifying one of these classes will have a direct effect on the other. Notice in particular the confusing way in which we must intialize an instance of the Car class since it depends on the existence of a Driver.

In particular, it's very easy to find yourself in a circular dependency if you're working with classes in different files. If Car and Driver were classes in separate `.py` files you might accidentally code them so that they depend on each other, and then you'll have yourself a big plate of OOP spaghetti. Sometimes you'll want to develop some sort of dependency between classes. But if you plan out your structure beforehand you'll be able to avoid making this dependency circular. Let's refactor the example so there's only a one way dependency:

```
class Car():
    def __init__(self, model):
        self.model = model

class Driver():
    def __init__(self, name, car):
        self.name = name
        self.car = car
    def drives(self):
        return self.car.model

optima = Car('Optima')
anthony = Driver('Anthony', optima)

print "Anthony drives an", anthony.drives()
```

Here we've made the design choice to only have Driver depend on Car. We could have done this the other way, but I find this more natural. After all, a car can exist without a driver, but a driver is just a person without their car!

A great piece of advice: "Never adapt a language to fit your design, adapt your design to fit a language!"

[WB]: https://plus.google.com/events/cavgrjngs1jqv3su7eslf4a4438?authkey=COnLwf_ord7nMg