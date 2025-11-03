# 1. List, Tuple, Dictionary, Set/FrozenSet
```python
l = [1,2,3,4]
t = (1,2,3,4)
d = {1:"1", 2:"2", 3:"3"}
l.append(5)
l.insert(2, 6)
d.update({4:"4"})
print(l, t, d)
del d[4]
l.remove(5)
print(l, t, d)
```
# 2. Lambda Function
```python
double = lambda x: x * 2
print(double(5))

```
# 3. Class Method, Static Method, Instance Method
```python

class Employee:
    company_name = "TechCorp"  

    def __init__(self, name, salary):
        self.name = name       
        self.salary = salary

    # Instance Method — works with *object data*
    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")

    # Class Method — works with *class data*
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
        print(f"Company name changed to: {cls.company_name}")

    # Static Method — *utility function*, no access to class or instance
    @staticmethod
    def is_workday(day):
        return day.lower() not in ["saturday", "sunday"]


# Create an object
e1 = Employee("Mukul", 50000)

# Instance method → acts on specific object
e1.show_details()

# Class method → acts on class itself
Employee.change_company("BestPeers")

# Static method → independent utility
print("Is Monday a workday?", Employee.is_workday("Monday"))
print("Is Sunday a workday?", Employee.is_workday("Sunday"))
```
# 4. Shallow Copy, Deep Copy
```python
import copy

# Original list with nested list inside
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow_copied = copy.copy(original)

# Deep copy
deep_copied = copy.deepcopy(original)

print("Original:", original)
print("Shallow Copy:", shallow_copied)
print("Deep Copy:", deep_copied)

# Now modify one inner list in the original
original[0][0] = 99

print("\nAfter modifying original[0][0] = 99")
print("Original:", original)
print("Shallow Copy:", shallow_copied)  # Will also change (shared inner list)
print("Deep Copy:", deep_copied)        # Unaffected (independent copy)
```
# 5. Generators, Iterators
```python
# Generators
def count(n):
    for i in range(n):
        yield i + 1
    
n = 5
gen = count(n)
print(next(gen))
print(next(gen))
print(next(gen))


def greeter():
    name = yield "What's your name?"
    yield f"Hello, {name}!"

g = greeter()
print(next(g))        
print(next(g)) 

# Iterators

nums = [1, 2, 3]

# Convert iterable to iterator
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```
# 6. Enum
```python
from enum import Enum, auto

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    

class Status(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    DONE = auto()

# print(Status.PENDING.value)


class Shape(Enum):
    CIRCLE = "O"
    SQUARE = "[]"

    def describe(self):
        return f"This is a {self.name} with symbol {self.value}"

print(Shape.SQUARE.describe())


for color in Color:
    print(color)

```
# 7. Zip
```python

a = (1, 2, 3, 4)
b = ('a', 'b', 'c')

pair = list(zip(a, b))  # Zipping
print(pair)

c, d = zip(*pair)  # Unzipping
print("c:", c)
print("d:", d)
```
# 8. map, Filter, Reduce
```python

from functools import reduce

l = [1, 2, 3, 4]

squares = list(map(lambda x: x**2, l))     # Map
even = list(filter(lambda x: x % 2 == 0, l)) # Filter
sum_val = reduce(lambda x, y: x + y, l)      # Reduce

print(squares)
print(even)
print(sum_val)
```
# 9. Exception Handling
```python
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers only.")
else:
    print(f"Result is: {result}")
finally:
    print("Program execution completed.")
```
# 10. str, repr
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"


p = Person("Alice", 30)

print(p)       
print(str(p))  
print(repr(p)) 
p    
```
# 11. File Handling
```python
# f = open('data.txt', 'r')


# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# # for i in f:
# #     print(i.strip())

# f = open('data.txt', 'w')

# f.write("I am Mukul Malse")

f = open('data.txt', 'a')
# f.write("\n This is newly added line.")
# f.write("This is newly added line 2.")

lines = ["Aa\n", "Bb\n", "Cc\n"]

f.writelines(lines)
f.close()

```
# 12. Context management
```python
with open("data.txt", "a") as f:
    f.write("Its 23 October today")

with open("data.txt", "r") as f:
    print(f.read())


# File Handling

try:
    with open("data.txt", "r") as f:
        d = f.read()
        print(d)
except FileNotFoundError as e:
    print("Error Handled", e)

# Custom Context Management

class MyContext:
    def __enter__(self):
        print("Entering Context...")
        return "resources"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit Context...")
        if exc_type:
            print("Error", exc_value)
        return True

with MyContext() as m:
    print("Inside Block...")
    
    raise ValueError("Something went wrong.")

```
