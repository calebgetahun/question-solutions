from typing import Optional
from BinaryTree import TreeNode, BinaryTree

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, treeOne, treeTwo):
        if not treeOne and not treeTwo:
            return True
        
        if not treeOne or not treeTwo:
            return False
        
        if treeOne.val != treeTwo.val:
            return False
        
        return self.isSameTree(treeOne.left, treeTwo.left) and self.isSameTree(treeOne.right, treeTwo.right)

if __name__ == "__main__":
    sol = Solution()
    tree = BinaryTree()
    tree.generate_random_tree()
    subTree = BinaryTree()
    subTree.root.val = 3
    subTree.root.left = TreeNode(6)
    subTree.root.right = TreeNode(7)
    print(sol.isSubtree(tree.root, subTree.root))

# TC: O(N * M) where N and M are the number of nodes in the tree and subtree respectively
# SC: o(N + M) because of our calls to isSameTree which goes to as large as M will get and the initial isSubtree call which goes to as large as N will get