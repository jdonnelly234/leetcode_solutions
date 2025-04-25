# 1413. Minimum Value to Get Positive Step by Step Sum
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/

# Given an array of integers nums, you start with an initial positive value startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Efficient solution

# Time complexity = O(n) - input array is passed over once
# Space complexity = O(1) - only primitive datat types used

def min_start_val(nums):
    total = min_prefix = 0

    for num in nums:
        total += num
        min_prefix = min(min_prefix, total)

    return 1 - min_prefix

test1 = [3, -4, 7, -5, 0, 10]
test2 = [1, 2]
test3 = [-7, -9, -2]

print(min_start_val(test1)) # Correctly outputs 2
print(min_start_val(test2)) # Correctly outputs 1
print(min_start_val(test3)) # Correctly outputs 19