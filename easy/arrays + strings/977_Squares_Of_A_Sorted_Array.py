# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Brute force

# Time complexity = O(n log n) - inbuilt sort() is based on Timsort
# Space complexity = O(1) (ignoring internal space used by sort())

def sorted_squares(nums):
    for i in range(len(nums)):
        nums[i] = square(nums[i])

    nums.sort()

    return nums

def square(n):

    return n * n

# Optimised with two-pointer

# Time complexity = O(n) as squaring and inserting only require one pass through array
# Space complexity = O(n) as new result array for storing sorted squares is allocated memory

def sorted_squares_optimised(nums):
    left = 0
    right = len(nums) - 1

    result = [0] * len(nums)
    pos = len(nums) - 1

    while left <= right:
        if nums[left] ** 2 > nums[right] ** 2:
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1

        pos -= 1

    return result

test = [-4, -1, 0, 5, 13, 25]
print(sorted_squares(test)) # Correct output - [0, 1, 16, 25, 169, 625]

test2 = [-4, -1, 0, 5, 13, 25]
print(sorted_squares_optimised(test2)) # Correct output - [0, 1, 16, 25, 169, 625]