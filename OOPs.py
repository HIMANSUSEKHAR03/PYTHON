

## 1) Example: Car class

# This is the simplest and best starting point.


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} {self.color} car is starting.")

    def stop(self):
        print(f"{self.brand} car is stopping.")

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.start()
car2.start()
car1.stop()


### What this teaches
# - `class Car`: blueprint
# - `self.brand`: attribute
# - `start()`: method
# - `car1` and `car2`: objects


## 2) Example: Bank account

# This is excellent for understanding encapsulation.

# ```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Aman", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())

### What this teaches
# - private data with `__balance`
# - use methods instead of direct access
# - hiding implementation details

# This is a classic OOP concept.


## 3) Example: Animal inheritance

# This explains inheritance clearly.

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


### What this teaches
# - parent class: `Animal`
# - child classes: `Dog`, `Cat`
# - same method name, different behavior

# This is polymorphism too.

# ---

## 4) Example: Employee and Manager

This is a very common real-life example.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus

m = Manager("Riya", 50000, 10000)
print(m.get_salary())
print(m.total_salary())
```

### What this teaches
- inheritance
- `super()`
- child class extending parent class

---

## 5) Example: Shape abstraction

This helps understand abstraction.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(4, 5)
c = Circle(3)

print(r.area())
print(c.area())
```

### What this teaches
- abstract class
- abstract method
- common behavior with different implementations

---

## 6) Example: Student management system

This is an excellent project-style OOP example.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return "Pass"
        return "Fail"

s1 = Student("Aman", 78)
s2 = Student("Neha", 35)

print(s1.name, s1.result())
print(s2.name, s2.result())
```

### What this teaches
- object state
- behavior with data
- real-world modeling

---

## 7) Example: Laptop object

This is very easy to visualize.

```python
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def specs(self):
        print(f"{self.brand} laptop with {self.ram} RAM and {self.storage} storage.")

l1 = Laptop("Dell", "16GB", "512GB")
l2 = Laptop("HP", "8GB", "256GB")

l1.specs()
l2.specs()
```

### What this teaches
- objects with multiple attributes
- realistic modeling

---

## 8) Best real-world analogy

Think of OOP like a school system:

```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(self.name, self.roll_no)

class ScienceStudent(Student):
    def __init__(self, name, roll_no, subject):
        super().__init__(name, roll_no)
        self.subject = subject

    def display(self):
        print(self.name, self.roll_no, self.subject)

s = ScienceStudent("Ravi", 12, "Physics")
s.display()
```

This teaches:
- inheritance
- overriding
- object properties

---

## The 4 core OOP ideas to remember

### 1. Encapsulation
Wrap data and methods together

```python
class Person:
    def __init__(self, name):
        self.name = name
```

### 2. Inheritance
Reuse from parent class

```python
class Teacher(Person):
    pass
```

### 3. Polymorphism 
# Same method, different behavior


class Cat:
    def sound(self):
        print("Meow")

### 4. Abstraction
class Vehicle:
    def start(self):
        pass


## Best order to learn OOP

# 1. Class + object
# 2. Constructor `__init__`
# 3. Attributes
# 4. Methods
# 5. Inheritance
# 6. Encapsulation
# 7. Polymorphism
# 8. Abstraction

# ---

## One very important rule

# If you want to truly understand OOP, always ask:
# - What is the object?
# - What data does it hold?
# - What actions can it perform?
# - How does one class relate to another?

## Best example to remember forever

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

d1 = Dog("Tommy", 3)
d2 = Dog("Bruno", 5)

d1.bark()
d2.bark()


# This single example teaches:
# - class
# - object
# - attribute
# - method
# - multiple instances
