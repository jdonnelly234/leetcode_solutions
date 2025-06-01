# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
import unittest


# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's
# next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Optimal with Floyd's Cycle Finding Algorithm
# Time complexity = O(n) - worst case is entire linked list is traversed when there is no cycle, or list is very large
#                          and cycle is not found till the end
# Space complexity = O(1) - only int's used for slow and fast pointers

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def floyds_cycle_finding_algo(self, head):
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

class TestHasCycle(unittest.TestCase):

    def test_empty_list(self):
        """Test case for an empty linked list."""
        s = Solution()
        self.assertFalse(s.floyds_cycle_finding_algo(None))

    def test_single_node_no_cycle(self):
        """Test case for a single node list with no cycle."""
        s = Solution()
        head = ListNode(1)
        self.assertFalse(s.floyds_cycle_finding_algo(head))

    def test_two_nodes_no_cycle(self):
        """Test case for a two-node list with no cycle."""
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        self.assertFalse(s.floyds_cycle_finding_algo(head))

    def test_two_nodes_cycle(self):
        """Test case for a two-node list with a cycle (2 -> 1)."""
        s = Solution()
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node2.next = head  # Cycle: 2 points back to 1
        self.assertTrue(s.floyds_cycle_finding_algo(head))

    def test_multiple_nodes_no_cycle(self):
        """Test case for a multi-node list with no cycle."""
        s = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        self.assertFalse(s.floyds_cycle_finding_algo(head))

    def test_multiple_nodes_cycle_end_to_middle(self):
        """Test case for a multi-node list with a cycle (end to middle)."""
        s = Solution()
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node3  # Cycle: 5 points back to 3

        self.assertTrue(s.floyds_cycle_finding_algo(head))

    def test_multiple_nodes_cycle_end_to_start(self):
        """Test case for a multi-node list with a cycle (end to start)."""
        s = Solution()
        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)

        head.next = node2
        node2.next = node3
        node3.next = head  # Cycle: 3 points back to 1

        self.assertTrue(s.floyds_cycle_finding_algo(head))

    def test_long_list_no_cycle(self):
        """Test case for a longer list with no cycle."""
        s = Solution()
        head = ListNode(1)
        current = head
        for i in range(2, 101): # Create 100 nodes
            current.next = ListNode(i)
            current = current.next
        self.assertFalse(s.floyds_cycle_finding_algo(head))

    def test_long_list_with_cycle(self):
        """Test case for a longer list with a cycle."""
        s = Solution()
        head = ListNode(1)
        current = head
        cycle_start_node = None
        for i in range(2, 101):
            current.next = ListNode(i)
            current = current.next
            if i == 50: # Make 50 the cycle start
                cycle_start_node = current
        current.next = cycle_start_node # Create cycle

        self.assertTrue(s.floyds_cycle_finding_algo(head))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)