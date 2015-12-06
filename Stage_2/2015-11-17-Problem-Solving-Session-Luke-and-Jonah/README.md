#Problem Solving Session

The link to the video can be found [here](https://plus.google.com/u/0/events/c9vns1l2dqmqj43gc0npabsn53k?authkey=CMLg6p_swOOEowE).


Today we'll be solving two problems live.  In the first, Jonah presents Luke with the problem found [here](http://codingbat.com/prob/p118406).  In the second, Luke gives Jonah the problem found [here](https://projecteuler.net/problem=11).  

###First problem
First, the problem stump:

We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops

This is pretty similar to a problem Luke solved with Anthony a few months ago; his first approach is very similar to that one:

```python
def make_bricks(small, big, goal):
    current_len = 0
    big_used = 0
    small_used = 0
    while current_len < goal:
        counter += 1
        if big_used < big and current_len + 5 <= goal:
            big_used += 1
            current_len += 5
        elif small_used < small and current_len + 1 <= goal:
            small_used += 1
            current_len += 1
        else:
            break
    if current_len == goal:
        return True
    return False
```

However, the website wasn't accepting the answer because it was timing out!  To figure out what was happening, Luke started to test it on his own machine.  To do this, he added a counter and a break to make sure that the loop would definately finish:

```python
def make_bricks(small, big, goal):
    current_len = 0
    big_used = 0
    small_used = 0
    counter = 0
    while current_len < goal:
        counter += 1
        if big_used < big and current_len + 5 <= goal:
            big_used += 1
            current_len += 5
        elif small_used < small and current_len + 1 <= goal:
            small_used += 1
            current_len += 1
        elif counter >1000:
            print "infinite loop"
            break
        else:
            break
    if current_len == goal:
        return True
    return False
```

This seemed to work perfectly on his machine, but the website still wouldn't take the answer.  After noticing that the website said a loop wasn't necessary, Luke tried to solve the problem without using any loops.  To do this, he utilized Python's integer floor rounding. 

#####Integer division
In Python, as well as many other languages, if you divide two ints, you will always get an int as an answer, even though the numerator may not be divisible by the denominator.  It does this by *always* truncating (rounding down).  So, in Python, 5/2 == 2, although any float makes the answer a float (5.0/2 == 2.5).

#####Back to first problem

Luke then solved the problem without loops:

```python
def make_bricks(small, big, goal):
    if big * 5 + small < goal:
        return False

    max_with_big = big * 5
    if max_with_big >= goal:
        big_used = goal // 5
    else:
        big_used = big
    left = goal - big_used * 5
    if small >= left:
        return True
    return False
```

This, the website accepted!

###Second Problem



