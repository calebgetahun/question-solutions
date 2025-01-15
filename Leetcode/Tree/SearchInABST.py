from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
    
if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    print(sol.searchBST(tree, 4))

# TC: O(logN) since we cut search space in half each iteration
# SC: O(h), h = height of tree. If balanced, this will be roughly logN. Iteratively could also be done in constant space