## WE WILL SOLVE 10 QUESTIONS IN PYTHON THAT WILL COVER SOME BASICS OF THE PYTHON PROGRAMMING LANGUAGE
## QUESTION 1: PROGRAM TO perform all the arithmatic operations in TWO NUMBERS IN PYTHON 
a=eval(input("enter the first number:")) ## I HAVE TAKEN EVAL INPUT FROM THE USER SO THAT IT CAN TAKE ANY TYPE OF NUMBER LIKE INTEGER OR FLOAT
b=eval(input("enter the second number:"))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
# OUTPUT:
# enter the first number:10
# enter the second number:2
# Addition: 12
# Subtraction: 8
# Multiplication: 20
# Division: 5.0
# Modulus: 0
# Exponentiation: 100
# Floor Division: 5

##QUESTION 2: BY IMPORTING THE MATH MODULE WE WILL PERFORM SOME OPEARTIONS LIKE SQUARE ROOT, SINE, COSINE, TANGENT, LOGARITHM, FACTORIAL, CEIL AND FLOOR FUNCTIONS AND EXPONENTIATION FUNCTION
import math
from random import random
from tokenize import Number
N1 = eval(input("Enter the first number: "))
N2 = eval(input("Enter the second number: "))

print("Square Root of N1:", math.sqrt(N1))  ### IT WILL RETURN THE SQUARE ROOT OF THE GIVEN NUMBER
print("Sine of N1:", math.sin(N1))    ### IT WILL RETURN THE SINE VALUE OF THE GIVEN NUMBER
print("Cosine of N1:", math.cos(N1))  ## IT WILL RETURN THE COSINE VALUE OF THE GIVEN NUMBER
print("Tangent of N1:", math.tan(N1)) ## IT WILL RETURN THE TANGENT VALUE OF THE GIVEN NUMBER
print("Logarithm of N1:", math.log(N1))   ### IT WILL RETURN THE LOGARITHM OF THE GIVEN NUMBER
print("Factorial of N1:", math.factorial(int(N1))) ## FACTORIAL FUNCTION WILL TAKE ONLY INTEGER VALUE SO I HAVE CONVERTED THE FLOAT OR ANY TYPE  VALUE TO INTEGER VALUE USING INT() FUNCTION AAND IT WILL GIVE THE FACTORIAL OF THAT INTEGER VALUE
print("Ceil of N1:", math.ceil(N1))   ### IT WILL RETURN CEIL VALUE MEANS THE VALUE WHICH IS GREATER THAN OR EQUAL TO THE GIVEN NUMBER
print("Floor of N1:", math.floor(N1)) ## IT WILL RETURN FLOOR VALUE MEANS THE VALUE WHICH IS LESS THAN OR EQUAL TO THE GIVEN NUMBER
print("Exponentiation of N1 and N2:", math.pow(N1, N2))  ### IT WILL RETURN THE EXPONENTIATION VALUE OF THE GIVEN TWO NUMBERS AND THE N2WILL BE THE POWER OF N1

# OUTPUT : 
# Square Root of N1: 3.1622776601683795
# Sine of N1: -0.5440211108893698
# Cosine of N1: -0.8390715290764524
# Tangent of N1: 0.6483608274590866
# Logarithm of N1: 2.302585092994046
# Factorial of N1: 3628800
# Ceil of N1: 10
# Floor of N1: 10
# Exponentiation of N1 and N2: 100000.0

# QUESTION 3 : CALCULATE THE AREA AND PERIMETER OF ALL SHAPES LIKE SQUARE, RECTANGLE, CIRCLE, TRIANGLE etc. USING PYTHON PROGRAMMING LANGUAGE
side = eval(input("Enter the side of the square: "))
area_square = side ** 2
perimeter_square = 4 * side
print("Area of square:", area_square)
print("Perimeter of square:", perimeter_square)
length = eval(input("Enter the length of the rectangle: "))
width = eval(input("Enter the width of the rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area of rectangle:", area_rectangle)
print("Perimeter of rectangle:", perimeter_rectangle)
base = eval(input("Enter the base of the triangle: "))
height = eval(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
perimeter_triangle = base + height + (base ** 2 + height ** 2)
print("Area of triangle:", area_triangle)
print("Perimeter of triangle:", perimeter_triangle)
radius = eval(input("Enter the radius of the circle: "))
area_circle = math.pi * radius ** 2
perimeter_circle = 2 * math.pi * radius
print("Area of circle:", area_circle)
print("Perimeter of circle:", perimeter_circle)

# OUTPUT : 
# Enter the side of the square: 4
# Area of square: 16
# Perimeter of square: 16
# Enter the length of the rectangle: 20
# Enter the width of the rectangle: 10
# Area of rectangle: 200
# Perimeter of rectangle: 60
# Enter the base of the triangle: 3
# Enter the height of the triangle: 5
# Area of triangle: 7.5
# Perimeter of triangle: 42
# Enter the radius of the circle: 2
# Area of circle: 12.566370614359172
# Perimeter of circle: 12.566370614359172 (AND ALL IN CM)

##QUESTION 4 : WRITE A PROGRAM TO SWAP VZRIABLES IN PYTHON WITHOUT USING THIRD VARIABLE
a = eval(input("Enter the first number: ")) 
b = eval(input("Enter the second number: "))
print("Before swapping: a =", a, "b =", b)
a = a + b     ## I TAKEN A AS 10 AND B AS 5 SO A+B=15 AND THEN I SUBTRACTED B FROM A+B SO 15-5=10 AND THEN I SUBTRACTED A FROM A+B SO 15-10=5
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

# OUTPUT : 
# Enter the first number: 10
# Enter the second number: 5
# Before swapping: a = 10 b = 5
# After swapping: a = 5 b = 10

## QUESTION 5 : WRITEA PROGRAM TO CONVERT KILOMETERS TO METERS, CENTIMETERS, MILLIMETERS, MILES, YARDS, FEET AND INCHES
kilometers = eval(input("Enter distance in kilometers: "))
meters = kilometers * 1000
centimeters = meters * 100
millimeters = centimeters * 10
miles = kilometers * 0.621371
yards = kilometers * 1093.61
feet = kilometers * 3280.84
inches = feet * 12

print("Distance in different units:")
print("Meters:", meters)
print("Centimeters:", centimeters)
print("Millimeters:", millimeters)
print("Miles:", miles)
print("Yards:", yards)
print("Feet:", feet)
print("Inches:", inches)

# OUTPUTS : Enter distance in kilometers: 2
# Distance in different units:
# Meters: 2000
# Centimeters: 200000
# Millimeters: 2000000
# Miles: 1.242742
# Yards: 2187.22
# Feet: 6561.68
# Inches: 78740.16

##QUESTION 6 : WRITE A PROGRAM TO CHECK A NUMBERS IS EVEN OR ODD, POSITIVE OR NEGATIVE, AND PRIME OR NOT
N = eval(input("Enter a number: "))
if N > 0:
    print("The number is positive.")
elif N==0:
    print("The number is zero.")
else:
    print("The number is negative.")
print(f"The number is {'even' if N % 2 == 0 else 'odd'}.")
print(f"The number is {'prime' if N > 1 and all(N % i != 0 for i in range(2, int(N**0.5) + 1)) else 'not prime'}.")

# OUTPUT : 
# Enter a number: 5
# The number is positive.
# The number is odd.
# The number is prime.

## QUESTION 7 : CHECK WHETHER A YEAR IS LEAPYEAR OR NOT AND HOW MANY MONTS , WEEKS, DAYS, HOURS, MINUTES AND SECONDS AND ALSO THE SUNDAYS ARE IN THAT YEAR
year = eval(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year AND THE DAYS IN THAT YEAR ARE 366.")
else:
    print(f"{year} is not a leap year AND THE DAYS IN THAT YEAR ARE 365.")

days_in_year = 366 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 365
months = 12
weeks = days_in_year // 7
hours = days_in_year * 24   
minutes = hours * 60
seconds = minutes * 60
SUndays = weeks  
print(f"Months: {months}, Weeks: {weeks}, Days: {days_in_year}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}, Sundays: {SUndays}")

# OUTPUT : 
# Enter a year: 2029
# 2029 is not a leap year AND THE DAYS IN THAT YEAR ARE 365.
# Months: 12, Weeks: 52, Days: 365, Hours: 8760, Minutes: 525600, Seconds: 31536000, Sundays: 52

## QUESTION 8 : WRITEA PROGRAM TO GENERATE 3 RANDOM NUMBERS BETWEEN 1 TO 100 AND CHECK EHICH ONE IS THE LARGEST AND SMALLEST NUMBER AND WHICH ONE IS EVEEN OR ODD.
import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print("Generated numbers:", num1, num2, num3)
print("Largest number:", max(num1, num2, num3))
print("Smallest number:", min(num1, num2, num3))
print("Number 1 is", "even" if num1 % 2 == 0 else "odd")
print("Number 2 is", "even" if num2 % 2 == 0 else "odd")
print("Number 3 is", "even" if num3 % 2 == 0 else "odd")

# OUTPUT : 
# Generated numbers: 24 72 14
# Largest number: 72
# Smallest number: 14
# Number 1 is even
# Number 2 is even
# Number 3 is even

## QUESTION 9 : WRITEA PROGRAM TO DISPLAY THE MULTIPLICATION TABLE OF A NUMBER ENTERED BY THE USER
num = eval(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# OUPUT : 
# Enter a number to display its multiplication table: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60

##QUESTION 10 : WRITE A PROGRAM TO SHOW THE ASCII VALUE OF THE NUMBER OR THE CHARACTER ENTERED:
value=input("enter the character or the number : ")
if len(value)==1:
    ascii_value=ord(value)
    print(f"the ascii vale of {value} is {ascii_value}.")
else :
    print("enter the correct value to find the ascii value of it")

# OUTPUT : 
# enter the character or the number : A
# the ascii vale of A is 65.
























