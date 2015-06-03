#Logistics, Project 1, and Text Editors


Hi everyone,

Thanks for attending the Webcast earlier today (Tuesday, February 17) about a
small logistical thing regarding the forums versus the Google+ community, some
pitfalls to watch out for with respect to project 1 (and HTML in general), and
how to work with a text editor.

If you missed it, you can get to it by navigating [here][hangout].

Here's what Surajit, Luke, and I (Chrisna) covered:

## Forums vs. Google+

We encourage you to use our [discussion forums][discourse] to share anything
that you'd like to about the Nanodegree program, your journey to learning how
to program, and more. Join us!

## Project 1

Overall, we really like what we've seen so far in our discussion forums'
"sharing notes" threads:

- [Work Session 1][ws1]
- [Work Session 2][ws2]
- [Work Session 3][ws3]

We've noticed a few recurring issues that we'd like to point out here and
discuss, so let's get started!

### Correctly nesting and closing tags

It's important to ensure that HTML tags are nested correctly. This means that
everything that starts inside a given tag must end before its outer tag ends.
Here's an example where that isn't the case:

```html
<strong><a href="https://www.udacity.com">This site rocks!</strong></a>
```

Here, we start bolding text and start a link, but we stop bolding text before
we end the link. This is what we should do instead:

```html
<strong><a href="https://www.udacity.com">This site rocks!</a></strong>
```

And, here's an example of us forgetting to close some tags, which is also a
good opportunity for us to show you how to create a list. A list is a standard
element in HTML -- you can create an ordered (numbered) list with `ol` and a
bulleted list with `ul`. These tags start a list, and, once you're in a list,
it's up to you to create items in your list with `li`, as you can see below:

```html
<ol>
  <li>Apples
  <li>Bananas
  <li>Mandarins
</ol>
```

We forgot to close each of our list items, so let's fill them in:

```html
<ol>
  <li>Apples</li>
  <li>Bananas</li>
  <li>Mandarins</li>
</ol>
```

Curiously, both of these examples look the same if you compare the incorrect
and correct versions in a browser (or in [CodePen][cp]). So, why should we
bother to make sure our code is correct? What does it even mean for code to be
correct?

One way to assess correctness is by using a [validator][w3c].

HTML is similar to English in this way: even though native English speakers are
often able to understand grammatically incorrect English, it's still worth
trying to follow the rules as closely as we can.

Browsers are very good at putting together something reasonable when given
malformed HTML, but we, as programmers, shouldn't take that for granted. Just
because your page looks fine to us in Chrome or Safari or IE doesn't mean that
it looks good everywhere. People communicate with webpages in many different
ways -- through mobile apps, technology that allows handicapped people to
interact with the Internet, and much, much more. Making the Internet work for
all of us requires us to be mindful of that!

### Correctly spelling tags

Instead of giving you an indication that you've made a mistake, misspelling a
tag will either not change anything or make the text on your webpage look
"unstyled."

For instance, if you misspell the `p` tag by calling it `paragraph` instead,
paragraphs don't come with a predefined style, so your page will probably look
exactly the same either way (assuming you aren't yourself defining a style for
the `p` element.).

If, instead, you try to insert a header into your page with `h1` but
accidentally call it `h12`, the text inside an `h12` tag won't look very
header-like because `h12` isn't a real header tag.

### `b` vs. `strong` (semantics vs. style)

Best practices today dictate that HTML tags should be used more for semantics
(the meaning of your content) rather than the style of your content (is this
bold?). The `b` tag is a "style" tag whereas the `strong` tag is a "semantic"
tag that means that you want to emphasize the content inside that tag. It just
so happens that the standard way to style that is by **bolding** it.

This goes the other way too. We've seen some students use the `blockquote`
element in attempts to indent text in a certain way, especially since any
spaces after the first space do not matter in HTML. It turns out that
`blockquote` should only be used in cases where something is being quoted (i.e.
a novel or movie).

### Showing HTML inside a webpage

The less than sign (&lt;) and greater than signs (&gt;) are special characters
in HTML because they're what we use to denote tags. How do we insert them as
text into our page so that they show up? We have to use a special sequence of
characters to get them to show up.

`&lt;` will show up as &lt; and `&gt;` will show up as &gt;.

### Putting `head` elements inside the `body`

We've seen a few instances of the `title` element ending up in the `body`
instead of the `head`. This element corresponds to what shows up in a browser's
tab when someone visits your site rather than something on your page, which is
why it should go into the `head` rather than the `body`.

### Getting images to show up

It's important to make sure that `img` tags point to locations that the thing
that is displaying our page has access to. It's perfectly fine to point to
images on your computer when you are working on your site on your computer, but
those images don't exist (yet) on the Internet, so once you try to put your
site on [CodePen][cp], you have to put your images in places that it can
access.

One easy way to do this is to upload your images to a site on the Internet
called [imgur][i]. Once you upload an image there, it will give you a direct
link to the image, which you can use in the `src` attribute instead of the path
to a file on your own computer.

Old:

```html
<img src="/Users/Chrisna/Downloads/awesome.jpg" alt="An awesome picture">
```

New:

```html
<img src="http://chrisna.org/images/night-over-new-york.jpg" alt="An awesome picture">
```

## Text Editors

[Sublime Text][st] is pretty cool! A working setup we like involves the
following steps to transition from [CodePen][cp]:

1. Copy HTML into an empty tab in Sublime Text. Save the HTML file somewhere.
2. Open a new tab in Sublime Text and copy CSS into it, if you have any. Save
   that file in the same folder as the HTML file and remember its name.
3. Ensure that a `link` element exists in the `head` of the HTML file that
   points to any CSS files that you have:
   `<link rel="stylesheet" href="main.css">`
4. Open HTML file in your favorite browser.

You'll have to refresh your browser and save your HTML and CSS file
periodically, but other than that, it's a pretty nice way to get some
programming done!

[hangout]: https://plus.google.com/events/cpuimfqjau4fv3nra5a98dnving?authkey=CI-l9J7pqpam3gE
[discourse]: http://discussions.udacity.com
[ws1]: http://discussions.udacity.com/t/sharing-work-session-1-notes/2597
[ws2]: http://discussions.udacity.com/t/sharing-work-session-2-notes/2695
[ws3]: http://discussions.udacity.com/t/sharing-work-session-3-notes/3850
[cp]: http://codepen.io/pen/
[w3c]: http://validator.w3.org
[i]: http://imgur.com
[st]: http://www.sublimetext.com
