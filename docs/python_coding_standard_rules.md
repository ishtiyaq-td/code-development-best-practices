# Python Coding Standard Rules

## Rules for filename and folder name

All the files and folders should be in lowercase only and should be separated with underscore only.

## Python Naming Convention

The style guide for Python is based on [Guido’s](https://www.python.org/doc/essays/styleguide/) naming convention recommendations.

| Type                       | Public             | Internal            |
| -------------------------- | ------------------ | ------------------- |
| Packages                   | lower_with_under   |                     |
| Modules                    | lower_with_under   | _lower_with_under   |
| Classes                    | CapWords           | _CapWords           |
| Exceptions                 | CapWords           |                     |
| Functions                  | lower_with_under() | _lower_with_under() |
| Global/Class Constants     | CAPS_WITH_UNDER    | _CAPS_WITH_UNDER    |
| Global/Class Variables     | lower_with_under   | _lower_with_under   |
| Instance Variables         | lower_with_under   | _lower_with_under   |
| Method Names               | lower_with_under() | _lower_with_under() |
| Function/Method Parameters | lower_with_under   |                     |
| Local Variables            | lower_with_under   |                     |

### Python Naming Convention > Class Naming

#### PascalCase

* Begin with an uppercase letter
* Preferably a noun e.g. Car, Bird, MountainBike
* Avoid acronyms and abbreviations

```python
class Car:
    ...
```

#### Private Class

Python does not support privacy directly. This naming convention is used as a weak internal use indicator.

* Should follow the above naming conventions
* Should use a leading underscore (_) to distinguish between "public" and "private" classes
* For more read the [official python documentation](https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references).

```python
class _Car: # private class
```

### Python Naming Convention > Constant Naming

#### SCREAMING_SNAKE_CASE

* Should be all uppercase letters e.g. AGE, HEIGHT
* If the name contains multiple words, it should be separated by underscores (_) such as DAYS_IN_MONTH
* May contain digits but not as the first letter

```python
class Product:
    MAX_TEMPERATURE = 36;
```

### Python Naming Convention > Method Naming

#### snake_case

* Should be all in lowercase
* Preferably a verb e.g. get_car(), purchase(), book()
* If the name contains multiple words, it should be separated by underscores \(\_\) e.g. get\_json\(\)

```python
class Person:
    def get_height(self):
        return self.height
```

#### Private Method

Python does not support privacy directly. This naming convention is used as a weak internal use indicator.

* Should follow the above naming conventions
* Should use a leading underscore (_) to distinguish between "public" and "private" functions in a module
* For more read the [official python documentation](https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references). 

```python
class Person:
    def _foot_to_centimeter(self): # private method
        return self.height * 30.48
```

### Python module Convention > Module Naming

#### snake_case

* Should be all in lowercase letters such as requests, math
* If contains multiple words, it should be separated by underscores (_) e.g. expression_engine.py
* Should resonate with the class or methods inside the module

```python
from math import factorial
class Car:
    ...
```

### Python Naming Convention > Variable Naming

#### snake_case

* Should be all in lowercase
* Not begin with the special characters like e.g. & (ampersand), $ (dollar)
* If the name contains multiple words, it should be separated by underscores (_) e.g. json_string
* Avoid one-character variables e.g. a, b

```python
class Student
    age = None
    ...
```

#### Private Variable

Python does not support privacy directly. This naming convention is used as a weak internal use indicator.

* Should follow the above naming conventions
* Should use a leading underscore (_) to distinguish between "public" and "private" variables
* For more read the [official python documentation](https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references). 

```python
class Student:
    age = None # public variable
    _id = 0 # Private variable
```

### Python module Convention > Package Naming

#### snake_case

* Should be in lowercase.
* If the name contains multiple words, an underscore (_) should separate it.E.g. expression_engine
* The name should resonate with the class or methods inside the module

```python
from math import factorial
class Car:
    ...
```

### Python Naming Convention > Exception Naming

#### PascalCase

* Exceptions should be classes and hence the class naming convention should be used.
* Add a suffix "Error" on your exception names, provided the exception is actually an error.
* Avoid acronyms and abbreviations

```python
class ElectricCarError(Exception):
    """Basic exception for errors raised by non electric cars"""
    def __init__(self, car, type):
        if type is not "electric":
            msg = "%s is not an electric car" % car
        super(ElectricCarError, self).__init__(msg)
        self.car = car
```

The underscore (\_)  has special meaning in Python.

#### For ignoring values

If you do not need a specific value(s) while unpacking an object, just assign the value(s) to an underscore.

```python
x, _, y = (1, 2, 3)

# Ignore the multiple values. It is called "Extended Unpacking" which is available in only Python 3.x
x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5  

# ignore the index
for _ in range(10):
    task()  

# Ignore a value of specific location
for _, val in list_of_tuples: # [(1,2),(3,4),(5,6)]
    print(val) # output - 3
```

##### \_single_leading_underscore

This convention is used for declaring private variables, functions, methods and classes. Anything with this convention are ignored in `from module import *`.

##### single_trailing_underscore_

This convention should be used for avoiding conflict with Python keywords or built-ins.

```python
class_ = dict(n=50, boys=25, girls=25)
# avoiding clash with the class keyword
```

##### \__double_leading_underscore

Double underscore will mangle the attribute names of a class to avoid conflicts of attribute names between classes. Python will automatically add "\_ClassName" to the front of the attribute name which has a double underscore in front of it.

[Read more](https://docs.python.org/3/tutorial/classes.html#private-variables)

##### \__double_leading_and_trailing_underscore\_\_

This convention is used for special variables or ( magic )methods  such as`__init__`, `__len__`. These methods provides special syntactic features.

```python
class FileObject:
    '''Wrapper for file objects to make sure the file gets closed on deletion.'''

    def __init__(self, filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')
```

[List of magic methods](https://github.com/RafeKettler/magicmethods/blob/master/magicmethods.pdf).
