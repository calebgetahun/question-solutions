from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
if __name__ == "__main__":
    sol = Solution()
    p = TreeNode(3, TreeNode(2), TreeNode(4))
    q = TreeNode(3, TreeNode(2), TreeNode(4))
    r = TreeNode(3, TreeNode(4), TreeNode(5))

    print(sol.isSameTree(p, q))
    print(sol.isSameTree(q, r))

# TC: O(N + M) where N and M are the number of nodes in p and q, respectively
# SC: O(h) for recursion depth