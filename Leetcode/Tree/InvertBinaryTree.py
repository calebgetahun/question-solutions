from typing import Optional
from data_structures.BinaryTree import *

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def preorder(root: TreeNode):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.generate_random_tree()
    tree.pre_order(tree.root)
    print()
    
    sol = Solution()
    inverted_root = sol.invertTree(tree.root)
    tree.pre_order(tree.root)

# TC: O(N)
# SC: O(h), height of tree
