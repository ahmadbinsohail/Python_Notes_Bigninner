# 4th Lecture - Python Notes

This folder contains the learning files for the 4th lecture in Python.

## Folder Contents

1. `4th_Lec_(Classes).py`  
   This file explains the concept of classes in Python. It shows how to create a class, assign attributes, create objects, call methods, and use inheritance.

2. `Exeptions_(handing errors).py`  
   This file demonstrates Python exception handling. It shows how to use `try`, `except`, and how to handle invalid input and division by zero.

---

## 1) `4th_Lec_(Classes).py`

### What this code is doing

This file creates a class called `Human`.

### Class Structure

- `__init__(self, x, y, n)` is the constructor.
- It initializes the attributes:
  - `self.x`
  - `self.y`
  - `self.name`
- Class variables:
  - `age = 0`
  - `height = 0`
  - `color = 0`

### Methods

- `speak()` prints a greeting using the person's name.
- `eat()` prints the word `Eating`.

### Object Creation

The code creates two objects:

- `ahmad = Human(1, 1, "Ahmad Raza")`
- `ali = Human(2, 2, "Ali raza")`

Each object has its own values for `x`, `y`, and `name`.

### How the code works step by step

- `print(ahmad.age)` prints the initial age value.
- `ahmad.speak()` calls the method `speak()`.
- `ahmad.age = 20` changes the age of the object.
- `print(ahmad.x)` and `print(ahmad.y)` display the x and y values.
- `ali.eat()` calls the `eat()` method for `ali`.
- `Human.eat(ahmad)` calls the `eat()` method through the class itself.

### Inheritance

This part shows inheritance:

- `class Men(Human):` means `Men` inherits from `Human`.
- `class Women(Human):` means `Women` also inherits from `Human`.

The child classes call the parent class constructor using `super().__init__()` and add their own attribute:

- `self.hair = "Short"` in `Men`
- `self.hair = "Long"` in `Women`

The program then creates:

- `asma = Women("Asma")`
- `tayyab = Men("Tayyab")`

and prints their hair and age values.

### Learning purpose

This file teaches:

- how to define classes
- how to create objects
- how to use instance attributes
- how methods work
- how inheritance works

---

## 2) `Exeptions_(handing errors).py`

### What this code is doing

This file demonstrates how to handle errors in Python using `try` and `except`.

### Code explanation

```python
try:
    age = int(input("Enter your code here "))
    dev = 100 / age
    print(age)
except ValueError:
    print("Invalid Value ")
except ZeroDivisionError:
    print("Age cannot be zero ")
```

### How it works

- `input()` gets user input.
- `int(...)` converts the input to an integer.
- If user enters a non-numeric value, then `ValueError` occurs.
- If the user enters `0`, then `100 / age` causes a division by zero, which triggers `ZeroDivisionError`.

### Why exception handling is useful

This prevents the program from crashing when the user enters invalid input or a zero value.

### Learning purpose

This file teaches:

- how to use `try`
- how to catch errors with `except`
- how to avoid program crashes from bad user input

---

## Summary

This folder teaches two important Python concepts:

- Classes and Object-Oriented Programming
- Exception Handling

These are beginner-friendly examples meant to help understand basic Python programming logic.
