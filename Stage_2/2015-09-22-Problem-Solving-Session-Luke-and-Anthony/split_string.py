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

#Luke's Solution
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


#Anthony's Solution
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

#Tests
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
