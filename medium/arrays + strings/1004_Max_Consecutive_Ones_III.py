# 1004. Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/description/

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the
# array if you can flip at most k 0's.

# Time complexity = O(n) - Each value in nums is processed at most twice so n + n = 2n = n.
#                          Nested while loop will be linear regardless of input size so doesn't change complexity
# Space complexity = O(1) - Only primitive data types used

def longest_ones(nums, k):
    left = right = curr = zero_num = ans = 0

    while right < len(nums):
        if nums[right] == 0:
            zero_num += 1

        curr += 1
        right += 1

        while zero_num > k:
            if nums[left] == 0:
                zero_num -= 1
            curr -= 1
            left += 1


        ans = max(ans, curr)

    return ans

# === Test Cases ===
assert longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6, "Test Case 1 Failed"
print("Test Case 1 Passed")

assert longest_ones([1,1,1,1,1], 2) == 5, "Test Case 2 Failed"
print("Test Case 2 Passed")

assert longest_ones([0,0,0], 1) == 1, "Test Case 3 Failed"
print("Test Case 3 Passed")

assert longest_ones([1,0,1,0,1], 0) == 1, "Test Case 4 Failed"
print("Test Case 4 Passed")

assert longest_ones([], 2) == 0, "Test Case 5 Failed"
print("Test Case 5 Passed")

assert longest_ones([0], 1) == 1, "Test Case 6 Failed"
print("Test Case 6 Passed")

assert longest_ones([1, 0, 1, 1, 0, 1], 10) == 6, "Test Case 7 Failed"
print("Test Case 7 Passed")

assert longest_ones([0, 0, 0, 0], 4) == 4, "Test Case 8 Failed"
print("Test Case 8 Passed")

print("\nAll test cases passed!")





