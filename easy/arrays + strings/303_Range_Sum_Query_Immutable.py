# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/description/

# Given an integer array nums, handle multiple queries of the following type:
#
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
# (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        """
        :type nums: List[int]
        """


    def sum_range(self, left, right):
        sums = 0
        for i in range(left, right + 1):
            sums += self.nums[i]

        return sums

test = NumArray([1,2,4,5,6,7])
test2 = NumArray([1])
test3 = NumArray([0,2,4,0,7])

print(test.sum_range(0, 4))
print(test2.sum_range(0, 0))
print(test3.sum_range(2, 3))

