# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Optimal
# Time complexity = O(n) - worst case requires traversal through entire list where n = len(head)
# Space complexity = O(1) - only pointers to ListNodes are used which remain constant space regardless of input size

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse_between(self, head, left, right):
        if not head or not head.next:
            return head

        # Removes need to edit actual head of list if left = 1, means actual head of list is always pointed to.
        dummy = ListNode(0, head)

        left_prev = dummy

        for _ in range(left - 1):
            left_prev = left_prev.next

        curr = left_prev.next
        prev = None

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next

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

    def test_reverse_between_middle(self):
        # List: 1 -> 2 -> 3 -> 4 -> 5
        # Reverse from left=2 to right=4 (i.e., reverse 2 -> 3 -> 4)
        # Expected: 1 -> 4 -> 3 -> 2 -> 5
        head = self._list_to_linked_list([1, 2, 3, 4, 5])
        left = 2
        right = 4
        reversed_head = self.solution.reverse_between(head, left, right)
        self.assertEqual(self._linked_list_to_list(reversed_head), [1, 4, 3, 2, 5])

    def test_reverse_between_from_head(self):
        # List: 1 -> 2 -> 3 -> 4 -> 5
        # Reverse from left=1 to right=3 (i.e., reverse 1 -> 2 -> 3)
        # Expected: 3 -> 2 -> 1 -> 4 -> 5
        head = self._list_to_linked_list([1, 2, 3, 4, 5])
        left = 1
        right = 3
        reversed_head = self.solution.reverse_between(head, left, right)
        self.assertEqual(self._linked_list_to_list(reversed_head), [3, 2, 1, 4, 5])

    def test_reverse_between_to_tail(self):
        # List: 1 -> 2 -> 3 -> 4 -> 5
        # Reverse from left=3 to right=5 (i.e., reverse 3 -> 4 -> 5)
        # Expected: 1 -> 2 -> 5 -> 4 -> 3
        head = self._list_to_linked_list([1, 2, 3, 4, 5])
        left = 3
        right = 5
        reversed_head = self.solution.reverse_between(head, left, right)
        self.assertEqual(self._linked_list_to_list(reversed_head), [1, 2, 5, 4, 3])

    def test_reverse_between_entire_list(self):
        # List: 1 -> 2 -> 3
        # Reverse from left=1 to right=3 (i.e., reverse 1 -> 2 -> 3)
        # Expected: 3 -> 2 -> 1
        head = self._list_to_linked_list([1, 2, 3])
        left = 1
        right = 3
        reversed_head = self.solution.reverse_between(head, left, right)
        self.assertEqual(self._linked_list_to_list(reversed_head), [3, 2, 1])

    def test_reverse_between_single_node(self):
        # List: 1 -> 2 -> 3
        # Reverse from left=2 to right=2 (i.e., reverse 2)
        # Expected: 1 -> 2 -> 3 (no change)
        head = self._list_to_linked_list([1, 2, 3])
        left = 2
        right = 2
        reversed_head = self.solution.reverse_between(head, left, right)
        self.assertEqual(self._linked_list_to_list(reversed_head), [1, 2, 3])

    def test_reverse_between_two_nodes(self):
        # List: 1 -> 2
        # Reverse from left=1 to right=2
        # Expected: 2 -> 1
        head = self._list_to_linked_list([1, 2])
        left = 1
        right = 2
        reversed_head = self.solution.reverse_between(head, left, right)
        self.assertEqual(self._linked_list_to_list(reversed_head), [2, 1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)