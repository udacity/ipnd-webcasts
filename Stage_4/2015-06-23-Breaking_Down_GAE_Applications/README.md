# Webcast: Breaking Down GAE Apps

## Webcast Recording/Prezi

Here is the link to the [video][recording]

Here is the link to the [Prezi presentation](http://prezi.com/aioszmdowod3/?utm_campaign=share&utm_medium=copy&rc=ex0share)
##What We Will Learn
We will go over 3 main things in this Webcast:
- Post and Get methods
- Web Apps on Localhost/Deployment
- Templates
- Datastore
- Debugging

###Post and Get Methods
We’re used to webpages being static things hosted by a server. For the purposes of this course, we send either GET requests or POST requests. The way this happens is that when you follow a link or type a url into the browser, your computer will send a small file to the server called a request message. For GET the information in the url is sent in this message and in response we get a message with status and the content.

Let's imagine for example we want to make a change to the website, like posting a comment to a Youtube page.
In this case what’s happening is that the browser is sending a POST request which sends the server a message with the data that we’ve written and the server records our witty comment for everyone to see. 

###Web Apps on Localhost
What you’ll be building in this course works on the same principal for what you see on your computer side, but on the server side things look a little different.
When thinking about your web app, the best way to visualize it is in the folder that you have created for it. The most fundamental part of your app is the Python script app.py. This is the hub of the wheel, the brain of your web app if you will. With your webapp, app.py is what will create the webpage and push it back to your browser whenever it recieves a request.  All the other files serve to support this script, hence the hub analogy.

Localhost is just a fancy word for your home computer. We'll build the app on our own computers and then when we’re done we deploy them on the server, where they are available to anyone with an internet connection.
One of the supporting files which isn’t discussed too much in the course is the .yaml file. This is essentially a file which handles requests made to the server and directs them to the right place. If we have multiple scripts for multiple parts of our site, it points the request to the appropriate script. For this project, since we only have one script, all requests that go to your-app-name.appspot.com/ will run app.py.

###Templates
So there’s other folder within the app folder called Templates, this is where we keep HTML templates for app.py to use. These templates allow us to 
 - keep our python code clean by keeping the html in a separate file. We call this ‘abstraction’ if you remember.
 - It also allows us to reuse code easily, avoiding repetition
 
The templates are coded using something called Jinja. We aren’t really going to cover Jinja, but it’s a way to implement Python functions to create these templates. The Python script passes information through the template to generate the HTML that is included in the response message to the client. In Steve's example: the app.py pulls information from the get request using `self.request.get_all(“food”)` and passes it into a list variable called `food`. It then passes that list into our template comment.html by setting the variable `items` within that to the `items` that we just pulled from the GET request.

###Datastore
Datastore is the last piece of the puzzle and potentially the most confusing. We have one course to teach you everything about databases, which you previously knew nothing about. I will refer you primarily to last week’s webcast which is online. [Mark covered the finer points of how Google Datastore works]()

For our purposes, imagine the datastore as just another server to store data on. The data is stored as individual ‘entities’ which in this case could be a comment on your page. The comment contains a bunch of characteristic information contained within the entity: id, content, author, time of writing, etc. Python takes that information in when the user submits it using a POST or GET request and stores it in the datastore using the `.put()` function. When it’s time to retrieve it, the Python function pulls it out of the server using a database query, puts it into the page and then sends it our way.
####Debugging
One of the best ways to debug your webapp is to check your App Engine Launcher logs. Oftentimes the culprit will show up in the logs and you can track down the problem in your Python file, template file, or yaml file.
##Summary

- POST and GET requests are small files sent to servers to which it responds with its own file containing html
- Google App Engine webapps are centered around the Python script which runs them
- Debug early and often to make sure that you don't get lost in the forest looking for bugs later on.

[recording]: https://plus.google.com/events/cpm2kk5vibmee7in94puhjgid3c?authkey=COSrhrar14PXYA
