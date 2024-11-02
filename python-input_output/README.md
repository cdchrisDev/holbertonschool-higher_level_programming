# This is python INPUT and OUTPUT
### Resources
* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) *(until “11.4 Binary Files” (included))*
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) *(ch. 8 p 180-183 and ch. 14 p 326-333)*
* [sys package](https://docs.python.org/3/library/sys.html)
## 0. Write a function that reads a text file (UTF8) and prints it to stdout:
* **Prototype**: `def read_file(filename=""):`
* You must use the `with` statement
* You don’t need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
```
## 1. Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
* **Prototype**: `def write_file(filename="", text=""):`
* You must use the `with` statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

guillaume@ubuntu:~/$ ./1-main.py
24
guillaume@ubuntu:~/$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
def write_file(filename="", text=""):
    cnt = 0
    with open(filename, 'w', encoding='utf-8') as f:
        for c in text:
            f.write(c)
            cnt += 1
        return cnt
```
## 2. Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
* **Prototype**: `def append_write(filename="", text=""):`
* If the file doesn’t exist, it should be created
* You must use the `with` statement
* You don’t need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

guillaume@ubuntu:~/$ cat file_append.txt
cat: file_append.txt: No such file or directory
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file_append.txt
This School is so cool!
guillaume@ubuntu:~/$ ./2-main.py
24
guillaume@ubuntu:~/$ cat file_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
def append_write(filename="", text=""):
    cnt = 0
    with open(filename, 'a', encoding="utf-8") as f:
        for c in text:
            f.write(c)
            cnt += 1
        return cnt
```
## 3. Write a function that returns the JSON representation of an object (string):
* **Prototype**: `def to_json_string(my_obj):`
* You don’t need to manage exceptions if the object can’t be serialized.
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}
<class 'str'>
[TypeError] Object of type set is not JSON serializable
guillaume@ubuntu:~/$ 
```
**SOLVED**
```
#!/usr/bin/python3
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
```
