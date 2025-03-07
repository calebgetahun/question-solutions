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

if __name__ == "__main__":
    sol = Solution()
    tree = BinaryTree()
    tree.generate_random_tree()

    print(sol.levelOrder(tree.root))