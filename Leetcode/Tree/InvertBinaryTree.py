from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    print(root.val)
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_left = TreeNode(4)
    left_right = TreeNode(5)
    right_left = TreeNode(6)
    right_right = TreeNode(7)
    root.left = left
    root.right = right
    root.left.left = left_left
    root.left.right = left_right
    root.right.left = right_left
    root.right.right = right_right
    
    sol = Solution()
    inverted_root = sol.invertTree(root)
    preorder(inverted_root)

# TC: O(N)
# SC: O(h), height of tree
