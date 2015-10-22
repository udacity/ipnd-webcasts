Problem Solving Session 10/20
==========================================

Here is a link to the [Webcast][WB]

Jonah and Luke run through two problems and demonstrate how to approach solving the probems in Python.

The key things that Mark and Luke both do is to first outline:

* What are the inputs
* What are the outputs
* How do you get from the input to the output in a simple mechanical way (how would we do it manually)
* Figure out how to code the mechanical solution in Python

Along their problem solving sessions, Mark and Luke demonstrate the importance of checking the validity of their code by executing their code every few lines they've typed.

This makes sure that if an error pops up, they can recognize where the error occurred and immediately address it without having to spend time finding out what is causing the error.

#Problem 1

A puzzle/python problem sourced from [Python Challenge](http://www.pythonchallenge.com/pc/def/map.html)


##Starting Off
Luke analyzed the image and figured out that the puzzle was a simple translation/substitution cypher. He talked through how he would take the string in as an input, shift each the ASCII code for each letter forward by two and then output the result.

His initial result worked for most letters, but was very messy, since it shifted non-letter characters forward, resulting in a bunch of jumbled characters. Also the letters y and z would be not be shifted properly either.

His next iteration ignored whitespace characters and included a special case for y and z. This outputted the translated message, which gave the solution to proceed to the next challenge.

Here is Luke's solution:

```python
string_to_convert = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

list_to_convert = "abcdefghijklmnopqrstuvwx"
special_convert = {"y" : "a", "z": "b"}

def cipher(string):
    result = ""
    for char in string:
        if char in list_to_convert:
            result += chr(ord(char) + 2)
        elif char in special_convert:
            result += special_convert[char]
        else:
            result += char
    return result

print cipher(string_to_convert)

print cipher("map")
```
 
#Problem 2
Problem comes from [CS101](https://www.udacity.com/course/viewer#!/c-cs101/l-48683810/e-48750084/m-48735060)
> Write a procedure date_converter which takes two inputs. The first is 
> a dictionary and the second a string. The string is a valid date in  the format month/day/year. The procedure ? should return the date written in the form <day> <name of month> <year>. For example , if the dictionary is in English,
```python
english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}
```
then  "5/11/2012" should be converted to "11 May 2012". 

Jonah thought about the inputs and realized that he needed to read in a string, process it into a list, and then output it as a reformatted string. He looked up a function to change a string into a list by defining the character / as a separator. He realized that in order to find the month that maps to a number he would need to change the string form of the month into a integer and then find the value connected with that in the dictionary. After testing his code, he realized that he was only coding for the dictionary 'English' so he replaced that with the function argument variable 'index' which was being passed in. His final solution can be found here.
```
def date_converter(index, date):
    returnlist = date.split('/')
    returnlist[0] = int(returnlist[0])
    output = returnlist[1] +' '+ index[returnlist[0]] + ' ' + returnlist[2]
    return output
```
Jonah and Luke then discussed their approach to problem solving by talking through the problem at hand. Pseudocode makes less sense if you are comfortable with a language, although makes more sense with larger-scale projects. The fastest way to solve a problem is just to write a little bit of code that gets you close to the solution and then refine until you can solve the problem completely. This is what's known as fast iteration.
[WB]: https://www.youtube.com/watch?v=SV2wrbhOfE0
