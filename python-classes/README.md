# Python - Classes And Objects
### Resources
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/5envVBirO286MdSZgZ4DoQ)
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/sCdUrEsHLFH2NpUzI5Xx8w)
* [Properties Vs Getters and Setters](https://intranet.hbtn.io/rltoken/3B0RWILA_kSjK5udEbFt-A)
* [Python Classes and Objects](https://intranet.hbtn.io/rltoken/cwqg7Ud04LTDsatPT17CaQ)
* [OOP](https://intranet.hbtn.io/rltoken/6cZhWLe083CJERYLjAM0BQ)
## Learning Objectives
* What is OOP
	* Is a paradigm model that organize program designing around data wraped as objects
* first class everything
	* [Everythin is treated the same way](http://python-history.blogspot.com/2009/02/first-class-everything.html)
* What is a class
	* Classes provide a means of bundling data and functionality together. It creates a new type of object, Allowing new instances of that type to be made
* What is an Object and an instance
	* **object**:<br /> An objet is something a variable can refer to
	* **Instance**:<br /> An instance of a class is also an object
* What is an attribute
	* Python class attributes are variables of a class that are shared between all of its instances
* What are and how to use public, protected and private attributes
	* **ACCESS MODIFIERS**:
	* Public: The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default
	* Protected: The members of a class that are declared protected are only accessible to a class derived from it. Data members of a class are declared protected by adding a single `_` (underscore symbol) before data member of that class
	* Private: The members of a class that are declared private are accessible within the class only, private access modifier is the most secure modifier. Data members of a class are declared private by adding a double underscore `__` (symbol) before the data member of the class
* What is `self`
	* A representation of the instance of the class
* What is a method
	* A function that belongs to an object
* What is the special `__init__` method and how to use it
	* is an instance method that initializes a newly created object
* What is Data Abstraction, Data Encapsulation, and information hiding
	* **Data Abstraction**: a programming concept that hides complex implementation details while exposing only essential information and functionalities to users
	* **Data Encapsulation**: encapsulation refers to the bundling of data with the mechanisms or methods that operate on the data. It may also refer to the limiting of direct access to some of that data, such as an object's components
	* **Information hiding**: information hiding is the principle of segregation of the design decisions in a computer program that are most likely to change, thus protecting other parts of the program from extensive modification if the design decision is changed.
* What is a property
	*  is a special sort of class member, intermediate in functionality between a field and a method
* What is the difference between an attribute and a property in Python
	* attributes are simply data members of an object, while properties are methods that are accessed like attributes but actually perform some computation when called.
* What is the Pythonic way to write getters and setters in Python
	* Using the property() function to achieve getters and setter behavior. In Python, property() is a built-in function for creating and returning a property object. There are three methods on a property object: getter(), setter(), and delete().
 
