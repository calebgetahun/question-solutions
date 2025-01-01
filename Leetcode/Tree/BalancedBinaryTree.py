from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        balance = self.height(root)

        if balance != -1:
            return True
        return False
    
    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(0)
    left_node = TreeNode(1)
    right_node = TreeNode(2)
    root.left = left_node
    root.right = right_node
    right_left = TreeNode(3)
    right_right = TreeNode(4)
    root.right.left = right_left
    root.right.right = right_right

    print(sol.isBalanced(root))

    root.right.right.right = TreeNode(5)
    print(sol.isBalanced(root))

# TC: O(N)
# SC: O(N)
