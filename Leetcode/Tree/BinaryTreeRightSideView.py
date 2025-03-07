from typing import Optional, List
from data_structures import GenerateBinaryTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    tree_root = GenerateBinaryTree.GenericBinaryTree().root
    print(sol.rightSideView(tree_root))