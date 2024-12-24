from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1

        return head.next

def create_linked_list(vals: list):
    head = ListNode()
    temp = head
    for val in vals:
        curr = ListNode(val)
        temp.next = curr
        temp = temp.next
    return head.next

def print_linked_list(head: ListNode):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    list1 = create_linked_list([1,1,4,5,6])
    list2 = create_linked_list([1,3,4])

    sol = Solution()
    print_linked_list(sol.mergeTwoLists(list1, list2))
    
# TC: O(n + m) where n = number of nodes in list1 and m = number of nodes in list2
# SC: O(1)