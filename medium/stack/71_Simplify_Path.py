# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/description/

# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
# Your task is to transform this absolute path into its simplified canonical path.
#
# The rules of a Unix-style file system are as follows:
#
# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
# For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#
# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

# Optimal
# Time complexity = O(n) - .split is O(n) time, each non '/' element needs to be checked in main for loop to find
#                          correct canonical path which is O(n), O(n) + O(n) = O(2n) = O(n)
# Space complexity = O(n) - stack could contain n elements in worst-case where n is non '/' chars in path

import unittest

class Solution:
    def simplifyPath(self, path):

        dirs = path.split('/')
        stack = []

        for d in dirs:
            if d == '' or d == '.':
                continue        # Skips current loop if empty or '.' pointing to current directory
            elif d == '..':
                if stack:       # If stack is non-empty only previous directory can be popped else error will occur
                    stack.pop()
            else:
                stack.append(d)

        return "/" + "/".join(stack)    #IMPORTANT: '/' before the .join is the delimiter

class TestSimplifyPath(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Solution class for each test method
        self.solution = Solution()

    def test_simplify_path(self):
        # Basic cases
        self.assertEqual(self.solution.simplifyPath("/home/"), "/home")
        self.assertEqual(self.solution.simplifyPath("/a/./b/../../c/"), "/c")
        self.assertEqual(self.solution.simplifyPath("/home//foo/"), "/home/foo")

        # Root directory
        self.assertEqual(self.solution.simplifyPath("/"), "/")
        self.assertEqual(self.solution.simplifyPath("/."), "/")
        self.assertEqual(self.solution.simplifyPath("/.."), "/")
        self.assertEqual(self.solution.simplifyPath("/../"), "/")

        # Complex cases
        self.assertEqual(self.solution.simplifyPath("/a/b/c"), "/a/b/c")
        self.assertEqual(self.solution.simplifyPath("/a/../b/c"), "/b/c")
        self.assertEqual(self.solution.simplifyPath("/a/b/c/d/.././../e/"), "/a/b/e")
        self.assertEqual(self.solution.simplifyPath("/..."), "/...") # '...' is a valid directory name
        self.assertEqual(self.solution.simplifyPath("/home/user/.././photos"), "/home/photos")

        # Paths starting with '..' or '.' but ending up at root
        self.assertEqual(self.solution.simplifyPath("/../"), "/")
        self.assertEqual(self.solution.simplifyPath("/../a/b/../c"), "/a/c")

        # Empty string and just multiple slashes
        self.assertEqual(self.solution.simplifyPath("//"), "/") # Multiple slashes should reduce to single /
        self.assertEqual(self.solution.simplifyPath("/a//b//c"), "/a/b/c")

# This block allows you to run the tests when the script is executed directly
if __name__ == '__main__':
    unittest.main() # unittest.main() will discover and run tests in the current file
