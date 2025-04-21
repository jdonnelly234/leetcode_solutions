# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

# Given an integer x, return true if x is a palindrome, and false otherwise.

# String based

# Time complexity = O(n) - str(x) creation requires n time when n = number of digits in x
# Space complexity = O(n) - str(x) conversion creates new string of size n (number of digits)

def is_palindrome(x):
    if x < 0:
        return False

    if 10 > x >= 0:
        return True

    stringed = str(x)
    left = 0
    right = len(stringed) - 1

    while left < right:
        if stringed[left] != stringed[right]:
            return False

        left += 1
        right -= 1

    return True

# Optimised (no string conversion)

# Time complexity = O(log n) - skipping str conversion and only processing digits
#                                                           |
#                                                       The number of digits in a number n is floor(log₁₀(n)) + 1
#                                                       because each digit represents a power of 10.
#                                                       This means digit-based operations run in O(log n) time
# Space complexity = O(1) - changes to x are made in place, no creation of additional data structures

def is_palindrome_optimised(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev_half = 0
    while x > rev_half:
        rev_half = (rev_half * 10) + (x % 10)
        x //= 10

    return (x == rev_half) or (x == rev_half // 10)

x = 12321
y = 532
z = -43

print(is_palindrome(x)) # Correct output - True
print(is_palindrome(y)) # Correct output - False
print(is_palindrome(z)) # Correct output - False

print(is_palindrome_optimised(x)) # Correct output - True
print(is_palindrome_optimised(y)) # Correct output - False
print(is_palindrome_optimised(z)) # Correct output - False