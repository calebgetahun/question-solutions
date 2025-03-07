from typing import Optional, List
from data_structures.BinaryTree import *

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = []
        q.append(root)
        
        while q:
            curr = q[0]
            for _ in range(len(q)):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            res.append(curr.val)

        return res

if __name__ == "__main__":
    sol = Solution()
    tree = BinaryTree()
    tree.generate_random_tree()
    print(sol.rightSideView(tree.root))