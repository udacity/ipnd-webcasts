Famous Algorithms: Sorting Data
===

# How would you sort data?

You've probably already come across a time or two where you had a set of data (perhaps stored in a list) that you need to have sorted in a certain way. Even if you haven't dealt with sorting data in Python, you've undoubtedly had to sort _something_ in your life whether it be a list of your favorite movies or numbers in a spreadsheet at your job.

Why do we care so much about sorting data? It's quite simple actually. Sorted data is organized, and organized data is easier to work with and understand. When data is organized we can more easily observe trends and draw conclusions on the meaning of the data.

Python makes sorting very easy, easier than its ever been in the history of computing actually! To sort a list of data in Python, we simply have to write: `list = sorted(list)`. That's it! The list is now sorted. 

But it wasn't always that easy. In this webcast, we'll explore two important sorting algorithms and discuss how they changed the face of computer programming. While you won't have to ever implement one of these algorithms in a job, gaining an appreciation for them will help you become a better programmer (and they're the basis of a lot of common interview questions too).

# A Simple Approach: Bubble Sort

One of the simplest sorting algorithms is known as "bubble sort." It's an incredibly intuitive algorithm and thus quite easy to understand and implement. The idea of the algorithm is this:

1) Start with the first two numbers in the list  
2) If the number on the right is smaller, swap their positions. Otherwise, continue.  
3) Repeat step 2 for the next two elements  
4) Repeat step 1 until the list has been passed through without making any swaps.

![](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

In pseudocode we might say:

```
for left, right in list:
	if left > right:
		swap left and right
	else:
		continue

repeat loop until no swaps are made
```	

So here's the catch: bubble sort is actually a really terrible algorithm. While it's a __really__ easy way for people to think about sorting, it can be incredibly slow. Evaluating the run-time of an algorithm is a core idea of computer science and oftentimes the most "obvious" algorithms are actuall the slowest (because nothing in life is easy). Let's think about that in the case of bubble sort:

In the best case scenario, the list we want to sort is already sorted! That means we only have to run through the list once to verify that the list is in fact in the right order. We can think about the number of comparisons we'd have to make. To go through an entire list of size `n`, we have to make `n` comparisons (the first and second elements, the second and third, third and fourth, and so on until the (n-1)th and nth elements).

But what about in the worst case? The worst case scenario happens when the smallest element starts in the last position in the list. Since each iteration of bubble sort only moves in element "forward" a maximum of one spaces, that means we'll need `n` iterations to move the smallest element to the first position. Since each iteration has `n` comparisons, this means the total run-time of bubble sort in the worst case is `n^2` comparisons. Imagine doing that on a massive database, like Google search results for example. That's a __LOT__ of comparisons!

The poor run-time of Bubble Sort is so famous that [Barack Obama once called it out in an interview at Google.](https://www.youtube.com/watch?v=k4RRi_ntQc8)

# An Efficient Approach: Merge Sort

Thankfully, computer scientists are very creative people and have come up with many faster ways to sort data. There are a large number of different methods. Here's just a few: Quick Sort, Heap Sort, and the one we'll go over next, Merge Sort. This sorting algorithm is used in a lot of applications, and a derivative of it known as Timsort is the default sorting algorithm in Python. Here's how merge sort works:

1) Divide the list into two equal sized lists  
2) Continue dividing these sublists in half until you end up with `n` sublists of 1 element each  
3) Sort the sublist (note a 1 element list is sorted by default)  
4) For every pair of sublists, compare the elements left to right and sort them into a combined sublist. The number of sublists should now be divided in half.  
5) Repeat step 4 until only one list remains (the sorted list)

![](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

In pseudocode we'll see we need two functions, one to divide the list and one to merge the sublists:

```
def mergesort(list):
	if list.length == 1:
		return list
	else:
		middle = list.length / 2
		for each item in list up to middle:
			add item to left
		for each item in list after middle:
			add item to right
		left = mergesort(left)
		right = mergesort(right)
		result = merge(left, right)
		return result
		
def merge(left, right):
	while left.length > 0 and right.length > 0:
		if first(left) <= first(right):
			append first(left) to result
			remove first from left
		else:
			append first(right) to result
			remove first from right
	if length(left) > 0:
		append left to result
	if length(right) > 0:
		append right to result
	return result
```

We call this type of algorithm "Divide & Conquer" since the basic steps are to repeatedly divide the list and then combine the sublists. This is a lot less obvious than Bubble Sort but we'll see that, on average, Merge Sort is a lot faster! The runtime analysis though is a bit more complicated, and we'll complete it by looking at each step of the algorithm:

1 & 2) To divide the list we simply have to take the length of the list and divide in half to get the indices for each sublist. The time this takes does not depend on the size of the list so we call this "constant time"

3) Sorting a sublist of length 1 takes constant time also (since we don't have to do anything other than verify the length is 1). We'll revisit this in a moment.

4) Here's where things get complicated. Each sublist is half the size of the previous sublist. Here's a tree diagram that shows how this plays out:

```
				n
			/		\
		n/2			 n/2
	  /		\		/	 \
	n/4		n/4	 n/4	 n/4
	 ... (many more divides)
1	1	1	1	1	...   1	(n times)
```

At each level, we need to make a certain number of comparisons to merge the two sublists. In fact, the number of comparisons we need to make is equal the size of the merged list. So `n` comparisons for the top level, `n/2` for the second, `n/4` for the third, and so on to the final level which has only 1 comparison (the single element to itself). Furthermore, notice that each level has twice as many sublists. So the total number of comparisons are actually `1 * n` for the top level, `2 * (n/2)` for the second, `4 * n/4` for the third, and so on to the final level which has `n * 1` total comparisons. Finally, notice that each of those expressions simplifies to just `n`.

So if each level takes `n` comparisons to sort and merge, all we need to know is how many levels there are. We won't go into the algebra here, but it can be shown that halving a list of size `n` until `n` sublists are created requires `log(n) + 1` levels (note the `log` is base 2). So the total comparisons for this algorithm is `n + nlog(n)`.

There's two interesting things about that run-time. First is that we can expect a run-time of `n * log(n)` regardless of the best/worst case scenarios. We thus refer to it as the "average run-time". Secondly, recall that the best-case run-time of Bubble Sort was `n` and the worst-case was `n^2`. Well, then notice this: `n < (n + nlog(n)) < n^2`. So Merge Sort is actually __worse__ than Bubble Sort in the best-case scenario!

In most programming languages, the sort method is some combination of an "efficient sort" (like Merge Sort) and a "simple sort" (like Bubble Sort). The efficient sort will be used first, and after the data is reasonably close to being sorted, the simple sort will kick in to finish the job. Python uses such an algorithm known as Timsort (invented by computer scientist Tim Peters in 2002).