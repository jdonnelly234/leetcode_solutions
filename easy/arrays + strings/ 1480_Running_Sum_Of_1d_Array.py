# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/description/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

# Time complexity O(n) - n - 1 elements visited through for loop.
# Space complexity O(n) - creation of new prefix array of len(n) is allocated memory.

def running_sum(nums):
    if not nums:
        return [0]

    run_sum = [nums[0]]

    for i in range(1, len(nums)):
        run_sum.append(nums[i] + run_sum[-1])

    return run_sum

test1 = [1, 2, 3, 4]
test2 = [-4, 8, -23, 165]
test3 = []
test4 = [4]

print(running_sum(test1)) # Correct output - [1, 3, 6, 10]
print(running_sum(test2)) # Correct output - [-4, 4, -19, 146]
print(running_sum(test3)) # Correct output - [0]
print(running_sum(test4)) # Correct output - [4]