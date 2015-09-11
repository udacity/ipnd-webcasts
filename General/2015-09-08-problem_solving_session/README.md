Problem Solving Session
==========================================

Here is a link to the [Webcast][WB]

Mark and Michael will run through two problems and demonstrate how to approach solving the probems in Python.

## Problem 1

Mark asked Michael the question:

> If I have a list of random numbers, what is the distribution of numbers in this list?

In other words, what is the frequency of the numbers that show up in the list. For example, given a list:

`my_list = [1,4,2,1,4]`

The distribution of the numbers of this list is:

> Number 1 appears 2 times
> 
> Number 2 appears 1 time
> 
> Number 4 appears 2 times

Therefore, Michael's first steps was to first understand the problem and define the inputs and outputs of his problem. He first planned out what are necessary steps to work from his input to produce his output. He wrote an outline:

```python
#Tally the occurrences of numbers

#Problem: Given a list of integers, I want to count their frequency

#Input: list1
#     for example, list1 = [0 1 24 3 14 5]

#Output: A dictionary containing the numbers in list1 and how often they appeared

#Plan:
#     Going to use while loop
#     The loop will continue as long as complete = 0, where complete is 0 if list1 still has numbers in it

#     Each loop we will do the following:
#       - Record the first entry as new_number in list1 
#       - Determine how many entries are in list1
#       - Use a for loop to count how many times new_number appears
#       - Record the index where in list1 each instance occured
#       - Exit for loop and delete all entries in list1 at the recorded indices
# 
#     Record new_number value and tally in a dictionary
#     Check to see if length(list1) == 0 if it is then exit while loop
#
#     Print results!
```

This is key to solving problems in general: write out what we plan to code first and then code it later in the computer. This helps a programmer focus on the bigger picture instead of getting lost in small tasks that may end up not working with the rest of the program.

Also notice how Michael created simple steps that can actually be done manually on pen and paper. Michael then created a small test case with small lists to figure out the manual process. He was able to figure out the appropriate processes that could handle lists of any size.

Below is Michael's final code:

```python
#Tally the occurences of numbers


#Problem: Given a list of integers, I want to count their frequency


#Input: list1
#     for example, list1 = [0 1 24 3 14 5]

#Output: A dictionary containing the numbers in list1 and how often they appeared

#Plan:
#     Going to use while loop
#     The loop will continue as long as complete = 0, where complete is 0 if list1 still has numbers in it

#     Each loop we will do the following:
#       - Record the first entry as new_number in list1 
#       - Determine how many entries are in list1
#       - Use a for loop to count how many times new_number appears
#       - Record the index where in list1 each instance occured
#       - Exit for loop and delete all entries in list1 at the recorded indices
# 
#     Record new_number value and tally in a dictionary
#     Check to see if length(list1) == 0 if it is then exit while loop
#
#     Print results!


#Let us make a function called tally to do this task!
def tally(list1):

  #criteria for while loop, boolean variable >>> 0 or 1
  complete = 0
  #initialize our dictionary to store tallies
  num_dict = {}
  #while loop to tally integers

  while complete != 1:
    #take first number in list
    new_number = list1[0]
    print list1
    #counter for my tally, NEED to set == 0 each loop
    count = 0
    #NOTE! That I also need to refresh my list_index each time in while loop
    list_index = []

    #len() function to determine how many entries
    length = len(list1)
    #for loop to go through the list1, where i is looping counter, i.e. range(0,100) = [0 2 3 4 ...100]
    for i in range(0,length):
      if list1[i] == new_number:
      	#count = count + 1, adding one to the count
         count += 1
         list_index.append(i)
         #del >>> delete my entry in list1

         #list1 = [5 4 3 2 1]
         #del list1[0]
         #list1 = [4 3 2 1]
         #list1[1]=? >>> 3... WRONG! 

         #CHANGING list1... now have to account that maybe this isn't best way

         #So, to avoid ^^^ keep a list of indices where list[i]=new_number, call it list_index
         #list_index = [3 17 83 ...] >>> index where I need to delete an entry
         # del list1[i] during the for loop is BAD

    #Go through the list and delete entries equal to new_number
    # setting up a for loop that will go through list_index with counter j >>> del list1[list_index[j]]
    #we are removing things from list1 so we need to keep track of how many we delete each loop!!!
    number_del=0
    for j in list_index:
      del list1[j-number_del]
      #we deleted something so we need to take that into account for the following index
      number_del +=1

      


    #Python dictionary >>> (key,value) pairs
    #NOTE key must be string or a number (I said that the key must be a string in the Webcast, but I was half-correct!)
    # dictionary >>> key = number that I am tallying and value = the actual tally
    # {(2,13), (14,1), ...}

    #We could convert new_number to string str() like this because I like my keys to be strings
    #key = str(new_number)
    #Instead we can use the actual number as the key!
    key = new_number
    value = count
  

    #ADD new entries to dictionary
    num_dict[key] = value
    #(key,value)


    #CHECK to see if list1 is empty or has no entries
    if len(list1) == 0:
      complete = 1

  return num_dict

#Here is an example list1

list1 = [2,2,3,1,5,6,23,6,3,3,1,7]

num_dict=tally(list1)

#Print my tallies
print num_dict
```

## Problem 2

Michael then presented Mark this problem: 

> You are given two lists. The lists have the same numbers in them except for one number. There is one list that has a number that is missing from the other list. Program a function to find this missing number.

Mark first made sure he understood the problem and asked questions for clarifications and to verify his assumptions about the problem.

He then started outlining the problem and identified the inputs of the function and the outputs of the function. During Mark's planning process, he asked Michael for more clarification on the inputs. It was good that he validated his assumptions about the inputs because his assumptions about the inputs were reversed compared to Michael's assumptions about the inputs. This was an important step that Mark took because he would have had to start the process all over if he later found out that the inputs were wrong.

Below is Mark's outline to first understand the problem:

```python
# What is the problem?
# Given a one list that has ~ 50 numbers
# Given another list that has ~50 numbers, there is one missing value
#
# Task is to find that one missing number.

# Assumptions
# Safe to assume that there is only one missing number
# Safe to assume that these numbers are whole numbers, can be positive or negative

# Inputs?
#
# 2 lists of integers

# Outputs?

# Find that one missing number >>> output is a number

# How do go from Input to Output? Can I first think of this process if I were to manually do this?

# Manually == Can I literally write it out on pencil and paper and solve it?


# Let's do that and take a look at both lists

# Have one list as my reference.
# Then have another list as my lookup.

# reference      |      lookup
#    1                     2
#    2                     1
#    3

# >>> 3 is my missing number!
```

Mark then started to write pseudocode that outlined the actual steps he would need to take to code the function. Below is his pseudocode:

```python
# Loop through reference list first
# Get a number from the reference list
# Check if this number exists in lookup list.
# If number does not exist, we have found our missing number! Hurray, return this number immediately

# If there are no numbers missing, print out "no numbers are missing!"
``` 

Once Mark outlined his code, he proceeded to write out the full code seen here:

```python
def find_missing_num(reference_list, lookup_list):
    """Finds the missing number in lookup_list
    # Loop through reference list first
    for num in reference_list:
        # Check if this number exists in lookup. If number does not exist, we have found our missing number! Hurray, return this number immediately
        if num not in lookup_list:
            return num  

    # If there are no numbers missing, print out "no numbers are missing!"
    return "no numbers are missing!"

# Test the function
ref_list = [1,2,3,4]
lookup_list = [2,4,1]

print find_missing_num(ref_list, lookup_list)
```

## Summary

Both coaches wrote out the problems first and made sure they understood the scope of the problem including the expected inputs and expected outputs of their program. This is a crucial skill to learn in order to solve problems in programming.

Both coaches then created small manageable example cases in order to test out the function. This is another crucial aspect to programming - write out test cases to make sure that the program works.

[WB]: https://plus.google.com/events/c58o2legbv7clhs9svsmsfo85ak?authkey=CLKIq9CW_OTWKA