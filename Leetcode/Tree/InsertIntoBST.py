from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while curr:
            if val < curr.val:
                if not curr.left:
                    new_node = TreeNode(val)
                    curr.left = new_node
                    return root
                else:
                    curr = curr.left
            elif val > curr.val:
                if not curr.right: 
                    new_node = TreeNode(val)
                    curr.right = new_node
                    return root
                else:
                    curr = curr.right
            
        return root

if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    insert = 5
    sol.insertIntoBST(tree, insert)
    print(tree.right.left.val)

# TC: O(logN) in a balanced tree aka the height of the tree
# SC: O(1)
