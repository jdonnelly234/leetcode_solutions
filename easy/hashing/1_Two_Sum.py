# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target. You may assume that each input would have exactly one solution, and you may not use the
# same element twice. You can return the answer in any order.

# Optimal with hash map
# Time complexity = O(n) - worst case is when each element of nums is added to hash map and no complement found where
#                          n = len(nums)
# Space complexity = O(n) - worst case where hash map stores each value, index pair in the array
#                           when no complement found

def two_sum_hashmap(nums, target):
    dic = {}

    for i in range(len(nums)):
        num = nums[i]

        needed_num = target - num
        if needed_num in dic:
            return [dic[needed_num], i]

        dic[num] = i

    return [-1, -1]

def test_two_sum():
    """
    Tests the two_sum function with various test cases.
    """
    test_cases = [
        # Basic test case
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        # Target at the end
        {"nums": [2, 7, 11, 15, 9], "target": 9, "expected": [0, 1]},
        # Negative numbers
        {"nums": [-1, -2, -3, -4, -5], "target": -8, "expected": [2, 4]},
        # Zero in the array
        {"nums": [0, 2, 3, 0], "target": 0, "expected": [0, 3]},
        # Large numbers
        {"nums": [1000000, 2000000, 3000000, 4000000], "target": 7000000, "expected": [2, 3]},
        # No solution
        {"nums": [1, 2, 3, 4, 5], "target": 10, "expected": [-1, -1]},
        # Duplicate numbers, but solution uses different instances
        {"nums": [3, 2, 4, 3], "target": 6, "expected": [1, 2]},
    ]

    for i, test_case in enumerate(test_cases):
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        actual = two_sum_hashmap(nums, target)  # Use the function name 'two_sum'
        assert actual == expected, f"Test case {i + 1} failed: nums={nums}, target={target}, expected={expected}, actual={actual}"
        print(f"Test case {i + 1} passed!")

if __name__ == "__main__":
    test_two_sum()