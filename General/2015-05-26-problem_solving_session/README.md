Problem Solving Session
==========================================

Here is a link to the [Webcast][WB]

Luke and Jeff will run through two problems and demonstrate how to approach solving the probems in Python.

The key things that Jeff and Luke both do is to first outline:

* What are the inputs
* What are the outputs
* How do you get from the input to the output in a simple mechanical way (how would we do it manually)
* Figure out how to code the mechanical solution in Python

Along their problem solving sessions, Jeff and Luke demonstrate the importance of checking the validity of their code by executing their code every few lines they've typed.

This makes sure that if an error pops up, they can recognize where the error occurred and immediately address it without having to spend time finding out what is causing the error.

#Problem 1

Here is the problem:

> Define a procedure, find_last, that takes as input two strings, a search string and a target string, and returns the last position in the search string where the target string appears, or -1 if there are no occurrences. Example: find_last('aaaa', 'a') returns 3. Make sure your procedure has a return statement.
> Here are test cases for you to test out:

> print find_last('aaaa', 'a') -> 3

> print find_last('aaaaa', 'aa') -> 3

> print find_last('aaaa', 'b') -> -1

> print find_last("111111111", "1") -> 8

> print find_last("222222222", "") ->  9

> print find_last("", "3") -> -1

> print find_last("", "") -> 0

##Starting Off
Luke started off by going over the problem and recognize what are the inputs and what are the outputs of this function. The inputs are two string variables that contain the string to search in and the string to find in the main string. The output is a number that gives us the index of where the last substring appears in the search string.

He recognized that he needs to use the find() method for strings and recognize that we can tell find() to start at any index. Since find() returns the first substring it sees in the target string, he realized that he needs to continually call find() until it cannot find anymore substrings in the target string.

In order to do this, he needs to use a while loop.

He then went and tried to find a solution using a while loop and use the find() method for strings, testing out several methods. His first few attempts made the code go into an infinite loop.

Luke then realized he needed to take a step back and actually print out what the values are in the loop and to also put in an artificial stopper to stop the loop after 10 iterations so the loop cannot go into an infinite loop.

After debugging, he realized that he needed to change his While loop conditions and need to add in a last_location variable to get the last position that find() returns.

Here is Luke's solution:

```
def find_last(search_string, target_string):
	 # First check to see whether the target string is even inside the search string
    if search_string.find(target_string) == -1:
        return -1
    current_location = 0
    # While the current_location is greater than -1
    while current_location >= 0:
        last_location = current_location
        # Continue to search for the next target string
        current_location = search_string.find(target_string, current_location + 1)
    return last_location

# Another method is to reverse the strings and search for the first occurrence
def find_last(search_string, target_string):
    # Use string splicing to reverse the strings
    last_location = search_string[::-1].find(target_string[::-1])
    if last_location < 0:
        return last_location
    else:
        return len(search_string) - len(target_string) - last_location
```

#Problem 2

This problem is taken from [Project Euler][PE]:

> If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

> NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

The answer is 21124

##Starting Off
Jeff started off by understanding the problem first and wrote out what are the inputs and what is the expected outputs. He also made sure that the spelling for these numbers use the British spelling of numbers.

This step is crucial because it gives Jeff a better idea of what he is actually dealing with.

He quickly figured out that he is going to need a reference list to convert integers into the actual words and decides to use a dictionary to act as a reference table for him. You can read more about dictionaries [here][dictionary].

Throughout the session, he constantly prints out his code to check his code and begins to outline what he plans to do. This is another crucial step to help a programmer focus in on what exactly needs to get done. Many programmers outline what they plan to do in pseudocode or in a plain human language that is understandable first.

Here is his outline:

* Convert number to word representation
  * Create lookup table from number to the actual word
  * Convert the number to a string to easily use string slicing to separate the thousandth, hundredth, tenth, and single digits.
  * Depending on what the digit is and its position, find the word that corresponds to that digit and build the string of words that represent that number.
* Count up the total number of letters
* Add value from 2 to sum_of_letters


Here is Jeff's solution:

```
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

# 3 -> 'three' -> 5
# 20 -> 'twenty' -> 6

numbers_to_strings = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'onehundred',
    200: 'twohundred',
    300: 'threehundred',
    400: 'fourhundred',
    500: 'fivehundred',
    600: 'sixhundred',
    700: 'sevenhundred',
    800: 'eighthundred',
    900: 'ninehundred',
    1000: 'onethousand'
}

# 72 -> 70 2 -> 'seventy', 'two' -> 10

def find_total_letters(n):
    list_of_numbers = range(1, n + 1)
    sum_of_letters = 0
    for number in list_of_numbers:
        # 1. convert number to the word representation
        if number in numbers_to_strings:
            word = numbers_to_strings[number]
        else:
            num_digits = len(str(number))
            if num_digits == 2:
                # Number is between 21 and 99
                tens_digit = int(str(number)[0]) * 10
                ones_digit = int(str(number)[1])
                word = numbers_to_strings[tens_digit] + numbers_to_strings[ones_digit]
            elif num_digits == 3:
                # Number is between 101 and 999
                hundreds_digit = int(str(number)[0]) * 100
                potential_tens_word = int(str(number)[1:])
                if potential_tens_word in numbers_to_strings:
                    # The last 2 digits exist as a word (ex. 11, eleven)
                    word = numbers_to_strings[hundreds_digit] + 'and' + numbers_to_strings[potential_tens_word]
                else:
                    tens_digit = int(str(number)[1]) * 10
                    ones_digit = int(str(number)[2])
                    word = numbers_to_strings[hundreds_digit] + 'and' + numbers_to_strings[tens_digit] + numbers_to_strings[ones_digit]

        # 2. count up the total number of letters
        word_length = len(word)

        # 3. add value from 2 to sum_of_letters
        sum_of_letters = sum_of_letters + word_length
    return sum_of_letters


print find_total_letters(1000)

```


[WB]: https://plus.google.com/events/cq3nc5eskr27eiv5uindf1m2olo?authkey=CLiIzMXV5Z32pAE
[PE]: https://projecteuler.net/
[dictionary]: http://www.tutorialspoint.com/python/python_dictionary.htm