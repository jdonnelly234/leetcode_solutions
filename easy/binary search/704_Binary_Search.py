# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
# to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

# Optimal
# Time complexity = O(log n) - search space is halved at each iteration of binary search where n = len(nums)
# Space complexity = O(1) - constant space used as only int pointers used to track array indices for search

import unittest

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_target_found_middle(self):
        """Test case where the target is in the middle of the array."""
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(self.solver.search(nums, target), 4)

    def test_target_found_first_element(self):
        """Test case where the target is the first element."""
        nums = [-1, 0, 3, 5, 9, 12]
        target = -1
        self.assertEqual(self.solver.search(nums, target), 0)

    def test_target_found_last_element(self):
        """Test case where the target is the last element."""
        nums = [-1, 0, 3, 5, 9, 12]
        target = 12
        self.assertEqual(self.solver.search(nums, target), 5)

    def test_target_not_found_less(self):
        """Test case where the target is not in the array and is smaller than all elements."""
        nums = [-1, 0, 3, 5, 9, 12]
        target = -5
        self.assertEqual(self.solver.search(nums, target), -1)

    def test_target_not_found_greater(self):
        """Test case where the target is not in the array and is greater than all elements."""
        nums = [-1, 0, 3, 5, 9, 12]
        target = 15
        self.assertEqual(self.solver.search(nums, target), -1)

    def test_target_not_found_middle(self):
        """Test case where the target is not in the array but falls within the range of elements."""
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        self.assertEqual(self.solver.search(nums, target), -1)

    def test_empty_array(self):
        """Test case with an empty array."""
        nums = []
        target = 5
        self.assertEqual(self.solver.search(nums, target), -1)

    def test_single_element_array_found(self):
        """Test case with a single-element array where target is found."""
        nums = [5]
        target = 5
        self.assertEqual(self.solver.search(nums, target), 0)

    def test_single_element_array_not_found(self):
        """Test case with a single-element array where target is not found."""
        nums = [5]
        target = 10
        self.assertEqual(self.solver.search(nums, target), -1)

    def test_even_length_array(self):
        """Test with an array of even length."""
        nums = [1, 2, 3, 4]
        target = 2
        self.assertEqual(self.solver.search(nums, target), 1)
        target = 4
        self.assertEqual(self.solver.search(nums, target), 3)
        target = 0
        self.assertEqual(self.solver.search(nums, target), -1)

    def test_odd_length_array(self):
        """Test with an array of odd length."""
        nums = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(self.solver.search(nums, target), 2)
        target = 1
        self.assertEqual(self.solver.search(nums, target), 0)
        target = 5
        self.assertEqual(self.solver.search(nums, target), 4)
        target = 0
        self.assertEqual(self.solver.search(nums, target), -1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

