# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/

# Given an array of integers nums, calculate the pivot index of this array. The pivot index is the index where the sum
# of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's
# right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements
# to the left. This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.

# Initial solution
# Time complexity = O(n) - two linear passes through nums to get prefix sum and when finding pivot index
# Space complexity - O(n) - prefix sum array is of length n where n = len(nums) and is allocated memory

def pivot_index(nums):
    if len(nums) == 1:
        return 0

    sums = [0, nums[0]]

    for i in range(1, len(nums)):
        sums.append(nums[i] + sums[-1])

    sums.append(0) # Extra 0's are padded to start and end to handle edge cases where i is at edge of sums

    for i in range(1, len(sums) - 1):
        if sums[i - 1] == sums[len(sums) - 2] - sums[i]:
            return i - 1

    return -1

# Optimised (space complexity = O(1) constant time as no need for prefix sum array

def pivot_index_optimal(nums):
    total = 0

    for num in nums:
        total += num

    left_sum = 0

    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i] # include nums[i] in subtraction as considering strictly left/right vals
        if left_sum == right_sum:
            return i

        left_sum += nums[i]

    return -1

def test_pivot_index():
    test_cases = [
        # (input, expected_output)
        ([1, 7, 3, 6, 5, 6], 3),     # Pivot at index 3
        ([1, 2, 3], -1),            # No pivot
        ([2, 1, -1], 0),            # Pivot at index 0
        ([0, 0, 0, 0, 1], 4),      # Pivot at end with all 0's prior
        ([1], 0),                   # Single element
        ([1, -1, 0], 2),            # Pivot at end
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = pivot_index_optimal(nums)
        assert result == expected, f"Test case {i + 1} failed: got {result}, expected {expected}"

    print("All test cases passed!")

test_pivot_index()