# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in
# the range that is missing from the array.

# Optimal (kinda Gauss' formula)
# Time complexity = O(n) - two for loops to get expected total and actual total to calculate difference, O(n) + O(n)
#                          = O(2n) = O(n)
# Space complexity = O(1) - only primitive data types used to track total counts, no additional data structures needed
#                           that require heavy allocation

def missing_number(nums):
    expected_total = actual_total = 0

    n = len(nums)

    for i in range(1, n + 1):
        expected_total += i

    for num in nums:
        actual_total += num

    return expected_total - actual_total

def test_missing_number():
    """
    Tests the missingNumber function with various test cases.
    """
    test_cases = [
        {"nums": [3, 0, 1], "expected": 2},
        {"nums": [0, 1], "expected": 2},
        {"nums": [9, 6, 4, 2, 3, 5, 7, 0, 1], "expected": 8},
        {"nums": [0], "expected": 1},  # Single element array
        {"nums": [1], "expected": 0},  # Single element array
        {"nums": [0, 2, 3], "expected": 1},  # Missing number in the middle
        {"nums": [1, 2, 3], "expected": 0},  # Missing number at the beginning
        {"nums": [0, 1, 2], "expected": 3},  # Missing number at the end
        {"nums": [4, 0, 2, 1], "expected": 3}, #unsorted
    ]

    for i, test_case in enumerate(test_cases):
        nums = test_case["nums"]
        expected = test_case["expected"]
        actual = missing_number(nums)  # Use the name of your chosen solution function
        assert actual == expected, f"Test case {i + 1} failed: nums={nums}, expected={expected}, actual={actual}"
        print(f"Test case {i + 1} passed!")


if __name__ == "__main__":
    test_missing_number()