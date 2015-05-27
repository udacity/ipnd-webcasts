Office Hours: Importance of Coding Style
==========================================

Here is a link to the [Office Hours Session][OH]

# What We Will Learn

  - Understand why having a consistent style is important
  - Understand good HTML and CSS style
  - Understand good Python style

# What is Coding Style?

Coding Style is how we write, organize, and present our code. This includes having consistent indentations, character spacings, variable names, and code organization.


# Why is Style Important?

Writing clean and organized code allows developers to:
  
* Write more efficienty 
* Understand code more efficiently
* Communicate in a common style

Having a good style helps our future selves to dive back into the code quickly and helps us effectively share code with other programmers.

# What's Good HTML and CSS Style?

###HTML

The most important aspects to consider for HTML style is to have:

* Consistent Indentations
* Lower Case Names
* Sparse Comments

####Consistent Indentations

Indentations should be consistent through the code and should follow a natural structure to help a reader understand how each HTML element relates to other elements. An example of good indentation:

```
<div>
  <div>
    <div>
      <p>Hello World!</p>
    </div>
  </div>
</div>
```

We can clearly see how all indentations take up the same amount of space and how each indentation tells us how all the div tags are nested within each other

An example of bad indentation:

```
<div>
<div>
       <div>
   <p>Hello World!</p></div></div>
</div>
```

We cannot really understand how all the `div` tags are structured and it makes it hard to figure out which `</div>` tag goes with its corresponding `<div>`. This can lead to having missing end tags in the HTML.

###Lower Case Names

It's more efficient to code all classes, attributes, and tags with lower case letters because it's faster to read and faster to code:

`<div id="num-1" class="article" tabindex=4></div>`

vs 

`<div iD="NUM-1" Class="Article" TABINDEX=4></div>`

###Sparse Comments

Comments should be used sparingly in HTML and should be used to help outline and organize sections of the HTML code.

```
<div>
  <div>
    <div>
      <p>Hello World!</p>
    </div>
  </div>
</div> <!--End Hello World Section-->
<div>
  <div>
    <div>
      <p>Hello Mom!</p>
    </div>
  </div>
</div> <!--End Hello Mom Section-->
<div>
  <div>
    <div>
      <p>Hello Dad!</p>
    </div>
  </div>
</div> <!--End Hello Dad Section-->
```

[CSS Tricks][HTML] has a great guide to illustrate what great HTML code should look like

###CSS
The most important aspects to consider for CSS style is to have:

* Consistent Indentations
* One attribute per line
* Consistent spaces

###Consistent Indentations

Below code illustrates consistent indentations in CSS:

```
body {
  font-family: Verdana, sans-serif;
  color: #666;
  font-size: 18px;
  line-height: 44px;
}

header {
  margin-top: 14px;
}

h1 {
  text-align: center;
  font-size: 24px;
}
```

Here is what inconsistent indentations look like:

```
body {
font-family: Verdana, sans-serif;
  color: #666;
 font-size: 18px;
 line-height: 44px;
}

header { margin-top: 14px; }

h1 {
text-align: center;
font-size: 24px;
}
```

Notice how it takes us a little bit more time to understand the flow and structure of the CSS code. It's important to make reading code as easy as possible to help other people understand and implement your code.

###One Attribute per Line

For development code, it's good to have one attribute per line. We should never put more than one attribute per line to make things easier to read.

```
body {
  font-family: Verdana, sans-serif;
  color: #666;
  font-size: 18px;
  line-height: 44px;
}
```

vs

```
body {  font-family: Verdana, sans-serif; color: #666; font-size: 18px;
  line-height: 44px; 
}
```

###Consistent Spaces

Spaces between attributes and values should be consistent across your entire CSS file. 
```
body {
  font-family: Verdana, sans-serif;
  color: #666;
  font-size: 18px;
  line-height: 44px;
}
```

vs

```
body {
  font-family:  Verdana, sans-serif;
  color:#666;
  font-size:   18px;
  line-height:    44px;
}
```

We prefer to put a space after the `:`:

`line-height: 44px;` vs `line-height:44px;`

in order to help separate the value from the attribute.

Final note, always remember to put a semicolon at the end of every CSS declaration!

###Tools

Here are some tools that will help clean up HTML and CSS code that you should check out:

[HTML Beautifier](http://www.cleancss.com/html-beautify/)

[CSS Beautifer](http://www.cleancss.com/css-beautify/)

# What's Good Python Style?

* Indentations
* Good Names
* Higher Level Comments


More information on good Python style can be found [here][PEP8]. 

###Indentations
Indentations are critical for Python to work. They also naturally help readers quickly understand the variable and function relationships that exist in the code. The common standard is to indent either with 2 spaces or 4 spaces:

```
def my_function():
  print "Hello!"
```

```
def my_function():
    print "Hello!"
```

Both indentations are correct. Make sure that we stay consistent with our indentation to help increase code readability. Here is an example with low-readability

```
def my_function():
 for num in range(10):
          print "Hello!"
```

The For loop line is indented with 1 space while the print "Hello!" line is indented with nine spaces.

###Good Names

Naming variables in regards to their context is an excellent to have self-documented code. We do not need to add many comments because our variable and function names tell us what exactly they represent. For example take this code:

```
def func():
  for e in range(100)
    print e
```

Prints out the variable `e`, 100 times. By reading the names and variables, it's not clear why we're printing out the variable `e`, 100 times.

We find out from the person who wrote the code that her intent was to count the number of friends she has. Therefore, we can refactor her code to reflect the intent of this code:

```
def count_friends():
  friend_count = 100
  for friend in range(friend_count):
    print friend
```

Just by reading the names, we have a better picture of what this code is trying to do without having to talk with the person who actually wrote this code.

###Higher Level Comments

This transitions into our final style tip: use higher level comments to comment your code. Good programmers will use good variable names and will add in comments to let everyone know "how" and "why" they are coding this section. The "what" is explained by looking at the code, but the "how" and "why" are explained using comments and [Doc Strings][DOCSTRINGS]. Let's put in DOCSTRINGS to tell everyone why this `count_friend` function exists.

```
def count_friends():
  """Function that prints out a number of friends to the screen in order to 
  make sure that we are not missing any friends when calculate the person's popularity. 
  """
  friend_count = 100
  for friend in range(friend_count):
    print friend
```

We now fully understand that `count_friends` to confirm our calculations so we can later calculate the person's popularity in our program.


# Summary

Developing good programming style should be a goal for beginner programmers because it lays the foundation for the programmer to code more efficiently and enable the programmer to successfully share his/her code.

Indentations, spaces, and variables names are one of the most important aspects of programming for any language. It helps organize our code efficiently and helps us better communicate with our fellow programmers.


# Follow Up Questions for Office Hours

Two students asked two great questions relating to styling lists and how to deal with a long link tag during the live Webcast. The questions are:

* How do you only bold the numbering in a ordered list?
> One way is to set the attribute: `font-weight: bold;` for the `li` tag and use a class to set the `font-weight: normal;` for the text that the `li` tag contains using a `span` tag

* How do you deal with long links in html code?
> We can simply put the rest of our code in a new line and leave the long link on one single line. Developers will be able to quickly realize that the long line just contains the long HTML link.

Below is example code that demonstrates these two answers:

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Foo</title>
  <style>

    li {
      font-weight: bold;
    }

    .no-bold {
      font-weight: normal;
    }

  </style>
</head>
<body>
  <ol>
    <li><span class="no-bold">Hello</span></li>
    <li><span class="no-bold">Hello</span></li>
    <li><a href="http://www.longlink.com/fjf/k4k4/fjkssl/kdjff/kfjjff/lksjd/fjdkfjf/kf">
      Long Link Here</a></li>
  </ol>
</body>
</html>
```

[OH]: https://plus.google.com/events/cfk75tn7au58r8ql8v1o9is5jbo?authkey=CPu2xbOt2aXqGA
[HTML]: https://css-tricks.com/what-beautiful-html-code-looks-like/
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[DOCSTRINGS]: https://www.python.org/dev/peps/pep-0257/
