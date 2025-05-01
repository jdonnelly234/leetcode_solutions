# 2540. Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/description/

# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer
# common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
#
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that int.

# Optimal

# Time complexity = O(n + m) - worst case scenario is having to check all elements in each array where n = len(nums1)
#                              and m = len(nums2)
# Space complexity = O(1) - constant total space complexity since only primitive types are used for two pointers
#                           to check arrays in place, no additional data structures that require allocated memory

def get_common(nums1, nums2):

    left = right = 0

    while left < len(nums1) and right < len(nums2):
        if nums1[left] == nums2[right]:
            return nums1[left]
        elif nums1[left] < nums2[right]:
            left += 1
        elif nums2[right] < nums1[left]:
            right += 1

    return -1

def test_get_common():
    """Tests the getCommon function with various inputs."""

    def run_test(nums1, nums2, expected):
        result = get_common(nums1, nums2)
        assert result == expected, f"Test failed for nums1={nums1}, nums2={nums2}. Expected {expected}, got {result}"
        print(f"Test passed for nums1={nums1}, nums2={nums2}, expected={expected}")

    # Test cases
    run_test([1, 2, 3], [2, 4, 6], 2)
    run_test([1, 3, 5], [2, 4, 6], -1)
    run_test([1, 2, 3], [1, 2, 3], 1)
    run_test([1], [1], 1)
    run_test([1], [2], -1)
    run_test([], [1, 2, 3], -1)
    run_test([1, 2, 3], [], -1)
    run_test([1, 1, 2], [1, 2, 2], 1)
    run_test([3, 5, 7], [1, 2, 3], 3)
    run_test([1, 2, 3], [0, 3], 3)

    print("All tests passed!")

test_get_common()