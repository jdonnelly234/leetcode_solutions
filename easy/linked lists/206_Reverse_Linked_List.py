# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Optimal
# Time complexity = O(n) - traversal of entire list required to reverse next pointers where n = len(head)
# Space complexity = O(1) - only 3 total pointer variables used which remains the same regardless of input size

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse_list(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

class TestReverseList(unittest.TestCase):

    # Helper function to convert a list to a linked list
    def _list_to_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert a linked list to a list
    def _linked_list_to_list(self, head):
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return arr

    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = None
        reversed_head = self.solution.reverse_list(head)
        self.assertIsNone(reversed_head)

    def test_single_node_list(self):
        head = self._list_to_linked_list([1])
        reversed_head = self.solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [1])

    def test_two_node_list(self):
        head = self._list_to_linked_list([1, 2])
        reversed_head = self.solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [2, 1])

    def test_multiple_node_list(self):
        head = self._list_to_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [5, 4, 3, 2, 1])

    def test_list_with_duplicates(self):
        head = self._list_to_linked_list([1, 2, 2, 1])
        reversed_head = self.solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), [1, 2, 2, 1])

    def test_long_list(self):
        long_list_values = list(range(100))
        head = self._list_to_linked_list(long_list_values)
        reversed_head = self.solution.reverse_list(head)
        self.assertEqual(self._linked_list_to_list(reversed_head), list(reversed(long_list_values)))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)