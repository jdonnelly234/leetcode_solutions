# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Two solutions with same time and space complexity
# Time complexity = O(n) - second solution is slightly better since at worst it requires one pass through of list
# Space complexity = O(1) - in both cases only single dummy node and pointer variables used

import unittest

# Two pass through - get length of list first
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def remove_nth_from_end_two_pass(self, head, n):
        if head is None or head.next is None:
            return None

        size_check = head
        length = 0

        while size_check:
            length += 1
            size_check = size_check.next

        dummy = ListNode(0, head)
        curr = dummy

        for _ in range(length - n):
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next

    # One pass through
    def remove_nth_from_end_one_pass(self, head, n):
        if head is None or head.next is None:
            return None

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

class TestRemoveNthFromEnd(unittest.TestCase):

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

    # --- Test cases applicable to both solutions ---

    def _run_common_tests(self, remove_func):
        # Test Case 1: Remove a middle node
        # List: 1 -> 2 -> 3 -> 4 -> 5, n = 2 (Remove 4)
        # Expected: 1 -> 2 -> 3 -> 5
        head = self._list_to_linked_list([1, 2, 3, 4, 5])
        result_head = remove_func(head, 2)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 5])

        # Test Case 2: Remove the head (n = length)
        # List: 1 -> 2 -> 3, n = 3 (Remove 1)
        # Expected: 2 -> 3
        head = self._list_to_linked_list([1, 2, 3])
        result_head = remove_func(head, 3)
        self.assertEqual(self._linked_list_to_list(result_head), [2, 3])

        # Test Case 3: Remove the tail (n = 1)
        # List: 1 -> 2 -> 3, n = 1 (Remove 3)
        # Expected: 1 -> 2
        head = self._list_to_linked_list([1, 2, 3])
        result_head = remove_func(head, 1)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2])

        # Test Case 4: Single node list (n = 1)
        # List: 1, n = 1 (Remove 1)
        # Expected: [] (None)
        head = self._list_to_linked_list([1])
        result_head = remove_func(head, 1)
        self.assertIsNone(result_head)

        # Test Case 5: Two node list, remove first (n = 2)
        # List: 1 -> 2, n = 2 (Remove 1)
        # Expected: [2]
        head = self._list_to_linked_list([1, 2])
        result_head = remove_func(head, 2)
        self.assertEqual(self._linked_list_to_list(result_head), [2])

        # Test Case 6: Two node list, remove second (n = 1)
        # List: 1 -> 2, n = 1 (Remove 2)
        # Expected: [1]
        head = self._list_to_linked_list([1, 2])
        result_head = remove_func(head, 1)
        self.assertEqual(self._linked_list_to_list(result_head), [1])

        # Test Case 7: Longer list
        # List: 1 -> ... -> 10, n = 4 (Remove 7)
        # Expected: 1 -> ... -> 6 -> 8 -> 9 -> 10
        head = self._list_to_linked_list(list(range(1, 11))) # [1, 2, ..., 10]
        result_head = remove_func(head, 4)
        self.assertEqual(self._linked_list_to_list(result_head), [1, 2, 3, 4, 5, 6, 8, 9, 10])

        # Test Case 8: Empty list (n = 1, or any n)
        # List: [], n = 1
        # Expected: None
        head = self._list_to_linked_list([])
        result_head = remove_func(head, 1)
        self.assertIsNone(result_head)

    def test_two_pass_solution(self):
        print("\n--- Running Two-Pass Solution Tests ---")
        self._run_common_tests(self.solution.remove_nth_from_end_two_pass)
        print("--- Two-Pass Solution Tests Complete ---")

    def test_one_pass_solution(self):
        print("\n--- Running One-Pass Solution Tests ---")
        self._run_common_tests(self.solution.remove_nth_from_end_one_pass)
        print("--- One-Pass Solution Tests Complete ---")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
