# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/description/

# Given a string s, reverse the string according to the following rules:
#
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Optimal with two pointers
# Time complexity = O(n) - one pass through of s is required to reverse letters where n = len(s)
# Space complexity = O(n) - python strings are immutable therefore s needs to be converted to list of length n
#                           where n = len(s)

def reverse_only_letters(s):
    if len(s) == 1:
        return s

    left = 0
    right = len(s) - 1

    listed_s = list(s)

    while left < right:
        if not listed_s[left].isalpha():
            left += 1

        elif not listed_s[right].isalpha():
            right -= 1
        else:
            listed_s[left], listed_s[right] = listed_s[right], listed_s[left]

            left += 1
            right -= 1

    return "".join(listed_s)

def run_reverse_only_letters_tests(reverse_func):
    """Runs test cases for the reverse_only_letters function."""

    def test_empty_string():
        assert reverse_func("") == ""
        print("test_empty_string passed")

    def test_only_letters():
        assert reverse_func("ab-cd") == "dc-ba"
        print("test_only_letters passed")

    def test_only_non_letters():
        assert reverse_func("--++") == "--++"
        print("test_only_non_letters passed")

    def test_mixed_letters_and_non_letters():
        assert reverse_func("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
        print("test_mixed_letters_and_non_letters passed")

    def test_leading_and_trailing_non_letters():
        assert reverse_func("!aB?c") == "!cB?a"
        print("test_leading_and_trailing_non_letters passed")

    def test_numbers_and_letters():
        assert reverse_func("7_28") == "7_28"
        print("test_numbers_and_letters passed")

    def test_complex_mixed_case():
        assert reverse_func("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
        print("test_complex_mixed_case passed")

    test_empty_string()
    test_only_letters()
    test_only_non_letters()
    test_mixed_letters_and_non_letters()
    test_leading_and_trailing_non_letters()
    test_numbers_and_letters()
    test_complex_mixed_case()

if __name__ == '__main__':
    run_reverse_only_letters_tests(reverse_only_letters)