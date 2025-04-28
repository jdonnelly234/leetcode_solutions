# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Time complexity - O(n) as n/2 elements swapped, we ignore constant
# Space complexity - O(1) as s is reversed in place, no additional memory allocated

def reversestring(s):
    if len(s) < 2:
        return s

    left = 0
    right = len(s) - 1

    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right]=tmp

        left += 1
        right -= 1


test = ['h', 'e', 'l', 'l', 'o']

reversestring(test)

print(test) # Correctly outputs - ['o', 'l', 'l', 'e', 'h']

