# Python - More Classes and Objects
### Resources
* [Object Oriented Programming ](https://python.swaroopch.com/oop.html)
* [Object Oriented Programming ](https://python-course.eu/oop/object-oriented-programming.php)
* [Class and instances Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
* [Properties vs Getter and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)
## 0. Write an empty class Rectangle that defines a rectangle:
* You are not allowed to import any module
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/$ 
```
**SOLVED**
```

```