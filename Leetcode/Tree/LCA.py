# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if not right else right
    
if __name__ == "__main__":
    sol = Solution()
    p = TreeNode(0)
    q = TreeNode(6)
    tree = TreeNode(3, TreeNode(5, q, TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, p, TreeNode(8)))
    print(sol.lowestCommonAncestor(tree, p, q).val)

# TC: O(N)
# SC: O(h)