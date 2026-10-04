## function-it is a block of code that performs a specific task. Functions are defined using the def keyword and can take input parameters and return output values. Functions can be called multiple times in a program, making them reusable and modular.
## user defined function
def add(a,b):
    return a+b

# calling the function
result = add(5, 3)
print(result)

##module-it is a file that contains a collection of related functions, classes, and variables. Modules can be imported into other Python programs using the import statement, allowing for code reuse and organization. Python has a large standard library of built-in modules, and users can also create their own custom modules.   
def sum(a,b):
    c = a+b
    return c
def multiply(a,b):
    c = a*b
    return c
print(sum(5,3),multiply(5,3))
##math module
import math
x=11.5
print(math.ceil(x))  # Output: 12   
print(math.floor(x)) # Output: 11
print(math.sqrt(x)) # Output: 4.0
print(math.fabs(x))  # Output: 11.5
print(math.factorial(int(x))) # Output: 120  
l=[1,2,3,4,5]
print(math.fsum(l)) # Output: 15.0  
## random module in python is used to generate random numbers and perform random operations. It provides various functions to generate random integers, floating-point numbers, and sequences. The random module is commonly used in simulations, games, and other applications that require randomness.
import random
print(random.random())  # Output: a random float between 0.0 and 1.0
print(random.randint(1, 10))  # Output: a random integer between 1 and 10
print(random.choice([1, 2, 3, 4, 5]))  # Output: a random element from the list
print(random.randrange(1, 10, 2))  # Output: a random odd integer between 1 and 9   
print(random.shuffle([1, 2, 3, 4, 5]))  # Output: shuffles the list in place    
print(random.sample([1, 2, 3, 4, 5], 3))  # Output: a random sample of 3 elements from the list     
print(random.uniform(1, 10))  # Output: a random float between 1.0 and 10.0 
## date time modules in python is used to work with dates and times. It provides classes for manipulating dates and times in both simple and complex ways. The datetime module allows you to create, format, and manipulate date and time objects, making it useful for applications that require date and time functionality.
import datetime
now = datetime.datetime.now()
print(now)  
## number guessing game using functions and modules
#import random  

#target = random.randint(1, 100)
#while (guess := int(input("Guess a number between 1 and 100: "))) != target:
   # print("Too high!"if guess > target else "Too low!")
#print("Congratulations! You guessed it right.")
## rock paper sissor game 
import random

while (u := input("Rock, Paper, or Scissors? (exit to quit): ").lower()) != 'exit':
    c = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {c}")
    print("Tie!" if u == c else "You win!" if (u, c) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")] else "You lose!")
## pickle module 
import pickle
l=[10,20,30,40]

