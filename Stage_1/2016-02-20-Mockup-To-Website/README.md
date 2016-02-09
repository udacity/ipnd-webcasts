#From Mockup to Website

[Link to the webcast](https://plus.google.com/u/1/events/cbai087i10ledi69is8ba11gej4?authkey=CIa-ip6mmabeFA)

#Explaining what we are going to do
When designing a website, it is often a good idea to design a *mockup*, either by hand on paper, or by generating a pdf.  This allows you to concentrate on *designing*, instead of *coding*.  

We won't be showing you how to make a mockup, as design is an We will be using the mockup provided in the course 'Intro to HTML and CSS', found [here](https://storage.googleapis.com/supplemental_media/udacityu/2790568610/mock3-portfolio-1.pdf). 

 There is a nice feature in designing things with tools built by other humans; the most natural method your mind works in is usually the one tools exist for!  

 What we will do here is to follow the division your mind already most likely wants to make, by dividing the page into boxes.

 We'll start in the top left, and go from left to right, and then top to bottom, following something called the 'grid based layout'.  

 We can use CSS to build our grid.

 Before we start that, let's build the most basic bit of HTML to link to our CSS file:

```html
 <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Luke's Webpage from Mockup</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>


</body>
</html>
```

From there, let's divide our mockup into boxes:

![mockup with boxes](http://i.imgur.com/t5fm8gu.png)

Let's build a grid into our CSS:

```css
/*First, let's make a class for our entire grid */
.grid {
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;
}

/*Now let's make a class for something which takes up a whole row.*/
.row {
    width: 100%;
    margin-bottom: 20px;
    display: flex;
}

/*Finally, we'll need to make a column class for every column; 12 columns is the standard*/
.col-1 {
    width: 8.33%;
}

/*Each column expands by 8.3333%*/
.col-2 {
    width: 16.66%;
}

.col-3 {
    width: 25%;
}

.col-4 {
    width: 33.33%;
}

.col-5 {
    width: 41.66%;
}

.col-6 {
    width: 50%;
}

.col-7 {
    width: 58.33%;
}

.col-8 {
    width: 66.66%;
}

.col-9 {
    width: 75%;
}

.col-10 {
    width: 83.33%;
}

.col-11 {
    width: 91.66%;
}

.col-12 {
    width: 100%;
}
```

Now, let's build our HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Luke's Webpage from Mockup</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <!-- Put the whole grid in one div -->
    <div class="grid">
        <div class="row top-line">
            <div class="col-2">
                <img src="http://i.imgur.com/bgJGtkO.png">
            </div> <!-- Udacity symbol -->
            <div class="col-10 signature">
                <h1>JANE DOETTE</h1>FRONT-END NINJA
            </div> <!-- Name and Title -->
        </div>
        <div class="row">
            <img class="center-image" src="http://i.imgur.com/IiJ8Wxx.png"><!-- Image -->
        </div>
        <div class="row featured-work">
          <h2>Featured Work</h2><!-- Featured Work -->
        </div>
        <div class="row featured-word-data"> <!-- featured work images and text -->
            <div class="col-4">
                <img src="http://i.imgur.com/4WI3E7I.png"><h3>APPIFY</h3>https://github.com/udacity/Appify/<!-- App image -->
            </div>
            <div class="col-4">
                <img src="http://i.imgur.com/fsOuoTo.png"><h3>SUNFLOWER</h3>https://github.com/udacity/Sunflower/<!-- Flower image -->
            </div>
            <div class="col-4">
                <img src="http://i.imgur.com/1hAJZCT.png"><h3>BOKEH</h3>https://github.com/udacity/Bokeh/<!-- Star image -->
            </div>
        </div>
    </div>
</body>
</html>
```

Our semi-finished CSS would then look like this:

```css
*{
    box-sizing: border-box;
    font-family: 'Lato', sans-serif;
}

.top-line {
    border-bottom: solid #bcbbbb;
}

.signature {
    text-align: right;
}

.center-image {
    text-align: center;
    margin: auto;
    width: 100%;
    max-height: 300px;
}

.featured-work {
    font: 21px;
    color: bcbbbb;
}

.featured-word-data {
    text-align: center;
}

h3 {
    font-size: 20px;
    color: #747704;
}
/*First, let's make a class for our entire grid */
.grid {
    margin: 0 auto;
    max-width: 1200px;
    width: 100%;
}

/*Now let's make a class for something which takes up a whole row.*/
.row {
    width: 100%;
    margin-bottom: 20px;
    display: flex;
}

/*Finally, we'll need to make a column class for every column; 12 columns is the standard*/
.col-1 {
    width: 8.33%;
}

/*Each column expands by 8.3333%*/
.col-2 {
    width: 16.66%;
}

.col-3 {
    width: 25%;
}

.col-4 {
    width: 33.33%;
}

.col-5 {
    width: 41.66%;
}

.col-6 {
    width: 50%;
}

.col-7 {
    width: 58.33%;
}

.col-8 {
    width: 66.66%;
}

.col-9 {
    width: 75%;
}

.col-10 {
    width: 83.33%;
}

.col-11 {
    width: 91.66%;
}

.col-12 {
    width: 100%;
}
```

##Summary

It's easy to note here that, although this is what we end up with, if you watch the video, it is obvious that the jumps are not nearly so sudden.  Instead, pieces are built in one by one; first, boxes (divs) are outlined so we can see where they are going, then HTML is added to put what we want in each given box, then we put some more CSS in to guide the HTML so as to make the mockup incrementally look more and more like the mockup, etc. etc....

Basically, the process is extremely incremental.  First build your basics, then add features one by one, testing to see what the page looks after every change along the way.  Things affecting structure are done first; these changes will need to happen in the HTML as well as the CSS.  After we finish all of the structure, we only need to change the CSS as we morph our page slowly into the mockup.  
