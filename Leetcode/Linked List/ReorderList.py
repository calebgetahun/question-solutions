from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderListBruteForceRecursion(self, head: Optional[ListNode]) -> None:
        def recurse(node):
            if not node or not node.next or not node.next.next:
                return 
            last = node
            while last.next.next:
                last = last.next
            curr = node.next
            node.next = last.next
            node.next.next = curr
            last.next = None
            recurse(curr)

        res = head
        recurse(res)
    
    # TC: O(N^2)
    # SC: O(N) -> recursion stack

    def reorderListLinearSpace(self, head: Optional[ListNode]) -> None:
        #find middle point of list
        #reverse second half of list
        #merge the two lists starting with the first node
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i, j = 0, len(nodes) - 1
        new_list = nodes[0]
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[j].next = None

        return new_list

    # TC: O(N)
    # SC: O(N)

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        #find middle point of list
        second = fast = head
        while fast and fast.next:
            fast = fast.next.next
            second = second.next
        
        set_non = head
        while set_non.next != second:
            set_non = set_non.next
        
        set_non.next = None

        #reverse second half of list
        prev = None
        next_n = second.next

        while next_n:
            second.next = prev
            prev = second
            second = next_n
            next_n = next_n.next
        
        second.next = prev

        #merge the two lists starting with the first node
        curr = head
        l1, l2 = curr.next, second.next
        
        while l1 and l2:
            curr.next = second
            curr = l1
            l1 = l1.next
            second.next = curr
            second = l2
            l2 = l2.next
        
        curr.next = second
    
    # TC: O(N)
    # SC: O(1)

if __name__ == "__main__":
    sol = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node_2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    node_3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol.reorderListBruteForceRecursion(node)
    sol.reorderListLinearSpace(node_2)
    sol.reorderList(node_3)

    while node and node_2 and node_3:
        if node.val != node_2.val != node_3.val:
            print("False")
        node = node.next
        node_2 = node_2.next
        node_3 = node_3.next

    print("True")
