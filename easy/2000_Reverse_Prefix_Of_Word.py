# 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/description/

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the
# index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
#
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and
# ends at 3 (inclusive). The resulting string will be "dcbaefd". Return the resulting string.

# Optimal(ish) - could use String slicing to be more Pythonic

# Time complexity = O(n) - passing through all of word in worst case which is length of n
# Space complexity = O(n) - new String required to store reversed prefix substring before concatenation, in worst case
#                           could be of length n - 1 = n

def reverse_prefix(word, ch):
    if ch not in word:
        return word

    right = char_index = 0

    prefix_substring = ""

    for right in range(len(word)):
        if word[right] == ch:
            char_index = right
            break

    while char_index >= 0:
        prefix_substring += word[char_index]
        char_index -= 1

    return prefix_substring + word[right + 1:]

# Slightly more spacially optimal using two pointers (O(1) auxiliary space since it is done in place but total
#                                                     complexities are same)

def reverse_prefix_two_pointers(word, ch):
    char_index = word.find(ch)
    if char_index == -1:
        return word

    word = list(word)  # Convert to list to allow in-place modification
    left, right = 0, char_index

    while left < right:
        word[left], word[right] = word[right], word[left] # Tuple packing allows handy swapping (remember this)
        left += 1
        right -= 1

    return ''.join(word)

# Test cases

def run_tests():
    assert reverse_prefix("abcdefd", "d") == "dcbaefd"    # Regular case
    assert reverse_prefix("xyxzxe", "z") == "zxyxxe"       # Reverse up to first z
    assert reverse_prefix("abcd", "z") == "abcd"           # ch not found, word unchanged
    assert reverse_prefix("a", "a") == "a"                 # Single character match
    assert reverse_prefix("a", "b") == "a"                 # Single character, no match
    assert reverse_prefix("", "a") == ""                   # Empty string
    assert reverse_prefix_two_pointers("abcabcabc", "c") == "cbaabcabc" # Multiple ch, first occurrence
    assert reverse_prefix_two_pointers("pppqqqrrr", "r") == "rqqqppprr" # First r found
    assert reverse_prefix_two_pointers("z", "z") == "z"                 # Single character, match itself
    assert reverse_prefix_two_pointers("zzzzzz", "z") == "z" + "zzzzz"  # Reverse only up to first z
    assert reverse_prefix_two_pointers("qwerty", "q") == "qwerty"       # ch at index 0 (no effect)
    assert reverse_prefix_two_pointers("a"*10000 + "b", "b") == "b" + "a"*10000  # Very long input
    print("All tests passed!")

run_tests()
