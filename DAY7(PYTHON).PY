# Five pattern questions covering Python basics.
# 1. Question: Print a 5 x 5 square of stars.
n = 5
for row in range(n):
    print("* " * n)

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# 2. Question: Print a right-angled triangle of stars.
n = 5
for row in range(1, n + 1):
    print("* " * row)

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *


# 3. Question: Print an inverted right-angled triangle of stars.
n = 5
for row in range(n, 0, -1):
    print("* " * row)

# Output:
# * * * * *
# * * * *
# * * *
# * *
# *


# 4. Question: Print a centered pyramid of stars.
n = 5
for row in range(1, n + 1):
    spaces = " " * (n - row)
    stars = "* " * row
    print(spaces + stars)

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


# 5. Question: Print a number triangle where each row counts from 1.
n = 5
for row in range(1, n + 1):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5