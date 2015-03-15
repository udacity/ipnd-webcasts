OH: The Nanodegree as a Whole and Stage 1
==========================================

Andy worked with Liz on her Stage 1 project. Watch Andy help Liz fix her Stage 1 project. [OH video](https://plus.google.com/events/cmtb5ijlk7s3jerqhq7op7jnfjo?authkey=COzZjMbU_baxrwE)

Liz is a project manager at Udacity and is working on completing the Intro to Programming  Nanodegree curriculum! Like many of you, Liz does not have any prior programming experience and she's excited to learn with everyone!

Problems Liz wants to Address
-----------------------------
  * The photo is too large for the page, it overlaps with some text, and would prefer the  photo to be a circle centered on the page.
  * The borders get more and more narrow as you scroll down the page
  * Improve organization of the code

###1. Fix the Structure
  * Use Scratchpad for instant feedback on the HTML
  * Copy and paste the HTML into Scratchpad to focus on the structure of the code
  * Use indentation of the code to keep track of the structure. Text that belongs to a  heading will be indented below the header (similar to an outline)
  * **Question:** What HTML tag should be used to contain a concept?
   * <div> since it will but the contents of the concept in its own box on the page.
  * **Question:** What's the difference between ```<p>``` and ```<div>```?
   * ```<div>``` is a structural element that helps organize the browser
   * The ```<p>``` tag is specifically for paragraphs, it lets us organize large bodies of text in HTML.
  * **TIP:** If you need to fix the indentation of a section in your HTML code, you can select  the section and hit "tab" the required number of times. To remove indentation, just press "tab" + "shift"
  * Correctly formatted HTML code will have a smooth indentation wave. (ie. no sudden changes  in indentation)
  * **TIP:** Add margins, borders, and background color to help visualize the structure of the  HTML code. This can be easily removed once the code is complete. 
```
<style>
  *{
    margin: 8px;
    border: red solid 2px;
    background-color: rgba(0, 0, 0, 0.15)
  }
</style>
```

###2. HTML Validator
  * You don't have to use the link from the course to access the HTML Validator. You can just  search for it on the internet.
 
###3. CSS
  * **Questions:** What does the dot mean in CSS? (Don't hesitate to search the internet for  the answer. You'll be surprised how easy it can be to find the answer)
   *  >A ```.``` prefix usually represents a class selector, but if it's immediately followed   by whitespace then it's a syntax error. 
  * Fixing the image:
   * Liz's original HTML (the entire ```<div>``` is being stylized):
```
<div  class="Header-image">
  <img src="http://i.imgur.com/An1q9ze.jpg">
</div>
```
   * Liz's corrected HTML (only the image is stylized, added a class name that will be used to center the image):
```
<div class="image-container">
  <img class="Header-image"  src="http://i.imgur.com/An1q9ze.jpg">
</div>
```
   * Liz's original CSS:
```
.header-image {
  width: 850px;
  height: 600px;
  border-radius: 425px;
  -webkit-border-radius: 150px;
  -moz-border-radius: 150px;
}
```
   * Liz's corrected CSS (correct the size to be the right scale and center the image)
```
.header-image {
  height: 300px;
  border-radius: 425px;
  -webkit-border-radius: 150px;
  -moz-border-radius: 150px;
}
.image-container {
  text-align: center;
}
```

###4. How to code/style things efficiently
  * If you find yourself styling many different things the same way, you can the style the shared  outer level of the HTML code.

###5. Easy ways to add content/how to fix the shrinking box problem
  * Make sure that the content is nested in a consistent way, the deeper an item is nested, the smaller the box.
  * Don't forget your closing tags!

###Questions:
>**Question:** Why doesn't changing the ```<div>``` change the image that it is contained in?

**Answer:** 
A ```<div>``` is a place to put stuff. We can change properties of a ```<div>```, for example we  could change the background color. But changing the properties doesn't change the image itself since the image is  an element that sits on top of the ```<div>```. 

>**Question:** It seems like the DOM tree is the same as HTML code, but in our lesson we were  taught it is different. Which is right?

**Answer:** They are similar in some ways but they are different. One difference is that people  usually say they are "manipulating the DOM." When people manipulate the DOM tree, it's like they're trimming the branches,  removing branches, or even grafting new branches to the tree. This analogy refers to the elements instead of  the HTML code that generates the website. 
