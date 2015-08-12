# Article taken from: https://www.python.org/about/success/wingide/
article = """
PARAGRAPH:
Wing IDE is a commercial integrated development environment for the Python programming language. Wing provides developers with a full-featured source editor, debugger, code browser, and many other tools specifically designed for use with Python. Wing works with all forms of Python, whether running as a stand-alone app, under a web server, or in a custom embedded scripting environment. Several GUI layers (wxPython, PyQt, PyGTK, and Tkinter) are supported, as are Zope and mod_python for web development, and pygame for game development.
PARAGRAPH:
Wing was inspired in 1999 by several experiences we, its developers, had using Python alongside other technologies. At that time, we were working as consultants charged with evaluating a number of alternatives for tiered web development. Some of these were based on Java and some on Visual Basic, MTS, and ASP. Concurrently, we happened to be using Python to prototype some of the functional requirements for the web-deployed business applications we were developing.
PARAGRAPH:
It wasn't long before we found ourselves comparing our Python prototypes favorably to the actual systems we were developing. Python was a much more productive way to work, and it seemed to result in at least as good an end product.
PARAGRAPH:
Unfortunately, our client never seriously considered Python simply because it wasn't a mainstream (namely Java or Microsoft) technology. But it was clear to us that Python could have been a significant cost saver and competitive advantage for them, and we saw a business opportunity in helping other organizations benefit by using Python.
PARAGRAPH:
Work on Wing IDE started almost right away, in mid 1999, initially on a part-time basis. We realized that writing an entire IDE wasn't going to be easy and wanted to be sure that Python was really as good as it appeared to us at the time. The logical way to approach this was to develop the IDE itself in Python. This would give us proof of concept and let us become early users as we started to develop and debug Wing IDE with itself.
PARAGRAPH:
To speed development and keep costs down, we chose to base Wing on as many open source modules as we could find. The GUI was written with GTK, which is accessed from Python via PyGTK. The source editor is based on Scintilla, an open source code editor component. And printing is implemented via py2pdf from ReportLab.
PARAGRAPH:
Initial development was on Linux but we planned to support at least Windows and eventually other Unix-like operating systems. For this reason, we avoided platform-specific implementations and chose cross-platform technologies.
PARAGRAPH:
Additional development tools used in the project included gcc, Gnu make, latex, pdflatex, latex2html, emacs/xemacs (before Wing was functional), Visual C++ 6, and cygwin.
PARAGRAPH:
Our work on Wing IDE has been quite a success. We were able to develop faster than we originally expected, and to deliver Wing IDE on Linux, Windows 98 through XP, Mac OS X with XDarwin, Solaris, and FreeBSD without major platform-specific development work. Today, our product is receiving good reviews and is selling well. All of this has been possible without any outside funding and with a development team of just two people.
PARAGRAPH:
The biggest benefits of using Python have been in overall productivity, cross-platform deployment, speed of the resulting application, scalability, rock-solid stability, and its strong support for mixed-language development.
PARAGRAPH:
Over the course of this project, we have been able to write on average over 175 lines of debugged, documented, tested code per developer per day. Over a period of 660 FTE days, we produced a total of approximately 121K lines, of which 77K were written in Python. Even without considering that a line of Python is typically equivalent to 10 or more lines of C, we were extremely pleased with this result.
PARAGRAPH:
The entire product, including third party open source modules, actually contains on the order of 1.2 million lines of code, of which 274K lines are Python.
PARAGRAPH:
So why was using Python so productive, even when only 63 percent of the code we wrote was in Python? There is no single answer to this question, but several:
PARAGRAPH:
Wing IDE runs on a variety of Posix operating systems and Windows. Throughout our development process, we've been very happy with the way that Python performed across platforms. The same Python source or compiled Python byte code files can be shipped to clients regardless of target platform, making support quite easy.
PARAGRAPH:
When we started to write in Python, our previous experience in compiled languages led us to believe that we would be spending a fair amount of time either optimizing code or converting it into C or C++ once we had prototyped it. As it turned out, most of the time Python produced a snappy end product that didn't require any extra work.
PARAGRAPH:
This happened partially because most Python code is really just a thin interpreted layer over functionality that is written in C or C++. In our case, this included not just Python's fast built-in data structures and standard libraries but also the bulk of the GTK GUI development layer and the Scintilla source editor.
PARAGRAPH:
In the course of development and in responding to thousands of support tickets over a three year period, we have never run into any significant problems with Python itself, either in scalability or stability. Wing IDE can handle software projects with thousands of Python files, and in many cases can run for weeks without problems. To our knowledge, we have yet to see Wing IDE crash because of a flaw in the Python interpreter or its standard libraries.
PARAGRAPH:
Python is almost always fast enough but we did run into a few cases where the interpreter did introduce too much overhead. The Wing IDE debugger and the source code analysis engine both contain modules that engage in extremely CPU intensive processing. These modules needed to be written in C in order to squeeze out as much speed as possible. Fortunately, Python is designed to make it quite easy to call back and forth between Python and C or C++.
PARAGRAPH:
In most cases, we wrote and debugged code first in Python, and then converted by hand into C. This approach worked well for us. Working initially in Python was much more efficient and the conversion process relatively painless.
PARAGRAPH:
Analysis of our records shows that 360 days were spent on 77K lines of Python code and 300 days (almost as much) on 44K of C, C++, or other code. From our experience with code conversions, we believe it is roughly correct for most types of performance-critical code to equate one line of Python with ten lines of C or C++ code. This means that about 5-10% of our application functionality is in C or C++ and the rest is in Python. Even considering that the C/C++ code is somewhat more complex than most of the Python code, these results confirm without any doubt that working in Python is far more productive than working in C or C++.
PARAGRAPH:
In hindsight, we believe that we could have converted smaller units of code into C, by writing more general data-driven processing engines, and by more carefully selecting code to convert instead of converting whole modules at a time. Our primary goal for Python in the future is to be able to use it more often, even in performance-critical sections of code. This effort should benefit from projects like pyrex, which allows the use of Python-like code in the development of compiled extension modules, and psyco, which is a just-in-time compiler for Python.
PARAGRAPH:
There are just two quirks that affected our development with Python. The relative impact they had on our project was tiny compared to Python's benefits but for balance we feel they are worth mentioning:
PARAGRAPH:
Like Java and other languages, Python occasionally deprecates old features, or fixes minor bugs in a way that can potentially break existing code. This is done over the course of a number of releases, so that programmers will first see deprecation warnings, and only later be impacted by the change. We ran into this only once when Python 2.0 began to disallow multiple arguments to the sequence append method. This problem required changing exactly three easily found calls in our code base of over 77K lines of Python.
PARAGRAPH:
Different versions of Python can produce incompatible compiled byte code and requires that C/C++ extension modules are compiled against a specific version of Python. For example, while Python 2.2.2 works happily with Python 2.2.1 or 2.2.0 byte code and extension modules, it will print warnings and may run into problems running against those compiled against Python 2.1.x or earlier. There are solid technical reasons behind this design choice, but it does require some additional work when packaging applications for distribution to users running different versions of Python. In the Wing IDE debugger, we solve the problem simply be storing separate directories for each interpreter version and importing modules accordingly at runtime. For the IDE itself, we solve it by shipping with a specific Python interpreter included; a task that's easily accomplished with support found in the Python standard library's distutils package.
PARAGRAPH:
No other language we have used has been this devoid of quirks, even those we have used much less intensively and across fewer language revisions.
PARAGRAPH:
Without Python, we could not have sustained the Wing IDE development effort long enough to produce what is now a successful software product. Python has been more productive, robust, and portable than any other technology we have tried. Through our experiences providing technical support for the IDE, we know that we are not alone in these assessments. Feedback from our customers often includes strong endorsements for the productivity of Python, Wing IDE, and related technologies such as Zope.
"""


#for each character in article:
#	add 1 to variable which is that character

#print dictionary of each character and its count
distribution = {}
article = article.replace('PARAGRAPH:', '')

for char in article:
	if char != '\n' and char != ' ':
		if char in distribution:
			distribution[char] += 1
		else:
			distribution[char] = 1

print distribution















