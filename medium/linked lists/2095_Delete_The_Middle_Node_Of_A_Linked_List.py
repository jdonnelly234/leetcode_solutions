# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋
# denotes the largest integer less than or equal to x.
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

# Optimal
# Time complexity = O(n) - n/2 of list is traversed and O(n/2) = O(n)
# Space complexity = O(1) - only one extra dummy Node used along with pointers, remains the same regardless of list size

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def delete_middle(self, head):
        if head is None or head.next is None:
            return None

        dummy = ListNode(0, head)

        slow = dummy
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return dummy.next

class TestDeleteMiddle(unittest.TestCase):

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

    def test_n_equals_1(self):
        # n = 1, middle node is index 0. [1] -> [] (None)
        head = self._list_to_linked_list([1])
        result_head = self.solution.delete_middle(head)
        self.assertIsNone(result_head) # Expecting None (empty list)

    def test_n_equals_2(self):
        # n = 2, middle node is index 1. [1, 2] -> [1]
        head = self._list_to_linked_list([1, 2])
        result_head = self.solution.delete_middle(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1])

    def test_n_equals_3(self):
        # n = 3, middle node is index 1. [1, 2, 3] -> [1, 3]
        head = self._list_to_linked_list([1, 2, 3])
        result_head = self.solution.delete_middle(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 3])

    def test_n_equals_4(self):
        # n = 4, middle node is index 2. [1, 2, 3, 4] -> [1, 2, 4]
        head = self._list_to_linked_list([1, 2, 3, 4])
        result_head = self.solution.delete_middle(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 4])

    def test_n_equals_5(self):
        # n = 5, middle node is index 2. [1, 2, 3, 4, 5] -> [1, 2, 4, 5]
        head = self._list_to_linked_list([1, 2, 3, 4, 5])
        result_head = self.solution.delete_middle(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 4, 5])

    def test_empty_list(self):
        # n = 0, head is None -> None
        head = self._list_to_linked_list([])
        result_head = self.solution.delete_middle(head)
        self.assertIsNone(result_head)

    def test_longer_list(self):
        # Test with a longer even list
        # n = 8, middle node is index 4. [1, 2, 3, 4, 5, 6, 7, 8] -> [1, 2, 3, 4, 6, 7, 8]
        head = self._list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        result_head = self.solution.delete_middle(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4, 6, 7, 8])

    def test_longer_odd_list(self):
        # Test with a longer odd list
        # n = 9, middle node is index 4. [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [1, 2, 3, 4, 6, 7, 8, 9]
        head = self._list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        result_head = self.solution.delete_middle(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
