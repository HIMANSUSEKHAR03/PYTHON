## WE WILL DISCUSS  Questions  which will Covers Topics (Syntax + Variables/Data Types + Operators)
### QUESTION 1: "The Student Report Card System"
# Write a complete program that:

# Requirements:

# Store student info: name (str), age (int), marks in 3 subjects (list), is_passed (bool), grade (None initially)

# Take one subject mark as user input (string) and convert it to int

# Calculate total and average using operators

# Use floor division and modulo to check if average is even

# Determine pass/fail using comparison and logical operators (and, or)

# Assign grade using if/elif/else

# Print a formatted report using f-strings with sep and end

# Use compound assignment operators (+=, /=) at least once

# Check if a subject is in the list

# Demonstrate == vs is with one example
#solution:
name = "Alice" ## it is a string
age = 16 ## it is an integer and the float will look like 16.0
marks = [85, 90, 78] ## it is a list of integers
is_passed = None ## it is a boolean value (True or False)
grade = None  ## it is a variable that will hold the grade (initially None)

# 2. User input + conversion
extra_mark = input("Enter one extra mark: ")   # string
extra_mark = int(extra_mark)                   # conversion or directly we can write int(input("Enter one extra mark: "))
marks.append(extra_mark) #it means we are adding the extra mark to the list of marks

# 3. Operators: total & average
total = sum(marks)
average = total / len(marks) ##it means we are calculating the average by dividing the total by the number of subjects (length of marks list)

# 4. Floor division & modulo
is_even = (int(average) // 2) == (average // 2)
remainder = int(average) % 2

# 5. Comparison + logical operators
is_passed = average >= 40 and len(marks) > 0

# 6. Grade assignment
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
else:
    grade = "C"

# 7. Formatted report
print("===== REPORT CARD =====")
print("Name:", name, "| Age:", age)
print("Marks:", marks)
print(f"Total: {total} | Average: {average:.2f}") ## f is used for formatting the string and .2f is used to format the average to 2 decimal places because f is used to embed expressions inside string literals
print("Average is even?", is_even)
print("Passed?", is_passed)
print("Grade:", grade)
print("=" * 23)

# 8. Compound assignment
bonus = 5
total += bonus          # total = total + bonus
average /= len(marks)   # average = average / len(marks)

# 9. Membership operator
print(85 in marks)      # True
print(100 not in marks) # True

# 10. == vs is
print(average == 84.33)   # value comparison
print(grade is "A")       # identity check (avoid for strings!)

## QUESTION 2: "The E-Commerce Cart Analyzer"
# Build a mini shopping cart system that:

# Requirements:

# Create a cart as a list of dictionaries — each item has name, price, qty

# Store user's wallet_balance (float) and is_premium (bool)

# Take user input for a discount code and convert type if numeric

# Loop-free calculation: compute subtotal, tax (use %), shipping

# Apply bitwise operator & to check if quantity is even

# Use and/or/not with short-circuit logic to determine final discount

# Use membership to check if an item is in the cart

# Demonstrate mutable vs immutable with a copy example

# Use tuple unpacking for coordinates/prices

# Print a bill using 3 different string formatting methods
# 1. Data structures
cart = [
    {"name": "Laptop", "price": 50000.0, "qty": 1},
    {"name": "Mouse",  "price": 500.0,   "qty": 3},
]

# 2. User variables
wallet_balance = 60000.0
is_premium = True

# 3. User input + conversion
code = input("Enter discount code: ")     # string
discount_pct = 0.0
if code.isdigit():                         # check before converting
    discount_pct = float(code) / 100
else:
    discount_pct = 0.10 if code == "SAVE10" else 0.0

# 4. Calculations
subtotal = sum(item["price"] * item["qty"] for item in cart)
tax = subtotal * 0.18
shipping = 0 if subtotal > 1000 else 50
final = subtotal + tax + shipping

# 5. Bitwise check (even quantity)
for item in cart:
    is_even_qty = (item["qty"] & 1) == 0
    print(f"{item['name']} qty even? {is_even_qty}")

# 6. Logical short-circuit
premium_discount = (final * 0.10) if (is_premium and final > 5000) else 0
payable = final - premium_discount

# 7. Membership
print("Laptop" in [i["name"] for i in cart])   # True

# 8. Mutable vs Immutable
original = [1, 2, 3]
copied = original.copy()
original.append(99)
print("Original:", original)   # [1, 2, 3, 99]
print("Copy:", copied)         # [1, 2, 3]

# 9. Tuple unpacking
laptop_price, mouse_price = 50000.0, 500.0
print(f"Laptop: {laptop_price}, Mouse: {mouse_price}")

# 10. Three formatting methods
print("===== CART SUMMARY =====")
print("Item 1: {} | ₹{} x {} = ₹{}".format("Laptop", 50000.0, 1, 50000.0))
print("Item 2: %s | ₹%s x %s = ₹%s" % ("Mouse", 500.0, 3, 1500.0))
print(f"Subtotal: ₹{subtotal}")
print(f"Tax (18%): ₹{tax}")
print(f"Shipping: ₹{shipping}")
print(f"Final: ₹{final}")
print(f"Premium discount: ₹{premium_discount}")
print(f"Payable: ₹{payable}")
print("Wallet sufficient?", wallet_balance >= payable)

## QUESTION 3: "The Number Analyzer + Identity Trap"
#  The Challenge:
# Write a program that:

# Requirements:

# Take two numbers from user (as strings) → convert to int and float

# Perform ALL 7 arithmetic operators and print results

# Demonstrate operator precedence with 2 + 3 * 4 ** 2 - 6 / 3

# Show == vs is with: ints, floats, strings, lists, tuples

# Show small int caching (256 is 256 vs 257 is 257)

# Demonstrate mutable trap: two variables pointing to same list

# Show compound assignment chain on one variable

# Use all bitwise operators on a = 12, b = 10

# Show truthiness of: 0, "", [], {}, None, "0", -1

# Show short-circuit magic: 0 or "default", 5 and 10, "" or [] or "hi"

# Print everything with clear labels and consistent formatting

# Solution:
# 1. User input + conversion
x = input("Enter first number: ")
y = input("Enter second number: ")
a = int(x)
b = float(y)

print("===== NUMBER ANALYZER =====")
print(f"a = {a}, b = {int(b)}")

# 2. All arithmetic operators
print(f"Sum: {a + b} | Diff: {a - b} | Prod: {a * b}")
print(f"Div: {a / b} | Floor: {a // b} | Mod: {a % b} | Pow: {a ** int(b)}")

# 3. Precedence
result = 2 + 3 * 4 ** 2 - 6 / 3
print("\n--- Precedence Test ---")
print(f"Result: {result}")   # 2 + 48 - 2.0 = 48.0 → check: 2+3*16-2 = 48

# 4. == vs is
print("\n--- == vs is ---")
print(f"100 == 100.0 → {100 == 100.0} | 100 is 100.0 → {100 is 100.0}")
print(f"[1,2] == [1,2] → {[1,2] == [1,2]} | [1,2] is [1,2] → {[1,2] is [1,2]}")
print(f"'abc' == 'abc' → {'abc' == 'abc'} | 'abc' is 'abc' → {'abc' is 'abc'}")

# 5. Small int caching
print("\n--- Small int caching ---")
p = 256; q = 256
r = 257; s = 257
print(f"256 is 256 → {p is q}")
print(f"257 is 257 → {r is s}")   # True in same code block

# 6. Mutable trap
print("\n--- Mutable Trap ---")
list1 = [1, 2, 3]
list2 = list1
list1.append(99)
print(f"list1: {list1}")
print(f"list2: {list2}  ← same reference!")

# 7. Compound assignment chain
print("\n--- Compound Assignment ---")
n = 10
n += 5; print(f"n += 5 → {n}")
n -= 3; print(f"n -= 3 → {n}")
n *= 2; print(f"n *= 2 → {n}")
n //= 4; print(f"n //= 4 → {n}")
n **= 3; print(f"n **= 3 → {n}")

# 8. All bitwise operators
print("\n--- Bitwise (a=12, b=10) ---")
print(f"AND: {a & 10} | OR: {a | 10} | XOR: {a ^ 10}") ## these bit wise operators perform operations like AND compare  
print(f"NOT a: {~a} | a<<1: {a << 1} | a>>1: {a >> 1}")

# 9. Truthiness
print("\n--- Truthiness ---")
print(f'bool(0)={bool(0)} | bool("")={bool("")} | bool([])={bool([])}')
print(f'bool({{}})={bool({})} | bool(None)={bool(None)}')
print(f'bool("0")={bool("0")} | bool(-1)={bool(-1)}')

# 10. Short-circuit
print("\n--- Short-circuit ---")
print(f'0 or "default" → {0 or "default"}')
print(f'5 and 10 → {5 and 10}')
print(f'"" or [] or "hi" → {"" or [] or "hi"}')






































































