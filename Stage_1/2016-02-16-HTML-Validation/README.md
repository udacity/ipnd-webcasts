Air Date: 2/16/2016
[video][recording]

# HTML validation


##What We Will Learn

- What is HTML validation and why it is important?
- How to debug a webpage

###Files
[error-filled file](non-validating.html)
[validated file](validating.html)

###Why is validating important
HTML stands for HyperText Markup Language, and much like any other language, it has rules and guidelines to follow. A webpage that follows all of these rules and guidelines is said to be validated. Validation makes sure that your page will run properly on any system or browser used to view it and allows for a common set of standards for programmers to agree on. Oftentimes, a page that doesn't validate will still work exactly as expected, in this case, why does validation matter.

In this case properly validated code is much like an essay with proper spelling, grammar, punctuation, and formatting. An essay without these things will still be readable, but one that follows these rules is easier to understand and is the mark of a professional. Your code may work, but if it doesn't validate, it makes it harder for other programmers to work with it and is a red flag for any employers.

###Debugging
[The W3C HTML Validator](https://validator.w3.org/#validate_by_input( is your best friend here. You will want to copy/paste your code into here as you validate and fix errors. It is important to note that the validator will really only tell you which line is causing issues and give a probable reason. It's up to you to diagnose exactly what the reason is and how to solve it. This is the 'fun' part of debugging.

You can see all of the changes we made [here](https://www.diffchecker.com/b9mceb5n)

Some highlights:
- All opened div tags must be closed!
- \<ul\> can only have \<li\> as a child, same goes for \<ol\>
- Any angle brackets must be escaped as &lt; and &gt; for left and right brackets respectively

[recording]: https://www.youtube.com/watch?v=vxe8LE0VgZY#t=17
