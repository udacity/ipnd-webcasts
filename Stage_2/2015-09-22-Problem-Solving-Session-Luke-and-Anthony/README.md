




Anthony's Problem:

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
