from data_structures.LinkedList import ListNode

class Solution:
    def sum_of_nodes(self, head: ListNode):
        res = 0
        curr = head
        while curr:
            res += curr.val
            curr = curr.next

        return res