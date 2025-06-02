# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Optimal
# Time complexity = O(n) - entire traversal through linked list required where len(head) = n
# Space complexity = O(1) - only integer var used for tracking current ListNode

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def delete_duplicates(self, head):

        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

class TestDeleteDuplicates(unittest.TestCase):

    # Helper function to create a linked list from a Python list
    def _create_linked_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert a linked list to a Python list
    def _linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_empty_list(self):
        """Test case for an empty linked list."""
        s = Solution()
        head = self._create_linked_list([])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [])

    def test_single_node_list(self):
        """Test case for a list with a single node."""
        s = Solution()
        head = self._create_linked_list([1])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1])

    def test_no_duplicates(self):
        """Test case for a list with no duplicate values."""
        s = Solution()
        head = self._create_linked_list([1, 2, 3, 4, 5])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4, 5])

    def test_consecutive_duplicates(self):
        """Test case for a list with consecutive duplicates."""
        s = Solution()
        head = self._create_linked_list([1, 1, 2, 3, 3, 3, 4])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4])

    def test_duplicates_at_head(self):
        """Test case for duplicates at the beginning of the list."""
        s = Solution()
        head = self._create_linked_list([1, 1, 1, 2, 3])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3])

    def test_duplicates_in_middle(self):
        """Test case for duplicates in the middle of the list."""
        s = Solution()
        head = self._create_linked_list([1, 2, 2, 3, 4])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4])

    def test_duplicates_at_end(self):
        """Test case for duplicates at the end of the list."""
        s = Solution()
        head = self._create_linked_list([1, 2, 3, 3, 3])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3])

    def test_all_duplicates(self):
        """Test case for a list where all elements are duplicates."""
        s = Solution()
        head = self._create_linked_list([5, 5, 5, 5])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [5])

    def test_long_list_with_mixed_duplicates(self):
        """Test case for a longer list with various duplicate scenarios."""
        s = Solution()
        head = self._create_linked_list([1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8])
        result_head = s.delete_duplicates(head)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)