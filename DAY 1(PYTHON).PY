 ## Question 1 : Print "Hello, World!" 5 times, each on a new line — first using a for loop, then using string multiplication
# Using string multiplication
print("Hello, World!\n" * 5)

## Question 2 :Store your name, age, and city in variables. Print this exact line using an f-string and also print the type of each variable.

name="Himansu" 
age=20
city="Bhubaneswar"
print(f"my name is {name},my age is {age},and i live in the city of {city}")
print(type(name))
print(type(age))
print(type(city))

## Question 3 : Print the following using a single print() statement (use sep and end):
print("day 1 python ","started ","already",sep="|",end =".")

## Question 4 : Given a = 5 and b = 10, swap them without a third variable. Print before and after.
a= 5
b= 10
print("Before swapping: a =", a, "b =", b)
a = a + b   
b = a - b   
a = a - b   
print("After swapping: a =", a, "b =", b)

## Question 5 : Take two numbers as input from the user. Print their sum, difference, product, quotient, floor division, remainder, and power — each on its own labeled line.

num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
print(f"Floor Division: {num1 // num2}")
print(f"Remainder: {num1 % num2}")
print(f"Power: {num1 ** num2}")

## question 6 : Q6. Ask the user for a number. Print:Its type,Its square,Its cube,Its square root (2 decimal places),Whether it's an integer or a float
#Edge case: Test with 5, 5.0, and -5. What changes?
num = eval(input("Enter a number: "))
print(f"Type: {type(num)}")
print(f"Square: {num ** 2}")
print(f"Cube: {num ** 3}")
import math
from pydoc import text
from string import digits
from unicodedata import digit
print(f"Square Root: {math.sqrt(num):.2f}")
if isinstance(num, int):
    print("It's an integer.")
else:
    print("It's a float.")

##Q7. Take a 3-digit number (e.g., 472). Extract and print:First digit,Middle digit,Last digit,Sum of all digits,Reversed number (e.g., 274),Do NOT use string slicing. Use only // and %.
num = eval(input("Enter a 3-digit number: "))
first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10
sum_of_digits = first_digit + middle_digit + last_digit
reversed_number = last_digit * 100 + middle_digit * 10 + first_digit

print(f"First digit: {first_digit}")
print(f"Middle digit: {middle_digit}")
print(f"Last digit: {last_digit}")
print(f"Sum of all digits: {sum_of_digits}")
print(f"Reversed number: {reversed_number}")

##Question 8 : Ask for Celsius. Convert to Fahrenheit and Kelvin. Print all three with 2 decimals.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")

# Then do the reverse — ask for Fahrenheit, print Celsius and Kelvin.
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
kelvin = celsius + 273.15

print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C = {kelvin:.2f}K")

## Question 9 : Q9. Ask for the user's birth year. Calculate their age (assume current year is 2026). Then calculate:Their age in months,Their age in days (assume 365.25 days/year),Their age in hours,Print all with proper labels.
#Edge case: If the user enters text instead of a number, catch it with try/except and print a helpful message.
import datetime
current_year = 2026
try:
    birth_year = int(input("Enter your birth year: "))
    age = current_year - birth_year
    age_in_months = age * 12
    age_in_days = age * 365.25
    age_in_hours = age_in_days * 24

    print(f"Your age is {age} years.")
    print(f"Your age in months is {age_in_months}.")
    print(f"Your age in days is {age_in_days:.2f}.")
    print(f"Your age in hours is {age_in_hours:.2f}.")
except ValueError:
    print("Please enter a valid year.")
## Question 10 : Q10. Ask the user for a principal amount P, annual rate R (in %), and time T (in years). Calculate:Simple Interest: SI = (P × R × T) / 100,Compound Interest: CI = P × (1 + R/100) ** T - P,Print both with 2 decimals, and also print the total amount for each.
    P = float(input("Enter the principal amount (P): "))
    R = float(input("Enter the annual rate (R) in %: "))
    T = float(input("Enter the time (T) in years: "))

    # Calculate Simple Interest
    SI = (P * R * T) / 100
    total_amount_SI = P + SI

    # Calculate Compound Interest
    CI = P * (1 + R / 100) ** T - P
    total_amount_CI = P + CI

    print(f"Simple Interest: {SI:.2f}")
    print(f"Total Amount with Simple Interest: {total_amount_SI:.2f}")
    print(f"Compound Interest: {CI:.2f}")
    print(f"Total Amount with Compound Interest: {total_amount_CI:.2f}")

## Question 11 : Given x = 10, print:type(x), id(x),x is 10,Create y = 10, print x is y,Create z = 1000, w = 1000, print z is w
##then in comments, explain why x is y is True but z is w might be False. (Hint: small int cache from -5 to 256.)
x = 10
print(type(x))
print(id(x))
print(x is 10)
y = 10
print(x is y)
z = 1000
w = 1000
print(z is w)  ## it might be False because Python caches small integers from -5 to 256, so x and y refer to the same object in memory, while z and w may not, as they are outside that range.

## Question 12 : Run this code and explain the output in comments:print(0.1 + 0.2),print(0.1 + 0.2 == 0.3)
##Then fix the comparison using round() or math.isclose().
print(0.1 + 0.2)  # This will print 0.30000000000000004 due to floating-point precision issues in binary representation.
print(0.1 + 0.2 == 0.3)  # This will print False because 0.1 + 0.2 does not exactly equal 0.3 due to the precision issue.
# Fixing the comparison using round()
print(round(0.1 + 0.2, 10) == 0.3)  # This will print True after rounding to 10 decimal places.

## Question 13 : -10 // 3,-10 % 3,10 // -3,10 % -3
##Then in comments, explain why floor division and modulo behave this way with negative numbers. (This is a classic interview gotcha.)
print(-10 // 3)  # This will print -4 because floor division rounds down to the nearest integer.
print(-10 % 3)   # This will print 2 because the result of modulo is always non-negative when the divisor is positive.
print(10 // -3)  # This will print -4 because floor division rounds down to the nearest integer.
print(10 % -3)   # This will print -2 because the result of modulo is always non-negative when the divisor is negative. The behavior of floor division and modulo with negative numbers can be counterintuitive, as they follow the rule that the result of the modulo operation has the same sign as the divisor.  

## Question 14 : Take any input from the user. Then:Print what they entered,Print its type,Try converting it to int, float, bool, and complex — catch errors for each,In comments, explain which conversions succeeded and why,Test with: "42", "3.14", "hello", "True", "".
n = input("Enter something: ")
print(f"You entered: {n}") 
print(f"Type: {type(n)}")
try:
    int_conversion = int(n)
    print(f"Integer conversion succeeded: {int_conversion}")

    float_conversion = float(n)
    print(f"Float conversion succeeded: {float_conversion}")

    bool_conversion = bool(n)
    print(f"Boolean conversion succeeded: {bool_conversion}")

    complex_conversion = complex(n)
    print(f"Complex conversion succeeded: {complex_conversion}")
except ValueError as e:
    print(f"Error occurred while converting: {e}")  ## trying to convert a non-numeric string like "hello" will raise a ValueError for int and float conversions. The bool conversion will always succeed, as any non-empty string evaluates to True, while an empty string evaluates to False. The complex conversion will succeed for numeric strings but fail for non-numeric strings like "hello".

## Question 15 : Q15. Ask for two numbers. Print:Which is bigger (or if they're equal),Their average,Their difference (absolute value),a ** b and b ** a — compare them
#Edge case: What if b = 0? Catch the ZeroDivisionError if it occurs.
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
print(f"Bigger number: {max(num1, num2)}" if num1 != num2 else "Both numbers are equal.")
average = (num1 + num2) / 2
print(f"Average: {average}")
print(f"Difference: {abs(num1 - num2)}")
try:
    print(f"a ** b: {num1 ** num2}")
    print(f"b ** a: {num2 ** num1}")
    print(f"Comparison: {'a ** b is greater' if num1 ** num2 > num2 ** num1 else 'b ** a is greater' if num2 ** num1 > num1 ** num2 else 'Both are equal'}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

## Question 16 : Bill Splitter-Take total bill, number of people, and tip percentage (e.g., 10 for 10%). Print:
#text
#Total bill:      1000.00
#Tip (10%):       100.00
#Grand total:     1100.00
#Per person:      275.00
#Format it as a neat table using f-string alignment
total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

tip_amount = total_bill * (tip_percentage / 100)
grand_total = total_bill + tip_amount
per_person = grand_total / num_people

print(f"Total bill:      {total_bill:<10.2f}")
print(f"Tip ({tip_percentage}%):       {tip_amount:<10.2f}")
print(f"Grand total:     {grand_total:<10.2f}")
print(f"Per person:      {per_person:<10.2f}")

## Question 17 : Seconds Converter
#Take an integer number of seconds (e.g., 3672). Convert to:1 hour, 1 minute, 12 seconds,Then do it the other way: take hours, minutes, seconds and print total seconds.
#Edge case: Test with 0, 59, 3600, 86399, 100000.
total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

## Question 18 : Q18. Currency Denomination
#Take an amount in rupees (e.g., 2873). Break it into the minimum number of notes of denominations 2000, 500, 200, 100, 50, 20, 10, 5, 2, 1.

#2000 x 1 = 2000
#500 x 1 = 500
#200 x 1 = 200
#100 x 1 = 100
#50 x 1 = 50
#20 x 1 = 20
#5 x 0 ...
#Hint: Use // and % repeatedly.
amount = int(input("Enter the amount in rupees: "))
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
print("Currency Denomination:")

for denomination in denominations:
    count = amount // denomination
    if count > 0:
        print(f"#{denomination} x {count} = {denomination * count}")
    amount %= denomination
    print(f"Remaining amount: {amount}")
                       