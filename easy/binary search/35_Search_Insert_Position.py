# 35. Search Insert Position

# https://leetcode.com/problems/search-insert-position/description/

# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

# O(log n) solution with binary search
# Time complexity = O(log n) - standard binary search complexity, search space is halved at each iteration
# Space complexity = O(1) - only integer pointers used

import unittest

class Solution(object):
    def searchInsert(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left # left will always return the first spot where target could be inserted if it isn't found

class TestSearchInsert(unittest.TestCase):

    def setUp(self):
        """Set up an instance of the Solution class before each test."""
        self.solver = Solution()

    # --- Previous test cases for other functions would go here, if any ---

    # NEW TEST CASE FUNCTION FOR searchInsert
    def test_search_insert_scenarios(self):
        """
        Test cases for the searchInsert method, covering found and insert positions.
        """
        # Test 1: Target found in the middle
        nums1 = [1, 3, 5, 6]
        target1 = 5
        self.assertEqual(self.solver.searchInsert(nums1, target1), 2, "Test 1 Failed: Target 5 should be at index 2")

        # Test 2: Target not found, should be inserted at the beginning
        nums2 = [1, 3, 5, 6]
        target2 = 0
        self.assertEqual(self.solver.searchInsert(nums2, target2), 0, "Test 2 Failed: Target 0 should be inserted at index 0")

        # Test 3: Target not found, should be inserted in the middle
        nums3 = [1, 3, 5, 6]
        target3 = 2
        self.assertEqual(self.solver.searchInsert(nums3, target3), 1, "Test 3 Failed: Target 2 should be inserted at index 1")

        # Test 4: Target not found, should be inserted at the end
        nums4 = [1, 3, 5, 6]
        target4 = 7
        self.assertEqual(self.solver.searchInsert(nums4, target4), 4, "Test 4 Failed: Target 7 should be inserted at index 4")

        # Test 5: Target found at the beginning
        nums5 = [1, 3, 5, 6]
        target5 = 1
        self.assertEqual(self.solver.searchInsert(nums5, target5), 0, "Test 5 Failed: Target 1 should be at index 0")

        # Test 6: Target found at the end
        nums6 = [1, 3, 5, 6]
        target6 = 6
        self.assertEqual(self.solver.searchInsert(nums6, target6), 3, "Test 6 Failed: Target 6 should be at index 3")

        # Test 7: Empty array
        nums7 = []
        target7 = 5
        self.assertEqual(self.solver.searchInsert(nums7, target7), 0, "Test 7 Failed: Empty array, target should be inserted at index 0")

        # Test 8: Single element array, target found
        nums8 = [5]
        target8 = 5
        self.assertEqual(self.solver.searchInsert(nums8, target8), 0, "Test 8 Failed: Single element found")

        # Test 9: Single element array, target smaller
        nums9 = [5]
        target9 = 3
        self.assertEqual(self.solver.searchInsert(nums9, target9), 0, "Test 9 Failed: Single element, target smaller")

        # Test 10: Single element array, target larger
        nums10 = [5]
        target10 = 7
        self.assertEqual(self.solver.searchInsert(nums10, target10), 1, "Test 10 Failed: Single element, target larger")

        # Test 11: Target just before an element
        nums12 = [10, 20, 30, 40]
        target12 = 25
        self.assertEqual(self.solver.searchInsert(nums12, target12), 2, "Test 11 Failed: Target 25 inserted at index 2")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)