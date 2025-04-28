# 1732. Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
# The biker starts his trip on point 0 with altitude equal 0. You are given an integer array gain of length n where
# gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
# Return the highest altitude of a point.

# Initial solution

# Time complexity = O(n) - two passes through gain array therefore O(n) + O(n) = O(2n) = O(n)
# Space complexity = O(n) - sums arrays for storing iterative sums of gains is allocated n memory where n = len(gain)

def largest_altitude(gain):
    sums = [0]

    for i in range(1, len(gain) + 1):
        sums.append(gain[i - 1] + sums[-1])

    curr = 0
    ans = float("-inf")

    for i in range(len(sums)):
        if sums[i] > curr:
            curr = sums[i]
        ans = max(ans, curr)

    return ans

# Slightly optimised - auxiliary space of O(1) since no additional sums array, however still total space complexity
#                      of O(n) as a passthrough of gain is required where n = len(gain)

def largest_altitude_optimum(gain):
    max_altitude = curr = 0

    for i in range(len(gain)):
        curr += gain[i]
        max_altitude = max(max_altitude, curr)

    return max_altitude

def run_tests():
    test_cases = [
        # Basic positive gains
        {"gain": [5, 1, 4], "expected": 10},
        # Basic negative gains
        {"gain": [-5, -2, -3], "expected": 0},
        # Mixed positive and negative gains
        {"gain": [-4, -3, -2, -1, 4, 3, 2], "expected": 0},
        # Single positive gain
        {"gain": [100], "expected": 100},
        # Single negative gain
        {"gain": [-50], "expected": 0},
        # Empty gain array
        {"gain": [], "expected": 0},
        # Trek ends at a high altitude
        {"gain": [1, 2, 3, 4, 5], "expected": 15},
        # Trek dips low but recovers
        {"gain": [-10, 5, -3, 8], "expected": 0},
        # Trek starts with a large drop
        {"gain": [-100, 10, 50], "expected": 0},
        # Trek oscillates
        {"gain": [5, -3, 2, -1, 4], "expected": 7},
        # All gains are zero
        {"gain": [0, 0, 0], "expected": 0},
        # Larger numbers
        {"gain": [1000, -500, 2000], "expected": 2500},
        # Negative gains followed by positive gains
        {"gain": [-5, -5, 10, 2], "expected": 2},
    ]

    for i, test in enumerate(test_cases):
        result = largest_altitude_optimum(test["gain"])
        if result == test["expected"]:
            print(f"Test case {i + 1}: Passed")
        else:
            print(f"Test case {i + 1}: Failed - Expected: {test['expected']}, Got: {result}, Input: {test['gain']}")

if __name__ == "__main__":
    run_tests()