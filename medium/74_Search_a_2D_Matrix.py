# 74. Search a 2D Matrix

# https://leetcode.com/problems/search-a-2d-matrix/description/

# You are given an m x n integer matrix (matrix) with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.

# Optimal
# Time complexity = O(log(m * n)) - worst case where m * n elements are checked, log because binary search halves search space at each loop iteration
# Space complexity = O(1) - constant space as only pointer variable used to store left, right, row and col pointers

import unittest

class Solution(object):
    def searchMatrix(self, matrix, target):

        # m is total number of rows, n is length of first row (which will be length of all rows)
        m, n = len(matrix), len(matrix[0])

        # right initialised to last value in 2D matrix
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            num = matrix[row][col]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

class TestSearchMatrix(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def test_medium_matrix_target_found(self):
        """
        Test with a medium-sized matrix where the target is found.
        """
        matrix = [
            [1, 4, 7, 11, 15],
            [18, 22, 26, 30, 34],
            [38, 42, 46, 50, 54],
            [58, 62, 66, 70, 74],
            [78, 82, 86, 90, 94]
        ]
        target = 46 # Should be at matrix[2][2] (conceptual index 12)
        self.assertTrue(self.solver.searchMatrix(matrix, target))

    def test_medium_matrix_target_not_found(self):
        """
        Test with a medium-sized matrix where the target is not found.
        """
        matrix = [
            [1, 4, 7, 11, 15],
            [18, 22, 26, 30, 34],
            [38, 42, 46, 50, 54],
            [58, 62, 66, 70, 74],
            [78, 82, 86, 90, 94]
        ]
        target = 45 # Not in the matrix
        self.assertFalse(self.solver.searchMatrix(matrix, target))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)