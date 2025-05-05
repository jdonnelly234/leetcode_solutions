# 2351. First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/description/

# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
#
# Note:
#
# A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
# s will contain at least one letter that appears twice.

# Optimal with set to enforce uniqueness of seen chars
# Time complexity = O(n) - worst case is iterating through entire array to check for seen chars
# Space complexity = O(n) - worst case is storing every char in s into seen set if no duplicates exist

def repeated_char(s):
    seen = set()

    for i in range(len(s)):
        if s[i] in seen:
            return s[i]

        seen.add(s[i])

    return ""

def test_repeated_char():
    """
    Tests the repeatedCharacter function with various test cases.
    """
    test_cases = [
        {"s": "abccba", "expected": "c"},
        {"s": "abcddcba", "expected": "d"},
        {"s": "aab", "expected": "a"},
        {"s": "abcdefgh", "expected": ""},  # No repeated character
        {"s": "aaaaaaaa", "expected": "a"}, # Repeated character at the beginning
        {"s": "baaaaaa", "expected": "a"}, # Repeated character after a non-repeating
        {"s": "aA", "expected": ""},       #Case sensitive
        {"s": "AbA", "expected": "A"},
    ]

    for i, test_case in enumerate(test_cases):
        s = test_case["s"]
        expected = test_case["expected"]
        actual = repeated_char(s)
        assert actual == expected, f"Test case {i + 1} failed: s={s}, expected={expected}, actual={actual}"
        print(f"Test case {i + 1} passed!")



if __name__ == "__main__":
    test_repeated_char()