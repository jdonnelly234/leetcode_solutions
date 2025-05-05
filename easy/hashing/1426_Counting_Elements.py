# 1426. Counting Elements
# https://leetcode.com/problems/counting-elements/description/

# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.
# If there are duplicates in arr, count them separately.

# Optimal with set
# Time complexity = O(n) - for loop to get unique elements then another for loop the check whether x + 1 in arr,
#                          O(n) + O(n) = O(2n) = O(n)
# Space complexity = O(n) - uniq_nums set for storing non-duplicate numbers to check x + 1 is required, allocates memory
#                           for n where len(arr) = n

def count_elements(arr):

    uniq_nums = set()

    for num in arr:
        uniq_nums.add(num)

    ans = 0
    for i in range(len(arr)):
        if arr[i] + 1 in uniq_nums:
            ans += 1

    return ans

def test_count_elements():
    """
    Tests the count_elements function with various test cases.
    """
    test_cases = [
        {"arr": [1, 2, 3], "expected": 2},
        {"arr": [1, 1, 3, 3, 0, 1, 1], "expected": 1},
        {"arr": [1, 1, 2, 2], "expected": 2},
        {"arr": [1, 3, 2, 4, 5, 0], "expected": 5},
        {"arr": [1, 1, 2], "expected": 2},
        {"arr": [1, 2, 3, 4, 5], "expected": 4},
        {"arr": [0, 0, 0, 0], "expected": 0},
        {"arr": [1, 1, 1, 1], "expected": 0},
        {"arr": [], "expected": 0},
        {"arr": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5], "expected": 8},
    ]

    for i, test_case in enumerate(test_cases):
        arr = test_case["arr"]
        expected = test_case["expected"]
        actual = count_elements(arr)
        assert actual == expected, f"Test case {i + 1} failed: arr={arr}, expected={expected}, actual={actual}"
        print(f"Test case {i + 1} passed!")



if __name__ == "__main__":
    test_count_elements()