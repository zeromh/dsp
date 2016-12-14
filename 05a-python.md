# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both are indexable and can contain items of different types. Lists are mutable. Tuples can be used as dictionary keys because they aren't mutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both can contain items of different types. Sets are unordered and therefore cannot be indexed. Lists are mutable and sets are immutable. For large sets/lists, it's much faster to find an element in a set because the set uses a hash table.

>>You might use a list to store words to iterate over, i.e. ['apple','banana',car']  
>>You might sets to see if one set contains another set, i.e. {1,2,3,4,5} - {3,1,2} = {4,5}

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function is an anonymous function that you can create as needed without saving it. You can use it anywhere you would use a normal function.  
Let's say you want to sort this list of tuples by the third item in each tuple:

```
sequence = [(0, 4, 'd'), (1, 3, 'e'), (2, 2, 'a'), (3, 1, 'b'), (4, 0, 'c')]
print sorted(sequence, key = lambda x: x[2])

#Output
[(2, 2, 'a'), (3, 1, 'b'), (4, 0, 'c'), (0, 4, 'd'), (1, 3, 'e')]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A comprehension is like a fast, one-liner for loop. Comprehensions also have an optional conditional statement.  
I could make every word in a list uppercase using a list comprehension:

```
t = ['boom','word','yeah']
[word.upper() for word in t]

#Output
['BOOM', 'WORD', 'YEAH']
```
Or I could use map and a lambda function to do the same thing:

```
map(lambda word: word.upper(), t)

#Output same as above
```
Here are two similar operations using a list comprehension or filter to only return words in the list that begin with 'y':

```
[word for word in t if word[0] == 'y']
filter(lambda word: word[0] == 'y', t)

#Output
['yeah']
```
Comprehensions tend to be faster/more efficient since they use optimized for loops, don't make new function calls, and only go through each sequence once.  
A comprehension can return a set just as easily as a list:
```
{word.upper() for word in t}

#Output
set(['WORD', 'BOOM', 'YEAH'])
```
Or a dictionary:
```
{word:word.upper() for word in t}

#Output
{'word': 'WORD', 'boom': 'BOOM', 'yeah': 'YEAH'}
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





