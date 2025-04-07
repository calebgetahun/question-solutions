from typing import Optional, List
from BinaryTree import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = dict()
        for i in range(len(inorder)):
            inorderIndex[inorder[i]] = i
        
        self.preorderIndex = 0
        def buildSubTree(left, right):
            if left >= right:
                return None
            
            root = TreeNode(preorder[self.preorderIndex])
            self.preorderIndex += 1
            root_index = inorderIndex[root.val]

            root.left = buildSubTree(left, root_index)
            root.right = buildSubTree(root_index+1, right)

            return root
        
        return buildSubTree(0, len(inorder))
    
def preorderTraversal(root, traversal: list):
    if not root:
        return
    
    traversal.append(root.val)
    preorderTraversal(root.left, traversal)
    preorderTraversal(root.right, traversal)

def inorderTraversal(root, traversal: list):
    if not root:
        return

    inorderTraversal(root.left, traversal)
    traversal.append(root.val)
    inorderTraversal(root.right, traversal)
            
if __name__ == "__main__":
    sol = Solution()
    preorder = [3,9,4,20,15,7]
    inorder = [9,4,3,15,20,7]
    tree = sol.buildTree(preorder, inorder)

    preAfter = []
    preorderTraversal(tree, preAfter)
    inAfter = []
    inorderTraversal(tree, inAfter)

    isValid = True
    for i in range(len(preorder)):
        if preorder[i] != preAfter[i]:
            isValid = False
        if inorder[i] != inAfter[i]:
            isValid = False
    
    if isValid:
        print("Tree generation is successful")
    else:
        print("Tree generation not successful")

# TC: O(N)
# SC: O(N)