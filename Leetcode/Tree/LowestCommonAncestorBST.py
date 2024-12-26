# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val >= min(p.val, q.val) and root.val <= max(p.val, q.val):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

if __name__ == "__main__":
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(6)
    left_left = TreeNode(1)
    left_right = TreeNode(3)
    right_left = TreeNode(5)
    right_right = TreeNode(7)
    root.left = left
    root.right = right
    root.left.left = left_left
    root.left.right = left_right
    root.right.left = right_left
    root.right.right = right_right

    p = right_left
    q = left_right

    sol = Solution()
    print(sol.lowestCommonAncestor(root, p, q).val)