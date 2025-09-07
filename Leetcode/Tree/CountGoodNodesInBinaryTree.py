from data_structures.BinaryTree import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node, path_max):
            if not node:
                return 0
            
            good_node = False
            if node.val >= path_max:
                good_node = True
            
            res = count(node.left, max(path_max, node.val)) + count(node.right, max(path_max, node.val))
            if good_node:
                return 1 + res
            else:
                return res
        return count(root, float('-inf'))
        
if __name__ == "__main__":
    sol = Solution()
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.left.left = TreeNode(3)
    tree.right = TreeNode(4)
    tree.right.left = TreeNode(1)
    tree.right.right = TreeNode(5)

    print(sol.goodNodes(tree))
    