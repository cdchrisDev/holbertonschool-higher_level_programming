# This is the If else statements Python Module (2/29)
### Resources
* [More Control Flow Tools (Read until “4.6. Defining Functions” included)](https://intranet.hbtn.io/rltoken/2JgLsB5c9CpN5xkYS9wMKQ)
* [IndentationError](https://intranet.hbtn.io/rltoken/2JgLsB5c9CpN5xkYS9wMKQ)
* [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/Bt4ISTvUyfB6lFxEoL3NwQ)
* [Learn to Program 2 : Looping](https://intranet.hbtn.io/rltoken/qwVdwqW4LROXY0CIbWNiAw)
* [Pycodestyle – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/8D5JdrayXbe3ZzPWr335dQ)
# Tasks
## 0. This program will assign a random signed `number` to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
* You can find the source code [here](https://intranet.hbtn.io/rltoken/aBRwd0uo_aZMPK2CBG1syg)
* The variable `number` will store a different value every time you will run this program
* You don’t have to understand what `import`, `random`. `randint` do. Please do not touch this code
* The output of the program should be:
    * The number, followed by
        + if the number is greater than 0: `is positive`
        + if the number is 0: `is zero`
        + if the number is less than 0: `is negative`
    * followed by a new line
```
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/$
```
**SOLVED**
```
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number} ", end="")
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
```