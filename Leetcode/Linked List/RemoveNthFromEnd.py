from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None

        slow = fast = head

        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head

def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("end of list")

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    head_edge_case = ListNode(1, ListNode(2))
    edge_n = 2

    printLinkedList(sol.removeNthFromEnd(head, n))
    printLinkedList(sol.removeNthFromEnd(head_edge_case, edge_n))

# TC: O(N)
# SC: O(1)