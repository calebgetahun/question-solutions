from typing import Optional, List
from data_structures.BinaryTree import *

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        traversal = []
        q = [[root, 0]]

        level_trav = 0
        level = []

        while q:
            curr, curr_level = q.pop(0)
            if curr_level == level_trav:
                level.append(curr.val)
            else:
                level_trav += 1
                traversal.append(level)
                level = [curr.val]
            if curr.left:
                q.append([curr.left, curr_level + 1])
            if curr.right:
                q.append([curr.right, curr_level + 1])
        traversal.append(level)

        return traversal

    def levelOrderShorter(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        traversal = []

        q = [root]

        while q:
            curr_level = []
            for _ in range(len(q)):
                popped = q.pop(0)
                curr_level.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            traversal.append(curr_level)
        return traversal
    

if __name__ == "__main__":
    sol = Solution()
    tree = BinaryTree()
    tree.generate_random_tree()

    print(sol.levelOrder(tree.root))
    print(sol.levelOrderShorter(tree.root))

# TC: O(N)
# SC: O(N)