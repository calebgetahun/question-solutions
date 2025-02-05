from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
if __name__ == "__main__":
    sol = Solution()
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

    second_half = sol.middleNode(linked_list)
    head = second_half
    while head:
        print(head.val, end=" -> ")
        head = head.next

# TC: O(N)
# SC: O(1)