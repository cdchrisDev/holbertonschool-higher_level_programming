# Python - Hello, World
* **Concepts**
	* [The Python Tutorial](https://intranet.hbtn.io/rltoken/dPj0pQKl_4ZuRk8oY_s6Wg)
	* [Python Programming: An introduction to computer science](https://intranet.hbtn.io/rltoken/m80k_C-bYzBqNccbtzY2Dg)
	* [Derek Banas' Learn to program](https://intranet.hbtn.io/rltoken/m80k_C-bYzBqNccbtzY2Dg)
	* [The python guru](https://intranet.hbtn.io/rltoken/9EJwb1y3Ha3aVgaM45z8XA)
	* [New string formatting](https://intranet.hbtn.io/rltoken/9EJwb1y3Ha3aVgaM45z8XA)
	* [Garbage collector](https://intranet.hbtn.io/rltoken/wz0Dq997wZFpwaFo3UhAdw)
	* [Python Interpreter](https://intranet.hbtn.io/rltoken/tHi0CphPU6xA2VGvVfVevA)
	* [Python bytecode](https://intranet.hbtn.io/rltoken/a4gn69uDQzfTiBGCKPbxDw)
### Resources
* [Learn to Program](https://intranet.hbtn.io/rltoken/a4gn69uDQzfTiBGCKPbxDw)
* [Whetting your Appetite](https://intranet.hbtn.io/rltoken/9w2S6R8vtwlmQcPg33445w)
* [Using the Python interpreter](https://intranet.hbtn.io/rltoken/9w2S6R8vtwlmQcPg33445w)
* [An informal introduction to python](https://intranet.hbtn.io/rltoken/9w2S6R8vtwlmQcPg33445w)
* [How to Use string formatters in Python 3](https://intranet.hbtn.io/rltoken/dd7bIKsC3_0wb3Np_8URUA)
* [Pycodestyle - Style Guide for python code](https://intranet.hbtn.io/rltoken/qHCPZY23PoEBaDVce2P0nw)
## Learning Objectives
* How to use the Python interpreter
* How to print text and variables using `print`
* How to use strings
* What are indexing and slicing in python
* What is the official Python coding style and how to check your code with `pycodestyle`

# Tasks

## 0. Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
Use the function print
```
guillaume@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/$
```
**SOLVED**
```
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

## 1. Complete this source code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py)
* The output of the script should be:
	* the number, followed by `Battery street`,
	* followed by a new line
* You are not allowed to cast the variable `number` into a string
* Your code must be 3 lines long
* You have to use f-strings [tips](https://intranet.hbtn.io/rltoken/dd7bIKsC3_0wb3Np_8URUA)
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```
**SOLVED**
```
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```

## 2. Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/4-print_float.py)
* The output of the program should be:
	* `Float:`, followed by the float with only 2 digits
	* followed by a new line
* You are not allowed to cast `number` to string
* You have to use f-strings
 ```
 guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
 ```
 **SOLVED**
 ```
 #!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
 ```
 
## 3. Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py)
* The output of the program should be:
	* 3 times the value of `str`
	* followed by a new line
	* followed by the 9 first characters of `str`
    * followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long
```
guillaume@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/$ 
```
**SOLVED**
```
#!/usr/bin/python3
str = "Holberton School"
print(f"{str * 3}")
print(str[0:9])
```

## 4. Complete this source code to print `Welcome to Holberton School!`

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py)
* You are not allowed to use any loops or conditional statements.
* You have to use the variables `str1` and `str2` in your new line of code
* Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/$ 
```
**SOLVED**
```
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```

## 5. Complete this source code

* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py)
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* `word_first_3` should contain the first 3 letters of the variable `word`
* `word_last_2` should contain the last 2 letters of the variable `word`
* `middle_word` should contain the value of the variable `word` without the first and last letters
```
guillaume@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/$ 
```
**SOLVED**
```
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[0:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```
## 6. Complete this source code to print `object-oriented programming with Python`, followed by a new line.
* You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py)
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals
```
guillaume@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/$ 
```
**SOLVED**
```
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)
```
## 7. Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
* Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
```
guillaume@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/$
```
**SOLVED**
```
#!/usr/bin/python3
import this
```
