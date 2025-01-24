from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.maxDepth(root.left) + 1
        right_height = self.maxDepth(root.right) + 1

        return max(left_height, right_height)
        
if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(8)))
    print(sol.maxDepth(tree))

# TC: O(N)
# SC: O(h)
