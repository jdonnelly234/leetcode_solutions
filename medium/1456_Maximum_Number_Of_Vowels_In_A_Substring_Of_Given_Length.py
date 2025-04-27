# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

#Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


# Sliding window (optimal)

# Time complexity = O(n) - only one pass through the array with left/right pointers where len(s) = n
# Space complexity is O(1) - only extra allocated memory required for vowels array
#                            which is fixed size regardless of input.

def maxVowels(s, k):

    if not s or k < 0:
        return 0

    left = right = curr = ans = 0

    vowels = ['a', 'e', 'i', 'o', 'u']
    while right < len(s):
        if s[right] in vowels:
            curr += 1

        right += 1

        while right - left > k:
            if s[left] in vowels:
                curr -= 1
            left += 1

        ans = max(ans, curr)

    return ans

# Test

print(maxVowels("abciiidef", 3), "# Expected: 3")
print(maxVowels("aeiou", 3), "# Expected: 3")
print(maxVowels("leetcode", 5), "# Expected: 3")
print(maxVowels("tryhard", 4), "# Expected: 1")
print(maxVowels("uioaeiou", 2), "# Expected: 2")
print(maxVowels("", 3), "# Expected: 0")            # Empty string
print(maxVowels("a", 1), "# Expected: 1")
print(maxVowels("xyz", 2), "# Expected: 0")
print(maxVowels("aaeiouu", 7), "# Expected: 7")
print(maxVowels("aaceiouxyz", 3), "# Expected: 3")
print(maxVowels("bgghiuoa", -1), "# Expected: 0")      # Invalid k