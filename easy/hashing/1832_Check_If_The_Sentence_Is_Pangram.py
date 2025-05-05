# 1832. Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing only lowercase English letters, return true if sentence is
# a pangram, or false otherwise.

# Optimal with set
# Time complexity = O(n) - required iteration over entire len(sentence) = n to check each element in sentence
# Space complexity = O(1) - max space used by seen is O(26) since there can be max 26 chars inserted for all
#                           letters in the alphabet, this is constant regardless of input size

def check_pangram(sentence):

    seen_letters = set()

    for i in range(len(sentence)):
        seen_letters.add(sentence[i].lower())

    return len(seen_letters) == 26

def test_check_pangram():
    """
    Tests the check_pangram function with various test cases.
    """
    test_cases = [
        {"sentence": "thequickbrownfoxjumpsoverthelazydog", "expected": True},
        {"sentence": "leetcode", "expected": False},
        {"sentence": "TheQuickBrownFoxJumpsOverTheLazyDog", "expected": True},  # Uppercase
        {"sentence": "the quick brown fox jumps over the lazy dog", "expected": False},  # Spaces
        {"sentence": "abcdefghijklmnopqrstuvwxy", "expected": False},  # Missing one letter
        {"sentence": "aaaaaaaaaaaaaaaaaaaaaaaaaa", "expected": False}, #only one letter
        {"sentence": "", "expected": False},  # Empty string
        {"sentence": "abcdefghijklmnopqrstuvwxyz"*2, "expected": True}, #long pangram
    ]

    for i, test_case in enumerate(test_cases):
        sentence = test_case["sentence"]
        expected = test_case["expected"]
        actual = check_pangram(sentence)
        assert actual == expected, f"Test case {i + 1} failed: sentence='{sentence}', expected={expected}, actual={actual}"
        print(f"Test case {i + 1} passed!")


if __name__ == "__main__":
    test_check_pangram()
