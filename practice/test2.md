# 🐍 Python Deep Dive  
**Generators | Enum | Zip | Map / Filter / Reduce | str & repr**

---

## Generators

```python
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


## Enum
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


## Zip and unzip

a = (1, 2, 3, 4)
b = ('a', 'b', 'c')

pair = list(zip(a, b))  # Zipping
print(pair)

c, d = zip(*pair)  # Unzipping
print("c:", c)
print("d:", d)

## Map, Filter, Reduce

from functools import reduce

l = [1, 2, 3, 4]

squares = list(map(lambda x: x**2, l))     # Map
even = list(filter(lambda x: x % 2 == 0, l)) # Filter
sum_val = reduce(lambda x, y: x + y, l)      # Reduce

print(squares)
print(even)
print(sum_val)


## str and repr

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"


p = Person("Alice", 30)

print(p)        # Calls __str__
print(str(p))   # Explicit str()
print(repr(p))  # Explicit repr()
p               # REPL auto calls __repr__

```

