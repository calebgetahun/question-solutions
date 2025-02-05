from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        #at any node, the left and right path have length k and k_1. The curr_max can be the max at that node between the left and right added together or another max determined earlier
        # self.curr_max = -1
        def findHeight(root):
            if not root:
                return 0, 0

            left_diameter, left_height = findHeight(root.left)
            right_diameter, right_height = findHeight(root.right)

            max_d = max(left_height+right_height, left_diameter, right_diameter)
            max_h = max(left_height, right_height) + 1
            return max_d, max_h

        return findHeight(root)[0]
        
if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5))))
    print(sol.diameterOfBinaryTree(tree))

# TC: O(N)
# SC: O(h), where h is the height of the tree
