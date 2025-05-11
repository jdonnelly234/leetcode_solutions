# 1550. Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2025-05-11

# Given an integer array arr, return true if there are three consecutive odd numbers in the array.
# Otherwise, return false.

# Solution
# Time complexity = O(n) - at worst passing through length of array once if there are not 3 consecutive odd's
# Space complexity = O(1) - only using primitive data types

def three_consecutive_odds(arr):

    right = odd_count = 0

    while right < len(arr):
        if arr[right] % 2 == 1:
            odd_count += 1
        else:
            odd_count = 0

        if odd_count == 3:
            return True

        right += 1

    return False

def test_three_consecutive_odds():

    # Test cases
    assert not three_consecutive_odds([])
    assert not three_consecutive_odds([2, 4, 6, 8])
    assert not three_consecutive_odds([1, 3])
    assert not three_consecutive_odds([2, 1, 3])
    assert not three_consecutive_odds([1, 2, 3])
    assert three_consecutive_odds([1, 3, 5, 2, 4])
    assert three_consecutive_odds([2, 4, 1, 3, 5, 6])
    assert three_consecutive_odds([2, 4, 6, 1, 3, 5])
    assert three_consecutive_odds([1, 3, 5, 7, 2])
    assert not three_consecutive_odds([1, 2, 3, 2, 5])
    assert not three_consecutive_odds([1, 3, 2, 5, 7])

    print("All test cases passed!")

if __name__ == "__main__":
    test_three_consecutive_odds()