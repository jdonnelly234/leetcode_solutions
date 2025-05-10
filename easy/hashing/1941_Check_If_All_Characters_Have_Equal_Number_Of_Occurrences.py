# 1941. Check if All Characters Have Equal Number of Occurrences
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

# Given a string s, return true if s is a good string, or false otherwise.
#
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# Optimal with defaultdict(int)
# Time complexity = O(n) - populating hash map requires one loop over s where n = len(s) and covnerting to set requires
#                          n operations similarly, O(2n) = O(n)
# Space complexity = O(n) - worst case with very long string where occurence count of each char is never equal

from collections import defaultdict
def are_occurrences_equal(s):

    counts = defaultdict(int)

    for char in s:
        counts[char] += 1

    ans = set(counts.values())  # Set length will be 1 if all values are the same

    return len(ans) == 1

def test_are_occurrences_equal():
    # Test case 1: All characters have equal occurrences
    s1 = "aabbcc"
    expected1 = True
    actual1 = are_occurrences_equal(s1)
    assert actual1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {actual1}"
    print(f"Test Case 1 Passed: Input '{s1}', Output '{actual1}'")

    # Test case 2: Characters have different occurrences
    s2 = "abacbcc"
    expected2 = False
    actual2 = are_occurrences_equal(s2)
    assert actual2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {actual2}"
    print(f"Test Case 2 Passed: Input '{s2}', Output '{actual2}'")

    # Test case 3: Single character string
    s3 = "a"
    expected3 = True
    actual3 = are_occurrences_equal(s3)
    assert actual3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {actual3}"
    print(f"Test Case 3 Passed: Input '{s3}', Output '{actual3}'")

    # Test case 4: String with repeating characters but equal counts
    s4 = "aaaa"
    expected4 = True
    actual4 = are_occurrences_equal(s4)
    assert actual4 == expected4, f"Test Case 4 Failed: Expected {expected4}, got {actual4}"
    print(f"Test Case 4 Passed: Input '{s4}', Output '{actual4}'")

    # Test case 5: Longer string with equal counts
    s5 = "mnnmmmnnmmnnmmnn"
    expected5 = True
    actual5 = are_occurrences_equal(s5)
    assert actual5 == expected5, f"Test Case 5 Failed: Expected {expected5}, got {actual5}"
    print(f"Test Case 5 Passed: Input '{s5}', Output '{actual5}'")

    # Test case 6: Longer string with unequal counts
    s6 = "aabbc"
    expected6 = False
    actual6 = are_occurrences_equal(s6)
    assert actual6 == expected6, f"Test Case 6 Failed: Expected {expected6}, got {actual6}"
    print(f"Test Case 6 Passed: Input '{s6}', Output '{actual6}'")

    # Test case 7: String with mixed case (case-sensitive)
    s7 = "aA"
    expected7 = True
    actual7 = are_occurrences_equal(s7)
    assert actual7 == expected7, f"Test Case 7 Failed: Expected {expected7}, got {actual7}"
    print(f"Test Case 7 Passed: Input '{s7}', Output '{actual7}'")

    print("\nAll test cases completed.")

# Run the test function
test_are_occurrences_equal()