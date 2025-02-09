from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head
        
        curr = head
        total_nodes = 0
        random_ptr = dict()
        while curr:
            random_ptr[curr] = total_nodes
            total_nodes += 1
            curr = curr.next
        
        new_list = [None] * total_nodes    
        new_list[0] = Node(head.val)
        old = head.next

        for i in range(1, total_nodes):
            new_node = Node(old.val)
            new_list[i] = new_node
            new_list[i-1].next = new_node
            old = old.next
        
        new_list[-1].next = None

        curr = head
        for j in range(total_nodes):
            if not curr.random:
                new_list[j].random = None
            else:
                new_list[j].random = new_list[random_ptr[curr.random]]
            
            curr = curr.next

        return new_list[0]
    
if __name__ == "__main__":
    sol = Solution()
    n_1 = Node(7)
    n_2 = Node(13)
    n_3 = Node(11)
    n_4 = Node(10)
    n_5 = Node(1)
    n_1.next = n_2
    n_1.random = None
    n_2.next = n_3
    n_2.random = n_1
    n_3.next = n_4
    n_3.random = n_5
    n_4.next = n_5
    n_4.random = n_3
    n_5.next = None
    n_5.random = n_1

    head = n_1
    deep_copy = sol.copyRandomList(head)

    is_the_same = True

    while head and deep_copy:
        if head.val != deep_copy.val:
            print("node values not the same")
            is_the_same = False
        
        if head.random and deep_copy.random:
            if head.random.val != deep_copy.random.val:
                print("random pointers not the same")
                is_the_same = False
        elif head.random is None and deep_copy.random is None:
            pass
        else:
            print("random pointers not the same")
            is_the_same = False

        head = head.next
        deep_copy = deep_copy.next

    print(f"Are both lists the same: {is_the_same}")
            
# TC: O(N)
# SC: O(N)