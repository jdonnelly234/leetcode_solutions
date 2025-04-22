# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.

# === Optimal with sliding window ===

# Time complexity = O(n) - left/right window passes over array once where n = len(nums)
# Space complexity = O(1) - Constant time, only primitive data types used

def find_max_average(nums, k):
    if k > len(nums):
        return 0

    if len(nums) == 1:
        return nums[0] / float(k)

    left = right = curr = 0
    ans = float('-inf')     # setting initial ans to -inf to handle arrays of entirely negative ints

    while right < len(nums):
        curr += nums[right]
        right += 1

        if (right - left) > k:
            curr -= nums[left]
            left += 1

        if right - left == k:
            ans = max(ans, curr / float(k))

    return ans


# === Test Case 1: Simple Positive ===
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
expected1 = 12.75
assert abs(find_max_average(nums1, k1) - expected1) < 1e-5, "Test Case 1 Failed"
print("Test Case 1 Passed")

# === Test Case 2: All Negative ===
nums2 = [-1, -12, -5, -6, -50, -3]
k2 = 2
expected2 = -5.5
assert abs(find_max_average(nums2, k2) - expected2) < 1e-5, "Test Case 2 Failed"
print("Test Case 2 Passed")
