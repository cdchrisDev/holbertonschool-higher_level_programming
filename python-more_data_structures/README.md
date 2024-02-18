# Python - More Data Structures: Set, Dictionary
### Resoruces
* [Data structures](https://intranet.hbtn.io/rltoken/K8JSw_eMWjw6EzmAL1S8bQ)
* [Lambda, filter, reduce and map](https://intranet.hbtn.io/rltoken/K8JSw_eMWjw6EzmAL1S8bQ)
* [Learn to program 12 Lambda map Filter Reduce](https://intranet.hbtn.io/rltoken/NnWm29rFmdDcjcdRQX1tEw)
## Learning Objectives
* What are sets and how to use them
	* Set is a data type in python used to store several items in a single variable
```
Set items can be of any data type and be mixed
============================================
STRset = {"a", "b", "c"}
INTset = {1, 2, 3, 4}
BOOLset = {False, False, True}
MIXEDset = {10.0, "Hi", (11, 22, 33)}
```
* What are the most common methods of set and how to use them
	* **Intersection**:<br /> The intersection of two sets is a set of elements that are shared by both sets
	* **Discard**:<br /> Removes the specified element fro the set if it is present.
	* **Symmetric difference**:<br /> Each of the union, intersection, difference, and symmetric difference operators listed above has an augmented assigment form can be used to modify a set.
	* **Union**: Set Union operation. Union of 2 functions is the set of all the elements from both sets in a single different set.
	* **Copy**: Create a new set based on an existing set, but do not want to modify the original set.
* When to use sets versus list
	* The primary difference between list and set is that a list allows duplicate elements and maintains their order, while a set ensures element uniqueness without any guaranteed order. Since lists are ordered, position indexing is allowed in them. However, in unordered items like sets, positional indexing is not possible.
* How to iterate into a set
	* `for val in set_val`
* What are dictionaries and how to use them 
	* A dictionary is a sequences of key/pair values assign to a var<br /> To illustrate, the following examples all return a dictionary equal to `{"one": 1, "two: 2, "three": 3}`
```
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> f = dict({'one': 1, 'three': 3}, two=")
```
* When to use dictionaries versus list
	* When we want to use unordered sequences we use `dict or set` otherwise `list`
* What is a key in a dictionary
	* Keys are analogous to indexes of a list
* How to iterate over a dictionary
	* `for key in dict`
* What is lambda function
	*  is a way to create small anonymous functions
* What are the map, reduce and filter functions
	* **map()**: used to return a list, where each element of the result list was the result of the function func applied on the corresponding element of the list or tuple "seq". With Python 3, map() returns an iterator.
	* **Filtering**: offers an elegant way to filter out all the elements of a sequences for which the function returs True
	* **Reduce**: continually applies the function func() to the sequences seq. It returns a single value
```
Guido van Rossum hates reduce(), as we can learn from his statement in a posting, March 10, 2005, in artima.com:

"So now reduce(). This is actually the one I've always hated most, because, apart from a few examples involving + or *, almost every time I see a reduce() call with a non-trivial function argument, I need to grab pen and paper to diagram what's actually being fed into that function before I understand what the reduce() is supposed to do. So in my mind, the applicability of reduce() is pretty much limited to associative operators, and in all other cases it's better to write out the accumulation loop explicitly." 
```
Write a function that compues the square value of all integers of a matrix
* Prototype: `def square_matrix_simple(matrix=[]):`
* `matrix` is a 2 dimensional array
* Returns a new matrix:
	* Same size as `matrix`
	* Each value should be the square of the value of the input
* You are not allowed to import any module
* You are allowed to use regular loops, `map`, etc
```
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
```
