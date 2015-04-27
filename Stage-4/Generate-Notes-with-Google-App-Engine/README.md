# Office Hours: Generate Notes with Google App Engine

## Office Hours Recording

Here is the link to the [Office Hour Recording][recording]

##What We Will Learn
We will go over 3 main things in this office hours:
- How to use webapp2
- How to put your notes up on GAE
- How `*args` and `**kwargs` work as arguments and parameters to functions

###How to use webapp2
A few links which will help you learn how webapp2 works:
- https://webapp-improved.appspot.com/api/webapp2.html
- https://webapp-improved.appspot.com/guide/handlers.html


Every url in your website needs a Handler: A handler will specify what code runs when a user goes to a particular url on your website.

On the bottom of your Google App Engine code, you’ll notice something like this:
```python
app = webapp2.WSGIApplication([
    (r'/products/(\d+)', ProductHandler),
    (r’/‘, ‘HelloWebapp2),  
])
```
Notice the parameter that webapp2.WSGIApplication takes as an input: a list, each containing a tuple matching url *paths* (or, specifically, regex (regular expressions) that match possible url paths) to class names.  This is the ‘routes’ parameter, and it will match each url path set with the class name of the class which specifies the behavior that the particular url path will run on the website.


Each class specified here will also inherit from webapp2 (either directly or indirectly); this time from webapp2.RequestHandler
```python
class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write(‘Hello World!’)
```
These classes will specify HTTP requests and what will be run on those requests; you’ll generally be specifying get() and post() here.

You will normally specify some sort of generic Handler class, which will handle different types of of html generation and which your url path specific classes will inherit from.  An example is below:

```python
import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Handler(webapp2.RequestHandler): 
    """
    Basic Handler; will be inherited by more specific path Handlers
    """
    def write(self, *a, **kw):
        "Write small strings to the website"
        self.response.out.write(*a, **kw)  

    def render_str(self, template, **params):  
        "Render jija2 templates"
        t = JINJA_ENVIRONMENT.get_template(template)
        return t.render(params)   
    
    def render(self, template, **kw):
        "Write the jinja template to the website"
        self.write(self.render_str(template, **kw)) 
```

###Putting Your notes online

One thing that you will use GAE for is putting your notes online.  The easiest way to this would be to use the above basic Handler, and use a get function like the below:
```python
class SomeHandler(Handler):
    def get(self):
        self.render("your_notes.html")
```
Now, if you specify a path for your html to live on, you can view them online!  Let’s use /notes for our path:

```python
app = webapp2.WSGIApplication([
    ('/notes', SomeHandler)
], debug=True)
```
If we want to use css styling, we should make sure GAE uses it:

first, add a folder to our .yaml
```yaml
- url: /static
  static_dir: static
```
Make sure to do this *before* this:
```yaml
- url: .*
  script: main.app
```
Or the static files won't be read.  Then put your css files in that folder you created (which I've named 'static'), and make sure your html references that path.

If you deploy your app from GAE launcher, you can now view your notes directly online!  

###`*args` and `**kwargs`
A useful link explaining how to use them: http://stackoverflow.com/questions/3394835/args-and-kwargs
`*args` can be used to pass multiple parameters into a function, while `**kwargs` can pass an undetermined number of named parameters into a function. 

####Named parameters
Python functions can accept both named and unnamed parameters.  Let's show a function for demonstration:
```python
def some_function(param1, param2):
    print param1, param2
```
Now, we can pass in 2 unnamed parameters and see what we get:
```python
some_function(1,2)
#>>>1, 2
```
This is the normal way you've been passing in parameters to a function.  Parameters can also be specified by name, instead of position:
```python
some_function(param2 = 1, param1 = 2)
#>>>2, 1
```
Notice that we specified param2, which is the second parameter in the definition, first.
####`*args`
Now, moving to passing in function multiple parameters with *args:
```python
some_list = [1,2]
some_function(*some_list)
#>>>1,2
```
Here, you see that despite the fact that the function took 2 parameters, it successfully ran with a single unpacked list as input.  
####`**kwargs`
The same could be done with named parameters:
```python
some_dict = {"param1" : "parameter 1", "param2": "parameter 2"}
some_function(**some_dict)
#>>>parameter 1 parameter 2
```

This can also be done in reverse; defining a function to take multiple parameters, whether named (`**kwargs`) or unnamed (`*args`)
```python
def some_other_function(*args, **kwargs):
    for arg in args:  #args is like a list
        print arg
    for kwarg in kwargs:  #kwargs is like a dictionary
        print kwarg, kwargs[kwarg]

x = 1
y = 2
z = ['a', 'b']
a_dict = {'hello': 'World!'}
a_tuple = (1,2,3,4,5)

some_other_function(x, y, z, some_dictionary = a_dict, some_tuple = a_tuple)     
#>>>args:
#>>>1
#>>>2
#>>>['a', 'b']
#>>>kwargs:
#>>>some_dictionary  :  {'hello': 'World!'}
#>>>some_tuple  :  (1, 2, 3, 4, 5)
```

##Summary

- webapp2 is the main Python module you will be using for Google App engine; it creates a WSGIApplication application which will direct your url paths to the Python code which will handle them.  
- `*args` and `**kwargs` can let you give an indeterminate number of parameters to a function, or pass in lists, tuples, or dictionaries into functions which take multiple specific parameters

[recording]: https://plus.google.com/events/c961d2sebb3p5feb3phjunbldmo?authkey=CMTukIqEyNuiIA

