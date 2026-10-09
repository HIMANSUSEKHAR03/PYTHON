## NOW WE WILL COVER ANOTHER 10 QUESTIONS THAT WILL COVER THE BASICS OF PYTHON
## QUESTION 1: FIND THE FACTORIAL OF EACH NUMBER BETWEEN 1 AND 1000.

factorial = 1
for num in range(1, 21):
    factorial *= num
    print(f"{num}! = {factorial}")
# OUTPUT : 
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362880
# 10! = 3628800
# 11! = 39916800
# 12! = 479001600
# 13! = 6227020800
# 14! = 87178291200
# 15! = 1307674368000
# 16! = 20922789888000
# 17! = 355687428096000
# 18! = 6402373705728000
# 19! = 121645100408832000
# 20! = 2432902008176640000

## QUESTION 2: FIND ARMSTRONG AND FIBONACCI NUMBERS FROM 0 TO 50.

numbers = range(51)

armstrong_numbers = [
    number
    for number in numbers
    if number == sum(int(digit) ** len(str(number)) for digit in str(number))
]

fibonacci_numbers = []
previous, current = 0, 1
while previous <= 50:
    fibonacci_numbers.append(previous)
    previous, current = current, previous + current

print("Armstrong numbers:", armstrong_numbers)
print("Fibonacci numbers:", fibonacci_numbers)

# OUTPUT :
# Armstrong numbers: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

## QUESTION 3: FIND ALL NATURAL NUMBERS BETWEEN 1 AND 50 AND THEIR SUM.

natural_numbers = list(range(1, 51))
total = sum(natural_numbers)

print("Natural numbers from 1 to 50:", natural_numbers)
print("Sum:", total)

# OUTPUT :
# Natural numbers from 1 to 50: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# Sum: 1275

## QUESTION 4: DISPLAY THE FIRST SIX POWERS OF A NUMBER.

number = eval(input("enter the number : "))
powers = []

for exponent in range(1, 7):
    powers.append(number ** exponent)

print(f"First six powers of {number}:", powers)

# OUTPUT : 
# enter the number : 3
# First six powers of 3: [3, 9, 27, 81, 243, 729]

## QUESTION 5: FIND WHICH NUMBERS FROM 1 TO 50 DIVIDE A GIVEN NUMBER.

given_number = int(input("Enter an integer: "))
divisors = [
    divisor
    for divisor in range(1, 51)
    if given_number % divisor == 0
]

print(f"{given_number} is divisible by:", divisors)

# OUTPUT :
# Enter an integer: 10
# 10 is divisible by: [1, 2, 5, 10]

## QUESTION 6: FIND THE FACTORS OF TWO NUMBERS, THEIR HCF, AND THEIR LCM.

number1 = int(input("Enter the first positive integer: "))
number2 = int(input("Enter the second positive integer: "))

if number1 <= 0 or number2 <= 0:
    raise ValueError("Both numbers must be positive integers.")

factors1 = [factor for factor in range(1, number1 + 1) if number1 % factor == 0]
factors2 = [factor for factor in range(1, number2 + 1) if number2 % factor == 0]

hcf = max(factor for factor in factors1 if number2 % factor == 0)
lcm = number1 * number2 // hcf

print(f"Factors of {number1}:", factors1)
print(f"Factors of {number2}:", factors2)
print("HCF:", hcf)
print("LCM:", lcm)

# OUTPUT :
# Enter the first positive integer: 23
# Enter the second positive integer: 24
# Factors of 23: [1, 23]
# Factors of 24: [1, 2, 3, 4, 6, 8, 12, 24]
# HCF: 1
# LCM: 552

## QUESTION 7: SHUFFLE A DECK OF PLAYING CARDS.

import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = [
    "Ace", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "Jack", "Queen", "King",
]
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

random.shuffle(deck)
print("Shuffled deck:")
for card in deck:
    print(card)

# OUTPUT :
# Shuffled deck:
# 4 of Diamonds
# 9 of Hearts
# Jack of Spades
# 9 of Clubs
# 3 of Hearts
# 2 of Diamonds
# Queen of Clubs
# 8 of Hearts
# 5 of Diamonds
# 4 of Hearts
# Queen of Diamonds
# Ace of Diamonds
# 10 of Diamonds
# 4 of Clubs
# 6 of Clubs
# Ace of Spades
# 6 of Hearts
# Queen of Spades
# Ace of Hearts
# Jack of Hearts
# 3 of Spades
# 7 of Diamonds
# 4 of Spades
# 9 of Diamonds
# King of Spades
# 5 of Clubs
# 3 of Clubs
# Queen of Hearts
# 6 of Diamonds
# 2 of Hearts
# King of Clubs
# 10 of Clubs
# 10 of Hearts
# King of Hearts
# 9 of Spades
# 7 of Clubs
# 10 of Spades
# 5 of Spades
# Jack of Diamonds
# 5 of Hearts
# 7 of Hearts
# 8 of Clubs
# 3 of Diamonds
# 6 of Spades
# 2 of Clubs
# 8 of Spades
# Jack of Clubs
# 8 of Diamonds
# 7 of Spades
# King of Diamonds
# 2 of Spades
# Ace of Clubs

## QUESTION 8: DISPLAY THE CALENDAR FOR A GIVEN YEAR.

import calendar

year = int(input("Enter the year: "))
print(calendar.calendar(year))

# OUTPUT :
# Enter the year: 2026
#                                   2026

#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1                         1
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       2  3  4  5  6  7  8
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15       9 10 11 12 13 14 15
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      16 17 18 19 20 21 22
# 26 27 28 29 30 31         23 24 25 26 27 28         23 24 25 26 27 28 29
#                                                     30 31

#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
#  6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
# 13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
# 20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
# 27 28 29 30               25 26 27 28 29 30 31      29 30

#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#        1  2  3  4  5                      1  2          1  2  3  4  5  6
#  6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
# 13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
# 20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
# 27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
#                           31

#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1          1  2  3  4  5  6
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
# 26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
#                           30

## QUESTION 9 : Write a program to check whether a given number is a palindrome.

number = int(input("Enter an integer: "))
if str(number) == str(number)[::-1]:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

# OUTPUT: Enter an integer: 56
# 56 is not a palindrome.

## QUESTION 10: COUNT THE LETTERS, VOWELS, AND CONSONANTS IN A SENTENCE.

text = input("Enter a sentence: ")
letters = [character for character in text if character.isalpha()]
vowels = [character for character in letters if character.lower() in "aeiou"]
consonants = [character for character in letters if character.lower() not in "aeiou"]

print("Number of letters:", len(letters))
print("Number of vowels:", len(vowels))
print("Number of consonants:", len(consonants))

# OUTPUT : 
# Enter a sentence: hello himansu you are a pwerfull and a fearless man
# Number of letters: 42
# Number of vowels: 18
# Number of consonants: 24