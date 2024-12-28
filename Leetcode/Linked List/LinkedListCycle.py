from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next
        return False
    
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    print(sol.hasCycle(head))

    head = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    head.next = node_2
    node_2.next = node_3
    node_3.next = head

    print(sol.hasCycle(head))
    
# TC: O(N) using the tortoise and hare algorithm
# SC: O(1)
