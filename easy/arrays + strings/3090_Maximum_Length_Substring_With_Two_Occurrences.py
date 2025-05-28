# 3090. Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/?envType=problem-list-v2&envId=sliding-window


# Given a string s, return the maximum length of a substring such that it contains at most two
# occurrences of each character.

# Sliding window
# Time complexity = O(n) - worst case is iterating through entire string s where n = len(s)
# Space complexity = O(1) - counts dictionary will hold 26 distinct keys in worst case and O(26) = O(1)

from collections import defaultdict

def maximumLengthSubstring(s):
    if not s:
        return 0

    counts = defaultdict(int)

    left = right = 0
    ans = 0

    while right < len(s):
        counts[s[right]] += 1

        while counts[s[right]] > 2:
            counts[s[left]] -= 1
            left += 1

        curr = right - left + 1
        ans = max(ans, curr)

        right += 1

    return ans

def run_tests():

    test_cases = [
        ("bcbbbcba", 4),
        ("abcde", 5),
        ("aaaaa", 2),
        ("", 0),
        ("abacaba", 5),
        ("aabccddeeffg", 12),
        ("topcoderopen", 10),
        ("leetcode", 7),
        ("zzzaac", 5)
    ]

    print("Running tests for maximumLengthSubstring:\n")
    for s, expected in test_cases:
        result = maximumLengthSubstring(s)
        test_status = "PASSED" if result == expected else "FAILED"
        print(f"Input: '{s}'")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Status: {test_status}\n")
        if test_status == "FAILED":
            print("--- Test Failed ---\n") # Highlight failures

if __name__ == "__main__":
    run_tests()