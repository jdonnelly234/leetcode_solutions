# 2090. K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-averages/description/

# You are given a 0-indexed array nums of n integers, and an integer k.The k-radius average for a subarray of nums
# centered at some index i with the radius k is the average of all elements in nums
# between the indices i - k and i + k (inclusive). If there are less than k elements before or after the
# index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x, using integer division.
# The integer division truncates toward zero, which means losing its fractional part.

# For both of below:
# Time complexity = O(n) - prefix solution iterates through nums twice ie O(n) + O(n) = O(2n) = O(n)
#                          sliding window solution only iterates through once but still O(n)
# Total space complexity = O(n) - prefix solution allocates two arrays with len(nums) ie O(n) + O(n) = O(2n) = O(n)
#                           sliding window allocates one array with len(nums) but still O(n) <- slightly more efficient
#                           since auxiliary space used is O(1), whereas prefix solution is O(n) due to sums array

# Prefix sum

def get_avgs_prefix(nums, k):
    avgs = []
    sums = [nums[0]]

    for i in range(1, len(nums)):
        sums.append(nums[i] + sums[-1])

    divisor = (k * 2) + 1

    for i in range(len(nums)):
        if (i - k) < 0 or (i + k) > len(nums) - 1:
            avgs.append(-1)
        else:
            if i - (k + 1) < 0:
                avgs.append(sums[i + k] // divisor)
            else:
                avgs.append((sums[i + k] - sums[i - (k + 1)]) // divisor)

    return avgs

# Sliding window without prefix sum

def get_avgs_sliding(nums, k):
    avgs = [-1] * len(nums)  # Fixed the length reference
    total = 0
    left = 0
    for right, n in enumerate(nums):
        total += n
        if right - left == 2 * k:
            avgs[left + k] = total // (2 * k + 1)
            total -= nums[left]
            left += 1

    return avgs

