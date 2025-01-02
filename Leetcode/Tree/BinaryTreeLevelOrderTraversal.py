from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        traversal = []
        q = [[root, 0]]

        level_trav = 0
        level = []

        while q:
            curr, curr_level = q.pop(0)
            if curr_level == level_trav:
                level.append(curr.val)
            else:
                level_trav += 1
                traversal.append(level)
                level = [curr.val]
            if curr.left:
                q.append([curr.left, curr_level + 1])
            if curr.right:
                q.append([curr.right, curr_level + 1])
        traversal.append(level)

        return traversal

if __name__ == "__main__":
    sol = Solution()
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

    print(sol.levelOrder(root))