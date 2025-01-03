from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        nxt = head.next

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

if __name__ == "__main__":
    sol = Solution()
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    head = linked_list
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()
    
    reversed_list = sol.reverseList(linked_list)
    head = reversed_list

    while head:
        print(head.val, end=" -> ")
        head = head.next

# TC: O(N)
# SC: O(1)