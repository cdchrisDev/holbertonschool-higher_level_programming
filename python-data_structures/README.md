# Python - Data structures: List and tuples
### Resources
* [3.1.3 Lists](https://intranet.hbtn.io/rltoken/UCQlbIrhZJVRfxndAcskkw)
* [Data structures](https://intranet.hbtn.io/rltoken/89W42byWTSM4e25VSPKMRg)
* [Learn to program 6: Lists](https://intranet.hbtn.io/rltoken/JNLdadDW7IWjwW9dbcEyhg)
## Learning Objectives
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the `del` statement and how to use it
# Task
## 0. Write a function that prints all integers of a list.
* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print('{:d}'.format(i))
```
## 1. Write a function that retrieves an element from a list.
* Prototype: `def element_at(my_list, idx):`
* If `idx` is negative, the function should return `None`
* If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
* You are not allowed to import any module
* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    else:
        return my_list[idx]
```
## 2. Write a function that replaces an element of a list at a specific position.

* Prototype: `def replace_in_list(my_list, idx, element):`
* If `idx` is negative, the function should not modify anything, and returns the original list
If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use `try/except`
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
```
## 3. Write a function that prints all integers of a list, in reverse order.
* Prototype: `def print_reversed_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    my_list.reverse()
    for i in my_list:
        print('{:d}'.format(i))
```
## 4. Write a function that replaces an element in a list at a specific position without modifying the original list.
* Prototype: `def new_in_list(my_list, idx, element):`
* If `idx` is negative, the function should return a copy of the original `list`
* If `idx` is out of range (> of number of element in my_list), the function should return a copy of the original `list`
* You are not allowed to import any module
* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list[:]
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    else:
        list[idx] = element
        return list
```
## 5. Write a function that removes all characters c and C from a string.
* Prototype: `def no_c(my_string):`
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use `str.replace()`
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def no_c(my_string):
    result = []
    for i in my_string:
        if i != 'c' and i != 'C':
            result.append(i)
    return ''.join(result) # concat to empty string
```
## 6. Write a function that prints a matrix of integers.
* Prototype: `def print_matrix_integer(matrix=[[]]):`
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j < len(matrix[i]) - 1:
                print(" ", end="")
        print()
```
## 7. Write a function that adds 2 tuples.
* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Returns a tuple with 2 integers:
    * The first element should be the addition of the first element of each argument
    * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value `0` for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
```
## 8. Write a function that returns a tuple with the length of a string and its first character.
* Prototype: `def multiple_returns(sentence):`
* If the sentence is empty, the first character should be equal to `None`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)

    return len(sentence), sentence[0]
```
## 9. Write a function that finds the biggest integer of a list.
* Prototype: `def max_integer(my_list=[]):`
* If the list is empty, return `None`
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin `max()`
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/$ ./9-main.py
Max: 90
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    i = len(my_list) - 1
    my_list.sort()

    return my_list[i]
```
## 10. Write a function that finds all multiples of 2 in a list.
* Prototype: `def divisible_by_2(my_list=[]):`
* Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_ls = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_ls.append(True)
        else:
            new_ls.append(False)
    return new_ls
```
## 11. Write a function that deletes the item at a specific position in a list.
* Prototype: `def delete_at(my_list=[], idx=0):`
* If `idx` is negative or out of range, nothing change (returns the same list)
* You are not allowed to use `pop()`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    del my_list[idx]
    return my_list
```
## 12. Complete the source code in order to switch value of `a` and `b`
* You can find the source code [here](https://intranet.hbtn.io/rltoken/9viUCbnIwdfsOPV_UrvIRA)
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/$ 
```
**SOLVED**
```
#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
```
