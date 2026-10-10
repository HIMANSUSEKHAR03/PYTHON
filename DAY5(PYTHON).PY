
## PYTHON ADVANCED CONCEPTS - 10 MASTER QUESTIONS


# QUESTION 1: MODULES


# First create a helper module
with open("math_utils.py", "w") as f:
    f.write("""
PI = 3.14159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def is_even(n):
    return n % 2 == 0
""")

# Now import it in different ways
import math
import math_utils
from math_utils import square, cube
import math_utils as mu

print("square of 5:", math_utils.square(5))
print("square of 4:", square(4))
print("cube of 3:", cube(3))
print("is 10 even:", mu.is_even(10))
print("PI value:", math_utils.PI)
print("sqrt of 16:", math.sqrt(16))
print("module name:", math_utils.__name__)

# OUTPUT:
# Q1: MODULES
# square of 5: 25
# square of 4: 16
# cube of 3: 27
# is 10 even: True
# PI value: 3.14159
# sqrt of 16: 4.0
# module name: math_utils


# QUESTION 2: ERROR HANDLING


class NegativeNumberError(Exception):
    pass

def divide(a, b):
    try:
        if a < 0 or b < 0:
            raise NegativeNumberError("negative number not allowed")
        result = a / b
    except ZeroDivisionError:
        return "error: cannot divide by zero"
    except NegativeNumberError as e:
        return "error: " + str(e)
    except TypeError:
        return "error: invalid input type"
    else:
        return "result is " + str(result)
    finally:
        print("  tried:", a, "/", b)

def open_file(filename):
    try:
        f = open(filename, "r")
        content = f.read()
        f.close()
        return content
    except FileNotFoundError:
        return "error: file not found - " + filename
    finally:
        print("  file operation done:", filename)

print(divide(10, 2))
print(divide(10, 0))
print(divide(-5, 2))
print(divide("abc", 2))
print()
print(open_file("data.txt"))

# OUTPUT:
# Q2: ERROR HANDLING

#   tried: 10 / 2
# result is 5.0
#   tried: 10 / 0
# error: cannot divide by zero
#   tried: -5 / 2
# error: negative number not allowed
#   tried: abc / 2
# error: invalid input type
#
#   file operation done: data.txt
# error: file not found - data.txt

# QUESTION 3: DECORATORS

import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("  time taken:", round(end - start, 4), "seconds")
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("  calling", func.__name__, "with", args)
        result = func(*args, **kwargs)
        print("  returned:", result)
        return result
    return wrapper

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                print("  run number", i + 1)
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@timer
@logger
@repeat(3)
def add(a, b):
    time.sleep(0.05)
    return a + b

print(add(5, 3))
print("function name:", add.__name__)

# OUTPUT:
# Q3: DECORATORS
#   run number 1
#   calling add with (5, 3)
#   returned: 8
#   run number 2
#   calling add with (5, 3)
#   returned: 8
#   run number 3
#   calling add with (5, 3)
#   returned: 8
#   time taken: 0.1503 seconds
# 8
# function name: add

# QUESTION 4: ITERATORS


import itertools

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

def fib_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("using class:", list(Fibonacci(8)))
print("using generator:", list(fib_generator(8)))
print("infinite sliced:", list(itertools.islice(infinite_fib(), 10)))

it = iter(Fibonacci(3))
print("manual next calls:", next(it), next(it), next(it))

try:
    next(it)
except StopIteration:
    print("iteration finished")

# OUTPUT:
# Q4: ITERATORS
# using class: [0, 1, 1, 2, 3, 5, 8, 13]
# using generator: [0, 1, 1, 2, 3, 5, 8, 13]
# infinite sliced: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# manual next calls: 0 1 1
# iteration finished

# QUESTION 5: REGULAR EXPRESSIONS


import re

def check_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))

def check_phone(phone):
    pattern = r"^[6-9]\d{9}$"
    return bool(re.match(pattern, phone))

def check_password(pwd):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    return bool(re.match(pattern, pwd))

print("email user@example.com:", check_email("user@example.com"))
print("email bad-email:", check_email("bad-email"))
print("phone 9876543210:", check_phone("9876543210"))
print("phone 1234567890:", check_phone("1234567890"))
print("password Pass@123:", check_password("Pass@123"))
print("password weakpass:", check_password("weakpass"))

text = "contact us at a@x.com or b@y.org"
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
print("found emails:", emails)

masked = re.sub(r"\d", "#", "my number is 12345")
print("masked:", masked)

parts = re.split(r"[,;|]", "apple,banana;cherry|date")
print("split parts:", parts)

date = "25/12/2024"
match = re.match(r"(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})", date)
print("date parts:", match.groupdict())

# OUTPUT:
# email user@example.com: True
# email bad-email: False
# phone 9876543210: True
# phone 1234567890: False
# password Pass@123: True
# password weakpass: False
# found emails: ['a@x.com', 'b@y.org']
# masked: my number is #####
# split parts: ['apple', 'banana', 'cherry', 'date']
# date parts: {'day': '25', 'month': '12', 'year': '2024'}


# QUESTION 6: VARIABLE SCOPE


count = 0

def increase():
    global count
    count = count + 1
    return count

def create_counter():
    num = 0
    def increment():
        nonlocal num
        num = num + 1
        return num
    return increment

name = "global"

def show_shadow():
    name = "local"
    return name

value = 100

def cause_error():
    try:
        print(value)
        value = 200
    except UnboundLocalError as e:
        return "error: " + str(e)

def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

print("global count:", increase(), increase())

c1 = create_counter()
c2 = create_counter()
print("counter 1:", c1(), c1(), c1())
print("counter 2:", c2(), c2())

print("shadow returns:", show_shadow())
print("outer name:", name)
print("unbound error:", cause_error())

double = make_multiplier(2)
triple = make_multiplier(3)
print("double(5):", double(5))
print("triple(5):", triple(5))

# OUTPUT:
# Q6: VARIABLE SCOPE
# global count: 1 2
# counter 1: 1 2 3
# counter 2: 1 2
# shadow returns: local
# outer name: global
# unbound error: error: cannot access local variable 'value' where it is not associated with a value
# double(5): 10
# triple(5): 15


# QUESTION 7: DECORATOR + ERROR HANDLING + SCOPE

import functools

error_list = []

class InputError(Exception):
    pass

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_list.append(func.__name__ + ": " + str(e))
            print("  caught error:", e)
            return None
    return wrapper

def check_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for num in args:
            if isinstance(num, (int, float)) and num < 0:
                raise InputError("negative value: " + str(num))
        return func(*args, **kwargs)
    return wrapper

@handle_errors
@check_positive
def safe_divide(a, b):
    return a / b

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
print("-5 / 2 =", safe_divide(-5, 2))

print("errors collected:")
for err in error_list:
    print("  ", err)

# OUTPUT:
# Q7: DECORATOR + ERROR + SCOPE
# 10 / 2 = 5.0
#   caught error: division by zero
# 10 / 0 = None
#   caught error: negative value: -5
# -5 / 2 = None
# errors collected:
#    safe_divide: division by zero
#    safe_divide: negative value: -5


# QUESTION 8: ITERATOR + REGEX + MODULE

import re
import itertools

log_data = [
    "2024-01-15 ERROR: database failed",
    "2024-01-15 INFO: server started",
    "2024-01-16 ERROR: connection timeout",
    "2024-01-16 INFO: user logged in",
    "2024-01-17 ERROR: disk full",
]

def read_logs(lines):
    pattern = r"(\d{4}-\d{2}-\d{2})\s+(\w+):\s+(.+)"
    for line in lines:
        match = re.match(pattern, line)
        if match:
            yield {
                "date": match.group(1),
                "level": match.group(2),
                "message": match.group(3)
            }

print("all log entries:")
for entry in read_logs(log_data):
    print("  ", entry["date"], entry["level"], "-", entry["message"])

print("only errors:")
for entry in read_logs(log_data):
    if entry["level"] == "ERROR":
        print("  ", entry["date"], "-", entry["message"])

print("count by date:")
parsed = list(read_logs(log_data))
for date, group in itertools.groupby(parsed, key=lambda x: x["date"]):
    print("  ", date, ":", len(list(group)), "entries")

# OUTPUT:

# all log entries:
#    2024-01-15 ERROR - database failed
#    2024-01-15 INFO - server started
#    2024-01-16 ERROR - connection timeout
#    2024-01-16 INFO - user logged in
#    2024-01-17 ERROR - disk full
# only errors:
#    2024-01-15 - database failed
#    2024-01-16 - connection timeout
#    2024-01-17 - disk full
# count by date:
#    2024-01-15 : 2 entries
#    2024-01-16 : 2 entries
#    2024-01-17 : 1 entries

# QUESTION 9: DECORATOR + SCOPE + ITERATOR

import functools

def remember(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print("  already computed", args)
            return cache[args]
        result = func(*args)
        cache[args] = result
        print("  computing", args, "=", result)
        return result
    return wrapper

@remember
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("fibonacci numbers:")
for i in range(8):
    print("  fib(" + str(i) + ") =", fib(i))

class FibIterator:
    def __init__(self, limit):
        self.limit = limit
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.limit:
            raise StopIteration
        result = fib(self.i)
        self.i += 1
        return result

print("fib iterator:", list(FibIterator(8)))

# OUTPUT:
# fibonacci numbers:
#   computing (0,) = 0
#   fib(0) = 0
#   computing (1,) = 1
#   fib(1) = 1
#   already computed (0,)
#   computing (2,) = 1
#   fib(2) = 1
#   already computed (1,)
#   already computed (2,)
#   computing (3,) = 2
#   fib(3) = 2
#   already computed (2,)
#   already computed (3,)
#   computing (4,) = 3
#   fib(4) = 3
#   already computed (3,)
#   already computed (4,)
#   computing (5,) = 5
#   fib(5) = 5
#   already computed (4,)
#   already computed (5,)
#   computing (6,) = 8
#   fib(6) = 8
#   already computed (5,)
#   already computed (6,)
#   computing (7,) = 13
#   fib(7) = 13
# fib iterator: [0, 1, 1, 2, 3, 5, 8, 13]


# QUESTION 10: ALL 6 TOPICS TOGETHER

import re
import functools

settings = {
    "max_retries": 3,
    "allowed_domains": ["example.com", "test.org"]
}

class EmailError(Exception):
    pass

class TooManyRetries(Exception):
    pass

def retry(attempts):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("  attempt", i, "failed:", e)
                    if i == attempts:
                        raise TooManyRetries("tried " + str(attempts) + " times")
        return wrapper
    return decorator

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("  calling", func.__name__, "with", args[0])
        result = func(*args, **kwargs)
        print("  returned:", result)
        return result
    return wrapper

def verify_email(email):
    match = re.match(r"^[\w\.-]+@([\w\.-]+\.\w{2,})$", email)
    if not match:
        raise EmailError("invalid email: " + email)
    domain = match.group(1)
    if domain not in settings["allowed_domains"]:
        raise EmailError("domain not allowed: " + domain)
    return email

class EmailList:
    def __init__(self, emails):
        self.emails = emails
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.emails):
            raise StopIteration
        email = self.emails[self.index]
        self.index += 1
        return email

@retry(settings["max_retries"])
@trace
def process(email):
    return verify_email(email)

emails_to_test = [
    "user@example.com",
    "admin@test.org",
    "bad-email",
    "user@other.com"
]

for email in EmailList(emails_to_test):
    print()
    print("processing:", email)
    try:
        result = process(email)
        print("success:", result)
    except (EmailError, TooManyRetries) as e:
        print("failed:", e)

# OUTPUT:

#
# processing: user@example.com
#   calling process with user@example.com
#   returned: user@example.com
# success: user@example.com
#
# processing: admin@test.org
#   calling process with admin@test.org
#   returned: admin@test.org
# success: admin@test.org
#
# processing: bad-email
#   calling process with bad-email
#   attempt 1 failed: invalid email: bad-email
#   attempt 2 failed: invalid email: bad-email
#   attempt 3 failed: invalid email: bad-email
# failed: tried 3 times
#
# processing: user@other.com
#   calling process with user@other.com
#   attempt 1 failed: domain not allowed: other.com
#   attempt 2 failed: domain not allowed: other.com
#   attempt 3 failed: domain not allowed: other.com
# failed: tried 3 times


