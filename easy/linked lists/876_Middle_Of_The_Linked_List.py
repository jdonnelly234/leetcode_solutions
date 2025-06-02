# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

# Solution with tortoise and hare
# Time complexity = O(n) - always have to traverse through list at max rate of n/2 due to fast pointer, O(n/2) = O(n)
# Space complexity = O(1) - constant as only using int's for pointers

import unittest

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middle_node(self, head):
        if head is None:
            return None
        if head.next is None:
            return head

        slow = head
        fast = head

        # Loop condition takes care of odd and even lengths, if fast is None then len(list) is even, if fast.next is None then len(list) is odd
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

class TestMiddleNode(unittest.TestCase):

    def test_empty_list(self):
        """Test case for an empty linked list."""
        s = Solution()
        self.assertIsNone(s.middle_node(None)) # Expect None for empty list

    def test_single_node(self):
        """Test case for a single node list."""
        s = Solution()
        head = ListNode(1)
        result = s.middle_node(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 1)

    def test_two_nodes(self):
        """Test case for a two-node list (middle should be the second node)."""
        s = Solution()
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        result = s.middle_node(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2) # For even length, it's the second of the two middle nodes

    def test_three_nodes(self):
        """Test case for a three-node list (middle should be the second node)."""
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        result = s.middle_node(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 2)

    def test_four_nodes(self):
        """Test case for a four-node list (middle should be the third node)."""
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        result = s.middle_node(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3) # For even length, it's the second of the two middle nodes

    def test_five_nodes(self):
        """Test case for a five-node list (middle should be the third node)."""
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        result = s.middle_node(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)

    def test_long_odd_list(self):
        """Test case for a longer odd-length list."""
        s = Solution()
        head = ListNode(1)
        current = head
        # Create a list of 21 nodes (1 to 21)
        for i in range(2, 22):
            current.next = ListNode(i)
            current = current.next
        # Middle node should be 11 (21 // 2 + 1)
        result = s.middle_node(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 11)

    def test_long_even_list(self):
        """Test case for a longer even-length list."""
        s = Solution()
        head = ListNode(1)
        current = head
        # Create a list of 20 nodes (1 to 20)
        for i in range(2, 21):
            current.next = ListNode(i)
            current = current.next
        # Middle node should be the second of the two middle nodes (10, 11) which is 11
        result = s.middle_node(head)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 11)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)