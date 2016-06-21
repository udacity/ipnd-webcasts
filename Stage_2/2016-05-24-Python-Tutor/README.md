# Webcast: Python Tutor

## Recording

You can watch the recorded webcast [here](https://www.youtube.com/watch?v=hrSWb6kPmlA)

## Main Features of Python Tutor

[Python Tutor](http://pythontutor.com/) is a resource that could prove helpful for you as you start writing your own computer programs. Python Tutor visualizes your code at every step of its execution.

Let's start with some example code:

```
def listSum(numbers):
  if not numbers:
    return 0
  else:
    (f, rest) = numbers
    return f + listSum(rest)

myList = (1, (2, (3, None)))
total = listSum(myList)
```

If we input this to Python Tutor and click "Visualize Execution" we can step through this code line-by-line.

Click "Forward >" and you'll see that Python has defined the function `listSum` in the "Global frame"

Notice that Python Tutor also uses green and red arrows to indicate the line that was just run and the next line to run, respectively. After defining `listSum` at line 1, you might think that the next line to execute is line 2. But look at the red arrow, it's pointing to line 8! In Python, defining a function __does not run it__. So we skip over the code in the function and go to the next line at the global scope.

Python then defines a tuple names `myList` and then we call the `listSum` function on the value of `myList`. Notice that Python Tutor has visualized this function call with a new frame, named `listSum`. This is the "local frame" of the function we just called. 

We can follow along with the rest of the code using Python Tutor, which will use arrows to indicate return values. Notice that every time we call `listSum` again, a new local frame is created. The values created in one frame are not accessible in another, unless they communicate via a return statement.

At the end we can see the final result, `6`, saved to the variable `total` in the global frame.

Try running your own code in Python Tutor! Is there anything that it does that surprises you?