# Two DSA questions with Python solutions.

# 1. Question: Given a list of integers and a target, return the indices of
#    two numbers that add up to the target.
def two_sum(numbers, target):
    seen = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index
    return []


numbers = [2, 7, 11, 15]
target = 9
print("Two Sum:", two_sum(numbers, target))

# Output:
# Two Sum: [0, 1]


# 2. Question: Find the index of a target in a sorted list using binary
#    search. Return -1 if the target is not present.
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


sorted_numbers = [1, 3, 5, 7, 9, 11]
target = 7
print("Binary Search index:", binary_search(sorted_numbers, target))

# Output:
# Binary Search index: 3