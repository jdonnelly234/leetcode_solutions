# 1208. Get Equal Substrings Within Budget
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/

# You are given two strings s and t of the same length and an integer maxCost.
#
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the
# absolute difference between the ASCII values of the characters).
#
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of
# t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to
# its corresponding substring from t, return 0.

# Optimal with sliding window
# Time complexity = O(n) - both input arrays have same length of n, arrays are passed through once
# Space complexity = O(1) - only primitive data types used for pointers and tracking

def equal_substring(s, t, maxCost):
    left = right = curr_cost = ans = 0

    while left < len(s) and right < len(t):
        curr_cost += abs(ord(s[right]) - ord(t[right]))

        while curr_cost > maxCost:
            curr_cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1

        ans = max(ans, right - left + 1)

        right += 1

    return ans

def test_equal_substring():
    def assert_equal(s, t, maxCost, expected):
        result = equal_substring(s, t, maxCost)
        if result == expected:
            print(f"Test passed for s='{s}', t='{t}', maxCost={maxCost}: Result = {result}")
        else:
            print(f"Test failed for s='{s}', t='{t}', maxCost={maxCost}: Expected = {expected}, Got = {result}")

    # Include a variety of test cases to cover different scenarios
    assert_equal("abcd", "bcdf", 3, 3)
    assert_equal("abcd", "cdef", 3, 1)
    assert_equal("abcd", "acde", 0, 1)
    assert_equal("krrgw", "zjxss", 19, 2)
    assert_equal("pxezla", "loveyy", 0, 0)
    assert_equal("mryisc", "tiyuct", 8, 1)
    assert_equal("jildzejo", "wmrydddi", 9, 3)
    assert_equal("aaaaaaaa", "bbbbbbbb", 100, 8)
    assert_equal("abcdefg", "abcdefg", 0, 7)
    assert_equal("abcdefg", "hijklmn", 1, 0)
    assert_equal("", "", 0, 0) # Empty strings
    assert_equal("a", "b", 1, 1)
    assert_equal("a", "b", 0, 0)

test_equal_substring()