




Anthony's Problem:

```python
def split_string(target, separators):
    output = []
    start = 0
​
    for i in range(0, len(target)):
        if target[i] in separators:
            if i != start:
                output.append(target[start:i])
            start = i + 1
    if start != len(target):
        output.append(target[start:])
​
    return output
​
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']
​
out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
# #>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']
​
out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
# #>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
```

Luke's Solution:
```python
#https://www.udacity.com/course/viewer#!/c-cs101/l-48737171/e-48299954/m-48632793
# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.
def split_string(source, splitlist):
    outlist = []
    current = ""
    for character in source:
        if character in splitlist:
            if current:
                outlist.append(current)
                current = ""
        else:
            current += character
    if current:
        outlist.append(current)
    return outlist

    
#Tests:
out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
```

Luke's Problem:

```python
small_brick_size = 1
large_brick_size = 5

def make_bricks(target_len, supply_small_bricks, supply_large_bricks):
    can_make_bricks = supply_small_bricks*small_brick_size + supply_large_bricks*large_brick_size >= target_len
    if not can_make_bricks:
        return False
    len_so_far = 0
    large_bricks_to_buy = 0
    small_bricks_to_buy = 0
    while large_bricks_to_buy < supply_large_bricks and len_so_far + large_brick_size <= target_len:
        large_bricks_to_buy += 1
        len_so_far += large_brick_size
    while small_bricks_to_buy < supply_small_bricks and len_so_far + small_brick_size <= target_len:
        small_bricks_to_buy += 1
        len_so_far += small_brick_size
    if len_so_far != target_len:
        return False
    return small_bricks_to_buy, large_bricks_to_buy


print make_bricks(6, 100, 100)
```

Anthony's Solution

```python
import random
​
def makebricks (small, large, goal):
    sm = 0
    lg = 0
    while goal > 0:
        if large > 0 and goal >= 5:
            lg += 1
            goal -= 5
            large -= 1
        elif small > 0:
            sm += 1
            goal -= 1
            small -= 1
        elif goal > 0:
            return "Not possible"
    return "small: " + str(sm) + " large: " + str(lg)
​
print makebricks(3, 5, 8)
print makebricks(0, 5, 8)
print makebricks(0, 5, 5)
print makebricks(20, 4, 4)
print makebricks(10, 5, 28)
​
# def shuffle(words):
#     words = words.split()
#     for i in range(len(words)-1, 0, -1):
#         j = random.randint(0, i)
#         words[i], words[j] = words[j], words[i]
#     return " ".join(words)
​
# print shuffle("1 2 3 4 5 6 7")
# print shuffle("a b c d e f g")
```
