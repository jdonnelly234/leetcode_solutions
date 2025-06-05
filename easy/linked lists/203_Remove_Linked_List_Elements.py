# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that
# has Node.val == val, and return the new head.

# Optimal
# Time complexity = O(n) - one pass through required to check if all Node.val are equal where n = len(head)
# Space complexity = O(1) - only pointers used for tracking curr and one additional dummy ListNode

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return None

        dummy = ListNode(0, head)

        curr = dummy

        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

class TestRemoveElements(unittest.TestCase):

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

    def test_remove_middle_elements(self):
        # List: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
        # Expected: 1 -> 2 -> 3 -> 4 -> 5
        head = self._list_to_linked_list([1, 2, 6, 3, 4, 5, 6])
        result_head = self.solution.removeElements(head, 6)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4, 5])

    def test_remove_all_elements(self):
        # List: 7 -> 7 -> 7 -> 7, val = 7
        # Expected: [] (None)
        head = self._list_to_linked_list([7, 7, 7, 7])
        result_head = self.solution.removeElements(head, 7)
        self.assertIsNone(result_head)

    def test_remove_head_element(self):
        # List: 7 -> 1 -> 2 -> 3, val = 7
        # Expected: 1 -> 2 -> 3
        head = self._list_to_linked_list([7, 1, 2, 3])
        result_head = self.solution.removeElements(head, 7)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3])

    def test_remove_tail_element(self):
        # List: 1 -> 2 -> 3 -> 6, val = 6
        # Expected: 1 -> 2 -> 3
        head = self._list_to_linked_list([1, 2, 3, 6])
        result_head = self.solution.removeElements(head, 6)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3])

    def test_remove_consecutive_elements(self):
        # List: 1 -> 6 -> 6 -> 2 -> 6, val = 6
        # Expected: 1 -> 2
        head = self._list_to_linked_list([1, 6, 6, 2, 6])
        result_head = self.solution.removeElements(head, 6)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2])

    def test_no_elements_removed(self):
        # List: 1 -> 2 -> 3, val = 4
        # Expected: 1 -> 2 -> 3 (no change)
        head = self._list_to_linked_list([1, 2, 3])
        result_head = self.solution.removeElements(head, 4)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3])

    def test_empty_list(self):
        # List: [], val = 1
        # Expected: [] (None)
        head = self._list_to_linked_list([])
        result_head = self.solution.removeElements(head, 1)
        self.assertIsNone(result_head)

    def test_single_node_remove(self):
        # List: [1], val = 1
        # Expected: [] (None)
        head = self._list_to_linked_list([1])
        result_head = self.solution.removeElements(head, 1)
        self.assertIsNone(result_head)

    def test_single_node_no_remove(self):
        # List: [1], val = 2
        # Expected: [1]
        head = self._list_to_linked_list([1])
        result_head = self.solution.removeElements(head, 2)
        self.assertEqual(self._linked_list_to_list(result_head), [1])

    def test_remove_from_list_with_two_elements(self):
        # List: [4, 5], val = 4
        # Expected: [5]
        head = self._list_to_linked_list([4, 5])
        result_head = self.solution.removeElements(head, 4)
        self.assertEqual(self._linked_list_to_list(result_head), [5])

        # List: [4, 5], val = 5
        # Expected: [4]
        head = self._list_to_linked_list([4, 5])
        result_head = self.solution.removeElements(head, 5)
        self.assertEqual(self._linked_list_to_list(result_head), [4])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)