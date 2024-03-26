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
	* **Union**:<br /> Set Union operation. Union of 2 functions is the set of all the elements from both sets in a single different set.
	* **Copy**:<br /> Create a new set based on an existing set, but do not want to modify the original set.
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
# Task
## 0. Write a function that compues the square value of all integers of a matrix
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
**SOLVED**
```
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_ls = [x[:] for x in matrix]
    for x in range(len(matrix)):
        for i in range(len(matrix[x])):
            new_ls[x][i] = new_ls[x][i] ** 2
    return new_ls
```
## 1. Write a function that replaces all occurrences of an element by another in a new list.
* **Prototype**: `def search_replace(my_list, search, replace):`
* `my_list is the initial list`
* `search` is the element to replace in the list
* `replace` is the new element
You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_ls = my_list[:]
    for z in range(len(new_ls)):
        if new_ls[z] == search:
            new_ls[z] = replace
    return new_ls
```
## 2. Write a function that adds all unique integers in a list (only once for each integer).
* **Prototype**: `def uniq_add(my_list=[]):`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

guillaume@ubuntu:~/$ ./2-main.py
Result: 15
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = sum(set(my_list))
    return s
```
## 3. Write a function that returns a set of common elements in two sets.
* **Prototype**: `def common_elements(set_1, set_2):`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/$ ./3-main.py
['C']
guillaume@ubuntu:~/$
```
**SOLVED**
```
#!/usr/bin/python3
def common_elements(set_1, set_2):
    return (set_1 & set_2)
```
## 4. Write a function that returns a set of all elements present in only one set.
* **Prototype**: `def only_diff_elements(set_1, set_2):`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

guillaume@ubuntu:~/$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
guillaume@ubuntu:~/$
```
**SOLVED**
```
#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)
```
## 5. Write a function that returns the number of keys in a dictionary.
* **Prototype**: `def number_keys(a_dictionary):`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

guillaume@ubuntu:~/$ ./5-main.py
Number of keys: 3
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def number_keys(a_dictionary):
    return len(a_dictionary.keys())
```
## 6. Write a function that prints a dictionary by ordered keys.
* **Prototype**: `def print_sorted_dictionary(a_dictionary):`
* You can assume that all keys are strings
* Keys should be sorted by alphabetic order
* Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
* Dictionary values can have any type
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_ls = list(sorted(a_dictionary))
    for i in range(len(new_ls)):
        print("{:s}: {}".format(new_ls[i], a_dictionary[new_ls[i]]))

```
## 7. Write a function that replaces or adds key/value in a dictionary.
* **Prototype**: `def update_dictionary(a_dictionary, key, value):`
* `key` argument will be always a string
* `value` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
```
## 8. Write a function that deletes a key in a dictionary.
* **Prototype**: `def simple_delete(a_dictionary, key=""):`
* `key` argument will be always a string
* If a key doesn’t exist, the dictionary won’t change
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
```
## 9. Write a function that returns a new dictionary with all values multiplied by 2
* **Prototype**: `def multiply_by_2(a_dictionary):`
* You can assume that all values are only integers
* Returns a new dictionary
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

guillaume@ubuntu:~/$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_ls = a_dictionary.copy()
    key = list(new_ls.keys())
    [new_ls[key[i]]for i in range(len(key))]
    return new_ls

```
## 10. Write a function that returns a key with the biggest integer value.
* **Prototype**: `def best_score(a_dictionary):`
* You can assume that all values are only integers
* If no score found, return `None`
* You can assume all students have a different score
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

guillaume@ubuntu:~/$ ./10-main.py
Best score: Molly
Best score: None
guillaume@ubuntu:~/$
```
**SOLVED**
```
#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    key = list(a_dictionary.keys())
    score = key[0]
    for i in range(len(key)):
        if a_dictionary[score] >= a_dictionary[key[i]]:
            continue
        else:
            score = key[i]
    return score
```
## 11. Write a function that returns a list with all values multiplied by a number without using any loops.
* **Prototype**: `def multiply_list_map(my_list=[], number=0):`
* Returns a new list:
    * Same length as `my_list`
    * Each value should be multiplied by `number`
* Initial list should not be modified
* You are not allowed to import any module
* You have to use `map`
* Your file should be max 3 lines
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/$
```
**SOLVED**
```
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
```
## 12. Write a function that returns a list with all values multiplied by a number without using any loops.
* Prototype: `def multiply_list_map(my_list=[], number=0):`
* Returns a new list:
    * Same length as `my_list`
    * Each value should be multiplied by `number`
* Initial list should not be modified
* You are not allowed to import any module
* You have to use `map`
* Your file should be max 3 lines
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
        'XC': 90, 'CD': 400, 'CM': 900
    }
    num = 0
    i = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    while i < len(roman_string):
        if roman_string[i:i+2] in rom_dict:
            num += rom_dict[roman_string[i:i+2]]
            i = i + 2
        else:
            num += rom_dict[roman_string[i]]
            i = i + 1
    return num
```