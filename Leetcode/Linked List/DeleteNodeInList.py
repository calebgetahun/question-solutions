from LinkedList import ListNode

class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    sol = Solution()
    node = ListNode(1)
    head = node.createList([4,5,1,9])

    toBeRemoved = head.next

    sol.deleteNode(toBeRemoved)
    
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

# TC: O(1)
# SC: O(1)
