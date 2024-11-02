# This is the Clases Python Module (Object Oriented Programing) [7/25]
### Resources
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/5envVBirO286MdSZgZ4DoQ) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/sCdUrEsHLFH2NpUzI5Xx8w) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
* [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/3B0RWILA_kSjK5udEbFt-A)
* [Learn to Program 9 : Object Oriented Programming](https://intranet.hbtn.io/rltoken/5u8UhnaTWX2A-G7LICKCDw)
* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/cwqg7Ud04LTDsatPT17CaQ)
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/6cZhWLe083CJERYLjAM0BQ)
## 0. Write an empty class `Square` that defines a square:
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
"""This is the Square module"""


class Square:
    """Define a square"""

    pass
```
## 1. Write a class Square that defines a square by: (based on `0-square.py`)
* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)
* You are not allowed to import any module
**Why?**
<br />

*Why size is private attribute?*
<br />

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
"""This is the square module"""


class Square:
    """define a square"""

    def __init__(self, size):
        """init square"""

        self.__size = size
```
## 2. Write a class `Square` that defines a square by: (based on `1-square.py`)
* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
"""This is the square module"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """init square"""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
```
## 3. Write a class `Square` that defines a square by: (based on `2-square.py`)
* Private instance attribute: `size`
* Instantiation with optional `size`: `def __init__(self, size=0):`
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the message size must be >= 0
* Public instance method: `def area(self):` that returns the current square area
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Private instance attribute: size
    Instantiation with area method """

    def __init__(self, size=0):
        """Initializes attribute size """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)
```
## 4. Write a class `Square` that defines a square by: (based on `3-square.py`)
* Private instance attribute: `size`:
    * property `def size(self)`: to retrieve it
    * property setter `def size(self, value)`: to set it:
        + `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        + if `size` is less than `0`, raise a `ValueError` exception with the `message size must be >= 0`
* Instantiation with optional `size`: `def __init__(self, size=0):`
* Public instance method: `def area(self)`: that returns the current square area
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$
```
**SOLVED**
```
"""Access and update private attribute"""


class Square:
    """Private instance attribute: size
    Instantiation with area method """

    def __init__(self, size=0):
        """Initializes attribute size """
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
```
## 5. Write a class `Square` that defines a square by: (based on `4-square.py`)
* Private instance attribute: `size:`
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        + `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        + if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
* Instantiation with optional `size`: `def __init__(self, size=0):
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to 0, print an empty line
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
""" Printing a square"""


class Square:
    """Private instance attribute: size
    Instantiation with area method prints squares """

    def __init__(self, size=0):
        """Initializes attribute size """
        self.__size = size

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
        if self.size <= 0:
            print()
```
## 6. Write a class Square that defines a square by: (based on 5-square.py)
* Private instance attribute: `size:`
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        + `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        + if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
* Private instance attribute: `position:`
    * property def `position(self):` to retrieve it
    * property setter `def position(self, value):` to set it:
        + position must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message position `must be a tuple of 2 positive integers`
* Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
* Public instance method: `def area(self):` that returns the current square area
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to 0, print an empty line
    * `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Private instance attribute: size
    Instantiation with area and position method """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes attribute size """
        self.size = size
        self.position = position

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Initializes attribute position"""
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print method"""
        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.size):
                for e in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
```