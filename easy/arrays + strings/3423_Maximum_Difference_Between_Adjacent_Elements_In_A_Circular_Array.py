# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12


# Given a circular array nums, find the maximum absolute difference between adjacent elements.
#
# Note: In a circular array, the first and last elements are adjacent.

# Optimal
# Time complexity = O(n) - required to check each array element once (one extra for first element since circular) where n = len(nums)
# Space complexity = O(1) - constant total space as only two int's used for storing difference and answer

import unittest

class Solution(object):
    def maxAdjacentDistance(self, nums):

        ans = float('-inf')
        diff = 0

        for i in range(0, len(nums)):
            if i == len(nums) - 1:
                diff = abs(nums[i] - nums[0])
            else:
                diff = abs(nums[i] - nums[i + 1])
            ans = max(ans, diff)

        return ans

class TestMaxAdjacentDistance(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_empty_array(self):
        # According to LeetCode constraints, nums.length is usually >= 1.
        # If it could be empty, you might want to define expected behavior (e.g., raise error, return 0).
        # Assuming for now it won't be empty based on typical problem constraints.
        # If a problem defines an empty array as valid input, it would specify the return value.
        # For this problem, usually n >= 1. Let's assume n >= 1 for now.
        pass # No direct test for empty array if constraints say n >= 1

    def test_single_element_array(self):
        # For a single element, the "circular" difference is with itself, which is 0.
        # Or, if the problem implies at least two distinct elements for "adjacent", then this case might not occur.
        # Given the phrasing "adjacent elements", a single element array technically has no adjacent elements.
        # However, if it's considered circular, then nums[0] and nums[0] are adjacent.
        self.assertEqual(self.solver.maxAdjacentDistance([5]), 0)

    def test_two_element_array(self):
        self.assertEqual(self.solver.maxAdjacentDistance([1, 5]), 4)
        self.assertEqual(self.solver.maxAdjacentDistance([5, 1]), 4)
        self.assertEqual(self.solver.maxAdjacentDistance([10, 10]), 0)

    def test_positive_numbers(self):
        self.assertEqual(self.solver.maxAdjacentDistance([1, 2, 3, 4, 5]), 4)
        self.assertEqual(self.solver.maxAdjacentDistance([1, 5, 2, 8]), 7) # abs(2-8)=6, abs(8-1)=7
        self.assertEqual(self.solver.maxAdjacentDistance([10, 1, 7, 3]), 9) # abs(10-1)=9

    def test_negative_numbers(self):
        self.assertEqual(self.solver.maxAdjacentDistance([-1, -5, -2, -8]), 7) # abs(-2 - (-8)) = 6, abs(-8 - (-1)) = 7
        self.assertEqual(self.solver.maxAdjacentDistance([-10, -1, -7, -3]), 9) # abs(-10 - (-1)) = 9

    def test_mixed_numbers(self):
        self.assertEqual(self.solver.maxAdjacentDistance([-1, 5, -2, 8]), 10) # abs(-1-5)=6, abs(5-(-2))=7, abs(-2-8)=10, abs(8-(-1))=9
        self.assertEqual(self.solver.maxAdjacentDistance([0, 10, -5, 2]), 15) # abs(10-(-5))=15

    def test_duplicates(self):
        self.assertEqual(self.solver.maxAdjacentDistance([5, 5, 5, 5]), 0)
        self.assertEqual(self.solver.maxAdjacentDistance([1, 5, 1, 5]), 4)

    def test_large_numbers(self):
        self.assertEqual(self.solver.maxAdjacentDistance([1000000, 1, 2000000, 2]), 1999999) # abs(2000000 - 2) = 1999998, abs(2 - 1000000) = 999998
        self.assertEqual(self.solver.maxAdjacentDistance([999999999, 1, 999999998]), 999999998) # abs(1-999999998) = 999999997, abs(999999998-999999999) = 1, abs(999999999-1) = 999999998

    def test_edge_case_circular(self):
        # Test the circular adjacency explicitly
        self.assertEqual(self.solver.maxAdjacentDistance([1, 2, 10]), 9) # abs(1-2)=1, abs(2-10)=8, abs(10-1)=9
        self.assertEqual(self.solver.maxAdjacentDistance([10, 2, 1]), 9) # abs(10-2)=8, abs(2-1)=1, abs(1-10)=9

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)