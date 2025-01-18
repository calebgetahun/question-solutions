from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        values = []
        
        def inOrder(root, values):
            if not root:
                return

            inOrder(root.left, values)
            values.append(root.val)
            inOrder(root.right, values)

        inOrder(root, values)
        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False
        return True
    
    def isValidBSTUsingRanges(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left, right):
            if not root:
                return True

            if root.val <= left or root.val >= right:
                return False
            
            left = helper(root.left, left, root.val)
            right = helper(root.right, root.val, right)
        
            return left and right

        left, right = float('-inf'), float('inf')
        return helper(root, left, right)
    

if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    print(sol.isValidBST(tree))
    print(sol.isValidBSTUsingRanges(tree))

# TC: O(N) where N is the number of nodes in our tree
# SC: O(N + h) = O(N) since we store all our nodes values in a list for comparison