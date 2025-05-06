# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

# Optimal with two pointers
# Time complexity = O(n) - worst case is an array with descending/ascending values where each element will need to be
#                          visited
# Space complexity = O(1) - only primitive data types used to store pointer indices and current area value

def most_water(height):
    left = curr_area = ans = 0
    right = len(height) - 1

    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)

        if height[right] <= height[left]:
            right -= 1
        elif height[left] <= height[right]:
            left += 1

        ans = max(ans, curr_area)


    return ans

def test_max_area(most_water):

    test_cases = [
        ([], 0, "Empty array"),
        ([1], 0, "Single element array"),
        ([1, 2], 1, "Two element array (increasing)"),
        ([2, 1], 1, "Two element array (decreasing)"),
        ([2, 2], 2, "Two element array (equal)"),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, "Basic case"),
        ([1, 2, 3, 4, 5], 6, "Increasing heights"),
        ([5, 4, 3, 2, 1], 6, "Decreasing heights"),
        ([1, 2, 2, 1], 3, "Duplicate heights"),
        ([5, 5, 5, 5], 15, "All equal heights"),
        ([10, 5, 15, 2, 8], 32, "Larger numbers"),
        ([3, 9, 3, 4], 9, "Peak in the middle"),
    ]

    for i, (input_heights, expected_output, description) in enumerate(test_cases):
        actual_output = most_water(input_heights)
        if actual_output == expected_output:
            print(f"Test Case {i + 1} ({description}): Passed")
        else:
            print(f"Test Case {i + 1} ({description}): Failed")
            print(f"  Input: {input_heights}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual: {actual_output}")
        print("-" * 30)

if __name__ == '__main__':

    test_max_area(most_water)