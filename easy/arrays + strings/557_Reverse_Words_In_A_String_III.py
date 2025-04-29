# 557. Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

# Given a string s, reverse the order of characters in each word within a sentence while still preserving
# whitespace and initial word order.

# Optimal with two pointers
# Time complexity = O(n) - at least one pass through of array is required to reverse all elements where n = len(s)
# Space complexity = O(1) - python strings are immutable therefore can't be done in place and needs to be converted
#                           to list (same as char array), this will require allocated space of n where n = len(s)

def reverse_words(s):
    if len(s) == 1:
        return s

    listed_s = list(s)

    left = right = 0

    while right < len(listed_s) - 1:
        if listed_s[right] == " ":
            word_end = right - 1
            while left < word_end:
                listed_s[left], listed_s[word_end] = listed_s[word_end], listed_s[left]
                left += 1
                word_end -= 1
            left = right + 1
        right += 1

    while left < right:
        listed_s[left], listed_s[right] = listed_s[right], listed_s[left]
        left += 1
        right -= 1

    return "".join(listed_s)

def run_all_tests():
    """Runs all test cases for the reverseWords method of the given solution class."""

    def test_empty_string():
        assert reverse_words("") == ""
        print("test_empty_string passed")

    def test_single_word():
        assert reverse_words("hello") == "olleh"
        print("test_single_word passed")

    def test_multiple_words():
        assert reverse_words("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
        print("test_multiple_words passed")

    def test_string_with_punctuation():
        assert reverse_words("Hello, world!") == ",olleH !dlrow"
        print("test_string_with_punctuation passed")

    def test_string_with_numbers():
        assert reverse_words("123 abc 456") == "321 cba 654"
        print("test_string_with_numbers passed")

    # Run the tests
    test_empty_string()
    test_single_word()
    test_multiple_words()
    test_string_with_punctuation()
    test_string_with_numbers()

run_all_tests()

