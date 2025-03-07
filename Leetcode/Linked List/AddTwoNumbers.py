from typing import Optional
from data_structures.LinkedList import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        res = ListNode(-1)
        node = res
        dec_val = 0
        while l1 or l2 or rem:
            curr = rem
            if l1:
                curr += l1.val
                l1 = l1.next

            if l2:
                curr += l2.val
                l2 = l2.next

            rem = curr // 10
            curr %= 10
            node.next = ListNode(curr)
            node = node.next

        return res.next
            
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    
if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    printLinkedList(sol.addTwoNumbers(l1, l2))

# TC: O(N + M), where N and M are the length of both linked lists
# SC: O(1)